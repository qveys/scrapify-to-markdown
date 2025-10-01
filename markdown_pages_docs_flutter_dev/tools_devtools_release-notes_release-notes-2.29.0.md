1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.29.0 release notes](/tools/devtools/release-notes/release-notes-2.29.0)

DevTools 2.29.0 release notes
=============================

The 2.29.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Fix a bug with service extension states not being cleared on app disconnect. - [#6547](https://github.com/flutter/devtools/pull/6547)* Improved styling of bottom status bar when connected to an app. - [#6525](https://github.com/flutter/devtools/pull/6525)* Added a workaround to fix copy button functionality in VSCode. - [#6598](https://github.com/flutter/devtools/pull/6598)

Performance updates
-------------------

[#](#performance-updates)

* Added an option in the "Enhance Tracing" menu for tracking platform channel activity. This is useful for apps with plugins. - [#6515](https://github.com/flutter/devtools/pull/6515)

  ![Track platform channels setting](/tools/devtools/release-notes/images-2.29.0/track_platform_channels.png "Track platform channels setting")* Made the Performance screen available when there is no connected app. Performance data that was previously saved from DevTools can be reloaded for viewing from this screen. - [#6567](https://github.com/flutter/devtools/pull/6567)* Added an "Open" button to the Performance controls for loading data that was previously saved from DevTools. - [#6567](https://github.com/flutter/devtools/pull/6567)

      ![Open file button on the performance screen](/tools/devtools/release-notes/images-2.29.0/open_file_performance_screen.png "Open file button on the performance screen")

CPU profiler updates
--------------------

[#](#cpu-profiler-updates)

* Tree guidelines are now always enabled for the "Bottom Up" and "Call Tree" tabs. - [#6534](https://github.com/flutter/devtools/pull/6534)* Made the CPU profiler screen available when there is no connected app. CPU profiles that were previously saved from DevTools can be reloaded for viewing from this screen. - [#6567](https://github.com/flutter/devtools/pull/6567)* Added an "Open" button to the CPU profiler controls for loading data that was previously saved from DevTools. - [#6567](https://github.com/flutter/devtools/pull/6567)

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Network statuses now show with an error color when the request failed. - [#6527](https://github.com/flutter/devtools/pull/6527)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.29.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.29.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.29.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.29.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.29.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.29.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.29.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.29.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   