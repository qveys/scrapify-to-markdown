Restore state on Android
========================

1. [Platform integration](/platform-integration) chevron\_right- [Android](/platform-integration/android) chevron\_right- [Restore state on Android](/platform-integration/android/restore-state-android)

When a user runs a mobile app and then selects another app to run, the first app is moved to the background, or *backgrounded*. The operating system (both iOS and Android) might kill the backgrounded app to release memory and improve performance for the app running in the foreground.

When the user selects the app again, bringing it back to the foreground, the OS relaunches it. But, unless you've set up a way to save the state of the app before it was killed, you've lost the state and the app starts from scratch. The user has lost the continuity they expect, which is clearly not ideal. (Imagine filling out a lengthy form and being interrupted by a phone call *before* clicking **Submit**.)

So, how can you restore the state of the app so that it looks like it did before it was sent to the background?

Flutter has a solution for this with the [`RestorationManager`](https://api.flutter.dev/flutter/services/RestorationManager-class.html) (and related classes) in the [services](https://api.flutter.dev/flutter/services/services-library.html) library. With the `RestorationManager`, the Flutter framework provides the state data to the engine *as the state changes*, so that the app is ready when the OS signals that it's about to kill the app, giving the app only moments to prepare.

Instance state vs long-lived state

When should you use the `RestorationManager` and when should you save state to long term storage? *Instance state* (also called *short-term* or *ephemeral* state), includes unsubmitted form field values, the currently selected tab, and so on. On Android, this is limited to 1 MB and, if the app exceeds this, it crashes with a `TransactionTooLargeException` error in the native code.

Overview
--------

[#](#overview)

You can enable state restoration with just a few tasks:

1. Define a `restorationScopeId` for classes like `CupertinoApp`, `MaterialApp`, or `WidgetsApp`.- Define a `restorationId` for widgets that support it, such as [`TextField`](https://api.flutter.dev/flutter/material/TextField/restorationId.html) and [`ScrollView`](https://api.flutter.dev/flutter/widgets/ScrollView/restorationId.html). This automatically enables built-in state restoration for those widgets.- For custom widgets, you must decide what state you want to restore and hold that state in a [`RestorableProperty`](https://api.flutter.dev/flutter/widgets/RestorableProperty-class.html). (The Flutter API provides various subclasses for different data types.) Define those `RestorableProperty` widgets in a `State` class that uses the [`RestorationMixin`](https://api.flutter.dev/flutter/widgets/RestorationMixin-mixin.html). Register those widgets with the mixin in a `restoreState` method.- If you use any Navigator API (like `push`, `pushNamed`, and so on) migrate to the API that has "restorable" in the name (`restorablePush`, `restorablePushNamed`, and so on) to restore the navigation stack.

Other considerations:

* Providing a `restorationScopeId` to `MaterialApp`, `CupertinoApp`, or `WidgetsApp` automatically enables state restoration by injecting a `RootRestorationScope`. If you need to restore state *above* the app class, inject a `RootRestorationScope` manually.* **The difference between a `restorationId` and a `restorationScopeId`:** Widgets that take a `restorationScopeId` create a new `restorationScope` (a new `RestorationBucket`) into which all children store their state. A `restorationId` means the widget (and its children) store the data in the surrounding bucket.

Restoring navigation state
--------------------------

[#](#restoring-navigation-state)

If you want your app to return to a particular route that the user was most recently viewing (the shopping cart, for example), then you must implement restoration state for navigation, as well.

If you use the Navigator API directly, migrate the standard methods to restorable methods (that have "restorable" in the name). For example, replace `push` with [`restorablePush`](https://api.flutter.dev/flutter/widgets/Navigator/restorablePush.html).

Testing state restoration
-------------------------

[#](#testing-state-restoration)

To test state restoration, set up your mobile device so that it doesn't save state once an app is backgrounded. To learn how to do this for both iOS and Android, check out [Testing state restoration](https://api.flutter.dev/flutter/services/RestorationManager-class.html#testing-state-restoration) on the [`RestorationManager`](https://api.flutter.dev/flutter/services/RestorationManager-class.html) page.

*warning* Warning

Don't forget to reenable storing state on your device once you are finished with testing!

Other resources
---------------

[#](#other-resources)

For further information on state restoration, check out the following resources.

* To learn more about short term and long term state, check out [Differentiate between ephemeral state and app state](/data-and-backend/state-mgmt/ephemeral-vs-app).* You might want to check out packages on pub.dev that perform state restoration, such as [`statePersistence`](https://pub.dev/packages/state_persistence).* For more information on navigation and the [`go_router`](https://pub.dev/packages/go_router) package, check out [Navigation and routing](/ui/navigation) and the [State restoration](https://pub.dev/documentation/go_router/latest/topics/State%20restoration-topic.html) topic on pub.dev.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/restore-state-android/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/restore-state-android.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/restore-state-android/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/restore-state-android.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-23. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/android/restore-state-android.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/restore-state-android/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/restore-state-android.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   