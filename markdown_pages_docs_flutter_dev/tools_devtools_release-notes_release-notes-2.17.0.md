1. [Tools](/tools) chevron\_right- [Flutter and Dart DevTools](/tools/devtools) chevron\_right- [DevTools release notes](/tools/devtools/release-notes) chevron\_right- [2.17.0 release notes](/tools/devtools/release-notes/release-notes-2.17.0)

DevTools 2.17.0 release notes
=============================

The 2.17.0 release of the Dart and Flutter DevTools includes the following changes among other general improvements. To learn more about DevTools, check out the [DevTools overview](https://docs.flutter.dev/tools/devtools).

Inspector updates
-----------------

[#](#inspector-updates)

* Added support for manually setting the package directories for your app. If you've ever loaded the Inspector and noticed that some of your widgets aren't present in the widget tree, this might indicate that the package directories for your app haven't been set or detected properly. Your package directories determine which widgets the Inspector considers to be from *your* application. If you see an empty Inspector widget tree, or if you develop widgets across multiple packages, and want widgets from all these locations to show up in your tree, check the **Inspector Settings** dialog to ensure that your package directories are properly configured - [#4306](https://github.com/flutter/devtools/pull/4306)

  ![frame_analysis](/tools/devtools/release-notes/images-2.17.0/package_directories.png "package directories")

Performance updates
-------------------

[#](#performance-updates)

* Added a **Frame Analysis** tab to the Performance page. When analyzing a janky Flutter frame, this view provides hints for how to diagnose the jank and detects expensive operations that might have contributed to the slow frame time. This view also shows a breakdown of your Flutter frame time per phase (**Build**, **Layout**, **Paint**, and **Raster**) to try to guide you in the right direction - [#4339](https://github.com/flutter/devtools/pull/4339)

  ![frame_analysis](/tools/devtools/release-notes/images-2.17.0/frame_analysis.png "frame analysis")

Full commit history
-------------------

[#](#full-commit-history)

To find a complete list of changes since the previous release, check out [the diff on GitHub](https://github.com/flutter/devtools/compare/v2.16.0...v2.17.0).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.17.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.17.0.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.17.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.17.0.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.17.0.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/tools/devtools/release-notes/release-notes-2.17.0/&page-source=https://github.com/flutter/website/tree/main/src/content/tools/devtools/release-notes/release-notes-2.17.0.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   