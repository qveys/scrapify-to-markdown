1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.24.0 release notes](/tools/devtools/release-notes/release-notes-2.24.0)

DevTools 2.24.0 release notes
=============================

The 2.24.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Improve the overall performance of DevTools tables - [#5664](https://github.com/flutter/devtools/pull/5664), [#5696](https://github.com/flutter/devtools/pull/5696)

CPU profiler updates
--------------------

[#](#cpu-profiler-updates)

* Fix bug with CPU flame chart selection and tooltips - [#5676](https://github.com/flutter/devtools/pull/5676)

Debugger updates
----------------

[#](#debugger-updates)

* Improve support for inspecting `UserTag` and `MirrorReferent` instances - [#5490](https://github.com/flutter/devtools/pull/5490)* Fix expression evaluation bug where selecting an autocomplete result for a field would clear the current input - [#5717](https://github.com/flutter/devtools/pull/5717)* Make selection of a stack frame scroll to the frame location in the source code - [#5722](https://github.com/flutter/devtools/pull/5722)* Improve performance of searching for a file and searching in a file - [#5733](https://github.com/flutter/devtools/pull/5733)* Disable syntax highlighting for files with more than 100,000 characters due to performance constraints - [#5743](https://github.com/flutter/devtools/pull/5743)* Fix bug where source code wasn't visible if syntax highlighting for a file was disabled - [#5743](https://github.com/flutter/devtools/pull/5743)* Prevent file names and source code from getting out of sync - [#5827](https://github.com/flutter/devtools/pull/5827)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.23.1...v2.24.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.24.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.24.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.24.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.24.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.24.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.24.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.24.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   