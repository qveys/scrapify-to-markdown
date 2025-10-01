iOS FlutterViewController splashScreenView made nullable
========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [iOS FlutterViewController splashScreenView made nullable](/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable)

Summary
-------

[#](#summary)

The `FlutterViewController` property `splashScreenView` has been changed from `nonnull` to `nullable`.

Old declaration of `splashScreenView`:

objc

```
@property(strong, nonatomic) UIView* splashScreenView;
```

New declaration of `splashScreenView`:

objc

```
@property(strong, nonatomic, nullable) UIView* splashScreenView;
```

Context
-------

[#](#context)

Prior to this change, on iOS the `splashScreenView` property returned `nil` when no splash screen view was set, and setting the property to `nil` removed the splash screen view. However, the `splashScreenView` API was incorrectly marked `nonnull`. This property is most often used when transitioning to Flutter views in iOS add-to-app scenarios.

Description of change
---------------------

[#](#description-of-change)

While it was possible in Objective-C to work around the incorrect `nonnull` annotation by setting `splashScreenView` to a `nil` `UIView`, in Swift this caused a compilation error:

```
error build: Value of optional type 'UIView?' must be unwrapped to a value of type 'UIView'
```

[PR #34743](https://github.com/flutter/engine/pull/34743) updates the property attribute to `nullable`. It can return `nil` and can be set to `nil` to remove the view in both Objective-C and Swift.

Migration guide
---------------

[#](#migration-guide)

If `splashScreenView` is stored in a `UIView` variable in Swift, update to an optional type `UIView?`.

Code before migration:

swift

```
  var splashScreenView = UIView()
  var flutterEngine = FlutterEngine(name: "my flutter engine")
  let flutterViewController = FlutterViewController(engine: flutterEngine, nibName: nil, bundle: nil)
  splashScreenView = flutterViewController.splashScreenView // compilation error: Value of optional type 'UIView?' must be unwrapped to a value of type 'UIView'
```

Code after migration:

swift

```
  var splashScreenView : UIView? = UIView()
  var flutterEngine = FlutterEngine(name: "my flutter engine")
  let flutterViewController = FlutterViewController(engine: flutterEngine, nibName: nil, bundle: nil)
  let splashScreenView = flutterViewController.splashScreenView // compiles successfully
  if let splashScreenView = splashScreenView {
  }
```

Timeline
--------

[#](#timeline)

In stable release: 3.7

References
----------

[#](#references)

Relevant PR:

* [Make splashScreenView of FlutterViewController nullable](https://github.com/flutter/engine/pull/34743)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ios-flutterviewcontroller-splashscreenview-nullable.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   