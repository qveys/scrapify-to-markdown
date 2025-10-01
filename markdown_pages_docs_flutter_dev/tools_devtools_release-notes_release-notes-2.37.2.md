1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.37.2 release notes](/tools/devtools/release-notes/release-notes-2.37.2)

DevTools 2.37.2 release notes
=============================

The 2.37.2 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](/tools/devtools/overview).

General updates
---------------

[#](#general-updates)

* Improved messaging when a screen is unavailable for the platform of the connected app. - [#7958](https://github.com/flutter/devtools/pull/7958)* Fixed a bug where an infinite spinner was shown upon app disconnect. - [#7992](https://github.com/flutter/devtools/pull/7992)* Fixed a bug where trying to reuse a disconnected DevTools instance would fail. - [#8009](https://github.com/flutter/devtools/pull/8009)

Performance updates
-------------------

[#](#performance-updates)

* Removed the "Raster Stats" feature. This tool did not work for the Impeller rendering engine, and the information it gave for the SKIA rendering engine was often misleading and unactionable. Users should follow the official Flutter guidance for [Performance and optimization](/perf) when debugging the rendering performance of their Flutter apps. - [#7981](https://github.com/flutter/devtools/pull/7981).

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Fixed an issue where socket statistics were being reported as web sockets. - [#8061](https://github.com/flutter/devtools/pull/8061)

  ![Network profiler correctly displaying socket statistics](/tools/devtools/release-notes/images-2.37.2/socket-profiling.png "Network profiler correctly displaying socket statistics")* Added query parameters to the request details view. - [#7825](https://github.com/flutter/devtools/pull/7825)

VS Code Sidebar updates
-----------------------

[#](#vs-code-sidebar-updates)

* Added buttons for all DevTools tools in the sidebar by default, even when there are no debug sessions available. - [#7947](https://github.com/flutter/devtools/pull/7947)

  ![DevTools tools in the sidebar](/tools/devtools/release-notes/images-2.37.2/devtools_in_sidebar.png)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.37.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.37.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.37.2.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.37.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.37.2.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.37.2.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.37.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.37.2.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   