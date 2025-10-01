Android v1 embedding app and plugin creation deprecation
========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Android v1 embedding app and plugin creation deprecation](/release/breaking-changes/android-v1-embedding-create-deprecation)

Summary
-------

[#](#summary)

The `flutter create` templates for apps and plugins no longer create Android wrapping based on the v1 Android embedding as part of our gradual Android v1 embedding deprecation process described in our [Android Migration Summary](/go/android-migration-summary).

Application projects using the v1 Android embedding are encouraged to migrate following the steps described in [Upgrading pre 1.12 Android projects](https://github.com/flutter/flutter/blob/main/docs/platforms/android/Upgrading-pre-1.12-Android-projects.md).

Plugins targeting the v1 Android embedding are encouraged to migrate following the instructions in [Supporting the new Android plugins APIs](/release/breaking-changes/plugin-api-migration).

Context
-------

[#](#context)

In Flutter version 1.12, we launched a v2 set of Android APIs based on the [`io.flutter.embedding`](https://cs.opensource.google/flutter/engine/+/master:shell/platform/android/io/flutter/embedding/) package in order to enable the [add-to-app](/add-to-app) workflow on Android.

Over time, we gradually deprecated the older v1 Android embeddings based on the [`io.flutter.app`](https://cs.opensource.google/flutter/engine/+/master:shell/platform/android/io/flutter/app/.) package.

As of Q2 2020, only 26% of applications used the v1 embeddings.

Since the v2 embeddings were strongly established over the 7 months since the launch of Flutter v1.12, we disabled the creation of new app and plugin projects using the v1 embeddings.

Description of change
---------------------

[#](#description-of-change)

The `flutter config` command no longer has a toggleable `enable-android-embedding-v2` flag (which defaulted to true since v1.12). All projects created with `flutter create` and `flutter create -t plugin` exclusively use the Android v2 embedding.

Existing v1 applications continue to work.

Existing v1 applications consuming plugins now receive a warning prompt to migrate to v2 embedding.

Existing v1 applications consuming a plugin that targets only the v2 embedding won't build and must migrate. This has been the case since v1.12. However, the likelihood of encountering this increases as plugin developers create and publish v2 only plugins.

Existing v2 applications continue to work with or without plugins.

Existing v2 applications consuming plugins that only target the v1 embedding continue to receive a warning prompt. The likelihood of encountering this decreases as plugin developers create and publish v2 plugins.

Migration guide
---------------

[#](#migration-guide)

For more information, see [Upgrading pre 1.12 Android projects](https://github.com/flutter/flutter/blob/main/docs/platforms/android/Upgrading-pre-1.12-Android-projects.md).

Timeline
--------

[#](#timeline)

Landed in version: 1.20.0-8.0  
 In stable release: 1.22

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-v1-embedding-create-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-v1-embedding-create-deprecation.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-v1-embedding-create-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-v1-embedding-create-deprecation.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-v1-embedding-create-deprecation.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-v1-embedding-create-deprecation/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-v1-embedding-create-deprecation.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   