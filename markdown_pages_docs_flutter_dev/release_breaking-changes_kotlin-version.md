Required Kotlin version
=======================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Required Kotlin version](/release/breaking-changes/kotlin-version)

*error* Important

As of Flutter 3.16, the default Gradle build scripts differ across Flutter versions. For example, the Kotlin version is now configured in the `android/settings.gradle` file. If you have generated your project with an older version of Flutter, it's advisable to upgrade your build scripts to the newest form. For more information, see [Issue 10380](https://github.com/flutter/website/issues/10380) and [Issue 135392](https://github.com/flutter/flutter/issues/135392).

Summary
-------

[#](#summary)

To build a Flutter app for Android, Kotlin 1.5.31 or greater is required.

If your app uses a lower version, you will receive the following error message:

```
┌─ Flutter Fix ────────────────────────────────────────────────────────────┐
│                                                                          │
│ [!] Your project requires a newer version of the Kotlin Gradle plugin.   │
│ Find the latest version on                                               │
│ https://kotlinlang.org/docs/gradle.html#plugin-and-versions, then update │
│ <path-to-app>/android/build.gradle:                                      │
│ ext.kotlin_version = '<latest-version>'                                  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

Context
-------

[#](#context)

Flutter added support for [foldable devices](https://developer.android.com/guide/topics/large-screens/learn-about-foldables) on Android. This required adding an AndroidX dependency to the Flutter embedding that requires apps to use Kotlin 1.5.31 or greater.

Description of change
---------------------

[#](#description-of-change)

A Flutter app compiled for Android now includes the Gradle dependency `androidx.window:window-java`.

Migration guide
---------------

[#](#migration-guide)

Open `<app-src>/android/build.gradle`, and change `ext.kotlin_version`:

groovy

```
buildscript {
    ext.kotlin_version = '1.3.50'
    ext.kotlin_version = '1.5.31'
```

Timeline
--------

[#](#timeline)

Landed in version: v2.9.0 beta  
 In stable release: 2.10

References
----------

[#](#references)

Relevant PR:

* [PR 29585: Display Features support](https://github.com/flutter/engine/pull/29585)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/kotlin-version/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/kotlin-version.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/kotlin-version/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/kotlin-version.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-25. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/kotlin-version.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/kotlin-version/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/kotlin-version.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   