Hosting native macOS views in your Flutter app with Platform Views
==================================================================

1. [Platform integration](/platform-integration) chevron\_right- [macOS](/platform-integration/macos) chevron\_right- [macOS platform-views](/platform-integration/macos/platform-views)

Platform views allow you to embed native views in a Flutter app, so you can apply transforms, clips, and opacity to the native view from Dart.

This allows you, for example, to use the native web views directly inside your Flutter app.

*info* Note

This page discusses how to host your own native macOS views within a Flutter app. If you'd like to embed native Android views in your Flutter app, see [Hosting native Android views](/platform-integration/android/platform-views). If you'd like to embed native iOS views in your Flutter app, see [Hosting native iOS views](/platform-integration/ios/platform-views).

*merge\_type* Version note

Platform view support on macOS isn't fully functional as of the current release. For example, gesture support isn't yet available on macOS. Stay tuned for a future stable release.

macOS uses Hybrid composition, which means that the native `NSView` is appended to the view hierarchy.

To create a platform view on macOS, use the following instructions:

On the Dart side
----------------

[#](#on-the-dart-side)

On the Dart side, create a `Widget` and add the build implementation, as shown in the following steps:

In the Dart widget file, make changes similar to those shown in `native_view_example.dart`:

1. Add the following imports:

   dart

   ```
   import 'package:flutter/foundation.dart';
   import 'package:flutter/services.dart';
   ```

   - Implement a `build()` method:

     dart

     ```
     Widget build(BuildContext context) {
       // This is used in the platform side to register the view.
       const String viewType = '<platform-view-type>';
       // Pass parameters to the platform side.
       final Map<String, dynamic> creationParams = <String, dynamic>{};

       return AppKitView(
         viewType: viewType,
         layoutDirection: TextDirection.ltr,
         creationParams: creationParams,
         creationParamsCodec: const StandardMessageCodec(),
       );
     }
     ```

For more information, check out the [`AppKitView`](https://api.flutter.dev/flutter/widgets/AppKitView-class.html) API docs.

On the platform side
--------------------

[#](#on-the-platform-side)

Implement the factory and the platform view. The `NativeViewFactory` creates the platform view, and the platform view provides a reference to the `NSView`. For example, `NativeView.swift`:

NativeView.swift

swift

```
import Cocoa
import FlutterMacOS

class NativeViewFactory: NSObject, FlutterPlatformViewFactory {
  private var messenger: FlutterBinaryMessenger

  init(messenger: FlutterBinaryMessenger) {
    self.messenger = messenger
    super.init()
  }

  func create(
    withViewIdentifier viewId: Int64,
    arguments args: Any?
  ) -> NSView {
    return NativeView(
      viewIdentifier: viewId,
      arguments: args,
      binaryMessenger: messenger)
  }

  /// Implementing this method is only necessary when
  /// the `arguments` in `createWithFrame` is not `nil`.
  public func createArgsCodec() -> (FlutterMessageCodec & NSObjectProtocol)? {
    return FlutterStandardMessageCodec.sharedInstance()
  }
}

class NativeView: NSView {

  init(
    viewIdentifier viewId: Int64,
    arguments args: Any?,
    binaryMessenger messenger: FlutterBinaryMessenger?
  ) {
    super.init(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
    wantsLayer = true
    layer?.backgroundColor = NSColor.systemBlue.cgColor
    // macOS views can be created here
    createNativeView(view: self)
  }

    required init?(coder nsCoder: NSCoder) {
        super.init(coder: nsCoder)
    }

  func createNativeView(view _view: NSView) {
    let nativeLabel = NSTextField()
    nativeLabel.frame = CGRect(x: 0, y: 0, width: 180, height: 48.0)
    nativeLabel.stringValue = "Native text from macOS"
    nativeLabel.textColor = NSColor.black
    nativeLabel.font = NSFont.systemFont(ofSize: 14)
    nativeLabel.isBezeled = false
    nativeLabel.focusRingType = .none
    nativeLabel.isEditable = true
    nativeLabel.sizeToFit()
    _view.addSubview(nativeLabel)
  }
}
```

Finally, register the platform view. This can be done in an app or a plugin.

For app registration, modify the App's `MainFlutterWindow.swift`:

MainFlutterWindow.swift

swift

```
import Cocoa
import FlutterMacOS

class MainFlutterWindow: NSWindow {
  override func awakeFromNib() {
    // ...

    let registrar = flutterViewController.registrar(forPlugin: "plugin-name")
    let factory = NativeViewFactory(messenger: registrar.messenger)
    registrar.register(
      factory,
      withId: "<platform-view-type>")
  }
}
```

For plugin registration, modify the plugin's main file:

Plugin.swift

swift

```
import Cocoa
import FlutterMacOS

public class Plugin: NSObject, FlutterPlugin {
  public static func register(with registrar: FlutterPluginRegistrar) {
    let factory = NativeViewFactory(messenger: registrar.messenger)
    registrar.register(factory, withId: "<platform-view-type>")
  }
}
```

For more information, check out the API docs for:

* [`FlutterPlatformViewFactory`](https://api.flutter.dev/ios-embedder/protocol_flutter_platform_view_factory-p.html)* [`FlutterPlatformView`](https://api.flutter.dev/ios-embedder/protocol_flutter_platform_view-p.html)* [`PlatformView`](https://api.flutter.dev/javadoc/io/flutter/plugin/platform/PlatformView.html)

Putting it together
-------------------

[#](#putting-it-together)

When implementing the `build()` method in Dart, you can use [`defaultTargetPlatform`](https://api.flutter.dev/flutter/foundation/defaultTargetPlatform.html) to detect the platform, and decide which widget to use:

dart

```
Widget build(BuildContext context) {
  // This is used in the platform side to register the view.
  const String viewType = '<platform-view-type>';
  // Pass parameters to the platform side.
  final Map<String, dynamic> creationParams = <String, dynamic>{};

  switch (defaultTargetPlatform) {
    case TargetPlatform.android:
    // return widget on Android.
    case TargetPlatform.iOS:
    // return widget on iOS.
    case TargetPlatform.macOS:
    // return widget on macOS.
    default:
      throw UnsupportedError('Unsupported platform view');
  }
}
```

Performance
-----------

[#](#performance)

Platform views in Flutter come with performance trade-offs.

For example, in a typical Flutter app, the Flutter UI is composed on a dedicated raster thread. This allows Flutter apps to be fast, as this thread is rarely blocked.

When a platform view is rendered with hybrid composition, the Flutter UI continues to be composed from the dedicated raster thread, but the platform view performs graphics operations on the platform thread. To rasterize the combined contents, Flutter performs synchronization between its raster thread and the platform thread. As such, any slow or blocking operations on the platform thread can negatively impact Flutter graphics performance.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/platform-views/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/platform-views.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/platform-views/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/platform-views.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/platform-views.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/macos/platform-views/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/macos/platform-views.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   