Set default of `SystemUiMode` to edge-to-edge
=============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Set default of `SystemUiMode` to edge-to-edge](/release/breaking-changes/default-systemuimode-edge-to-edge)

*info* Note

You might have found this page because you see a warning in the Google Play Console concerning "Edge-to-edge may not display for all users" or "Your app uses deprecated APIs or parameters for edge-to-edge". These warnings **will not** impact users.

This warning references deprecated code used in the Flutter engine to implement edge-to-edge mode. The engine relies on this deprecated code to avoid breaking changes for users, so it will continue to work should you set edge-to-edge mode in your app. See [flutter#169810](https://github.com/flutter/flutter/issues/169810) for more information.

Summary
-------

[#](#summary)

If your Flutter app targets Android SDK version 15, your app automatically displays in edge-to-edge mode, as documented on the [`SystemUiMode`](https://api.flutter.dev/flutter/services/SystemUiMode.html) API page. To maintain non-edge-to-edge app behavior (including an unset `SystemUiMode`), follow the steps in [migration guide](#migration-guide).

*info* Note

If your Flutter app targets Android SDK version 16 or later, your app automatically displays in edge-to-edge mode, and you cannot opt-out. To learn more about this change, check out the [Android 16 release notes](https://developer.android.com/about/versions/16/behavior-changes-16#edge-to-edge).

Context
-------

[#](#context)

By default, Android enforces [edge-to-edge mode](https://developer.android.com/develop/ui/views/layout/edge-to-edge) for all apps that target Android 15 or later. To learn more about this change, check out the [Android 15 release notes](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge). This impacts devices running on Android SDK 15+ or API 35+.

Prior to Flutter 3.27, Flutter apps target Android 14 by default and won't opt into edge-to-edge mode automatically, but your app *will* be impacted when you choose to target Android 15. If your app targets `flutter.targetSdkVersion` (as it does by default), then it targets Android 15 starting with Flutter version 3.27, automatically opting your app in to edge-to-edge.

If your app explicitly sets `SystemUiMode.edgeToEdge` to run in edge-to-edge mode by calling [`SystemChrome.setEnabledSystemUIMode`](https://api.flutter.dev/flutter/services/SystemChrome/setEnabledSystemUIMode.html), then your app is already migrated. Apps needing more time to migrate to edge-to-edge mode must use the following steps to opt out on devices running Android SDK 15.

Be aware of the following:

1. Android plans for the workaround detailed here to be temporary.- Flutter plans to align with Android (and iOS) to support edge-to-edge by default within the year, so **migrate to edge-to-edge mode before the operating system removes the ability to opt out**.

Migration guide
---------------

[#](#migration-guide)

To opt out of edge-to-edge on SDK 15, specify the new style attribute in each activity that requires it. If you have a parent style that child styles need to opt out of, you can modify the parent only. In the following example, update the style configuration generated from `flutter create`.

By default, the styles used in a Flutter app are set in the Android manifest file (`your_app/android/app/src/main/AndroidManifest.xml`). Generally, styles are denoted by `@style` and help theme your app. Modify these default styles in your manifest file:

AndroidManifest.xml

xml

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application ...>
        <activity ...>
            <!-- Style to modify: -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
            />
        </activity>
    </application>
</manifest>
```

Locate the style definition in: `your_app/android/app/src/main/res/values/styles.xml`.

Add the following attribute to the appropriate styles:

styles.xml

xml

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="LaunchTheme" parent="@android:style/Theme.Light.NoTitleBar">
        ...
        <!-- Add the following line: -->
        <item name="android:windowOptOutEdgeToEdgeEnforcement">true</item>
    </style>
    ...
    <style name="NormalTheme" parent="@android:style/Theme.Light.NoTitleBar">
        ...
	      <!-- Add the following line: -->
        <item name="android:windowOptOutEdgeToEdgeEnforcement">true</item>
    </style>
</resources>
```

Make sure to apply the same change in the night mode styles file as well: `your_app/android/app/src/main/res/values-night/styles.xml`.

Ensure both styles are updated consistently in both files.

This modified style opts your app out of edge-to-edge for apps targeting Android SDK 15. So now you're done!

Timeline
--------

[#](#timeline)

Starting in Flutter 3.27, Flutter apps target Android 15 by default, so if you wish to use this version and not manually set a lower target SDK version for your Flutter app, follow the preceding [migration steps](#migration-guide) to maintain an unset or non-edge-to-edge `SystemUiMode`.

Landed in version: 3.26.0-0.0.pre  
 Stable release: 3.27

References
----------

[#](#references)

* [The supported Flutter `SystemUiMode`s](https://api.flutter.dev/flutter/services/SystemUiMode.html)* [The Android 15 edge-to-edge behavior changes guide](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge)* [The Android 16 edge-to-edge behavior changes guide](https://developer.android.com/about/versions/16/behavior-changes-16#edge-to-edge)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-systemuimode-edge-to-edge/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-systemuimode-edge-to-edge.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-systemuimode-edge-to-edge/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-systemuimode-edge-to-edge.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-systemuimode-edge-to-edge.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-systemuimode-edge-to-edge/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-systemuimode-edge-to-edge.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   