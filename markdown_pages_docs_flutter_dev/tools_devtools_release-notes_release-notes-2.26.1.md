1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.26.1 release notes](/tools/devtools/release-notes/release-notes-2.26.1)

DevTools 2.26.1 release notes
=============================

The 2.26.1 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

General updates
---------------

[#](#general-updates)

* Added a new "Home" screen in DevTools that either shows the "Connect" dialog or a summary of your connected app, depending on the connection status in DevTools. Keep an eye on this screen for cool new features in the future. This change also enables support for static tooling (tools that don't require a connected app) in DevTools - [#6010](https://github.com/flutter/devtools/pull/6010)

  ![home screen](/tools/devtools/release-notes/images-2.26.1/home_screen.png "DevTools home screen")* Fixed overlay notifications so that they cover the area that their background blocks - [#5975](https://github.com/flutter/devtools/pull/5975)

Memory updates
--------------

[#](#memory-updates)

* Added a context menu to rename or delete a heap snapshot from the list - [#5997](https://github.com/flutter/devtools/pull/5997)* Warn users when HTTP logging may be affecting their app's memory consumption - [#5998](https://github.com/flutter/devtools/pull/5998)

Debugger updates
----------------

[#](#debugger-updates)

* Improvements to text selection and copy behavior in the code view, console, and variables windows - [#6020](https://github.com/flutter/devtools/pull/6020)

Network profiler updates
------------------------

[#](#network-profiler-updates)

* Added a selector to customize the display type of text and json responses (thanks to @hhacker1999!) - [#5816](https://github.com/flutter/devtools/pull/5816)

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.25.0...v2.26.1).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.26.1/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.26.1.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.26.1/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.26.1.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.26.1.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.26.1/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.26.1.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   