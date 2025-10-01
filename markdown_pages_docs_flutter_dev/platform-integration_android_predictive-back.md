Add the predictive-back gesture
===============================

1. [Platform integration](/platform-integration) chevron\_right- [Android](/platform-integration/android) chevron\_right- [Predictive-back](/platform-integration/android/predictive-back)

This feature has landed in Flutter, but it's not enabled by default in Android itself yet. You can try it out using the following instructions.

Configure your app
------------------

[#](#configure-your-app)

Make sure your app supports Android API 33 or higher, as predictive back won't work on older versions of Android. Then, set the flag `android:enableOnBackInvokedCallback="true"` in `android/app/src/main/AndroidManifest.xml`.

Configure your device
---------------------

[#](#configure-your-device)

You need to enable Developer Mode and set a flag on your device, so you can't yet expect predictive back to work on most users' Android devices. If you want to try it out on your own device though, make sure it's running API 33 or higher, and then in **Settings => System => Developer** options, make sure the switch is enabled next to **Predictive back animations**.

Set up your app
---------------

[#](#set-up-your-app)

The predictive back route transitions are currently not enabled by default, so for now you'll need to enable them manually in your app. Typically, you do this by setting them in your theme:

dart

```
MaterialApp(
  theme: ThemeData(
    pageTransitionsTheme: const PageTransitionsTheme(
      builders: <TargetPlatform, PageTransitionsBuilder>{
        // Set the predictive back transitions for Android.
        TargetPlatform.android: PredictiveBackPageTransitionsBuilder(),
      },
    ),
  ),
  ...
),
```

Run your app
------------

[#](#run-your-app)

Lastly, just make sure you're using at least Flutter version 3.22.2 to run your app, which is the latest stable release at the time of this writing.

For more information
--------------------

[#](#for-more-information)

You can find more information at the following link:

* [Android predictive back](/release/breaking-changes/android-predictive-back) breaking change

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/predictive-back/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/predictive-back.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/predictive-back/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/predictive-back.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/android/predictive-back.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/android/predictive-back/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/android/predictive-back.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   