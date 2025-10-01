1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.28.3 release notes](/tools/devtools/release-notes/release-notes-2.28.3)

DevTools 2.28.3 release notes
=============================

The 2.28.3 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

This was a cherry-pick release on top of DevTools 2.28.2. To learn about the improvements included in DevTools 2.28.2, please read the [release notes](/tools/devtools/release-notes/release-notes-2.28.2).

General updates
---------------

[#](#general-updates)

* Added a link to the new "Dive in to DevTools" YouTube [video](https://www.youtube.com/watch?v=_EYk-E29edo) in the bottom status bar. This video provides a brief tutorial for each DevTools screen. [#6554](https://github.com/flutter/devtools/pull/6554)

  ![Link to watch a DevTools tutorial video](/tools/devtools/release-notes/images-2.28.3/watch_tutorial_link.png "Link to watch a DevTools tutorial video")* Added a workaround to fix copy button functionality in VSCode. - [#6598](https://github.com/flutter/devtools/pull/6598)

Performance updates
-------------------

[#](#performance-updates)

* Disable the Raster Stats tool for the Impeller backend since it is not supported. - [#6616](https://github.com/flutter/devtools/pull/6616)

VS Code Sidebar updates
-----------------------

[#](#vs-code-sidebar-updates)

* When using VS Code with a light theme, the embedded sidebar provided by DevTools will now also show in the light theme. - [#6581](https://github.com/flutter/devtools/pull/6581)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.28.3).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.28.3/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.28.3.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.28.3/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.28.3.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.28.3.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.28.3/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.28.3.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   