Set up universal links for iOS
==============================

1. [Cookbook](/cookbook) chevron\_right- [Navigation](/cookbook/navigation) chevron\_right- [Set up universal links for iOS](/cookbook/navigation/set-up-universal-links)

Deep linking allows an app user to launch an app with a URI. This URI contains scheme, host, and path, and opens the app to a specific screen.

A *universal link*, a type of deep link exclusive to iOS devices, uses only the `http` or `https` protocols.

To set up universal links, you need to own a web domain. As a temporary solution, consider using [Firebase Hosting](https://firebase.google.com/docs/hosting) or [GitHub Pages](https://pages.github.com).

Once you've set up your deep links, you can validate them. To learn more, see [Validate deep links](/tools/devtools/deep-links).

Create or modify a Flutter app
------------------------------

[#](#create-or-modify-a-flutter-app)

Write a Flutter app that can handle an incoming URL.

This example uses the [go\_router](https://pub.dev/packages/go_router) package to handle the routing. The Flutter team maintains the `go_router` package. It provides a simple API to handle complex routing scenarios.

1. To create a new application, type `flutter create <app-name>`.

   ```
   flutter create deeplink_cookbook
   ```

   - To include the `go_router` package as a dependency, run `flutter pub add`:

     ```
     flutter pub add go_router
     ```

     - To handle the routing, create a `GoRouter` object in the `main.dart` file:

       main.dart

       dart

       ```
       import 'package:flutter/material.dart';
       import 'package:go_router/go_router.dart';

       void main() => runApp(MaterialApp.router(routerConfig: router));

       /// This handles '/' and '/details'.
       final router = GoRouter(
         routes: [
           GoRoute(
             path: '/',
             builder: (_, _) => Scaffold(
               appBar: AppBar(title: const Text('Home Screen')),
             ),
             routes: [
               GoRoute(
                 path: 'details',
                 builder: (_, _) => Scaffold(
                   appBar: AppBar(title: const Text('Details Screen')),
                 ),
               ),
             ],
           ),
         ],
       );
       ```

Adjust iOS build settings
-------------------------

[#](#adjust-ios-build-settings)

1. Launch Xcode.- Open the `ios/Runner.xcworkspace` file inside the Flutter project's `ios` folder.

     *merge\_type* Version note

     If you use a Flutter version earlier than 3.27, you need to manually opt in to deep linking by adding the key and value pair `FlutterDeepLinkingEnabled` and `YES` to `info.Plist`.

     *info* Note

     If you're using third-party plugins to handle deep links, such as [app\_links](https://pub.dev/packages/app_links), Flutter's default deeplink handler will break these plugins.

     If you use a third-party plugin, add the key and value pair `FlutterDeepLinkingEnabled` and `NO` to `info.Plist`.

### Add associated domains

[#](#add-associated-domains)

*warning* Warning

Personal development teams don't support the Associated Domains capability. To add associated domains, choose the IDE tab.

* [Xcode](#41-tab-panel)* [Other editors](#42-tab-panel)

1. Launch Xcode if necessary.- Click the top-level **Runner**.- In the Editor, click the **Runner** target.- Click **Signing & Capabilities**.- To add a new domain, click **+ Capability** under **Signing & Capabilities**.- Click **Associated Domains**.

             ![Xcode associated domains screenshot](/assets/images/docs/cookbook/set-up-universal-links-associated-domains.png)- In the **Associated Domains** section, click **+**.- Enter `applinks:<web domain="">`. Replace `<web domain="">` with your own domain name.

                 ![Xcode add associated domains screenshot](/assets/images/docs/cookbook/set-up-universal-links-add-associated-domains.png)

1. Open the `ios/Runner/Runner.entitlements` XML file in your preferred editor.- Add an associated domain inside the `<dict>` tag.

     xml

     ```
     <!--?xml version="1.0" encoding="UTF-8"?-->

     <plist version="1.0">
     <dict>
       <key>com.apple.developer.associated-domains</key>
       <array>
         <string>applinks:example.com</string>
       </array>
     </dict>
     </plist>
     ```

     - Save the `ios/Runner/Runner.entitlements` file.

To check that the associated domains you created are available, perform the following steps:

1. Launch Xcode if necessary.- Click the top-level **Runner**.- In the Editor, click the **Runner** target.- Click **Signing & Capabilities**. The domains should appear in the **Associated Domains** section.

         ![Xcode add associated domains screenshot](/assets/images/docs/cookbook/set-up-universal-links-add-associated-domains.png)

You have finished configuring the application for deep linking.

Associate your app with your web domain
---------------------------------------

[#](#associate-your-app-with-your-web-domain)

You need to host an `apple-app-site-association` file in the web domain. This file tells the mobile browser which iOS application to open instead of the browser. To create the file, find the `appID` of the Flutter app you created in the previous section.

### Locate components of the `appID`

[#](#locate-components-of-the-appid)

Apple formats the `appID` as `<team id>.<bundle id>`.

* Locate the bundle ID in the Xcode project.* Locate the team ID in the [developer account](https://developer.apple.com/account).

**For example:** Given a team ID of `S8QB4VV633` and a bundle ID of `com.example.deeplinkCookbook`, you would enter an `appID` entry of `S8QB4VV633.com.example.deeplinkCookbook`.

### Create and host `apple-app-site-association` JSON file

[#](#create-and-host-apple-app-site-association-json-file)

This file uses the JSON format. Don't include the `.json` file extension when you save this file. Per [Apple's documentation](https://developer.apple.com/documentation/xcode/supporting-associated-domains), this file should resemble the following content:

json

```
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appIDs": [
          "S8QB4VV633.com.example.deeplinkCookbook"
        ],
        "paths": [
          "*"
        ],
        "components": [
          {
            "/": "/*"
          }
        ]
      }
    ]
  },
  "webcredentials": {
    "apps": [
      "S8QB4VV633.com.example.deeplinkCookbook"
    ]
  }
}
```

1. Set one value in the `appIDs` array to `<team id>.<bundle id>`.- Set the `paths` array to `["*"]`. The `paths` array specifies the allowed universal links. Using the asterisk, `*` redirects every path to the Flutter app. If needed, change the `paths` array value to a setting more appropriate to your app.- Host the file at a URL that resembles the following structure.

       `<webdomain>/.well-known/apple-app-site-association`- Verify that your browser can access this file.

*info* Note

If you have more than one scheme/flavor, you can add more than one `appID` into the `appIDs` field.

Test the universal link
-----------------------

[#](#test-the-universal-link)

Test a universal link using a physical iOS device or the Simulator.

*info* Note

It might take up to 24 hours before Apple's [Content Delivery Network](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN) requests the `apple-app-site-association` (AASA) file from your web domain. Until the CDN requests the file, the universal link won't work. To bypass Apple's CDN, check out the [alternate mode section](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_associated-domains?language=objc).

1. Before testing, install the Flutter app on the iOS device or Simulator, Use `flutter run` on the desired device.

   ![Simulator screenshot](/assets/images/docs/cookbook/set-up-universal-links-simulator.png)

   When complete, the Flutter app displays on the home screen of the iOS device or Simulator.- If you test using the Simulator, use the Xcode CLI:

     ```
     xcrun simctl openurl booted https://<web domain>/details
     ```

     - If you test with a physical iOS device:
       1. Launch the **Note** app.- Type the URL in the **Note** app.- Click the resulting link.

       If successful, the Flutter app launches and displays its details screen.

       ![Deeplinked Simulator screenshot](/assets/images/docs/cookbook/set-up-universal-links-simulator-deeplinked.png)

Find the source code
--------------------

[#](#find-the-source-code)

You can find the source code for the [deeplink\_cookbook](https://github.com/flutter/codelabs/tree/main/deeplink_cookbook) recipe in the GitHub repo.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/set-up-universal-links/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/set-up-universal-links.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/set-up-universal-links/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/set-up-universal-links.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-19. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/set-up-universal-links.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/set-up-universal-links/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/set-up-universal-links.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   