Flutter and Dart DevTools
=========================

1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools)

What is DevTools?
-----------------

[#](#what-is-devtools)

DevTools is a suite of performance and debugging tools for Dart and Flutter. *Flutter DevTools* and *Dart DevTools* refer to the same set of tools.

![Dart DevTools Screens](/assets/images/docs/tools/devtools/dart-devtools.webp)

For a video introduction to DevTools, check out the following deep dive and use-case walkthrough:

[Watch on YouTube in a new tab: "Dive in to Flutter and Dart DevTools"](https://www.youtube.com/watch/_EYk-E29edo)

What can I do with DevTools?
----------------------------

[#](#what-can-i-do-with-devtools)

Here are some of the things you can do with DevTools:

* Inspect the UI layout and state of a Flutter app.* Diagnose UI jank performance issues in a Flutter app.* CPU profiling for a Flutter or Dart app.* Network profiling for a Flutter app.* Source-level debugging of a Flutter or Dart app.* Debug memory issues in a Flutter or Dart command-line app.* View general log and diagnostics information about a running Flutter or Dart command-line app.* Analyze code and app size.* Validate deep links in your Android or iOS app.

We expect you to use DevTools in conjunction with your existing IDE or command-line based development workflow.

How to launch DevTools
----------------------

[#](#start)

You can launch DevTools with the following tools:

* [VS Code](/tools/devtools/vscode)* [Android Studio/IntelliJ](/tools/devtools/android-studio)* [command line](/tools/devtools/cli)

Troubleshooting some standard issues
------------------------------------

[#](#troubleshooting-some-standard-issues)

**Question**: My app looks janky or stutters. How do I fix it?

**Answer**: Performance issues can cause [UI frames](/perf/ui-performance) to be janky and/or slow down some operations.

1. To detect which code impacts concrete late frames, start at [Performance > Timeline](/tools/devtools/performance#timeline-events-tab).- To learn which code takes the most CPU time in the background, use the [CPU profiler](/tools/devtools/cpu-profiler).

For more information, check out the [Performance](/perf) page.

**Question**: I see a lot of garbage collection (GC) events occurring. Is this a problem?

**Answer**: Frequent GC events might display on the DevTools > Memory > Memory chart. In most cases, it's not a problem.

If your app has frequent background activity with some idle time, Flutter might use that opportunity to collect the created objects without performance impact.

Providing feedback
------------------

[#](#providing-feedback)

Please give DevTools a try, provide feedback, and file issues in the [DevTools issue tracker](https://github.com/flutter/devtools/issues). Thanks!

DevTools versioning
-------------------

[#](#devtools-versioning)

DevTools is distributed as part of the Flutter SDK. To get access to the latest DevTools functionality, run `flutter upgrade` to get the most up-to-date version of Flutter. To access DevTools features before they hit the Flutter `stable` channel, consider switching to the `beta` or `main` channels.

Other resources
---------------

[#](#other-resources)

For more information on debugging and profiling Flutter apps, see the [Debugging](/testing/debugging) page and, in particular, its list of [other resources](/testing/debugging#other-resources).

For more information on using DevTools with Dart command-line apps, see the [DevTools documentation on dart.dev](https://dart.dev/tools/dart-devtools).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-07-16. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   