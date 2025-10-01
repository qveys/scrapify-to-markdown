MouseTracker no longer attaches annotations
===========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [MouseTracker no longer attaches annotations](/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations)

Summary
-------

[#](#summary)

Removed `MouseTracker`'s methods `attachAnnotation`, `detachAnnotation`, and `isAnnotationAttached`.

Context
-------

[#](#context)

Mouse events, such as when a mouse pointer has entered a region, exited, or is hovering over a region, are detected with the help of `MouseTrackerAnnotation`s that are placed on interested regions during the render phase. Upon each update (a new frame or a new event), `MouseTracker` compares the annotations hovered by the mouse pointer before and after the update, then dispatches callbacks accordingly.

The `MouseTracker` class, which manages the state of mouse pointers, used to require `MouseRegion` to attach annotations when mounted, and detach annotations when unmounted. This was used by `MouseTracker` to perform the *mounted-exit check* (for example, `MouseRegion.onExit` must not be called if the exit was caused by the unmounting of the widget), in order to prevent calling `setState` of an unmounted widget and throwing exceptions (explained in detail in [Issue #44631](https://github.com/flutter/flutter/pull/44631)).

This mechanism has been replaced by making `MouseRegion` a stateful widget, so that it can perform the mounted-exit check by itself by blocking the callback when unmounted. Therefore, these methods have been removed, and `MouseTracker` no longer tracks all annotations on the screen.

Description of change
---------------------

[#](#description-of-change)

The `MouseTracker` class has removed three methods related to attaching annotations:

dart

```
class MouseTracker extends ChangeNotifier {
  // ...
  void attachAnnotation(MouseTrackerAnnotation annotation) {/* ... */}

  void detachAnnotation(MouseTrackerAnnotation annotation) {/* ... */}

  @visibleForTesting
  bool isAnnotationAttached(MouseTrackerAnnotation annotation) {/* ... */}
}
```

`RenderMouseRegion` and `MouseTrackerAnnotation` no longer perform the mounted-exit check, while `MouseRegion` still does.

Migration guide
---------------

[#](#migration-guide)

Calls to `MouseTracker.attachAnnotation` and `detachAnnotation` should be removed with little to no impact:

* Uses of `MouseRegion` should not be affected at all.* If your code directly uses `RenderMouseRegion` or `MouseTrackerAnnotation`, be aware that `onExit` is now called when the exit is caused by events that used to call `MouseTracker.detachAnnotation`. This should not be a problem if no states are involved, otherwise you might want to add the mounted-exit check, especially if the callback is leaked so that outer widgets might call `setState` in it. For example:

Code before migration:

dart

```
class MyMouseRegion extends SingleChildRenderObjectWidget {
  const MyMouseRegion({this.onHoverChange});

  final ValueChanged<bool> onHoverChange;

  @override
  RenderMouseRegion createRenderObject(BuildContext context) {
    return RenderMouseRegion(
      onEnter: (_) { onHoverChange(true); },
      onExit: (_) { onHoverChange(false); },
    );
  }

  @override
  void updateRenderObject(BuildContext context, RenderMouseRegion renderObject) {
    renderObject
      ..onEnter = (_) { onHoverChange(true); }
      ..onExit = (_) { onHoverChange(false); };
  }
}
```

Code after migration:

dart

```
class MyMouseRegion extends SingleChildRenderObjectWidget {
  const MyMouseRegion({this.onHoverChange});

  final ValueChanged<bool> onHoverChange;

  @override
  RenderMouseRegion createRenderObject(BuildContext context) {
    return RenderMouseRegion(
      onEnter: (_) { onHoverChange(true); },
      onExit: (_) { onHoverChange(false); },
    );
  }

  @override
  void updateRenderObject(BuildContext context, RenderMouseRegion renderObject) {
    renderObject
      ..onEnter = (_) { onHoverChange(true); }
      ..onExit = (_) { onHoverChange(false); };
  }

  @override
  void didUnmountRenderObject(RenderMouseRegion renderObject) {
    renderObject
      ..onExit = onHoverChange == null ? null : (_) {};
  }
}
```

Calls to `MouseTracker.isAnnotationAttached` must be removed. This feature is no longer technically possible, since annotations are no longer tracked. If you somehow need this feature, please submit an issue.

Timeline
--------

[#](#timeline)

Landed in version: 1.15.4  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`MouseRegion`](https://api.flutter.dev/flutter/widgets/MouseRegion-class.html)* [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html)* [`MouseTrackerAnnotation`](https://api.flutter.dev/flutter/gestures/MouseTrackerAnnotation-class.html)* [`RenderMouseRegion`](https://api.flutter.dev/flutter/rendering/RenderMouseRegion-class.html)

Relevant PRs:

* [MouseTracker no longer requires annotations attached](https://github.com/flutter/flutter/issues/48453), which made the change* [Improve MouseTracker lifecycle: Move checks to post-frame](https://github.com/flutter/flutter/issues/44631), which first introduced the mounted-exit change, explained at *The change to onExit*.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-no-longer-attaches-annotations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   