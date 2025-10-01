Dropping support for Android KitKat
===================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Dropping support for Android KitKat](/release/breaking-changes/android-kitkat-deprecation)

Summary
-------

[#](#summary)

Flutter's minimum supported Android version is now Lollipop (API 21). Beginning with Flutter's 3.22 stable release, Flutter will no longer work on devices running Android KitKat (API 19).

Context
-------

[#](#context)

The context, purpose, and description of this deprecation can be found in the [go/rfc-android-k-deprecation](https://flutter.dev/go/rfc-android-k-deprecation) design document.

Migration guide
---------------

[#](#migration-guide)

Flutter developers targeting Android will need to increase the `minSdkVersion` in their `build.gradle` and `AndroidManifest.xml` files from `19` to at least `21`.

Timeline
--------

[#](#timeline)

In stable release: 3.22

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-kitkat-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-kitkat-deprecation.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-kitkat-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-kitkat-deprecation.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-kitkat-deprecation.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-kitkat-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-kitkat-deprecation.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   