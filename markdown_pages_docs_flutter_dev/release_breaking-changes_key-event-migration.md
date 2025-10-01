Migrate RawKeyEvent/RawKeyboard system to KeyEvent/HardwareKeyboard system
==========================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate RawKeyEvent/RawKeyboard system to KeyEvent/HardwareKeyboard system](/release/breaking-changes/key-event-migration)

Summary
-------

[#](#summary)

For some time now (years), Flutter has had two key event systems implemented. The new system reached parity with the old platform-specific raw key event system, and the raw system has been deprecated.

Context
-------

[#](#context)

In the original key event subsystem, handling each platform's quirks in the framework and in client apps caused overly complex code, and the old system didn't properly represent the true state of key events on the system.

The legacy API [`RawKeyboard`](https://api.flutter.dev/flutter/services/RawKeyboard-class.html) has been deprecated and will be removed in the future. The [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html) and [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html) APIs replace this legacy API. An example of this change is [`FocusNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusNode/onKeyEvent.html) replacing `FocusNode.onKey`.

The behavior of [`RawKeyboard`](https://api.flutter.dev/flutter/services/RawKeyboard-class.html) provided a less unified and less regular event model than [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html) does. Consider the following examples:

* Down events were not always matched with an up event, and vice versa (the set of pressed keys was silently updated).* The logical key of the down event was not always the same as that of the up event.* Down events and repeat events were not easily distinguishable (had to be tracked manually).* Lock modes (such as CapsLock) only had their "enabled" state recorded. There was no way to acquire their pressed state.

So, the new [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html)/[`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html)-based system was born and, to minimize breaking changes, was implemented in parallel with the old system with the intention of eventually deprecating the raw system. That time has arrived, and application developers should migrate their code to avoid breaking changes that will occur when the deprecated APIs are removed.

Description of change
---------------------

[#](#description-of-change)

Below are the APIs that have been deprecated.

### Deprecated APIs that have an equivalent

[#](#deprecated-apis-that-have-an-equivalent)

* [`Focus.onKey`](https://api.flutter.dev/flutter/services/Focus/onKey.html) => [`Focus.onKeyEvent`](https://api.flutter.dev/flutter/services/Focus/onKeyEvent.html)* [`FocusNode.attach`](https://api.flutter.dev/flutter/services/FocusNode/attach.html)'s `onKey` argument => `onKeyEvent` argument* [`FocusNode.onKey`](https://api.flutter.dev/flutter/services/FocusNode/onKey.html) => [`FocusNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusNode/onKeyEvent.html)* [`FocusOnKeyCallback`](https://api.flutter.dev/flutter/services/FocusOnKeyCallback-class.html) => [`FocusOnKeyEventCallback`](https://api.flutter.dev/flutter/services/FocusOnKeyEventCallback-class.html)* [`FocusScope.onKey`](https://api.flutter.dev/flutter/services/FocusScope/onKey.html) => [`FocusScope.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScope/onKeyEvent.html)* [`FocusScopeNode.onKey`](https://api.flutter.dev/flutter/services/FocusScopeNode/onKey.html) => [`FocusScopeNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScopeNode/onKeyEvent.html)* [`RawKeyboard`](https://api.flutter.dev/flutter/services/RawKeyboard-class.html) => [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html)* [`RawKeyboardListener`](https://api.flutter.dev/flutter/services/RawKeyboardListener-class.html) => [`KeyboardListener`](https://api.flutter.dev/flutter/services/KeyboardListener-class.html)* [`RawKeyDownEvent`](https://api.flutter.dev/flutter/services/RawKeyDownEvent-class.html) => [`KeyDownEvent`](https://api.flutter.dev/flutter/services/KeyDownEvent-class.html)* [`RawKeyEvent`](https://api.flutter.dev/flutter/services/RawKeyEvent-class.html) => [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html)* [`RawKeyUpEvent`](https://api.flutter.dev/flutter/services/RawKeyUpEvent-class.html) => [`KeyUpEvent`](https://api.flutter.dev/flutter/services/KeyUpEvent-class.html)

### APIs that have been discontinued

[#](#apis-that-have-been-discontinued)

These APIs are no longer needed once there is only one key event system, or their functionality is no longer offered.

* [`debugKeyEventSimulatorTransitModeOverride`](https://api.flutter.dev/flutter/services/debugKeyEventSimulatorTransitModeOverride-class.html)* [`GLFWKeyHelper`](https://api.flutter.dev/flutter/services/GLFWKeyHelper-class.html)* [`GtkKeyHelper`](https://api.flutter.dev/flutter/services/GtkKeyHelper-class.html)* [`KeyboardSide`](https://api.flutter.dev/flutter/services/KeyboardSide-class.html)* [`KeyDataTransitMode`](https://api.flutter.dev/flutter/services/KeyDataTransitMode-class.html)* [`KeyEventManager`](https://api.flutter.dev/flutter/services/KeyEventManager-class.html)* [`KeyHelper`](https://api.flutter.dev/flutter/services/KeyHelper-class.html)* [`KeyMessage`](https://api.flutter.dev/flutter/services/KeyMessage-class.html)* [`KeyMessageHandler`](https://api.flutter.dev/flutter/services/KeyMessageHandler-class.html)* [`KeySimulatorTransitModeVariant`](https://api.flutter.dev/flutter/services/KeySimulatorTransitModeVariant-class.html)* [`ModifierKey`](https://api.flutter.dev/flutter/services/ModifierKey-class.html)* [`RawKeyEventData`](https://api.flutter.dev/flutter/services/RawKeyEventData-class.html)* [`RawKeyEventDataAndroid`](https://api.flutter.dev/flutter/services/RawKeyEventDataAndroid-class.html)* [`RawKeyEventDataFuchsia`](https://api.flutter.dev/flutter/services/RawKeyEventDataFuchsia-class.html)* [`RawKeyEventDataIos`](https://api.flutter.dev/flutter/services/RawKeyEventDataIos-class.html)* [`RawKeyEventDataLinux`](https://api.flutter.dev/flutter/services/RawKeyEventDataLinux-class.html)* [`RawKeyEventDataMacOs`](https://api.flutter.dev/flutter/services/RawKeyEventDataMacOs-class.html)* [`RawKeyEventDataWeb`](https://api.flutter.dev/flutter/services/RawKeyEventDataWeb-class.html)* [`RawKeyEventDataWindows`](https://api.flutter.dev/flutter/services/RawKeyEventDataWindows-class.html)* [`RawKeyEventHandler`](https://api.flutter.dev/flutter/services/RawKeyEventHandler-class.html)* [`ServicesBinding.keyEventManager`](https://api.flutter.dev/flutter/services/ServicesBinding/keyEventManager.html)

Migration guide
---------------

[#](#migration-guide)

The Flutter framework libraries have already been migrated. If your code uses any of the classes or methods listed in the previous section, migrate to these new APIs.

### Migrating your code that uses `RawKeyEvent`

[#](#migrating-your-code-that-uses-rawkeyevent)

For the most part, there are equivalent `KeyEvent` APIs available for all of the `RawKeyEvent` APIs.

Some APIs relating to platform specific information contained in [`RawKeyEventData`](https://api.flutter.dev/flutter/services/RawKeyEventData-class.html) objects or their subclasses have been removed and are no longer supported. One exception is that [`RawKeyEventDataAndroid.eventSource`](https://api.flutter.dev/flutter/services/RawKeyEventDataAndroid/eventSource.html) information is accessible now as [`KeyEvent.deviceType`](https://api.flutter.dev/flutter/services/KeyEvent/deviceType.html) in a more platform independent form.

#### Migrating `isKeyPressed` and related functions

[#](#migrating-iskeypressed-and-related-functions)

If the legacy code used the [`RawKeyEvent.isKeyPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isKeyPressed.html), [`RawKeyEvent.isControlPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isControlPressed.html), [`RawKeyEvent.isShiftPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isShiftPressed.html), [`RawKeyEvent.isAltPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isAltPressed.html), or [`RawKeyEvent.isMetaPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isMetaPressed.html) APIs, there are now equivalent functions on the [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html) singleton instance, but are not available on [KeyEvent]. [`RawKeyEvent.isKeyPressed`](https://api.flutter.dev/flutter/services/RawKeyEvent/isKeyPressed.html) is available as [`HardwareKeyboard.isLogicalKeyPressed`](https://api.flutter.dev/flutter/services/HardwareKeyboard/isLogicalKeyPressed.html).

Before:

dart

```
KeyEventResult _handleKeyEvent(RawKeyEvent keyEvent) {
  if (keyEvent.isControlPressed ||
      keyEvent.isShiftPressed ||
      keyEvent.isAltPressed ||
      keyEvent.isMetaPressed) {
    print('Modifier pressed: $keyEvent');
  }
  if (keyEvent.isKeyPressed(LogicalKeyboardKey.keyA)) {
    print('Key A pressed.');
  }
  return KeyEventResult.ignored;
}
```

After:

dart

```
KeyEventResult _handleKeyEvent(KeyEvent _) {
  if (HardwareKeyboard.instance.isControlPressed ||
      HardwareKeyboard.instance.isShiftPressed ||
      HardwareKeyboard.instance.isAltPressed ||
      HardwareKeyboard.instance.isMetaPressed) {
    print('Modifier pressed: $keyEvent');
  }
  if (HardwareKeyboard.instance.isLogicalKeyPressed(LogicalKeyboardKey.keyA)) {
    print('Key A pressed.');
  }
  return KeyEventResult.ignored;
}
```

#### Setting `onKey` for focus

[#](#setting-onkey-for-focus)

If the legacy code was using the [`Focus.onKey`](https://api.flutter.dev/flutter/services/Focus/onKey.html), [`FocusScope.onKey`](https://api.flutter.dev/flutter/services/FocusScope/onKey.html), [`FocusNode.onKey`](https://api.flutter.dev/flutter/services/FocusNode/onKey.html), or [`FocusScopeNode.onKey`](https://api.flutter.dev/flutter/services/FocusScopeNode/onKey.html) parameters, then there is an equivalent [`Focus.onKeyEvent`](https://api.flutter.dev/flutter/services/Focus/onKeyEvent.html), [`FocusScope.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScope/onKeyEvent.html), [`FocusNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusNode/onKeyEvent.html), or [`FocusScopeNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScopeNode/onKeyEvent.html) parameter that supplies `KeyEvent`s instead of `RawKeyEvent`s.

Before:

dart

```
Widget build(BuildContext context) {
  return Focus(
    onKey: (RawKeyEvent keyEvent) {
      print('Key event: $keyEvent');
      return KeyEventResult.ignored;
    }
    child: child,
  );
}
```

After:

dart

```
Widget build(BuildContext context) {
  return Focus(
    onKeyEvent: (KeyEvent keyEvent) {
      print('Key event: $keyEvent');
      return KeyEventResult.ignored;
    }
    child: child,
  );
}
```

#### Repeat key event handling

[#](#repeat-key-event-handling)

If you were relying on the [`RawKeyEvent.repeat`](https://api.flutter.dev/flutter/services/RawKeyEvent/repeat.html) attribute to determine if a key was a repeated key event, that has now been separated into a separate [`KeyRepeatEvent`](https://api.flutter.dev/flutter/services/KeyRepeatEvent-class.html) type.

Before:

dart

```
KeyEventResult _handleKeyEvent(RawKeyEvent keyEvent) {
  if (keyEvent is RawKeyDownEvent) {
    print('Key down: ${keyEvent.data.logicalKey.keyLabel}(${keyEvent.repeat ? ' (repeated)' : ''})');
  }
  return KeyEventResult.ignored;
}
```

After:

dart

```
KeyEventResult _handleKeyEvent(KeyEvent _) {
  if (keyEvent is KeyDownEvent || keyEvent is KeyRepeatEvent) {
    print('Key down: ${keyEvent.logicalKey.keyLabel}(${keyEvent is KeyRepeatEvent ? ' (repeated)' : ''})');
  }
  return KeyEventResult.ignored;
}
```

Though it is not a subclass of [`KeyDownEvent`](https://api.flutter.dev/flutter/services/KeyDownEvent-class.html), a [`KeyRepeatEvent`](https://api.flutter.dev/flutter/services/KeyRepeatEvent-class.html) is also a key down event. Don't assume that `keyEvent is! KeyDownEvent` only allows key up events. Check both `KeyDownEvent` and `KeyRepeatEvent`.

Timeline
--------

[#](#timeline)

Landed in version: 3.18.0-7.0.pre  
 In stable release: 3.19.0

References
----------

[#](#references)

Replacement API documentation:

* [`Focus.onKeyEvent`](https://api.flutter.dev/flutter/services/Focus/onKeyEvent.html)* [`FocusNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusNode/onKeyEvent.html)* [`FocusOnKeyEventCallback`](https://api.flutter.dev/flutter/services/FocusOnKeyEventCallback-class.html)* [`FocusScope.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScope/onKeyEvent.html)* [`FocusScopeNode.onKeyEvent`](https://api.flutter.dev/flutter/services/FocusScopeNode/onKeyEvent.html)* [`HardwareKeyboard`](https://api.flutter.dev/flutter/services/HardwareKeyboard-class.html)* [`KeyboardListener`](https://api.flutter.dev/flutter/services/KeyboardListener-class.html)* [`KeyDownEvent`](https://api.flutter.dev/flutter/services/KeyDownEvent-class.html)* [`KeyRepeatEvent`](https://api.flutter.dev/flutter/services/KeyRepeatEvent-class.html)* [`KeyEvent`](https://api.flutter.dev/flutter/services/KeyEvent-class.html)* [`KeyEventHandler`](https://api.flutter.dev/flutter/services/KeyEventHandler-class.html)* [`KeyUpEvent`](https://api.flutter.dev/flutter/services/KeyUpEvent-class.html)

Relevant issues:

* [`RawKeyEvent` and `RawKeyboard`, et al should be deprecated and removed (Issue 136419)](https://github.com/flutter/flutter/issues/136419)

Relevant PRs:

* [Deprecate RawKeyEvent, et al. and exempt uses in the framework.](https://github.com/flutter/flutter/pull/136677)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/key-event-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/key-event-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/key-event-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/key-event-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/key-event-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   