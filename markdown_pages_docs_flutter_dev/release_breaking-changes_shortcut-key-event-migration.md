Migrate ShortcutActivator and ShortcutManager to KeyEvent system
================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate ShortcutActivator and ShortcutManager to KeyEvent system](/release/breaking-changes/shortcut-key-event-migration)

Summary
-------

[#](#summary)

For some time now (years), Flutter has had two key event systems implemented. The new system reached parity with the old platform-specific raw key event system, and the raw system will be removed. To prepare for that, the Flutter APIs that use the old system are being modified, and for a select few of them we have decided to make breaking changes in the API in order to preserve the quality of the API.

Context
-------

[#](#context)

In the original key event subsystem handling each platform's quirks in the framework and in client apps caused overly complex code, and the old system didn't properly represent the true state of key events on the system.

So, the new [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html)-based system was born, and to minimize breaking changes, was implemented in parallel with the old system with the intention of eventually deprecating the raw system. That time is quickly arriving, and to prepare for it, we have made some minimal breaking changes required to preserve the quality of the API.

Description of change
---------------------

[#](#description-of-change)

Summary of APIs that have been affected:

* `ShortcutActivator.accepts` now takes a `KeyEvent` and `HardwareKeyboard`.* `ShortcutActivator.isActivatedBy` is now deprecated. Just call `accepts` instead.* `ShortcutActivator.triggers` is now optional, and returns null if not implemented.* `ShortcutManager.handleKeypress` now takes a `KeyEvent`.

The change modifies the `ShortcutActivator.accepts` method to take a `KeyEvent` and `HardwareKeyboard` instead of the previous `RawKeyEvent` and `RawKeyboard`.

The meaning of `ShortcutActivator.accepts` has changed slightly. Before the change, it was assumed that `accepts` was only called if `ShortcutActivator.triggers` returned null, or if the key event sent to `accepts` had a logical key that was in the `triggers` list. Now it is always called, and may use the `triggers` list as a performance improvement, but is not required to. Flutter subclasses such as `SingleActivator` and `CharacterActivator` already do this.

The change also modifies the `ShortcutManager.handleKeypress` method to take a `KeyEvent` instead of `RawKeyEvent`.

Migration guide
---------------

[#](#migration-guide)

APIs provided by the Flutter framework are already migrated. Migration is needed only if you're using any of the methods listed in the previous section.

### Migrating your APIs that use `ShortcutActivator` or its subclasses.

[#](#migrating-your-apis-that-use-shortcutactivator-or-its-subclasses)

Pass a `KeyEvent` instead of a `RawKeyEvent` to `ShortcutActivator.accepts`. This may mean switching where you get your key events from. Depending on where you get them, this can either mean switching to using `Focus.onKeyEvent` instead of `Focus.onKey`, or a similar change if using `FocusScope`, `FocusNode` or `FocusScopeNode`.

If you're using a `RawKeyboardListener`, switch to using a `KeyboardListener` instead. If you're accessing `RawKeyboard` directly, use `HardwareKeyboard` instead. You'll find that there are non-raw equivalents for all of the key event sources.

### Migrating your APIs that extend `ShortcutActivator`

[#](#migrating-your-apis-that-extend-shortcutactivator)

The `ShortcutActivator.accepts` method was modified to take a `KeyEvent` and a `HardwareKeyboard` instead of a `RawKeyEvent` and `RawKeyboard`.

Before:

dart

```
class MyActivator extends ShortcutActivator {
  @override
  bool accepts(RawKeyEvent event, RawKeyboard state) {
    // ... (your implementation here)
    returns false;
  }
  // ...
}
```

After:

dart

```
class MyActivator extends ShortcutActivator {
  @override
  bool accepts(KeyEvent event, HardwareKeyboard state) {
    // ... (your implementation here)
    returns false;
  }
  // ...
}
```

### Migrating your APIs that extend `ShortcutManager`

[#](#migrating-your-apis-that-extend-shortcutmanager)

The `ShortcutManager` class was modified to take `KeyEvent`s in `handleKeypress` instead of `RawKeyEvent`s. One difference in the two APIs is that repeated keys are determined differently. In the `RawKeyEvent` case, the `repeat` member indicated a repeat, but in `RawKeyEvent` code, the event is a different type (`KeyRepeatEvent`).

Before:

dart

```
class _MyShortcutManager extends ShortcutManager {
  @override
  KeyEventResult handleKeypress(BuildContext context, RawKeyEvent event) {
    if (event is! RawKeyDownEvent) {
      return KeyEventResult.ignored;
    }
    if (event.repeat) {
      // (Do something with repeated keys.)
    }
    // ... (your implementation here)
    return KeyEventResult.handled;
  }
}
```

After:

dart

```
class _MyShortcutManager extends ShortcutManager {
  @override
  KeyEventResult handleKeypress(BuildContext context, KeyEvent event) {
    if (event is! KeyDownEvent && event is! KeyRepeatEvent) {
      return KeyEventResult.ignored;
    }
    if (event is KeyRepeatEvent) {
      // (Do something with repeated keys.)
    }
    // ... (your implementation here)
    return KeyEventResult.handled;
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.17.0-5.0.pre  
 In stable release: 3.19.0

References
----------

[#](#references)

API documentation:

* [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html)* [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html)* [`ShortcutActivator`](https://api.flutter.dev/flutter/widgets/ShortcutActivator-class.html)* [`ShortcutManager`](https://api.flutter.dev/flutter/widgets/ShortcutManager-class.html)

Relevant issues:

* [`RawKeyEvent` and `RawKeyboard`, et al should be deprecated and removed (Issue 136419)](https://github.com/flutter/flutter/issues/136419)

Relevant PRs:

* [Prepare ShortcutActivator and ShortcutManager to migrate to KeyEvent from RawKeyEvent](https://github.com/flutter/flutter/pull/136854)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/shortcut-key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/shortcut-key-event-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/shortcut-key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/shortcut-key-event-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/shortcut-key-event-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/shortcut-key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/shortcut-key-event-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   