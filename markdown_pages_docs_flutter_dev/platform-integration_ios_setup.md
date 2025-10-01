Set up iOS development
======================

1. [Platform integration](/platform-integration) chevron\_right- [iOS](/platform-integration/ios) chevron\_right- [Set up iOS development](/platform-integration/ios/setup)

Learn how to set up your development environment to run, build, and deploy Flutter apps for iOS devices.

*info* Note

If you haven't set up Flutter already, visit and follow the [Get started with Flutter](/get-started) guide first.

If you've already installed Flutter, ensure that it's [up to date](/install/upgrade).

Set up iOS tooling
------------------

[#](#set-up-tooling)

With Xcode, you can run Flutter apps on an iOS physical device or on the iOS Simulator.

1. ### Install Xcode

   If you haven't done so already, [install and set up the latest version of Xcode](https://developer.apple.com/xcode/).

   If you've already installed Xcode, update it to the latest version using the same installation method you used originally.- ### Set up Xcode command-line tools

     To configure the Xcode command-line tools to use the version of Xcode you installed, run the following command in your preferred terminal:

     ```
     sudo sh -c 'xcode-select -s /Applications/Xcode.app/Contents/Developer && xcodebuild -runFirstLaunch'
     ```

     If you downloaded Xcode elsewhere or need to use a different version, replace `/Applications/Xcode.app` with the path to there instead.- ### Agree to the Xcode licenses

       After you've set up Xcode and configured its command-line tools, agree to the Xcode licenses.
       1. Open your preferred terminal.- Run the following command to review and sign the Xcode licenses.

            ```
            sudo xcodebuild -license
            ```

            - Read and agree to all necessary licenses.

              Before agreeing to the terms of each license, read each with care.- ### Download prerequisite tooling

         To download iOS platform support and the latest iOS Simulator runtimes, run the following command in your preferred terminal.

         ```
         xcodebuild -downloadPlatform iOS
         ```

         - ### Install Rosetta

           If you're developing on an [Apple Silicon](https://support.apple.com/en-us/116943) (ARM) Mac, [install Rosetta 2](https://support.apple.com/en-us/102527):

           ```
           sudo softwareupdate --install-rosetta --agree-to-license
           ```

           - ### Install CocoaPods

             To support [Flutter plugins](/packages-and-plugins/developing-packages#types) that use native iOS or macOS code, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html#installation).

             Install CocoaPods by following the [CocoaPods installation guide](https://guides.cocoapods.org/using/getting-started.html#installation).

             If you've already installed CocoaPods, update it by following the [CocoaPods update guide](https://guides.cocoapods.org/using/getting-started.html#updating-cocoapods).

Set up an iOS device
--------------------

[#](#set-up-devices)

We recommend starting with the iOS Simulator as it's easier to get set up than a physical iOS device. However, you should also test your app on an actual physical device.

* [Simulator](#19-tab-panel)* [Physical device](#20-tab-panel)

Start the iOS Simulator with the following command:

```
open -a Simulator
```

If you need to install a simulator for a different OS version, check out [Downloading and installing additional Xcode components](https://developer.apple.com/documentation/xcode/downloading-and-installing-additional-xcode-components) on the Apple Developer site.

*warning* Warning

An upcoming change to iOS has caused a temporary break in Flutter's debug mode on physical devices running iOS 26 (currently in beta). If your physical device is already on iOS 26, we recommend switching to the **Simulator** tab and following the instructions. See [Flutter on latest iOS](/platform-integration/ios/ios-latest) for details.

Set up each iOS device on which you want to test.

1. ### Configure your physical iOS device

   1. Attach your iOS device to the USB port on your Mac.- On first connecting an iOS device to your Mac, your device displays the **Trust this computer?** dialog.- Click **Trust**.

          ![Trust Mac](/assets/images/docs/setup/trust-computer.png)- ### Configure your physical iOS device

     Apple requires enabling **[Developer Mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)** on the device to protect against malicious software.
     1. Tap on **Settings** > **Privacy & Security** > **Developer Mode**.- Tap to toggle **Developer Mode** to **On**.- Restart the device.- When the **Turn on Developer Mode?** dialog appears, tap **Turn On**.- ### Create a developer code signing certificate

       To send your app to a physical iOS device, *even* for testing, you must establish trust between your Mac and the device. In addition to trusting the device when that popup appears, you must upload a signed developer certificate to your device.

       To create a signed development certificate, you need an Apple ID. If you don't have one, [create one](https://support.apple.com/en-us/108647). You must also enroll in the [Apple Developer program](https://developer.apple.com/programs/) and create an [Apple Developer account](https://developer.apple.com/account). If you're just *testing* your app on an iOS device, a personal Apple Developer account is free and works.

       *info* Apple Developer program

       When you want to *deploy* your app to the App Store, you'll need to upgrade your personal Apple Developer account to a professional account.

       - ### Prepare the device

         1. Find the **VPN & Device Management** menu under **Settings**.

            Toggle your certificate to **Enable**.

            *info* Note

            If you can't find the **VPN & Device Management** menu, run your app on your iOS device once, then try again.

            - Under the **Developer App** heading, you should find your certificate.- Tap the certificate.- Tap **Trust "<certificate>"**.- When the dialog displays, tap **Trust**.

                    If the **codesign wants to access key...** dialog appears:
                    1. Enter your macOS password.- Tap **Always Allow**.

---

Start developing for iOS
------------------------

[#](#start-developing)

**Congratulations.** Now that you've set up iOS development for Flutter, you can continue your Flutter learning journey while testing on iOS or begin improving integration with iOS.

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Continue learning Flutter

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)* [Check out samples](/reference/learning-resources)* [Learn about Dart](/resources/bootstrap-into-dart)

![A representation of Flutter on multiple devices.](/assets/images/decorative/flutter-on-phone.svg)

Build for iOS

* [Build and deploy to iOS](/deployment/ios)* [Bind to native iOS code](/platform-integration/ios/c-interop)* [Leverage system frameworks](/platform-integration/ios/apple-frameworks)* [Embed native iOS views](/platform-integration/ios/platform-views)* [Use Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   