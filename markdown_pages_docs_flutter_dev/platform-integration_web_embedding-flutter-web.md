Adding Flutter to any web application
=====================================

1. [Platform integration](/platform-integration) chevron\_right- [Web](/platform-integration/web) chevron\_right- [Add Flutter to any web app](/platform-integration/web/embedding-flutter-web)

Flutter views and web content can be composed to produce a web application in different ways. Choose one of the following depending on your use-case:

* A Flutter view controls the full page ([full page mode](#full-page-mode))* Adding Flutter views to an existing web application ([embedded mode](#embedded-mode))

Full page mode
--------------

[#](#full-page-mode)

In full page mode, the Flutter web application takes control of the whole browser window and covers its viewport completely when rendering.

This is the default embedding mode for new Flutter web projects, and no additional configuration is needed.

html

```
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <script src="flutter_bootstrap.js" defer></script>
  </body>
</html>
```

When Flutter web is launched without referencing `multiViewEnabled` or a `hostElement`, it uses full page mode.

To learn more about the `flutter_bootstrap.js` file, check out [Customize app initialization](/platform-integration/web/initialization/).

### `iframe` embedding

[#](#iframe-embedding)

Full page mode is recommended when embedding a Flutter web application through an `iframe`. The page that embeds the `iframe` can size and position it as needed, and Flutter will fill it completely.

html

```
<iframe src="https://url-to-your-flutter/index.html"></iframe>
```

To learn more about the pros and cons of an `iframe`, check out the [Inline Frame element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) docs on MDN.

Embedded mode
-------------

[#](#embedded-mode)

Flutter web applications can also render content into an arbitrary number of elements (commonly `div`s) of another web application; this is called "embedded mode" (or "multi-view").

In this mode:

* A Flutter web application can launch, but doesn't render until the first "view" is added, with `addView`.* The host application can add or remove views from the embedded Flutter web application.* The Flutter application is notified when views are added or removed, so it can adjust its widgets accordingly.

### Enable multi-view mode

[#](#enable-multi-view-mode)

Enable multi-view mode setting `multiViewEnabled: true` in the `initializeEngine` method as shown:

flutter\_bootstrap.js

js

```
{{flutter_js}}
{{flutter_build_config}}

_flutter.loader.load({
  onEntrypointLoaded: async function onEntrypointLoaded(engineInitializer) {
    let engine = await engineInitializer.initializeEngine({
      multiViewEnabled: true, // Enables embedded mode.
    });
    let app = await engine.runApp();
    // Make this `app` object available to your JS app.
  }
});
```

### Manage Flutter views from JS

[#](#manage-flutter-views-from-js)

To add or remove views, use the `app` object returned by the `runApp` method:

js

```
// Adding a view...
let viewId = app.addView({
  hostElement: document.querySelector('#some-element'),
});

// Removing viewId...
let viewConfig = app.removeView(viewId);
```

### Handling view changes from Dart

[#](#handling-view-changes-from-dart)

View additions and removals are surfaced to Flutter through the [`didChangeMetrics` method](https://api.flutter.dev/flutter/widgets/WidgetsBindingObserver/didChangeMetrics.html) of the `WidgetsBinding` class.

The complete list of views attached to your Flutter app is available through the `WidgetsBinding.instance.platformDispatcher.views` iterable. These views are of [type `FlutterView`](https://api.flutter.dev/flutter/dart-ui/FlutterView-class.html).

To render content into each `FlutterView`, your Flutter app needs to create a [`View` widget](https://api.flutter.dev/flutter/widgets/View-class.html). `View` widgets can be grouped together under a [`ViewCollection` widget](https://api.flutter.dev/flutter/widgets/ViewCollection-class.html).

The following example, from the *Multi View Playground*, encapsulates the above in a `MultiViewApp` widget that can be used as the root widget for your app. A [`WidgetBuilder` function](https://api.flutter.dev/flutter/widgets/WidgetBuilder.html) runs for each `FlutterView`:

multi\_view\_app.dart

dart

```
import 'dart:ui' show FlutterView;
import 'package:flutter/widgets.dart';

/// Calls [viewBuilder] for every view added to the app to obtain the widget to
/// render into that view. The current view can be looked up with [View.of].
class MultiViewApp extends StatefulWidget {
  const MultiViewApp({super.key, required this.viewBuilder});

  final WidgetBuilder viewBuilder;

  @override
  State<MultiViewApp> createState() => _MultiViewAppState();
}

class _MultiViewAppState extends State<MultiViewApp> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _updateViews();
  }

  @override
  void didUpdateWidget(MultiViewApp oldWidget) {
    super.didUpdateWidget(oldWidget);
    // Need to re-evaluate the viewBuilder callback for all views.
    _views.clear();
    _updateViews();
  }

  @override
  void didChangeMetrics() {
    _updateViews();
  }

  Map<Object, Widget> _views = <Object, Widget>{};

  void _updateViews() {
    final Map<Object, Widget> newViews = <Object, Widget>{};
    for (final FlutterView view in WidgetsBinding.instance.platformDispatcher.views) {
      final Widget viewWidget = _views[view.viewId] ?? _createViewWidget(view);
      newViews[view.viewId] = viewWidget;
    }
    setState(() {
      _views = newViews;
    });
  }

  Widget _createViewWidget(FlutterView view) {
    return View(
      view: view,
      child: Builder(
        builder: widget.viewBuilder,
      ),
    );
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return ViewCollection(views: _views.values.toList(growable: false));
  }
}
```

For more information, check out [`WidgetsBinding` mixin](https://api.flutter.dev/flutter/widgets/WidgetsBinding-mixin.html) in the API docs, or the [Multi View Playground repo](https://github.com/goderbauer/mvp) that was used during development.

### Replace `runApp` by `runWidget` in Dart

[#](#replace-runapp-by-runwidget-in-dart)

Flutter's [`runApp` function](https://api.flutter.dev/flutter/widgets/runApp.html) assumes that there's at least one view available to render into (the `implicitView`), however in Flutter web's multi-view mode, the `implicitView` doesn't exist anymore, so `runApp` will start failing with `Unexpected null value` errors.

In multi-view mode, your `main.dart` must call the [`runWidget` function](https://api.flutter.dev/flutter/widgets/runWidget.html) instead. It doesn't require an `implicitView`, and will only render into the views that have been explicitly added into your app.

The following example uses the `MultiViewApp` described above to render copies of the `MyApp()` widget on every `FlutterView` available:

main.dart

dart

```
void main() {
  runWidget(
    MultiViewApp(
      viewBuilder: (BuildContext context) => const MyApp(),
    ),
  );
}
```

### Identifying views

[#](#identifying-views)

Each `FlutterView` has an identifier assigned by Flutter when attached. This `viewId` can be used to uniquely identify each view, retrieve its initial configuration, or decide what to render in it.

The `viewId` of the rendered `FlutterView` can be retrieved from its `BuildContext` like this:

dart

```
class SomeWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Retrieve the `viewId` where this Widget is being built:
    final int viewId = View.of(context).viewId;
    // ...
```

Similarly, from the `viewBuilder` method of the `MultiViewApp`, the `viewId` can be retrieved like this:

dart

```
MultiViewApp(
  viewBuilder: (BuildContext context) {
    // Retrieve the `viewId` where this Widget is being built:
    final int viewId = View.of(context).viewId;
    // Decide what to render based on `viewId`...
  },
)
```

Read more about the [`View.of` constructor](https://api.flutter.dev/flutter/widgets/View/of.html).

### Initial view configuration

[#](#initial-view-configuration)

Flutter views can receive any initialization data from JS when starting up. The values are passed through the `initialData` property of the `addView` method, as shown:

js

```
// Adding a view with initial data...
let viewId = app.addView({
  hostElement: someElement,
  initialData: {
    greeting: 'Hello, world!',
    randomValue: Math.floor(Math.random() * 100),
  }
});
```

In Dart, the `initialData` is available as a `JSAny` object, accessible through the top-level `views` property in the `dart:ui_web` library. The data is accessed through the `viewId` of the current view, as shown:

dart

```
final initialData = ui_web.views.getInitialData(viewId) as YourJsInteropType;
```

To learn how to define the `YourJsInteropType` class to map the `initialData` object passed from JS so it's type-safe in your Dart program, check out: [JS Interoperability](https://dart.dev/interop/js-interop) on dart.dev.

### View constraints

[#](#view-constraints)

By default, an embedded Flutter web view considers the size of its `hostElement` as an immutable property, and tightly constrains its layout to the available space.

On the web, it's common for the intrinsic size of an element to affect the layout of the page (like `img` or `p` tags that can reflow content around them).

When adding a view to Flutter web, you might configure it with constraints that inform Flutter of how the view needs to be laid out:

js

```
// Adding a view with initial data...
let viewId = app.addView({
  hostElement: someElement,
  viewConstraints: {
    maxWidth: 320,
    minHeight: 0,
    maxHeight: Infinity,
  }
});
```

The view constraints passed from JS need to be compatible with the CSS styling of the `hostElement` where Flutter is being embedded. For example, Flutter won’t try to "fix" contradictory constants like passing `max-height: 100px` in CSS, but `maxHeight: Infinity` to Flutter.

To learn more, check out the [`ViewConstraints` class](https://api.flutter.dev/flutter/dart-ui/ViewConstraints-class.html), and [Understanding constraints](/ui/layout/constraints).

Custom element (`hostElement`)
------------------------------

[#](#custom-element-hostelement)

*Between Flutter 3.10 and 3.24*  
 You can embed a single-view Flutter web app into any HTML element of your web page.

To tell Flutter web which element to render into, pass an object with a `config` field to the `_flutter.loader.load` function that specifies a `HTMLElement` as the `hostElement`.

js

```
_flutter.loader.load({
  config: {
    hostElement: document.getElementById('flutter_host'),
  }
});
```

To learn more about other configuration options, check out [Customizing web app initialization](/platform-integration/web/initialization).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/web/embedding-flutter-web/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/web/embedding-flutter-web.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/web/embedding-flutter-web/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/web/embedding-flutter-web.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/platform-integration/web/embedding-flutter-web.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/platform-integration/web/embedding-flutter-web/&page-source=https://github.com/flutter/website/tree/main/src/content/platform-integration/web/embedding-flutter-web.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   