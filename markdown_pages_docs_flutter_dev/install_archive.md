Flutter SDK archive
===================

1. [Install](/install) chevron\_right- [Archive](/install/archive)

*info* Developing in China

If you want to use Flutter in China, check out [using Flutter in China](/community/china). If you're not developing in China, ignore this notice and follow the other instructions on this page.

如果你正在中国的网络环境下配置 Flutter， 请参考 [在中国网络环境下使用 Flutter](https://docs.flutter.cn/community/china/) 文档.

Overview
--------

[#](#overview)

The Flutter SDK archive is a collection of all previous versions of the Flutter SDK. This archive is useful for developers who need to use an older version of Flutter for compatibility reasons or to investigate bugs.

The archive includes Flutter SDKs for Windows, macOS, and Linux on the following [channels](https://github.com/flutter/flutter/blob/main/docs/releases/Flutter-build-release-channels.md):

* **Stable channel**: This channel contains the most stable Flutter builds. Roughly every third beta version is promoted to the stable version. The stable channel is the recommended channel for new users and for production app releases.* **Beta channel**: This channel is the most recent version of Flutter that is available, but it is not yet stable. The beta branch is usually released on the first Wednesday of the month. A fix will typically end up in the beta channel about two weeks after it lands in the main channel. Releases are distributed as [installation bundles](https://github.com/flutter/flutter/blob/main/docs/infra/Flutter-Installation-Bundles.md).* **Main channel**: This channel has the newest features, but it hasn't been fully tested and might have some bugs. We don't recommend using it unless you're contributing to Flutter itself.

The following information is available for each Flutter release in the SDK archive:

* **Flutter version**: The version number of the Flutter SDK (for example, 3.35.0, 2.10.5) follows a modified [calendar versioning](https://calver.org/) scheme called *CalVer*. For more information, visit the [Flutter SDK versioning](https://github.com/flutter/flutter/blob/main/docs/releases/Release-versioning.md) page.* **Architecture**: The processor architecture the SDK is built for (for example, x64, arm64). This specifies the type of processor the SDK is compatible with.* **Ref**: The git commit hash that uniquely identifies the specific codebase used for that release.* **Release Date**: The date when that particular Flutter version was officially released.* **Dart version**: The corresponding version of the Dart SDK included in the Flutter SDK release.* **Provenance**: Provides details about the build process and origin of the SDK, potentially including information about security attestations or build systems used. Results are returned as JSON.

Stable channel
--------------

[#](#stable-channel)

* [Windows](#160-tab-panel)* [macOS](#161-tab-panel)* [Linux](#162-tab-panel)

Select from the following scrollable list:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flutter version Architecture Ref Release Date Dart version Provenance|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Loading... | | | | | | | | | | | |

Beta channel
------------

[#](#beta-channel)

* [Windows](#163-tab-panel)* [macOS](#164-tab-panel)* [Linux](#165-tab-panel)

Select from the following scrollable list:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flutter version Architecture Ref Release Date Dart version Provenance|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Loading... | | | | | | | | | | | |

Main channel
------------

[#](#main-channel)

[Installation bundles](https://github.com/flutter/flutter/blob/main/docs/infra/Flutter-Installation-Bundles.md) are not available for the `main` channel (which was previously known as the `master` channel). However, you can get the SDK directly from [GitHub repo](https://github.com/flutter/flutter) by cloning the main channel, and then triggering a download of the SDK dependencies:

```
git clone -b main https://github.com/flutter/flutter.git
./flutter/bin/flutter --version
```

More information
----------------

[#](#more-information)

To learn what's new in the major Flutter builds, check out the [release notes](/release/release-notes) page.

For details on how our installation bundles are structured, see [Installation bundles](https://github.com/flutter/flutter/blob/main/docs/infra/Flutter-Installation-Bundles.md).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/archive/&page-source=https://github.com/flutter/website/tree/main/src/content/install/archive.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/archive/&page-source=https://github.com/flutter/website/tree/main/src/content/install/archive.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-16. [View source](https://github.com/flutter/website/tree/main/src/content/install/archive.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/archive/&page-source=https://github.com/flutter/website/tree/main/src/content/install/archive.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   