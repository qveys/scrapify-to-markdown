UISceneDelegate adoption
========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [UISceneDelegate adoption](/release/breaking-changes/uiscenedelegate)

*info* Note

This is an upcoming breaking change that has not yet been finalized or implemented. The current details are provisional and may be altered. Further announcements will be made as the change approaches implementation.

Summary
-------

[#](#summary)

Apple now requires iOS developers to adopt the UISceneDelegate protocol, which changes the order of initialization when an application launches. If your app on iOS modifies `application:didFinishLaunchingWithOptions:`, it might have to be updated.

Background
----------

[#](#background)

Most Flutter apps won't have custom logic inside of `application:didFinishLaunchingWithOptions:`. Those apps won't need to do any code migration. In most cases, Flutter automatically migrates the `Info.plist`.

Apple now requires the adoption of `UISceneDelegate`, which reorders the initialization of iOS apps. After a `UISceneDelegate` is specified, initialization of the Storyboard is delayed until after calling `application:didFinishLaunchingWithOptions:`. That means `UIApplicationDelegate.window` and `UIApplicationDelegate.window.rootViewController` can't be accessed from `application:didFinishLaunchingWithOptions:`.

Apple is driving the adoption of the `UISceneDelegate` API since it allows apps to have multiple instances of their UIs, like multitasking on iPadOS.

Previously, Flutter’s documentation indicated that `application:didFinishLaunchingWithOptions:` was a good place to set up platform channels to create interop between the host application and Flutter. That is no longer a reliable place to register these platform channels, since the Flutter engine won't have been created yet.

Migration guide
---------------

[#](#migration-guide)

### Info.plist migration

[#](#info-plist-migration)

`UISceneDelegate`s must be specified in an app's `Info.plist` or in `application:configurationForConnectingSceneSession:options:`. The Flutter tool attempts to automatically edit the `Info.plist` if no `UISceneDelegate` is specified, so nothing might be required beyond running `flutter run` or `flutter build` again. Projects can be manually upgraded by adding the following to the `Info.plist`. `FlutterSceneDelegate` is the new class in the Flutter framework that performs as the `UISceneDelegate`.

Info.plist

xml

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
 <key>UIApplicationSceneManifest</key>
 <dict>
  <key>UIApplicationSupportsMultipleScenes</key>
  <false/>
  <key>UISceneConfigurations</key>
  <dict>
  <key>UIWindowSceneSessionRoleApplication</key>
    <array>
      <dict>
        <key>UISceneClassName</key>
        <string>UIWindowScene</string>
        <key>UISceneDelegateClassName</key>
        <string>FlutterSceneDelegate</string>
        <key>UISceneConfigurationName</key>
        <string>flutter</string>
        <key>UISceneStoryboardFile</key>
        <string>Main</string>
      </dict>
    </array>
   </dict>
 </dict>
</dict>
```

As seen in Xcode's editor:

![Xcode plist editor for UISceneDelegate](/assets/images/docs/breaking-changes/uiscenedelegate-plist.png)

### Creating platform channels in `application:didFinishLaunchingWithOptions:`

[#](#creating-platform-channels-in-application-didfinishlaunchingwithoptions)

Apps that create the `FlutterViewController` programmatically can continue to operate as before. Apps that rely on Storyboards (and XIBs) to create platform channels in `application:didFinishLaunchingWithOptions:` should now use the `FlutterPluginRegistrant` API to accomplish the same thing.

#### Before

[#](#before)

* [Swift](#13-tab-panel)* [Obj-C](#14-tab-panel)

swift

```
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
    let batteryChannel = FlutterMethodChannel(name: "samples.flutter.dev/battery",
                                              binaryMessenger: controller.binaryMessenger)
    batteryChannel.setMethodCallHandler({
      [weak self] (call: FlutterMethodCall, result: FlutterResult) -> Void in
      // This method is invoked on the UI thread.
      // Handle battery messages.
    })

    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
```

objc

```
@implementation AppDelegate
- (BOOL)application:(UIApplication*)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions {
  FlutterViewController* controller = (FlutterViewController*)self.window.rootViewController;

  FlutterMethodChannel* batteryChannel = [FlutterMethodChannel
                                          methodChannelWithName:@"samples.flutter.dev/battery"
                                          binaryMessenger:controller.binaryMessenger];

  [batteryChannel setMethodCallHandler:^(FlutterMethodCall* call, FlutterResult result) {
    // This method is invoked on the UI thread.
    // TODO
  }];

  [GeneratedPluginRegistrant registerWithRegistry:self];
  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
@end
```

#### After

[#](#after)

* [Swift](#15-tab-panel)* [Obj-C](#16-tab-panel)

swift

```
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate, FlutterPluginRegistrant {
  override func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    pluginRegistrant = self
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  func register(with registry: any FlutterPluginRegistry) {
    let registrar = registry.registrar(forPlugin: "battery")
    let batteryChannel = FlutterMethodChannel(name: "samples.flutter.dev/battery",
                                              binaryMessenger: registrar!.messenger())
    batteryChannel.setMethodCallHandler({
      [weak self] (call: FlutterMethodCall, result: FlutterResult) -> Void in
      // This method is invoked on the UI thread.
      // Handle battery messages.
    })

    GeneratedPluginRegistrant.register(with: registry)
  }
}
```

objc

```
@interface AppDelegate () <flutterpluginregistrant>
@end

@implementation AppDelegate
- (BOOL)application:(UIApplication*)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions {
  self.pluginRegistrant = self;
  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}

- (void)registerWithRegistry:(NSObject<flutterpluginregistry>*)registry {
  NSObject<flutterpluginregistrar>* registrar = [registry registrarForPlugin:@"battery"];
  FlutterMethodChannel* batteryChannel = [FlutterMethodChannel
                                          methodChannelWithName:@"samples.flutter.dev/battery"
                                          binaryMessenger:registrar.messenger];

  [batteryChannel setMethodCallHandler:^(FlutterMethodCall* call, FlutterResult result) {
    // This method is invoked on the UI thread.
    // TODO
  }];

  [GeneratedPluginRegistrant registerWithRegistry:registry];
}
@end
```

Set up the `FlutterPluginRegistrant` programmatically through the `FlutterAppDelegate`.

### Registering plugins in `application:didFinishLaunchingWithOptions:`

[#](#registering-plugins-in-application-didfinishlaunchingwithoptions)

Most legacy Flutter projects register plugins with `GeneratedPluginRegistrant` at application launch. The `GeneratedPluginRegistrant` object registers platform channels under the hood and should be migrated as [platform channels are migrating](#creating-platform-channels-in-application-didfinishlaunchingwithoptions). This will avoid any runtime warnings about using a `FlutterLaunchEngine`.

* [Swift](#17-tab-panel)* [Obj-C](#18-tab-panel)

swift

```
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate, FlutterPluginRegistrant {
  override func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    pluginRegistrant = self
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  func register(with registry: any FlutterPluginRegistry) {
    GeneratedPluginRegistrant.register(with: registry)
  }
}
```

objc

```
@interface AppDelegate () <flutterpluginregistrant>
@end

@implementation AppDelegate
- (BOOL)application:(UIApplication*)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions {
  self.pluginRegistrant = self;
  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}

- (void)registerWithRegistry:(NSObject<flutterpluginregistry>*)registry {
  [GeneratedPluginRegistrant registerWithRegistry:registry];
}
@end
```

### Bespoke FlutterViewController usage

[#](#bespoke-flutterviewcontroller-usage)

For apps that use a `FlutterViewController` instantiated from Storyboards in `application:didFinishLaunchingWithOptions:` for reasons other than creating platform channels, it is their responsibility to accommodate the new initialization order.

Migration options:

* Subclass `FlutterViewController` and put the logic in the subclasses' `awakeFromNib`.* Specify a `UISceneDelegate` in the `Info.plist` or in the `UIApplicationDelegate` and put the logic in `scene:willConnectToSession:options:`. For more information, check out [Apple's documentation](https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports).

#### Example

[#](#example)

swift

```
@objc class MyViewController: FlutterViewController {
  override func awakeFromNib() {
    self.awakeFromNib()
    doSomethingWithFlutterViewController(self)
  }
}
```

Timeline
--------

[#](#timeline)

* Landed in version: Not yet* In stable release: Not yet* Unknown: Apple changes their warning to an assert and Flutter apps that haven't adopted `UISceneDelegate` will start crashing on startup with the latest SDK.

References
----------

[#](#references)

* [Issue 167267](https://github.com/flutter/flutter/issues/167267) - The initial reported issue.* [Apple's documentation on specifying `UISceneDelegate`s](https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/uiscenedelegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/uiscenedelegate.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/uiscenedelegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/uiscenedelegate.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/uiscenedelegate.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/uiscenedelegate/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/uiscenedelegate.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   