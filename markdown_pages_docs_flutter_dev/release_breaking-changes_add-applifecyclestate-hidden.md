Migration guide for adding AppLifecycleState.hidden
===================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for adding AppLifecycleState.hidden](/release/breaking-changes/add-applifecyclestate-hidden)

Summary
-------

[#](#summary)

A new `hidden` state was added to the [`AppLifecycleState`](https://api.flutter.dev/flutter/dart-ui/AppLifecycleState.html) enum to denote when the application is not visible.

Context
-------

[#](#context)

The `AppLifecycleState` enum is used to indicate which lifecycle state the application is in when [`WidgetsBindingObserver.didChangeAppLifecycleState`](https://api.flutter.dev/flutter/widgets/WidgetsBindingObserver/didChangeAppLifecycleState.html) is called.

Description of change
---------------------

[#](#description-of-change)

The new state `AppLifecycleState.hidden` was added to the `AppLifecycleState` enum in the `dart:ui` package.

The `hidden` state is entered when all of the application views are no longer visible to the user. On Android and iOS, this state is entered briefly whenever the state machine traverses from inactive to paused, or from paused to inactive. It doesn't change when paused or inactive are entered. On other platforms, it will be in this state while the application is not visible.

Migration guide
---------------

[#](#migration-guide)

If code has switch statements that handle all cases of the `AppLifecycleState` enum, a new case will need to be added to handle the `AppLifecycleState.hidden` state.

Code before migration:

dart

```
void didChangeAppLifecycleState(AppLifecycleState state) {
  switch (state) {
    case AppLifecycleState.resumed:
    case AppLifecycleState.inactive:
      // Do something when the app is visible...
      break;
    case AppLifecycleState.paused:
    case AppLifecycleState.detached:
      // Do something when the app is not visible...
      break;
  }
}
```

Code after migration:

dart

```
void didChangeAppLifecycleState(AppLifecycleState state) {
  switch (state) {
    case AppLifecycleState.resumed:
    case AppLifecycleState.inactive:
      // Do something when the app is visible...
      break;
    case AppLifecycleState.hidden:  // <-- This is the new state.
    case AppLifecycleState.paused:
    case AppLifecycleState.detached:
      // Do something when the app is not visible...
      break;
  }
}
```

If there is already a `default:` case in the switch statement, or the code uses conditionals instead, then the code will compile without changes, but the default case or conditional will still need to be evaluated to decide if the `hidden` state should also be handled.

Timeline
--------

[#](#timeline)

Landed in version: 3.11.0-16.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

Relevant PRs:

* [PR 42418](https://github.com/flutter/engine/pull/42418): Adds `AppLifecycleState.hidden` enum value

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-applifecyclestate-hidden/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-applifecyclestate-hidden.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-applifecyclestate-hidden/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-applifecyclestate-hidden.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-applifecyclestate-hidden.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-applifecyclestate-hidden/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-applifecyclestate-hidden.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   