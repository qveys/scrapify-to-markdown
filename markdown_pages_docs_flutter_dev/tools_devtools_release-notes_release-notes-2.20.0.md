1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.20.0 release notes](/tools/devtools/release-notes/release-notes-2.20.0)

DevTools 2.20.0 release notes
=============================

The 2.20.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

CPU profiler updates
--------------------

[#](#cpu-profiler-updates)

* Add support for grouping samples by tag - [#4693](https://github.com/flutter/devtools/pull/4693)

  ![samples by tag](/tools/devtools/release-notes/images-2.20.0/4693.png "samples by tag")* Enable guidelines for tree view - [#4722](https://github.com/flutter/devtools/pull/4722)

    ![guidelines](/tools/devtools/release-notes/images-2.20.0/4722.png "guidelines")* Rename "Profile granularity" to "CPU sampling rate" and move down to the area it relates to - [#4803](https://github.com/flutter/devtools/pull/4722)

      ![sampling rate](/tools/devtools/release-notes/images-2.20.0/4803.png "sampling rate")

Memory updates
--------------

[#](#memory-updates)

* Retire the **Analysis** tab - [#4714](https://github.com/flutter/devtools/pull/4714)* Add a new tab, **Diff**, to enable memory leak detection and troubleshooting by comparing heap snapshots, providing insights about the number of instances, shallow size, retained size, and retaining paths - [#4714](https://github.com/flutter/devtools/pull/4714)

    ![diff](/tools/devtools/release-notes/images-2.20.0/4714.png "Diff in Memory tab")

Debugger updates
----------------

[#](#debugger-updates)

* Support for inspecting more types of instances in the variables viewer (Expandos, Types, TypeArguments, Parameters, Closures + closure Contexts, WeakProperty, Function, FunctionType, ReceivePort, Closure, RegExp) - [#4760](https://github.com/flutter/devtools/pull/4760)* Add support for displaying coverage in CodeView - [#4700](https://github.com/flutter/devtools/pull/4700)

    ![coverage](/tools/devtools/release-notes/images-2.20.0/4700.png "coverage in CodeView")

Network updates
---------------

[#](#network-updates)

* Display request data if content type is not json (thanks to @leungpuikuen!) - [#4602](https://github.com/flutter/devtools/pull/4602)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.19.0...v2.20.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.20.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.20.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.20.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.20.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.20.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.20.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.20.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   