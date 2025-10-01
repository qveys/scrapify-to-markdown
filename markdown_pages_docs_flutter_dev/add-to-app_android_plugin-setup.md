Manage plugins and dependencies in add-to-app
=============================================

1. [Add to app](/add-to-app) chevron\_right- [Add Flutter to Android](/add-to-app/android) chevron\_right- [Plugin setup](/add-to-app/android/plugin-setup)

This guide describes how to set up your project to consume plugins and how to manage your Gradle library dependencies between your existing Android app and your Flutter module's plugins.

A. Simple scenario
------------------

[#](#a-simple-scenario)

In the simple cases:

* Your Flutter module uses a plugin that has no additional Android Gradle dependency because it only uses Android OS APIs, such as the camera plugin.* Your Flutter module uses a plugin that has an Android Gradle dependency, such as [ExoPlayer from the video\_player plugin](https://github.com/flutter/packages/blob/main/packages/video_player/video_player_android/android/build.gradle), but your existing Android app didn't depend on ExoPlayer.

There are no additional steps needed. Your add-to-app module will work the same way as a full-Flutter app. Whether you integrate using Android Studio, Gradle subproject or AARs, transitive Android Gradle libraries are automatically bundled as needed into your outer existing app.

B. Plugins needing project edits
--------------------------------

[#](#b-plugins-needing-project-edits)

Some plugins require you to make some edits to the Android side of your project.

For example, the integration instructions for the [firebase\_crashlytics](https://pub.dev/packages/firebase_crashlytics) plugin require manual edits to your Android wrapper project's `build.gradle` file.

For full-Flutter apps, these edits are done in your Flutter project's `/android/` directory.

In the case of a Flutter module, there are only Dart files in your module project. Perform those Android Gradle file edits on your outer, existing Android app rather than in your Flutter module.

*info* Note

Astute readers might notice that the Flutter module directory also contains an `.android` and an `.ios` directory. Those directories are Flutter-tool-generated and are only meant to bootstrap Flutter into generic Android or iOS libraries. They should not be edited or checked-in. This allows Flutter to improve the integration point should there be bugs or updates needed with new versions of Gradle, Android, Android Gradle Plugin, etc.

For advanced users, if more modularity is needed and you must not leak knowledge of your Flutter module's dependencies into your outer host app, you can rewrap and repackage your Flutter module's Gradle library inside another native Android Gradle library that depends on the Flutter module's Gradle library. You can make your Android specific changes such as editing the AndroidManifest.xml, Gradle files or adding more Java files in that wrapper library.

C. Merging libraries
--------------------

[#](#c-merging-libraries)

The scenario that requires slightly more attention is if your existing Android application already depends on the same Android library that your Flutter module does (transitively via a plugin).

For instance, your existing app's Gradle might already have:

ExistingApp/app/build.gradle

groovy

```
…
dependencies {
    …
    implementation("com.crashlytics.sdk.android:crashlytics:2.10.1")
    …
}
…
```

And your Flutter module also depends on [firebase\_crashlytics](https://pub.dev/packages/firebase_crashlytics) via `pubspec.yaml`:

flutter\_module/pubspec.yaml

yaml

```
…
dependencies:
  …
  firebase_crashlytics: ^0.1.3
  …
…
```

This plugin usage transitively adds a Gradle dependency again via firebase\_crashlytics v0.1.3's own [Gradle file](https://github.com/firebase/flutterfire/blob/bdb95fcacf7cf077d162d2f267eee54a8b0be3bc/packages/firebase_crashlytics/android/build.gradle#L40):

"firebase\_crashlytics\_via\_pub/android/build.gradle

groovy

```
…
dependencies {
    …
    implementation("com.crashlytics.sdk.android:crashlytics:2.9.9")
    …
}
…
```

The two `com.crashlytics.sdk.android:crashlytics` dependencies might not be the same version. In this example, the host app requested v2.10.1 and the Flutter module plugin requested v2.9.9.

By default, Gradle v5 [resolves dependency version conflicts](https://docs.gradle.org/current/userguide/dependency_resolution.html#sub:resolution-strategy) by using the newest version of the library.

This is generally ok as long as there are no API or implementation breaking changes between the versions. For example, you might use the new Crashlytics library in your existing app as follows:

ExistingApp/app/build.gradle

groovy

```
…
dependencies {
    …
    implementation("com.google.firebase:firebase-crashlytics:17.0.0-beta03")
    …
}
…
```

This approach won't work since there are major API differences between the Crashlytics' Gradle library version v17.0.0-beta03 and v2.9.9.

For Gradle libraries that follow semantic versioning, you can generally avoid compilation and runtime errors by using the same major semantic version in your existing app and Flutter module plugin.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/android/plugin-setup/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/android/plugin-setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/android/plugin-setup/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/android/plugin-setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/add-to-app/android/plugin-setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/android/plugin-setup/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/android/plugin-setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   