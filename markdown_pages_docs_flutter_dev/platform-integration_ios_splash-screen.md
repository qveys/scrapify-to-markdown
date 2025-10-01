Adding a launch screen to your iOS app
======================================

1. [Platform integration](/platform-integration) chevron\_right- [iOS](/platform-integration/ios) chevron\_right- [Launch screen](/platform-integration/ios/launch-screen)

[Launch screens](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens) provide a simple initial experience while your iOS app loads. They set the stage for your application, while allowing time for the app engine to load and your app to initialize.

All apps submitted to the Apple App Store [must provide a launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) with an Xcode storyboard.

Customize the launch screen
---------------------------

[#](#customize-the-launch-screen)

The default Flutter template includes an Xcode storyboard named `LaunchScreen.storyboard` that can be customized with your own assets. By default, the storyboard displays a blank image, but you can change this. To do so, open the Flutter app's Xcode project by typing `open ios/Runner.xcworkspace` from the root of your app directory. Then select `Runner/Assets.xcassets` from the Project Navigator and drop in the desired images to the `LaunchImage` image set.

Apple provides detailed guidance for launch screens as part of the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/patterns/launching#launch-screens).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/launch-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/launch-screen.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/launch-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/launch-screen.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/launch-screen.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/ios/launch-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/ios/launch-screen.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   