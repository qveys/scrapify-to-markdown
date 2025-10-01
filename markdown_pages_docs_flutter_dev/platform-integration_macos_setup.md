Set up macOS development
========================

1. [Platform integration](/platform-integration) chevron\_right- [macOS](/platform-integration/macos) chevron\_right- [Set up macOS development](/platform-integration/macos/setup)

Learn how to set up your development environment to run, build, and deploy Flutter apps for the macOS desktop platform.

*info* Note

If you haven't set up Flutter already, visit and follow the [Get started with Flutter](/get-started) guide first.

If you've already installed Flutter, ensure that it's [up to date](/install/upgrade).

Set up tooling
--------------

[#](#set-up-tooling)

With Xcode, you can run Flutter apps on macOS as well as compile and debug native Swift and Objective-C code.

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

              Before agreeing to the terms of each license, read each with care.

              Once you've accepted all the necessary licenses successfully, the command should output how to review the licenses.- ### Install CocoaPods

         To support [Flutter plugins](/packages-and-plugins/developing-packages#types) that use native macOS code, install the latest version of [CocoaPods](https://cocoapods.org/).

         Install CocoaPods following the [CocoaPods installation guide](https://guides.cocoapods.org/using/getting-started.html#installation).

         If you've already installed CocoaPods, update it following the [CocoaPods update guide](https://guides.cocoapods.org/using/getting-started.html#updating-cocoapods).

Validate your setup
-------------------

[#](#validate-setup)

1. ### Check for toolchain issues

   To check for any issues with your macOS development setup, run the `flutter doctor` command in your preferred terminal:

   ```
   flutter doctor -v
   ```

   If you see any errors or tasks to complete under the **Xcode** section, complete and resolve them, then run `flutter doctor -v` again to verify any changes.- ### Check for macOS devices

     To ensure Flutter can find and connect to your macOS device correctly, run `flutter devices` in your preferred terminal:

     ```
     flutter devices
     ```

     If you set everything up correctly, there should be at least one entry with the platform marked as **macos**.- ### Troubleshoot setup issues

       If you need help resolving any setup issues, check out [Install and setup troubleshooting](/install/troubleshoot).

       If you still have issues or questions, reach out on one of the Flutter [community](https://flutter.dev/community) channels.

Start developing for macOS
--------------------------

[#](#start-developing)

Congratulations! Now that you've set up macOS desktop development for Flutter, you can continue your Flutter learning journey while testing on macOS or begin expanding integration with macOS.

![Dash helping you explore Flutter learning resources.](/assets/images/decorative/pointing-the-way.png)

Continue learning Flutter

* [Write your first app](/get-started/codelab)* [Learn the fundamentals](/get-started/fundamentals)* [Explore Flutter widgets](https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG)* [Check out samples](/reference/learning-resources)* [Learn about Dart](/resources/bootstrap-into-dart)

![An outline of Flutter desktop support.](/assets/images/decorative/flutter-on-desktop.svg)

Build for macOS

* [Build and deploy to macOS](/deployment/macos)* [Bind to native macOS code](/platform-integration/macos/c-interop)* [Embed native macOS views](/platform-integration/macos/platform-views)* [Set up app flavors](/deployment/flavors-ios)* [Use Swift Package Manager](/packages-and-plugins/swift-package-manager/for-app-developers)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/setup.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/setup.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-25. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/setup.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/setup/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/setup.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   