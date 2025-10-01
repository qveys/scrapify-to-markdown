Flutter now sets default `abiFilters` in Android builds
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Flutter now sets default `abiFilters` in Android builds](/release/breaking-changes/default-abi-filters-android)

Summary
-------

[#](#summary)

Starting in Flutter 3.35, the Flutter Gradle Plugin automatically sets [`abiFilters`](https://developer.android.com/reference/tools/gradle-api/8.7/com/android/build/api/dsl/Ndk#abiFilters()) for Android builds to prevent the inclusion of unsupported architectures in release APKs. This change can break custom `abiFilters` specified in your app's `build.gradle` file.

Context
-------

[#](#context)

This change was introduced to solve an issue where third-party dependencies with x86 native libraries would cause Google Play to incorrectly identify Flutter apps as supporting x86 devices. When users with x86 devices installed these apps, they would crash at runtime because Flutter's native libraries aren't available for x86.

The Flutter Gradle Plugin now automatically configures `abiFilters` to include only the architectures that Flutter supports. This prevents Google Play from making apps available to incompatible devices.

Description of change
---------------------

[#](#description-of-change)

The Flutter Gradle Plugin now programmatically sets `abiFilters` for non-debuggable builds when the `--splits-per-abi` option is not enabled by default to:

* `armeabi-v7a`* `arm64-v8a`* `x86_64`

Because this automatic configuration happens before your `build.gradle` files are processed, it might break custom `abiFilters` settings that depend on the set being empty.

Migration guide
---------------

[#](#migration-guide)

If your app doesn't customize `abiFilters`, no changes are required.

If your app needs to customize which architectures are included, you have several options:

### Option 1: Use the splits-per-abi flag

[#](#option-1-use-the-splits-per-abi-flag)

If you want to control architecture inclusion, use Flutter's built-in `--splits-per-abi` option instead of manually configuring `abiFilters`:

```
flutter build apk --splits-per-abi
```

This creates separate APKs for each architecture and automatically disables the automatic `abiFilters` configuration.

### Option 2: Clear and reconfigure abiFilters

[#](#option-2-clear-and-reconfigure-abifilters)

If you must use a single APK with custom architecture filters, clear the automatically set filters and configure your own in your `build.gradle`. For example:

kotlin

```
android {
    buildTypes {
        release {
            // Clear the automatically set filters.
            ndk.abiFilters.clear()
            // Set your custom filters.
            ndk.abiFilters.addAll(listOf("arm64-v8a"))
        }
    }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.35.0  
 In stable release: 3.35

Relevant issues:

* [Issue #174004](https://github.com/flutter/flutter/issues/174004)* [Issue #153476](https://github.com/flutter/flutter/issues/153476)

Relevant PRs:

* [PR #168293](https://github.com/flutter/flutter/pull/168293)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-abi-filters-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-abi-filters-android.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-abi-filters-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-abi-filters-android.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-26. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-abi-filters-android.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-abi-filters-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-abi-filters-android.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   