Debug performance for web apps
==============================

1. [Performance](/perf) chevron\_right- [Debug performance for web apps](/perf/web-performance)

*info* Note

Profiling Flutter web apps requires Flutter version 3.14 or later.

The Flutter framework emits timeline events as it works to build frames, draw scenes, and track other activity such as garbage collections. These events are exposed in the [Chrome DevTools performance panel](https://developer.chrome.com/docs/devtools/performance) for debugging.

*info* Note

For information on how to optimize web loading speed, check out the (free) article on Medium, [Best practices for optimizing Flutter web loading speed](https://blog.flutter.dev/best-practices-for-optimizing-flutter-web-loading-speed-7cc0df14ce5c).

You can also emit your own timeline events using the `dart:developer` [Timeline](https://api.flutter.dev/flutter/dart-developer/Timeline-class.html) and [TimelineTask](https://api.flutter.dev/flutter/dart-developer/TimelineTask-class.html) APIs for further performance analysis.

![Screenshot of the Chrome DevTools performance panel](/assets/images/docs/tools/devtools/chrome-devtools-performance-panel.png)

Optional flags to enhance tracing
---------------------------------

[#](#optional-flags-to-enhance-tracing)

To configure which timeline events are tracked, set any of the following top-level properties to `true` in your app's `main` method.

* [debugProfileBuildsEnabled](https://api.flutter.dev/flutter/widgets/debugProfileBuildsEnabled.html): Adds `Timeline` events for every `Widget` built.* [debugProfileBuildsEnabledUserWidgets](https://api.flutter.dev/flutter/widgets/debugProfileBuildsEnabledUserWidgets.html): Adds `Timeline` events for every user-created `Widget` built.* [debugProfileLayoutsEnabled](https://api.flutter.dev/flutter/rendering/debugProfileLayoutsEnabled.html): Adds `Timeline` events for every `RenderObject` layout.* [debugProfilePaintsEnabled](https://api.flutter.dev/flutter/rendering/debugProfilePaintsEnabled.html): Adds `Timeline` events for every `RenderObject` painted.

Instructions
------------

[#](#instructions)

1. *[Optional]* Set any desired tracing flags to true from your app's main method.- Run your Flutter web app in [profile mode](/testing/build-modes#profile).- Open up the [Chrome DevTools Performance panel](https://developer.chrome.com/docs/devtools/performance) for your application, and [start recording](https://developer.chrome.com/docs/devtools/performance/#record) to capture timeline events.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/web-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/web-performance.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/web-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/web-performance.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-05-06. [View source](https://github.com/flutter/website/tree/main/src/content/perf/web-performance.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/perf/web-performance/&page-source=https://github.com/flutter/website/tree/main/src/content/perf/web-performance.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   