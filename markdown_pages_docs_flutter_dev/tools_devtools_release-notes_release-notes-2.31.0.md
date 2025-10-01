1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.31.0 release notes](/tools/devtools/release-notes/release-notes-2.31.0)

DevTools 2.31.0 release notes
=============================

The 2.31.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Added a new feature for deep link validation, supporting deep link web checks on Android. - [#6935](https://github.com/flutter/devtools/pull/6935)* Added the basic plumbing to allow connections to a Dart Tooling Daemon. - [#7009](https://github.com/flutter/devtools/pull/7009)* Made table text selectable [#6919](https://github.com/flutter/devtools/pull/6919)

Inspector updates
-----------------

[#](#inspector-updates)

* When done typing in the search field, the next selection is now automatically selected - [#6677](https://github.com/flutter/devtools/pull/6677)* Added link to package directory documentation, from the inspect settings dialog - [#6825](https://github.com/flutter/devtools/pull/6825)

    ![Link to documentation](/tools/devtools/release-notes/images-2.31.0/link-to-doc.png "Link to documentation")* Fix bug where widgets owned by the Flutter framework were showing up in the widget tree view - [#6857](https://github.com/flutter/devtools/pull/6857)* Only cache pub root directories added by the user - [#6897](https://github.com/flutter/devtools/pull/6897)* Remove Flutter pub root if it was accidentally cached - [#6911](https://github.com/flutter/devtools/pull/6911)

Performance updates
-------------------

[#](#performance-updates)

* Changed raster layer preview background to a checkerboard. - [#6827](https://github.com/flutter/devtools/pull/6827)

CPU profiler updates
--------------------

[#](#cpu-profiler-updates)

* Added hover cards to show sampling rate for the item in drop down. - [#7010](https://github.com/flutter/devtools/pull/7010)

  ![Sampling rate for dropdown](/tools/devtools/release-notes/images-2.31.0/hover-for-dropdown.png "Sampling rate for dropdown")

Debugger updates
----------------

[#](#debugger-updates)

* Highlight `extension type` as a declaration keyword, highlight the `$` in identifier interpolation as part of the interpolation, and properly highlight comments within type arguments. - [6837](https://github.com/flutter/devtools/pull/6837)

Logging updates
---------------

[#](#logging-updates)

* Added scrollbar to details pane. - [#6917](https://github.com/flutter/devtools/pull/6917)

VS Code Sidebar updates
-----------------------

[#](#vs-code-sidebar-updates)

* Fixed an issue that prevented the VS code sidebar from loading in recent beta/master builds. - [#6984](https://github.com/flutter/devtools/pull/6984)

DevTools Extension updates
--------------------------

[#](#devtools-extension-updates)

* Fixed a couple bugs preventing Dart server apps from connecting to DevTools extensions. - [#6982](https://github.com/flutter/devtools/pull/6982), [#6993](https://github.com/flutter/devtools/pull/6993)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.31.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.31.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.31.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.31.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.31.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.31.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.31.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.31.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   