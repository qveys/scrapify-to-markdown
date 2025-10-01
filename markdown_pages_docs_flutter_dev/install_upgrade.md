Upgrade Flutter
===============

1. [Install](/install) chevron\_right- [Upgrade](/install/upgrade)

No matter which one of the Flutter release channels you follow, you can use the `flutter` command to upgrade your Flutter SDK or the packages that your app depends on.

Upgrade the Flutter SDK
-----------------------

[#](#upgrade-the-flutter-sdk)

To update the Flutter SDK use the `flutter upgrade` command:

```
flutter upgrade
```

This command gets the most recent version of the Flutter SDK that's available on your current Flutter channel.

If you are using the **stable** channel and want an even more recent version of the Flutter SDK, switch to the **beta** channel using `flutter channel beta`, and then run `flutter upgrade`.

### Keep informed

[#](#keep-informed)

We publish [migration guides](/release/breaking-changes) for known breaking changes.

We send announcements regarding these changes to the [Flutter announcements mailing list](https://groups.google.com/forum/#!forum/flutter-announce).

To avoid being broken by future versions of Flutter, consider submitting your tests to our [test registry](https://github.com/flutter/tests).

Switching Flutter channels
--------------------------

[#](#switching-flutter-channels)

Flutter has two release channels: **stable** and **beta**.

### The **stable** channel

[#](#the-stable-channel)

We recommend the **stable** channel for new users and for production app releases. The team updates this channel about every three months. The channel might receive occasional hot fixes for high-severity or high-impact issues.

The continuous integration for the Flutter team's plugins and packages includes testing against the latest **stable** release.

The latest documentation for the **stable** branch is at: <https://api.flutter.dev>

### The **beta** channel

[#](#the-beta-channel)

The **beta** channel has the latest stable release. This is the most recent version of Flutter that we have heavily tested. This channel has passed all our public testing, has been verified against test suites for Google products that use Flutter, and has been vetted against [contributed private test suites](https://github.com/flutter/tests). The **beta** channel receives regular hot fixes to address newly discovered important issues.

The **beta** channel is essentially the same as the **stable** channel but updated monthly instead of quarterly. Indeed, when the **stable** channel is updated, it is updated to the latest **beta** release.

### Other channels

[#](#other-channels)

We currently have one other channel, **main** (previously known as **master**). People who [contribute to Flutter](https://github.com/flutter/flutter/blob/main/CONTRIBUTING.md) use this channel.

This channel is not as thoroughly tested as the **beta** and **stable** channels.

We do not recommend using this channel as it is more likely to contain serious regressions.

The latest documentation for the **main** branch is at: <https://main-api.flutter.dev>

### Change channels

[#](#change-channels)

To view your current channel, use the following command:

```
flutter channel
```

To change to another channel, use `flutter channel <channel-name>`. Once you've changed your channel, use `flutter upgrade` to download the latest Flutter SDK and dependent packages for that channel. For example:

```
flutter channel beta
flutter upgrade
```

Switch to a specific Flutter version
------------------------------------

[#](#switch-to-a-specific-flutter-version)

To switch to a specific Flutter version:

1. Find your desired **Flutter version** on the [Flutter SDK archive](/install/archive).- Navigate to the Flutter SDK:

     ```
     cd /path/to/flutter
     ```

     *lightbulb* Tip

     You can find the Flutter SDK's path using `flutter doctor --verbose`.

     - Use `git checkout` to switch to your desired **Flutter version**:

       ```
       git checkout <Flutter version>
       ```

Upgrade packages
----------------

[#](#upgrade-packages)

If you've modified your `pubspec.yaml` file, or you want to update only the packages that your app depends upon (instead of both the packages and Flutter itself), then use one of the `flutter pub` commands.

To update to the *latest compatible versions* of all the dependencies listed in the `pubspec.yaml` file, use the `upgrade` command:

```
flutter pub upgrade
```

To update to the *latest possible version* of all the dependencies listed in the `pubspec.yaml` file, use the `upgrade --major-versions` command:

```
flutter pub upgrade --major-versions
```

This also automatically update the constraints in the `pubspec.yaml` file.

To identify out-of-date package dependencies and get advice on how to update them, use the `outdated` command. For details, see the Dart [`pub outdated` documentation](https://dart.dev/tools/pub/cmd/pub-outdated).

```
flutter pub outdated
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/upgrade/&page-source=https://github.com/flutter/website/tree/main/src/content/install/upgrade.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/upgrade/&page-source=https://github.com/flutter/website/tree/main/src/content/install/upgrade.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/install/upgrade.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/install/upgrade/&page-source=https://github.com/flutter/website/tree/main/src/content/install/upgrade.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   