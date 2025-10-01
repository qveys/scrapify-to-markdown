Android 14 nonlinear font scaling enabled
=========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Android 14 nonlinear font scaling enabled](/release/breaking-changes/android-14-nonlinear-text-scaling-migration)

Summary
-------

[#](#summary)

Android 14 introduced nonlinear font scaling up to 200%. It may change how your app looks when the user changes the accessibility text scaling in system preferences.

Background
----------

[#](#background)

The [Android 14 nonlinear font scaling](https://developer.android.com/about/versions/14/features#non-linear-font-scaling) feature prevents excessive accessibility font scaling by scaling larger text at a lesser rate when the user increases the text scaling value in system preferences.

Migration guide
---------------

[#](#migration-guide)

As the [Android 14 feature overview](https://developer.android.com/about/versions/14/features#non-linear-font-scaling) suggests, test your UI with the maximum font size enabled (`200%`). This should verify that your app can apply the font sizes correctly and can accommodate larger font sizes without impacting usability.

To adopt nonlinear font scaling in your app and custom widgets, consider migrating from `textScaleFactor` to `TextScaler`. To learn how to migrate to `TextScaler`, check out the [Deprecate `textScaleFactor` in favor of `TextScaler`](/release/breaking-changes/deprecate-textscalefactor) migration guide.

**Temporarily Opting Out**

To opt-out of nonlinear text scaling on Android 14 until you migrate your app, add a modified `MediaQuery` at the top of your app's widget tree:

dart

```
runApp(
  Builder(builder: (context) {
    final mediaQueryData = MediaQuery.of(context);
    final mediaQueryDataWithLinearTextScaling = mediaQueryData
      .copyWith(textScaler: TextScaler.linear(mediaQueryData.textScaler.textScaleFactor));
    return MediaQuery(data: mediaQueryDataWithLinearTextScaling, child: realWidgetTree);
  }),
);
```

This uses the deprecated `textScaleFactor` API. It will stop working once that API is removed from the Flutter API.

Timeline
--------

[#](#timeline)

Landed in version: 3.14.0-11.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`TextScaler`](https://api.flutter.dev/flutter/painting/TextScaler-class.html)

Relevant issues:

* [New font scaling system (Issue 116231)](https://github.com/flutter/flutter/issues/116231)

Relevant PRs:

* [Implementing TextScaler for nonlinear text scaling](https://github.com/flutter/engine/pull/44907)

See also:

* [Deprecate `textScaleFactor` in favor of `TextScaler`](/release/breaking-changes/deprecate-textscalefactor)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-14-nonlinear-text-scaling-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-14-nonlinear-text-scaling-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-14-nonlinear-text-scaling-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-14-nonlinear-text-scaling-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   