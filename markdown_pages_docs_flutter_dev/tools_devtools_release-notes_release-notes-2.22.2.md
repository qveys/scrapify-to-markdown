1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.22.2 release notes](/tools/devtools/release-notes/release-notes-2.22.2)

DevTools 2.22.2 release notes
=============================

The 2.22.2 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Prevent crashes if there is no main isolate - [#5232](https://github.com/flutter/devtools/pull/5232)

CPU profiler updates
--------------------

[#](#cpu-profiler-updates)

* Display stack frame URI inline with method name to ensure the URI is always visible in deeply nested trees - [#5181](https://github.com/flutter/devtools/pull/5181)

  ![inline uri](/tools/devtools/release-notes/images-2.22.2/5181.png "inline uri")* Add the ability to filter by method name or source URI - [#5204](https://github.com/flutter/devtools/pull/5204)

Memory updates
--------------

[#](#memory-updates)

* Change filter default to show only project and 3rd party dependencies - [#5201](https://github.com/flutter/devtools/pull/5201).

  ![filter default](/tools/devtools/release-notes/images-2.22.2/5201.png "filter default")* Support expression evaluation in console for running application - [#5248](https://github.com/flutter/devtools/pull/5248).

    ![evaluation](/tools/devtools/release-notes/images-2.22.2/5248.png "evaluation")* Add column `Persisted` for memory diffing - [#5290](https://github.com/flutter/devtools/pull/5290)

      ![persisted](/tools/devtools/release-notes/images-2.22.2/5290.png "persisted")

Debugger updates
----------------

[#](#debugger-updates)

* Add support for browser navigation history when navigating using the File Explorer - [#4906](https://github.com/flutter/devtools/pull/4906)* Designate positional fields for `Record` types with the getter syntax beginning at `$1` - [#5272](https://github.com/flutter/devtools/pull/5272)* Fix variable inspection for `Map` and `List` instances - [#5320](https://github.com/flutter/devtools/pull/5320)

      ![map and list](/tools/devtools/release-notes/images-2.22.2/5320.png "map and list")* Fix variable inspection for `Set` instances - [#5323](https://github.com/flutter/devtools/pull/5323)

        ![set](/tools/devtools/release-notes/images-2.22.2/5323.png "set")

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Improve reliability and performance of the Network tab - [#5056](https://github.com/flutter/devtools/pull/5056)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.21.1...v2.22.2).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.22.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.22.2.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.22.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.22.2.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.22.2.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.22.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.22.2.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   