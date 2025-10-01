Windows build path changed to add the target architecture
=========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Windows build path changed to add the target architecture](/release/breaking-changes/windows-build-architecture)

Summary
-------

[#](#summary)

Built executables for Flutter Windows apps are now located in architecture dependent folders.

Context
-------

[#](#context)

In preparation for supporting Windows on Arm64, the Windows build path was updated to add the build's target architecture.

Previously, Flutter builds for Windows assumed an x64 target architecture.

Migration guide
---------------

[#](#migration-guide)

You may need to update your infrastructure to use the new Flutter Windows build path.

Example build path before the migration:

```
build\windows\runner\Release\hello_world.exe
```

Example build path after the migration if targeting x64:

```
build\windows\x64\runner\Release\hello_world.exe
```

Example build path after the migration if targeting Arm64:

```
build\windows\arm64\runner\Release\hello_world.exe
```

If you use [`package:msix`](https://pub.dev/packages/msix), update to version 3.16.7 or newer.

Timeline
--------

[#](#timeline)

Landed in version: 3.15.0-0.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

Design document:

* [flutter.dev/go/windows-arm64](https://flutter.dev/go/windows-arm64)

Relevant pull requests:

* [Introduce architecture subdirectory for Windows build](https://github.com/flutter/flutter/pull/131843)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-build-architecture/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-build-architecture.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-build-architecture/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-build-architecture.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-12-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-build-architecture.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/windows-build-architecture/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/windows-build-architecture.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   