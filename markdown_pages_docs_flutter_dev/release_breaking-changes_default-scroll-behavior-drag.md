Default drag scrolling devices
==============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Default drag scrolling devices](/release/breaking-changes/default-scroll-behavior-drag)

Summary
-------

[#](#summary)

`ScrollBehavior`s now allow or disallow drag scrolling from specified `PointerDeviceKind`s. `ScrollBehavior.dragDevices`, by default, allows scrolling widgets to be dragged by all `PointerDeviceKind`s except for `PointerDeviceKind.mouse`.

Context
-------

[#](#context)

Prior to this change, all `PointerDeviceKind`s could drag a `Scrollable` widget. This did not match developer expectations when interacting with Flutter applications using mouse input devices. This also made it difficult to execute other mouse gestures, like selecting text that was contained in a `Scrollable` widget.

Now, the inherited `ScrollBehavior` manages which devices can drag scrolling widgets as specified by `ScrollBehavior.dragDevices`. This set of `PointerDeviceKind`s are allowed to drag.

Description of change
---------------------

[#](#description-of-change)

This change fixed the unexpected ability to scroll by dragging with a mouse.

If you have relied on the previous behavior in your application, there are several ways to control and configure this feature.

* Extend `ScrollBehavior`, `MaterialScrollBehavior`, or `CupertinoScrollBehavior` to modify the default behavior, overriding `ScrollBehavior.dragDevices`.
  + With your own `ScrollBehavior`, you can apply it app-wide by setting `MaterialApp.scrollBehavior` or `CupertinoApp.scrollBehavior`.+ Or, if you wish to only apply it to specific widgets, add a `ScrollConfiguration` above the widget in question with your custom `ScrollBehavior`.

Your scrollable widgets then inherit and reflect this behavior.

* Instead of creating your own `ScrollBehavior`, another option for changing the default behavior is to copy the existing `ScrollBehavior`, and set different `dragDevices`.
  + Create a `ScrollConfiguration` in your widget tree, and provide a modified copy of the existing `ScrollBehavior` in the current context using `copyWith`.

To accommodate the new configuration of drag devices in `ScrollBehavior`, `GestureDetector.kind` has been deprecated along with all subclassed instances of the parameter. A flutter fix is available to migrate existing code for all gesture detectors from `kind` to `supportedDevices`. The previous parameter `kind` only allowed one `PointerDeviceKind` to be used to filter gestures. The introduction of `supportedDevices` makes it possible for more than one valid `PointerDeviceKind`.

Migration guide
---------------

[#](#migration-guide)

### Setting a custom `ScrollBehavior` for your application

[#](#setting-a-custom-scrollbehavior-for-your-application)

Code before migration:

dart

```
MaterialApp(
  // ...
);
```

Code after migration:

dart

```
class MyCustomScrollBehavior extends MaterialScrollBehavior {
  // Override behavior methods and getters like dragDevices
  @override
  Set<PointerDeviceKind> get dragDevices => { 
    PointerDeviceKind.touch,
    PointerDeviceKind.mouse,
    // etc.
  };
}

// Set ScrollBehavior for an entire application.
MaterialApp(
  scrollBehavior: MyCustomScrollBehavior(),
  // ...
);
```

### Setting a custom `ScrollBehavior` for a specific widget

[#](#setting-a-custom-scrollbehavior-for-a-specific-widget)

Code before migration:

dart

```
final ScrollController controller = ScrollController();
ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
   return Text('Item $index');
 }
);
```

Code after migration:

dart

```
class MyCustomScrollBehavior extends MaterialScrollBehavior {
  // Override behavior methods and getters like dragDevices
  @override
  Set<PointerDeviceKind> get dragDevices => { 
    PointerDeviceKind.touch,
    PointerDeviceKind.mouse,
    // etc.
  };
}

// ScrollBehavior can be set for a specific widget.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: MyCustomScrollBehavior(),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
     return Text('Item $index');
    }
  ),
);
```

### Copy and modify existing `ScrollBehavior`

[#](#copy-and-modify-existing-scrollbehavior)

Code before migration:

dart

```
final ScrollController controller = ScrollController();
ListView.builder(
  controller: controller,
  itemBuilder: (BuildContext context, int index) {
   return Text('Item $index');
 }
);
```

Code after migration:

dart

```
// ScrollBehavior can be copied and adjusted.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: ScrollConfiguration.of(context).copyWith(dragDevices: {
    PointerDeviceKind.touch,
    PointerDeviceKind.mouse,
  }),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
     return Text('Item $index');
    }
  ),
);
```

### Migrate `GestureDetector`s from `kind` to `supportedDevices`

[#](#migrate-gesturedetectors-from-kind-to-supporteddevices)

Code before migration:

dart

```
VerticalDragGestureRecognizer(
  kind: PointerDeviceKind.touch,
);
```

Code after migration:

dart

```
VerticalDragGestureRecognizer(
  supportedDevices: <PointerDeviceKind>{ PointerDeviceKind.touch },
);
```

Timeline
--------

[#](#timeline)

Landed in version: 2.3.0-12.0.pre  
 In stable release: 2.5

References
----------

[#](#references)

API documentation:

* [`ScrollConfiguration`](https://api.flutter.dev/flutter/widgets/ScrollConfiguration-class.html)* [`ScrollBehavior`](https://api.flutter.dev/flutter/widgets/ScrollBehavior-class.html)* [`MaterialScrollBehavior`](https://api.flutter.dev/flutter/material/MaterialScrollBehavior-class.html)* [`CupertinoScrollBehavior`](https://api.flutter.dev/flutter/cupertino/CupertinoScrollBehavior-class.html)* [`PointerDeviceKind`](https://api.flutter.dev/flutter/dart-ui/PointerDeviceKind-class.html)* [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html)

Relevant issue:

* [Issue #71322](https://github.com/flutter/flutter/issues/71322)

Relevant PRs:

* [Reject mouse drags by default in scrollables](https://github.com/flutter/flutter/pull/81569)* [Deprecate GestureDetector.kind in favor of new supportedDevices](https://github.com/flutter/flutter/pull/81858)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-scroll-behavior-drag/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-scroll-behavior-drag.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-scroll-behavior-drag/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-scroll-behavior-drag.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-scroll-behavior-drag.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/default-scroll-behavior-drag/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/default-scroll-behavior-drag.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   