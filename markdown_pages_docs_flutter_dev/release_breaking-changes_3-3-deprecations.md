Deprecated API removed after v3.3
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v3.3](/release/breaking-changes/3-3-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 3.3 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-3-3) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations, listed by the affected class.

### `RenderUnconstrainedBox`

[#](#renderunconstrainedbox)

Supported by Flutter Fix: no

`RenderUnconstrainedBox` was deprecated in v2.1. Use `RenderConstraintsTransformBox` instead.

Where unconstrained in both axes, provide `ConstraintsTransformBox.unconstrained` to `constraintsTransform`.

If `RenderUnconstrainedBox.constrainedAxis` was previously set, replace respectively:

* Where `constrainedAxis` was previously `Axis.horizontal`, set `constraintsTransform` to `ConstraintsTransformBox.widthUnconstrained`.* Where `constrainedAxis` was previously `Axis.vertical`, set `constraintsTransform` to `ConstraintsTransformBox.heightUnconstrained`.

This change allowed for the introduction of several more types of constraint transformations through `ConstraintsTransformBox`. Other parameters of the old API are compatible with the new API.

**Migration guide**

Code before migration:

dart

```
// Unconstrained
final RenderUnconstrainedBox unconstrained = RenderUnconstrainedBox(
  textDirection: TextDirection.ltr,
  child: RenderConstrainedBox(
    additionalConstraints: const BoxConstraints.tightFor(height: 200.0),
  ),
  alignment: Alignment.center,
);

// Constrained in horizontal axis
final RenderUnconstrainedBox unconstrained = RenderUnconstrainedBox(
  constrainedAxis: Axis.horizontal,
  textDirection: TextDirection.ltr,
  child: RenderConstrainedBox(
    additionalConstraints: const BoxConstraints.tightFor(width: 200.0, height: 200.0),
  ),
  alignment: Alignment.center,
);

// Constrained in vertical axis
final RenderUnconstrainedBox unconstrained = RenderUnconstrainedBox(
  constrainedAxis: Axis.vertical,
  textDirection: TextDirection.ltr,
  child: RenderFlex(
    direction: Axis.vertical,
    textDirection: TextDirection.ltr,
    children: <RenderBox>[flexible],
  ),
  alignment: Alignment.center,
);
```

Code after migration:

dart

```
// Unconstrained
final RenderConstraintsTransformBox unconstrained = RenderConstraintsTransformBox(
  constraintsTransform: ConstraintsTransformBox.unconstrained,
  textDirection: TextDirection.ltr,
  child: RenderConstrainedBox(
    additionalConstraints: const BoxConstraints.tightFor(height: 200.0),
  ),
  alignment: Alignment.center,
);

// Constrained in horizontal axis
final RenderConstraintsTransformBox unconstrained = RenderConstraintsTransformBox(
  constraintsTransform: ConstraintsTransformBox.widthUnconstrained,
  textDirection: TextDirection.ltr,
  child: RenderConstrainedBox(
    additionalConstraints: const BoxConstraints.tightFor(width: 200.0, height: 200.0),
  ),
  alignment: Alignment.center,
);

// Constrained in vertical axis
final RenderConstraintsTransformBox unconstrained = RenderConstraintsTransformBox(
  constraintsTransform: ConstraintsTransformBox.widthUnconstrained,
  textDirection: TextDirection.ltr,
  child: RenderFlex(
    direction: Axis.vertical,
    textDirection: TextDirection.ltr,
    children: <RenderBox>[flexible],
  ),
  alignment: Alignment.center,
);
```

**References**

API documentation:

* [`RenderConstraintsTransformBox`](https://api.flutter.dev/flutter/rendering/RenderConstraintsTransformBox-class.html)* [`ConstraintsTransformBox`](https://api.flutter.dev/flutter/widgets/ConstraintsTransformBox-class.html)

Relevant PRs:

* Deprecated in [#78673](https://github.com/flutter/flutter/pull/78673)* Removed in [#111711](https://github.com/flutter/flutter/pull/111711)

---

### `DragAnchor`, `Draggable.dragAnchor` & `LongPressDraggable.dragAnchor`

[#](#draganchor-draggable-draganchor-longpressdraggable-draganchor)

Supported by Flutter Fix: yes

The enum `DragAnchor`, and its uses in `Draggable.dragAnchor` & `LongPressDraggable.dragAnchor` were deprecated in v2.1. Use `dragAnchorStrategy` instead.

This change allowed for more accurate feedback of the draggable widget when used in conjunction with other widgets like `Stack` and `InteractiveViewer`.

**Migration guide**

Code before migration:

dart

```
Draggable draggable = Draggable();
draggable = Draggable(dragAnchor: DragAnchor.child);
draggable = Draggable(dragAnchor: DragAnchor.pointer);

LongPressDraggable longPressDraggable = LongPressDraggable();
longPressDraggable = LongPressDraggable(dragAnchor: DragAnchor.child);
longPressDraggable = LongPressDraggable(dragAnchor: DragAnchor.pointer);
```

Code after migration:

dart

```
Draggable draggable = Draggable();
draggable = Draggable(dragAnchorStrategy: childDragAnchorStrategy);
draggable = Draggable(dragAnchorStrategy: pointerDragAnchorStrategy);

LongPressDraggable longPressDraggable = LongPressDraggable();
longPressDraggable = LongPressDraggable(dragAnchorStrategy: childDragAnchorStrategy);
longPressDraggable = LongPressDraggable(dragAnchorStrategy: pointerDragAnchorStrategy);
```

**References**

API documentation:

* [`Draggable`](https://api.flutter.dev/flutter/widgets/Draggable-class.html)* [`LongPressDraggable`](https://api.flutter.dev/flutter/widgets/LongPressDraggable-class.html)* [`DragAnchorStrategy`](https://api.flutter.dev/flutter/widgets/DragAnchorStrategy.html)

Relevant issues:

* [#73143](https://github.com/flutter/flutter/pull/73143)

Relevant PRs:

* Deprecated in [#79160](https://github.com/flutter/flutter/pull/79160)* Removed in [#111713](https://github.com/flutter/flutter/pull/111713)

---

### `ScrollBehavior.buildViewportChrome`

[#](#scrollbehavior-buildviewportchrome)

Supported by Flutter Fix: yes

The method `ScrollBehavior.buildViewportChrome` was deprecated in v2.1.

This method was used by the `Scrollable` widget to apply an overscroll indicator, like `GlowingOverscrollIndicator`, by default on the appropriate platforms. As more default decorators have been added, like `Scrollbar`s, each has instead been split into individual methods to replace `buildViewportChrome`.

This allows extending classes to only override the specific decorator, through `buildScrollbar` or `buildOverscrollIndicator`, rather than needing to rewrite code in order to maintain one or the other.

**Migration guide**

[In-depth migration guide available](/release/breaking-changes/default-desktop-scrollbars)

Code before migration:

dart

```
final ScrollBehavior scrollBehavior = ScrollBehavior();
scrollBehavior.buildViewportChrome(context, child, axisDirection);
```

Code after migration:

dart

```
final ScrollBehavior scrollBehavior = ScrollBehavior();
scrollBehavior.buildOverscrollIndicator(context, child, axisDirection);
```

**References**

Design document:

* [Exposing & Updating ScrollBehaviors](/go/exposing-scroll-behaviors)

API documentation:

* [`ScrollBehavior`](https://api.flutter.dev/flutter/widgets/ScrollBehavior-class.html)

Relevant issues:

* [Scrollbars should be always visible and instantiated by default on web and desktop](https://github.com/flutter/flutter/issues/40107)

Relevant PRs:

* [#76739](https://github.com/flutter/flutter/pull/76739)* Deprecated in [#78588](https://github.com/flutter/flutter/pull/78588)* Removed in [#111715](https://github.com/flutter/flutter/pull/111715)

---

Timeline
--------

[#](#timeline)

In stable release: 3.7

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-3-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-3-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-3-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-3-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-3-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/3-3-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/3-3-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   