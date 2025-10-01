Merged threads on macOS and Windows
===================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Merged threads on macOS and Windows](/release/breaking-changes/macos-windows-merged-threads)

Summary
-------

[#](#summary)

Flutter 3.35 merges the UI and platform threads by default on macOS and Windows.

Context
-------

[#](#context)

Originally, Flutter had separate threads to produce UI frames and to interact with the native platform.

The split-thread design prevented Flutter apps and plugins from using Dart FFI to interoperate with native APIs that must be called on the platform thread.

Description of change
---------------------

[#](#description-of-change)

Flutter 3.35 merges the UI and platform threads by default on macOS and Windows.

This mirrors iOS and Android, whose threads were merged by default in Flutter 3.29.

Migration guide
---------------

[#](#migration-guide)

Merged threads should not affect your app.

If you suspect merged threads has regressed your app, please reach out on [Issue 150525](https://github.com/flutter/flutter/issues/150525).

Timeline
--------

[#](#timeline)

Landed in version: 3.33.0-0.0.pre  
 In stable release: 3.35

References
----------

[#](#references)

Relevant issue:

* [Issue 150525](https://github.com/flutter/flutter/issues/150525)

Relevant PRs:

* [PR 166536](https://github.com/flutter/flutter/pull/166536)* [PR 167472](https://github.com/flutter/flutter/pull/167472)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/macos-windows-merged-threads/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/macos-windows-merged-threads.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/macos-windows-merged-threads/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/macos-windows-merged-threads.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-18. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/macos-windows-merged-threads.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/macos-windows-merged-threads/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/macos-windows-merged-threads.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   