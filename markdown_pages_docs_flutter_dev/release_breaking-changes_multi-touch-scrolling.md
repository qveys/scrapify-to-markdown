Default multitouch scrolling
============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Default multitouch scrolling](/release/breaking-changes/multi-touch-scrolling)

Summary
-------

[#](#summary)

`ScrollBehavior`s now allow or disallow scrolling speeds to be affected by the number of pointers on the screen. `ScrollBehavior.multitouchDragStrategy`, by default, prevents multiple pointers interacting wih the scrollable at the same time from affecting the speed of scrolling.

Context
-------

[#](#context)

Prior to this change, for each pointer dragging a `Scrollable` widget, the scroll speed would increase. This did not match platform expectations when interacting with Flutter applications.

Now, the inherited `ScrollBehavior` manages how multiple pointers affect scrolling widgets as specified by `ScrollBehavior.multitouchDragStrategy`. This enum, `MultitouchDragStrategy`, can also be configured for the prior behavior.

Description of change
---------------------

[#](#description-of-change)

This change fixed the unexpected ability to increase scroll speeds by dragging with more than one finger.

If you have relied on the previous behavior in your application, there are several ways to control and configure this feature.

* Extend `ScrollBehavior`, `MaterialScrollBehavior`, or `CupertinoScrollBehavior` to modify the default behavior, overriding `ScrollBehavior.multitouchDragStrategy`.
  + With your own `ScrollBehavior`, you can apply it app-wide by setting `MaterialApp.scrollBehavior` or `CupertinoApp.scrollBehavior`.+ Or, if you wish to only apply it to specific widgets, add a `ScrollConfiguration` above the widget in question with your custom `ScrollBehavior`.

Your scrollable widgets then inherit and reflect this behavior.

* Instead of creating your own `ScrollBehavior`, another option for changing the default behavior is to copy the existing `ScrollBehavior`, and set different `multitouchDragStrategy`.
  + Create a `ScrollConfiguration` in your widget tree, and provide a modified copy of the existing `ScrollBehavior` in the current context using `copyWith`.

To accommodate the new configuration `DragGestureRecognizer` was updated to support `MultitouchDragStrategy` as well in other dragging contexts.

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
  // Override behavior methods and getters like multitouchDragStrategy
  @override
  MultitouchDragStrategy getMultitouchDragStrategy(BuildContext context) => MultitouchDragStrategy.sumAllPointers;
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
  },
);
```

Code after migration:

dart

```
class MyCustomScrollBehavior extends MaterialScrollBehavior {
  // Override behavior methods and getters like multitouchDragStrategy
  @override
  MultitouchDragStrategy getMultitouchDragStrategy(BuildContext context) => MultitouchDragStrategy.sumAllPointers;
}

// ScrollBehavior can be set for a specific widget.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: MyCustomScrollBehavior(),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    },
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
  },
);
```

Code after migration:

dart

```
// ScrollBehavior can be copied and adjusted.
final ScrollController controller = ScrollController();
ScrollConfiguration(
  behavior: ScrollConfiguration.of(context).copyWith(
    multitouchDragStrategy: MultitouchDragStrategy.sumAllPointers,
  ),
  child: ListView.builder(
    controller: controller,
    itemBuilder: (BuildContext context, int index) {
      return Text('Item $index');
    },
  ),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.18.0-4.0.pre  
 In stable release: 3.19.0

References
----------

[#](#references)

API documentation:

* [`ScrollConfiguration`](https://api.flutter.dev/flutter/widgets/ScrollConfiguration-class.html)* [`ScrollBehavior`](https://api.flutter.dev/flutter/widgets/ScrollBehavior-class.html)* [`MaterialScrollBehavior`](https://api.flutter.dev/flutter/material/MaterialScrollBehavior-class.html)* [`CupertinoScrollBehavior`](https://api.flutter.dev/flutter/cupertino/CupertinoScrollBehavior-class.html)* [`MultitouchDragStrategy`](https://api.flutter.dev/flutter/gestures/MultitouchDragStrategy.html)* [`DragGestureRecognizer`](https://api.flutter.dev/flutter/gestures/DragGestureRecognizer-class.html)

Relevant issue:

* [Issue #11884](https://github.com/flutter/flutter/issues/11884)

Relevant PRs:

* [Introduce multi-touch drag strategies for DragGestureRecognizer](https://github.com/flutter/flutter/pull/136708)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/multi-touch-scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/multi-touch-scrolling.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/multi-touch-scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/multi-touch-scrolling.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-07-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/multi-touch-scrolling.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/multi-touch-scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/multi-touch-scrolling.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   