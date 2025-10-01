Add a Flutter screen to an iOS app
==================================

1. [Add to app](/add-to-app) chevron\_right- [Add Flutter to iOS](/add-to-app/ios) chevron\_right- [Add a Flutter screen](/add-to-app/ios/add-flutter-screen)

This guide describes how to add a single Flutter screen to an existing iOS app.

Start a FlutterEngine and FlutterViewController
-----------------------------------------------

[#](#start-a-flutterengine-and-flutterviewcontroller)

To launch a Flutter screen from an existing iOS app, you start a [`FlutterEngine`](https://api.flutter.dev/ios-embedder/interface_flutter_engine.html) and a [`FlutterViewController`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html).

*info* Note

The `FlutterEngine` serves as a host to the Dart VM and your Flutter runtime, and the `FlutterViewController` attaches to a `FlutterEngine` to pass input events into Flutter and to display frames rendered by the `FlutterEngine`.

The `FlutterEngine` might have the same lifespan as your `FlutterViewController` or outlive your `FlutterViewController`.

*lightbulb* Tip

It's generally recommended to pre-warm a long-lived `FlutterEngine` for your application because:

* The first frame appears faster when showing the `FlutterViewController`.* Your Flutter and Dart state will outlive one `FlutterViewController`.* Your application and your plugins can interact with Flutter and your Dart logic before showing the UI.

See [Loading sequence and performance](/add-to-app/performance) for more analysis on the latency and memory trade-offs of pre-warming an engine.

### Create a FlutterEngine

[#](#create-a-flutterengine)

Where you create a `FlutterEngine` depends on your host app.

* [SwiftUI](#72-tab-panel)* [UIKit-Swift](#73-tab-panel)* [UIKit-ObjC](#74-tab-panel)

In this example, we create a `FlutterEngine` object inside a SwiftUI [`Observable`](https://developer.apple.com/documentation/observation/observable) object called `FlutterDependencies`. Pre-warm the engine by calling `run()`, and then inject this object into a `ContentView` using the `environment()` view modifier.

MyApp.swift

swift

```
import SwiftUI
import Flutter
// The following library connects plugins with iOS platform code to this app.
import FlutterPluginRegistrant

@Observable
class FlutterDependencies {
 let flutterEngine = FlutterEngine(name: "my flutter engine")
 init() {
   // Runs the default Dart entrypoint with a default Flutter route.
   flutterEngine.run()
   // Connects plugins with iOS platform code to this app.
   GeneratedPluginRegistrant.register(with: self.flutterEngine);
 }
}

@main
struct MyApp: App {
   // flutterDependencies will be injected through the view environment.
   @State var flutterDependencies = FlutterDependencies()
   var body: some Scene {
     WindowGroup {
       ContentView()
         .environment(flutterDependencies)
     }
   }
}
```

As an example, we demonstrate creating a `FlutterEngine`, exposed as a property, on app startup in the app delegate.

AppDelegate.swift

swift

```
import UIKit
import Flutter
// The following library connects plugins with iOS platform code to this app.
import FlutterPluginRegistrant

@UIApplicationMain
class AppDelegate: FlutterAppDelegate { // More on the FlutterAppDelegate.
  lazy var flutterEngine = FlutterEngine(name: "my flutter engine")

  override func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Runs the default Dart entrypoint with a default Flutter route.
    flutterEngine.run();
    // Connects plugins with iOS platform code to this app.
    GeneratedPluginRegistrant.register(with: self.flutterEngine);
    return super.application(application, didFinishLaunchingWithOptions: launchOptions);
  }
}
```

The following example demonstrates creating a `FlutterEngine`, exposed as a property, on app startup in the app delegate.

AppDelegate.h

objc

```
@import UIKit;
@import Flutter;

@interface AppDelegate : FlutterAppDelegate // More on the FlutterAppDelegate below.
@property (nonatomic,strong) FlutterEngine *flutterEngine;
@end
```

AppDelegate.m

objc

```
// The following library connects plugins with iOS platform code to this app.
#import <flutterpluginregistrant generatedpluginregistrant.h="">

#import "AppDelegate.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary<uiapplicationlaunchoptionskey, id=""> *)launchOptions {
  self.flutterEngine = [[FlutterEngine alloc] initWithName:@"my flutter engine"];
  // Runs the default Dart entrypoint with a default Flutter route.
  [self.flutterEngine run];
  // Connects plugins with iOS platform code to this app.
  [GeneratedPluginRegistrant registerWithRegistry:self.flutterEngine];
  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}

@end
```

</uiapplicationlaunchoptionskey,>

### Show a FlutterViewController with your FlutterEngine

[#](#show-a-flutterviewcontroller-with-your-flutterengine)

* [SwiftUI](#75-tab-panel)* [UIKit-Swift](#76-tab-panel)* [UIKit-ObjC](#77-tab-panel)

The following example shows a generic `ContentView` with a [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) hooked to a flutter screen. First, create a `FlutterViewControllerRepresentable` to represent the `FlutterViewController`. The `FlutterViewController` constructor takes the pre-warmed `FlutterEngine` as an argument, which is injected through the view environment.

ContentView.swift

swift

```
import SwiftUI
import Flutter

struct FlutterViewControllerRepresentable: UIViewControllerRepresentable {
  // Flutter dependencies are passed in through the view environment.
  @Environment(FlutterDependencies.self) var flutterDependencies
  
  func makeUIViewController(context: Context) -> some UIViewController {
    return FlutterViewController(
      engine: flutterDependencies.flutterEngine,
      nibName: nil,
      bundle: nil)
  }
  
  func updateUIViewController(_ uiViewController: UIViewControllerType, context: Context) {}
}

struct ContentView: View {
  var body: some View {
    NavigationStack {
      NavigationLink("My Flutter Feature") {
        FlutterViewControllerRepresentable()
      }
    }
  }
}
```

Now, you have a Flutter screen embedded in your iOS app.

*info* Note

In this example, your Dart `main()` entrypoint function runs when the `FlutterDependencies` observable is initialized.

The following example shows a generic `ViewController` with a `UIButton` hooked to present a [`FlutterViewController`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html). The `FlutterViewController` uses the `FlutterEngine` instance created in the `AppDelegate`.

ViewController.swift

swift

```
import UIKit
import Flutter

class ViewController: UIViewController {
  override func viewDidLoad() {
    super.viewDidLoad()

    // Make a button to call the showFlutter function when pressed.
    let button = UIButton(type:UIButton.ButtonType.custom)
    button.addTarget(self, action: #selector(showFlutter), for: .touchUpInside)
    button.setTitle("Show Flutter!", for: UIControl.State.normal)
    button.frame = CGRect(x: 80.0, y: 210.0, width: 160.0, height: 40.0)
    button.backgroundColor = UIColor.blue
    self.view.addSubview(button)
  }

  @objc func showFlutter() {
    let flutterEngine = (UIApplication.shared.delegate as! AppDelegate).flutterEngine
    let flutterViewController =
        FlutterViewController(engine: flutterEngine, nibName: nil, bundle: nil)
    present(flutterViewController, animated: true, completion: nil)
  }
}
```

Now, you have a Flutter screen embedded in your iOS app.

*info* Note

Using the previous example, the default `main()` entrypoint function of your default Dart library would run when calling `run` on the `FlutterEngine` created in the `AppDelegate`.

The following example shows a generic `ViewController` with a `UIButton` hooked to present a [`FlutterViewController`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html). The `FlutterViewController` uses the `FlutterEngine` instance created in the `AppDelegate`.

ViewController.m

objc

```
@import Flutter;
#import "AppDelegate.h"
#import "ViewController.h"

@implementation ViewController
- (void)viewDidLoad {
    [super viewDidLoad];

    // Make a button to call the showFlutter function when pressed.
    UIButton *button = [UIButton buttonWithType:UIButtonTypeCustom];
    [button addTarget:self
               action:@selector(showFlutter)
     forControlEvents:UIControlEventTouchUpInside];
    [button setTitle:@"Show Flutter!" forState:UIControlStateNormal];
    button.backgroundColor = UIColor.blueColor;
    button.frame = CGRectMake(80.0, 210.0, 160.0, 40.0);
    [self.view addSubview:button];
}

- (void)showFlutter {
    FlutterEngine *flutterEngine =
        ((AppDelegate *)UIApplication.sharedApplication.delegate).flutterEngine;
    FlutterViewController *flutterViewController =
        [[FlutterViewController alloc] initWithEngine:flutterEngine nibName:nil bundle:nil];
    [self presentViewController:flutterViewController animated:YES completion:nil];
}
@end
```

Now, you have a Flutter screen embedded in your iOS app.

*info* Note

Using the previous example, the default `main()` entrypoint function of your default Dart library would run when calling `run` on the `FlutterEngine` created in the `AppDelegate`.

### *Alternatively* - Create a FlutterViewController with an implicit FlutterEngine

[#](#alternatively-create-a-flutterviewcontroller-with-an-implicit-flutterengine)

As an alternative to the previous example, you can let the `FlutterViewController` implicitly create its own `FlutterEngine` without pre-warming one ahead of time.

This is not usually recommended because creating a `FlutterEngine` on-demand could introduce a noticeable latency between when the `FlutterViewController` is presented and when it renders its first frame. This could, however, be useful if the Flutter screen is rarely shown, when there are no good heuristics to determine when the Dart VM should be started, and when Flutter doesn't need to persist state between view controllers.

To let the `FlutterViewController` present without an existing `FlutterEngine`, omit the `FlutterEngine` construction, and create the `FlutterViewController` without an engine reference.

* [SwiftUI](#78-tab-panel)* [UIKit-Swift](#79-tab-panel)* [UIKit-ObjC](#80-tab-panel)

ContentView.swift

swift

```
import SwiftUI
import Flutter

struct FlutterViewControllerRepresentable: UIViewControllerRepresentable {
  func makeUIViewController(context: Context) -> some UIViewController {
    return FlutterViewController(
      project: nil,
      nibName: nil,
      bundle: nil)
  }
  
  func updateUIViewController(_ uiViewController: UIViewControllerType, context: Context) {}
}

struct ContentView: View {
  var body: some View {
    NavigationStack {
      NavigationLink("My Flutter Feature") {
        FlutterViewControllerRepresentable()
      }
    }
  }
}
```

ViewController.swift

swift

```
// Existing code omitted.
func showFlutter() {
  let flutterViewController = FlutterViewController(project: nil, nibName: nil, bundle: nil)
  present(flutterViewController, animated: true, completion: nil)
}
```

ViewController.m

objc

```
// Existing code omitted.
- (void)showFlutter {
  FlutterViewController *flutterViewController =
      [[FlutterViewController alloc] initWithProject:nil nibName:nil bundle:nil];
  [self presentViewController:flutterViewController animated:YES completion:nil];
}
@end
```

See [Loading sequence and performance](/add-to-app/performance) for more explorations on latency and memory usage.

Using the FlutterAppDelegate
----------------------------

[#](#using-the-flutterappdelegate)

Letting your application's `UIApplicationDelegate` subclass `FlutterAppDelegate` is recommended but not required.

The `FlutterAppDelegate` performs functions such as:

* Forwarding application callbacks such as [`openURL`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623112-application) to plugins such as [local\_auth](https://pub.dev/packages/local_auth).* Keeping the Flutter connection open in debug mode when the phone screen locks.

### Creating a FlutterAppDelegate subclass

[#](#creating-a-flutterappdelegate-subclass)

Creating a subclass of the `FlutterAppDelegate` in UIKit apps was shown in the [Start a FlutterEngine and FlutterViewController section](/add-to-app/ios/add-flutter-screen/#start-a-flutterengine-and-flutterviewcontroller). In a SwiftUI app, you can create a subclass of the `FlutterAppDelegate` and annotate it with the [`Observable()`](https://developer.apple.com/documentation/observation/observable()) macro as follows:

MyApp.swift

swift

```
import SwiftUI
import Flutter
import FlutterPluginRegistrant

@Observable
class AppDelegate: FlutterAppDelegate {
  let flutterEngine = FlutterEngine(name: "my flutter engine")

  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
      // Runs the default Dart entrypoint with a default Flutter route.
      flutterEngine.run();
      // Used to connect plugins (only if you have plugins with iOS platform code).
      GeneratedPluginRegistrant.register(with: self.flutterEngine);
      return true;
    }
}

@main
struct MyApp: App {
  // Use this property wrapper to tell SwiftUI
  // it should use the AppDelegate class for the application delegate
  @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

  var body: some Scene {
      WindowGroup {
        ContentView()
      }
  }
}
```

Then, in your view, the `AppDelegate` is accessible through the view environment.

ContentView.swift

swift

```
import SwiftUI
import Flutter

struct FlutterViewControllerRepresentable: UIViewControllerRepresentable {
  // Access the AppDelegate through the view environment.
  @Environment(AppDelegate.self) var appDelegate
  
  func makeUIViewController(context: Context) -> some UIViewController {
    return FlutterViewController(
      engine: appDelegate.flutterEngine,
      nibName: nil,
      bundle: nil)
  }
  
  func updateUIViewController(_ uiViewController: UIViewControllerType, context: Context) {}
}

struct ContentView: View {
  var body: some View {
    NavigationStack {
      NavigationLink("My Flutter Feature") {
        FlutterViewControllerRepresentable()
      }
    }
  }
}
```

### If you can't directly make FlutterAppDelegate a subclass

[#](#if-you-cant-directly-make-flutterappdelegate-a-subclass)

If your app delegate can't directly make `FlutterAppDelegate` a subclass, make your app delegate implement the `FlutterAppLifeCycleProvider` protocol in order to make sure your plugins receive the necessary callbacks. Otherwise, plugins that depend on these events might have undefined behavior.

For instance:

* [Swift](#81-tab-panel)* [Objective-C](#82-tab-panel)

AppDelegate.swift

swift

```
import Foundation
import Flutter

@Observable
class AppDelegate: UIResponder, UIApplicationDelegate, FlutterAppLifeCycleProvider {

  private let lifecycleDelegate = FlutterPluginAppLifeCycleDelegate()

  let flutterEngine = FlutterEngine(name: "my flutter engine")

  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    flutterEngine.run()
    return lifecycleDelegate.application(application, didFinishLaunchingWithOptions: launchOptions ?? [:])
  }

  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    lifecycleDelegate.application(application, didRegisterForRemoteNotificationsWithDeviceToken: deviceToken)
  }

  func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
    lifecycleDelegate.application(application, didFailToRegisterForRemoteNotificationsWithError: error)
  }

  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    lifecycleDelegate.application(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    return lifecycleDelegate.application(app, open: url, options: options)
  }

  func application(_ application: UIApplication, handleOpen url: URL) -> Bool {
    return lifecycleDelegate.application(application, handleOpen: url)
  }

  func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
    return lifecycleDelegate.application(application, open: url, sourceApplication: sourceApplication ?? "", annotation: annotation)
  }

  func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem, completionHandler: @escaping (Bool) -> Void) {
    lifecycleDelegate.application(application, performActionFor: shortcutItem, completionHandler: completionHandler)
  }

  func application(_ application: UIApplication, handleEventsForBackgroundURLSession identifier: String, completionHandler: @escaping () -> Void) {
    lifecycleDelegate.application(application, handleEventsForBackgroundURLSession: identifier, completionHandler: completionHandler)
  }

  func application(_ application: UIApplication, performFetchWithCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    lifecycleDelegate.application(application, performFetchWithCompletionHandler: completionHandler)
  }

  func add(_ delegate: FlutterApplicationLifeCycleDelegate) {
    lifecycleDelegate.add(delegate)
  }
}
```

AppDelegate.h

objc

```
@import Flutter;
@import UIKit;
@import FlutterPluginRegistrant;

@interface AppDelegate : UIResponder <uiapplicationdelegate, flutterapplifecycleprovider="">
@property (strong, nonatomic) UIWindow *window;
@property (nonatomic,strong) FlutterEngine *flutterEngine;
@end
```

The implementation should delegate mostly to a `FlutterPluginAppLifeCycleDelegate`:

AppDelegate.m

objc

```
@interface AppDelegate ()
@property (nonatomic, strong) FlutterPluginAppLifeCycleDelegate* lifeCycleDelegate;
@end

@implementation AppDelegate

- (instancetype)init {
    if (self = [super init]) {
        _lifeCycleDelegate = [[FlutterPluginAppLifeCycleDelegate alloc] init];
    }
    return self;
}

- (BOOL)application:(UIApplication*)application
didFinishLaunchingWithOptions:(NSDictionary<uiapplicationlaunchoptionskey, id="">*))launchOptions {
    self.flutterEngine = [[FlutterEngine alloc] initWithName:@"io.flutter" project:nil];
    [self.flutterEngine runWithEntrypoint:nil];
    [GeneratedPluginRegistrant registerWithRegistry:self.flutterEngine];
    return [_lifeCycleDelegate application:application didFinishLaunchingWithOptions:launchOptions];
}

// Returns the key window's rootViewController, if it's a FlutterViewController.
// Otherwise, returns nil.
- (FlutterViewController*)rootFlutterViewController {
    UIViewController* viewController = [UIApplication sharedApplication].keyWindow.rootViewController;
    if ([viewController isKindOfClass:[FlutterViewController class]]) {
        return (FlutterViewController*)viewController;
    }
    return nil;
}

- (void)application:(UIApplication*)application
didRegisterUserNotificationSettings:(UIUserNotificationSettings*)notificationSettings {
    [_lifeCycleDelegate application:application
didRegisterUserNotificationSettings:notificationSettings];
}

- (void)application:(UIApplication*)application
didRegisterForRemoteNotificationsWithDeviceToken:(NSData*)deviceToken {
    [_lifeCycleDelegate application:application
didRegisterForRemoteNotificationsWithDeviceToken:deviceToken];
}

- (void)application:(UIApplication*)application
didReceiveRemoteNotification:(NSDictionary*)userInfo
fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
    [_lifeCycleDelegate application:application
       didReceiveRemoteNotification:userInfo
             fetchCompletionHandler:completionHandler];
}

- (BOOL)application:(UIApplication*)application
            openURL:(NSURL*)url
            options:(NSDictionary<uiapplicationopenurloptionskey, id="">*)options {
    return [_lifeCycleDelegate application:application openURL:url options:options];
}

- (BOOL)application:(UIApplication*)application handleOpenURL:(NSURL*)url {
    return [_lifeCycleDelegate application:application handleOpenURL:url];
}

- (BOOL)application:(UIApplication*)application
            openURL:(NSURL*)url
  sourceApplication:(NSString*)sourceApplication
         annotation:(id)annotation {
    return [_lifeCycleDelegate application:application
                                   openURL:url
                         sourceApplication:sourceApplication
                                annotation:annotation];
}

- (void)application:(UIApplication*)application
performActionForShortcutItem:(UIApplicationShortcutItem*)shortcutItem
  completionHandler:(void (^)(BOOL succeeded))completionHandler {
    [_lifeCycleDelegate application:application
       performActionForShortcutItem:shortcutItem
                  completionHandler:completionHandler];
}

- (void)application:(UIApplication*)application
handleEventsForBackgroundURLSession:(nonnull NSString*)identifier
  completionHandler:(nonnull void (^)(void))completionHandler {
    [_lifeCycleDelegate application:application
handleEventsForBackgroundURLSession:identifier
                  completionHandler:completionHandler];
}

- (void)application:(UIApplication*)application
performFetchWithCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
    [_lifeCycleDelegate application:application performFetchWithCompletionHandler:completionHandler];
}

- (void)addApplicationLifeCycleDelegate:(NSObject<flutterplugin>*)delegate {
    [_lifeCycleDelegate addDelegate:delegate];
}
@end
```

</uiapplicationopenurloptionskey,></uiapplicationlaunchoptionskey,></uiapplicationdelegate,>

Launch options
--------------

[#](#launch-options)

The examples demonstrate running Flutter using the default launch settings.

In order to customize your Flutter runtime, you can also specify the Dart entrypoint, library, and route.

### Dart entrypoint

[#](#dart-entrypoint)

Calling `run` on a `FlutterEngine`, by default, runs the `main()` Dart function of your `lib/main.dart` file.

You can also run a different entrypoint function by using [`runWithEntrypoint`](https://api.flutter.dev/ios-embedder/interface_flutter_engine.html#a019d6b3037eff6cfd584fb2eb8e9035e) with an `NSString` specifying a different Dart function.

*info* Note

Dart entrypoint functions other than `main()` must be annotated with the following in order to not be [tree-shaken](https://en.wikipedia.org/wiki/Tree_shaking) away when compiling:

dart

```
@pragma('vm:entry-point')
void myOtherEntrypoint() { ... };
```

### Dart library

[#](#dart-library)

In addition to specifying a Dart function, you can specify an entrypoint function in a specific file.

For instance the following runs `myOtherEntrypoint()` in `lib/other_file.dart` instead of `main()` in `lib/main.dart`:

* [Swift](#83-tab-panel)* [Objective-C](#84-tab-panel)

swift

```
flutterEngine.run(withEntrypoint: "myOtherEntrypoint", libraryURI: "other_file.dart")
```

objc

```
[flutterEngine runWithEntrypoint:@"myOtherEntrypoint" libraryURI:@"other_file.dart"];
```

### Route

[#](#route)

Starting in Flutter version 1.22, an initial route can be set for your Flutter [`WidgetsApp`](https://api.flutter.dev/flutter/widgets/WidgetsApp-class.html) when constructing the FlutterEngine or the FlutterViewController.

* [Swift](#85-tab-panel)* [Objective-C](#86-tab-panel)

swift

```
let flutterEngine = FlutterEngine()
// FlutterDefaultDartEntrypoint is the same as nil, which will run main().
engine.run(
  withEntrypoint: "main", initialRoute: "/onboarding")
```

objc

```
FlutterEngine *flutterEngine = [[FlutterEngine alloc] init];
// FlutterDefaultDartEntrypoint is the same as nil, which will run main().
[flutterEngine runWithEntrypoint:FlutterDefaultDartEntrypoint
                    initialRoute:@"/onboarding"];
```

This code sets your `dart:ui`'s [`PlatformDispatcher.defaultRouteName`](https://api.flutter.dev/flutter/dart-ui/PlatformDispatcher/defaultRouteName.html) to `"/onboarding"` instead of `"/"`.

Alternatively, to construct a FlutterViewController directly without pre-warming a FlutterEngine:

* [Swift](#87-tab-panel)* [Objective-C](#88-tab-panel)

swift

```
let flutterViewController = FlutterViewController(
      project: nil, initialRoute: "/onboarding", nibName: nil, bundle: nil)
```

objc

```
FlutterViewController* flutterViewController =
      [[FlutterViewController alloc] initWithProject:nil
                                        initialRoute:@"/onboarding"
                                             nibName:nil
                                              bundle:nil];
```

*lightbulb* Tip

In order to imperatively change your current Flutter route from the platform side after the `FlutterEngine` is already running, use [`pushRoute()`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html#ac7cffbf03f9c8c0b28d1f0dafddece4e) or [`popRoute()`](https://api.flutter.dev/ios-embedder/interface_flutter_view_controller.html#ac89c8010fbf7a39f7aaab64f68c013d2) on the `FlutterViewController`.

To pop the iOS route from the Flutter side, call [`SystemNavigator.pop()`](https://api.flutter.dev/flutter/services/SystemNavigator/pop.html).

See [Navigation and routing](/ui/navigation) for more about Flutter's routes.

### Other

[#](#other)

The previous example only illustrates a few ways to customize how a Flutter instance is initiated. Using [platform channels](/platform-integration/platform-channels), you're free to push data or prepare your Flutter environment in any way you'd like, before presenting the Flutter UI using a `FlutterViewController`.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/ios/add-flutter-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/ios/add-flutter-screen.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/ios/add-flutter-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/ios/add-flutter-screen.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/add-to-app/ios/add-flutter-screen.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/add-to-app/ios/add-flutter-screen/&page-source=https://github.com/flutter/website/tree/main/src/content/add-to-app/ios/add-flutter-screen.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   