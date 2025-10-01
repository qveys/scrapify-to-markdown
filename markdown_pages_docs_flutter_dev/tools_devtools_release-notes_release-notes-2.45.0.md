1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.45.0 release notes](/tools/devtools/release-notes/release-notes-2.45.0)

DevTools 2.45.0 release notes
=============================

The 2.45.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](/tools/devtools/overview).

General updates
---------------

[#](#general-updates)

* Added a memory pressure warning that allows you to reduce the memory usage of DevTools in order to avoid an OOM crash. - [#8989](https://github.com/flutter/devtools/pull/8989), [#8997](https://github.com/flutter/devtools/pull/8997), [#8998](https://github.com/flutter/devtools/pull/8998)* Fix a bug with the review history on disconnect experience. - [#8985](https://github.com/flutter/devtools/pull/8985)* Fixed bug where DevTools would automatically resume instead of pausing on breakpoint on connection. - [#8991](https://github.com/flutter/devtools/pull/8991)* Prevented text inputs from stealing focus from the IDE. - [#9091](https://github.com/flutter/devtools/pull/9091)

Inspector updates
-----------------

[#](#inspector-updates)

* Fixed bug where errors in the inspector tree (e.g. RenderFlex overflow errors) were not removed after a hot-reload. - [#9106](https://github.com/flutter/devtools/pull/9106)

Debugger updates
----------------

[#](#debugger-updates)

* Combine the Pause and Resume buttons into a single button. - [#9095](https://github.com/flutter/devtools/pull/9095)

Deep links tool updates
-----------------------

[#](#deep-links-tool-updates)

* Fixed an issue with Windows file paths showing incorrectly in the Deep Links page [#9027](https://github.com/flutter/devtools/pull/9027).* Fixed an issue with the Deep Links page crashing when no iOS configuration is present [#9027](https://github.com/flutter/devtools/pull/9027).

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes in this release, check out the [DevTools git log](https://github.com/flutter/devtools/tree/v2.45.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.45.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.45.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.45.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.45.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.45.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.45.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.45.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   