1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.40.2 release notes](/tools/devtools/release-notes/release-notes-2.40.2)

DevTools 2.40.2 release notes
=============================

The 2.40.2 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](/tools/devtools/overview).

General updates
---------------

[#](#general-updates)

* Add a setting that allows users to opt in to loading DevTools with WebAssembly. - [#8270](https://github.com/flutter/devtools/pull/8270)

  ![Wasm opt-in setting](/tools/devtools/release-notes/images-2.40.2/wasm_setting.png "DevTools setting to opt into wasm.")* Removed the legacy Provider screen from DevTools. The `package:provider` tool is now distributed as a DevTools extension from `package:provider`. Upgrade your `package:provider` dependency to use the extension. - [#8364](https://github.com/flutter/devtools/pull/8364)* Fixed a bug that was causing the DevTools release notes to always show. - [#8277](https://github.com/flutter/devtools/pull/8277)* Added support for loading extensions in pub workspaces [8347](https://github.com/flutter/devtools/pull/8347).* Mapped error stack traces to use the Dart source code locations so that they are human-readable. - [#8385](https://github.com/flutter/devtools/pull/8385)* Added handling for IDE theme change events to update embedded DevTools UI. - [#8336](https://github.com/flutter/devtools/pull/8336)* Fixed a bug that was causing data filters to be cleared when clearing data on the Network and Logging screens. - [#8407](https://github.com/flutter/devtools/pull/8407)* Fixed a bug that was causing the navigator to lose state when opening the VM Flags dialog. - [#8413](https://github.com/flutter/devtools/pull/8413)* Tables match IDE theme when embedded in an IDE. - [#8498](https://github.com/flutter/devtools/pull/8498)

Inspector updates
-----------------

[#](#inspector-updates)

* Added a setting to the Flutter Inspector controls that allows users to opt in to the newly redesigned Flutter Inspector. - [#8342](https://github.com/flutter/devtools/pull/8342)

  ![New inspector opt-in setting](/tools/devtools/release-notes/images-2.40.2/new_inspector.png "DevTools setting to opt into the new Flutter Inspector.")

Performance updates
-------------------

[#](#performance-updates)

* Fixed an issue with the "Refreshing timeline" overlay that was getting shown when it should not have been. - [#8318](https://github.com/flutter/devtools/pull/8318)

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Resolved an issue in `.har` export where response content was sometimes missing in the data. - [#8333](https://github.com/flutter/devtools/pull/8333)

Deep links tool updates
-----------------------

[#](#deep-links-tool-updates)

* Added support for validating iOS deep link settings. - [#8394](https://github.com/flutter/devtools/pull/8394)

  ![Deep link validator for iOS](/tools/devtools/release-notes/images-2.40.2/deep_link_ios.png "DevTools Deep link validator Page")

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.40.2).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.40.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.40.2.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.40.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.40.2.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.40.2.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.40.2/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.40.2.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   