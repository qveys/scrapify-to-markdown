Restore state on iOS
====================

1. [Platform integration](/platform-integration) chevron\_right- [iOS](/platform-integration/ios) chevron\_right- [Restore state on iOS](/platform-integration/ios/restore-state-ios)

When a user runs a mobile app and then selects another app to run, the first app is moved to the background, or *backgrounded*. The operating system (both iOS and Android) often kills the backgrounded app to release memory or improve performance for the app running in the foreground.

You can use the [`RestorationManager`](https://api.flutter.dev/flutter/services/RestorationManager-class.html) (and related) classes to handle state restoration. An iOS app requires [a bit of extra setup](https://api.flutter.dev/flutter/services/RestorationManager-class.html#state-restoration-on-ios) in Xcode, but the restoration classes otherwise work the same on both iOS and Android.

For more information, check out [State restoration on Android](/platform-integration/android/restore-state-android) and the [VeggieSeasons](https://github.com/samples/demos/tree/main/veggieseasons) code sample.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/restore-state-ios/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/restore-state-ios.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/restore-state-ios/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/restore-state-ios.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/restore-state-ios.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/restore-state-ios/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/restore-state-ios.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   