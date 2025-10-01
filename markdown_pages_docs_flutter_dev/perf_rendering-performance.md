Improving rendering performance
===============================

1. [Performance](/perf) chevron\_right- [Improving rendering performance](/perf/rendering-performance)

*info* Note

To learn how to use the **Performance View** (part of Flutter DevTools) for debugging performance issues, see [Using the Performance view](/tools/devtools/performance).

Rendering animations in your app is one of the most cited topics of interest when it comes to measuring performance. Thanks in part to Flutter's Skia engine and its ability to quickly create and dispose of widgets, Flutter applications are performant by default, so you only need to avoid common pitfalls to achieve excellent performance.

General advice
--------------

[#](#general-advice)

If you see janky (non-smooth) animations, make **sure** that you are profiling performance with an app built in *profile* mode. The default Flutter build creates an app in *debug* mode, which is not indicative of release performance. For information, see [Flutter's build modes](/testing/build-modes).

A couple common pitfalls:

* Rebuilding far more of the UI than expected each frame. To track widget rebuilds, see [Show performance data](/tools/android-studio#show-performance-data).* Building a large list of children directly, rather than using a ListView.

For more information on evaluating performance including information on common pitfalls, see the following docs:

* [Performance best practices](/perf/best-practices)* [Flutter performance profiling](/perf/ui-performance)

Mobile-only advice
------------------

[#](#mobile-only-advice)

Do you see noticeable jank on your mobile app, but only on the first run of an animation? To avoid this, make sure you're using Flutter's default graphic renderer, [Impeller](/perf/impeller).

Web-only advice
---------------

[#](#web-only-advice)

The following series of articles cover what the Flutter Material team learned when improving performance of the Flutter Gallery app on the web:

* [Optimizing performance in Flutter web apps with tree shaking and deferred loading](https://blog.flutter.dev/optimizing-performance-in-flutter-web-apps-with-tree-shaking-and-deferred-loading-535fbe3cd674)* [Improving perceived performance with image placeholders, precaching, and disabled navigation transitions](https://blog.flutter.dev/improving-perceived-performance-with-image-placeholders-precaching-and-disabled-navigation-6b3601087a2b)* [Building performant Flutter widgets](https://blog.flutter.dev/building-performant-flutter-widgets-3b2558aa08fa)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/rendering-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/rendering-performance.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/rendering-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/rendering-performance.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-12-19. [View source](https://github.com/flutter/website/tree/main/src/content/perf/rendering-performance.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/rendering-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/rendering-performance.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   