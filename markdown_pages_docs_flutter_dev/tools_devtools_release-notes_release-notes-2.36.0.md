1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.36.0 release notes](/tools/devtools/release-notes/release-notes-2.36.0)

DevTools 2.36.0 release notes
=============================

The 2.36.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](/tools/devtools).

Performance updates
-------------------

[#](#performance-updates)

* Added a feature for showing widget build counts. Enable this setting to see widget build counts for each Flutter frame in the "Frame Analysis" tool, or to see an aggregate summary of these counts in the new "Rebuild Stats" tool. - [#7838](https://github.com/flutter/devtools/pull/7838), [#7847](https://github.com/flutter/devtools/pull/7847)

  ![Track widget build counts setting](/tools/devtools/release-notes/images-2.36.0/track_build_counts_setting.png "Track widget build counts setting")

  ![Widget rebuild counts in the Frame Analysis view](/tools/devtools/release-notes/images-2.36.0/rebuild_counts_frame_analysis.png "Widget rebuilds counts for a flutter frame")

  ![Widget rebuild counts in the Rebuild Stats view](/tools/devtools/release-notes/images-2.36.0/rebuild_stats.png "Widget rebuilds counts aggregate stats")

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Added better support for narrow viewing windows, like when this screen is embedded in an IDE. - [#7726](https://github.com/flutter/devtools/pull/7726)

Deep links tool updates
-----------------------

[#](#deep-links-tool-updates)

* Adds an error page to explain the issue when the tool fails to parse the project. - [#7767](https://github.com/flutter/devtools/pull/7767)

DevTools Extension updates
--------------------------

[#](#devtools-extension-updates)

* Fixed an issue with detecting extensions for Dart or Flutter tests. - [#7717](https://github.com/flutter/devtools/pull/7717)* Fixed an issue with detecting extensions for nested Dart or Flutter projects. - [#7742](https://github.com/flutter/devtools/pull/7742)* Added an example to `package:devtools_extensions` that shows how to interact with the Dart Tooling Daemon from a DevTools extension. - [#7752](https://github.com/flutter/devtools/pull/7752)* Fixed a DevTools routing bug related to disabling an extension. - [#7791](https://github.com/flutter/devtools/pull/7791)* Fixed a bug causing a "Page Not Found" error when refreshing DevTools from an extension screen. - [#7822](https://github.com/flutter/devtools/pull/7822)* Fixed a theming issue when extensions are embedded in an IDE - [#7824](https://github.com/flutter/devtools/pull/7824)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.36.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.36.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.36.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.36.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.36.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.36.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.36.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.36.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   