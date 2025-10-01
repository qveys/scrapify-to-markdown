1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.14.0 release notes](/tools/devtools/release-notes/release-notes-2.14.0)

DevTools 2.14.0 release notes
=============================

The 2.14.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Added a link to the new DevTools [Discord channel](https://discord.com/channels/608014603317936148/958862085297672282) in the About DevTools dialog - [#4102](https://github.com/flutter/devtools/pull/4102)

  ![about-devtools](/tools/devtools/release-notes/images-2.14.0/image1.png "about devtools")

Network updates
---------------

[#](#network-updates)

* Added "Copy as URL" and "Copy as cURL" actions for selected requests in the network profiler (special thanks to [@jankuss](https://github.com/jankuss)!) - [#4113](https://github.com/flutter/devtools/pull/4113)

  ![network-request-copy-actions](/tools/devtools/release-notes/images-2.14.0/image2.png "network request copy actions")

Flutter inspector updates
-------------------------

[#](#flutter-inspector-updates)

* Added a setting to control whether hovering over a widget in the inspector displays its properties and values in a hover card - [#4090](https://github.com/flutter/devtools/pull/4090)

Debugger updates
----------------

[#](#debugger-updates)

* Added auto complete suggestions in the console (special thanks to [@jankuss](https://github.com/jankuss)!) - [#4062](https://github.com/flutter/devtools/pull/4062)

  ![auto-complete-suggestions](/tools/devtools/release-notes/images-2.14.0/image3.png "auto complete suggestions")* Added the option to copy the full file path for a selected library - [#4147](https://github.com/flutter/devtools/pull/4147)* Fixed formatting in the debugger exception menu - [#4066](https://github.com/flutter/devtools/pull/4066)

Memory updates
--------------

[#](#memory-updates)

* Fixed formatting for memory values in the heap tree view - [#4153](https://github.com/flutter/devtools/pull/4153)* Fixed a bug that was preventing GC events from showing up in the memory chart - [#4131](https://github.com/flutter/devtools/pull/4131)

Performance updates
-------------------

[#](#performance-updates)

* Warn users that the rendering layer toggles in the "More Debugging Options" menu are not available for profile mode apps - [#4075](https://github.com/flutter/devtools/pull/4075)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.13.1...v2.14.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.14.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.14.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.14.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.14.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.14.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.14.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.14.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   