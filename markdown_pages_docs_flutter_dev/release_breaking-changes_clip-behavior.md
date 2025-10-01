Clip Behavior
=============

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Clip Behavior](/release/breaking-changes/clip-behavior)

Summary
-------

[#](#summary)

Flutter now defaults to *not* clip except for a few specialized widgets (such as `ClipRect`). To override the no-clip default, explicitly set `clipBehavior` in widgets constructions.

Context
-------

[#](#context)

Flutter used to be slow because of clips. For example, the Flutter gallery app benchmark had an average frame rasterization time of about 35ms in May 2018, where the budget for smooth 60fps rendering is 16ms. By removing unnecessary clips and their related operations, we saw an almost 2x speedup from 35ms/frame to 17.5ms/frame.

The biggest cost associated with clipping at that time is that Flutter used to add a `saveLayer` call after each clip (unless it was a simple axis-aligned rectangle clip) to avoid the bleeding edge artifacts as described in [Issue 18057](https://github.com/flutter/flutter/issues/18057). Such behaviors were universal to material apps through widgets like `Card`, `Chip`, `Button`, and so on, which resulted in `PhysicalShape` and `PhysicalModel` clipping their content.

A `saveLayer` call is especially expensive in older devices because it creates an offscreen render target, and a render target switch can sometimes cost about 1ms.

Even without `saveLayer` call, a clip is still expensive because it applies to all subsequent draws until it's restored. Therefore a single clip may slow down the performance on hundreds of draw operations.

In addition to performance issues, Flutter also suffered from some correctness issues as the clip was not managed and implemented in a single place. In several places, `saveLayer` was inserted in the wrong place and it therefore only increased the performance cost without fixing any bleeding edge artifacts.

So, we unified the `clipBehavior` control and its implementation in this breaking change. The default `clipBehavior` is `Clip.none` for most widgets to save performance, except the following:

* `ClipPath` defaults to `Clip.antiAlias`* `ClipRRect` defaults to `Clip.antiAlias`* `ClipRect` defaults to `Clip.hardEdge`* `Stack` defaults to `Clip.hardEdge`* `EditableText` defaults to `Clip.hardEdge`* `ListWheelScrollView` defaults to `Clip.hardEdge`* `SingleChildScrollView` defaults to `Clip.hardEdge`* `NestedScrollView` defaults to `Clip.hardEdge`* `ShrinkWrappingViewport` defaults to `Clip.hardEdge`

Migration guide
---------------

[#](#migration-guide)

You have 4 choices for migrating your code:

1. Leave your code as is if your content does not need to be clipped (for example, none of the widgets' children expand outside their parent's boundary). This will likely have a positive impact on your app's overall performance.- Add `clipBehavior: Clip.hardEdge` if you need clipping, and clipping without anti-alias is good enough for your (and your clients') eyes. This is the common case when you clip rectangles or shapes with very small curved areas (such as the corners of rounded rectangles).- Add `clipBehavior: Clip.antiAlias` if you need anti-aliased clipping. This gives you smoother edges at a slightly higher cost. This is the common case when dealing with circles and arcs.- Add `clip.antiAliasWithSaveLayer` if you want the exact same behavior as before (May 2018). Be aware that it's very costly in performance. This is likely to be only rarely needed. One case where you might need this is if you have an image overlaid on a very different background color. In these cases, consider whether you can avoid overlapping multiple colors in one spot (for example, by having the background color only present where the image is absent).

For the `Stack` widget specifically, if you previously used `overflow: Overflow.visible`, replace it with `clipBehavior: Clip.none`.

For the `ListWheelViewport` widget, if you previously specified `clipToSize`, replace it with the corresponding `clipBehavior`: `Clip.none` for `clipToSize = false` and `Clip.hardEdge` for `clipToSize = true`.

Code before migration:

dart

```
    await tester.pumpWidget(
      Directionality(
        textDirection: TextDirection.ltr,
        child: Center(
          child: Stack(
            overflow: Overflow.visible,
            children: const <Widget>[
              SizedBox(
                width: 100,
                height: 100,
              ),
            ],
          ),
        ),
      ),
    );
```

Code after migration:

dart

```
    await tester.pumpWidget(
      Directionality(
        textDirection: TextDirection.ltr,
        child: Center(
          child: Stack(
            clipBehavior: Clip.none,
            children: const <Widget>[
              SizedBox(
                width: 100.0,
                height: 100.0,
              ),
            ],
          ),
        ),
      ),
    );
```

Timeline
--------

[#](#timeline)

Landed in version: *various*  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`Clip`](https://api.flutter.dev/flutter/dart-ui/Clip.html)

Relevant issues:

* [Issue 13736](https://github.com/flutter/flutter/issues/13736)* [Issue 18057](https://github.com/flutter/flutter/issues/18057)* [Issue 21830](https://github.com/flutter/flutter/issues/21830)

Relevant PRs:

* [PR 5420](https://github.com/flutter/engine/pull/5420): Remove unnecessary saveLayer* [PR 18576](https://github.com/flutter/flutter/pull/18576): Add Clip enum to Material and related widgets* [PR 18616](https://github.com/flutter/flutter/pull/18616): Remove saveLayer after clip from dart* [PR 5647](https://github.com/flutter/engine/pull/5647): Add ClipMode to ClipPath/ClipRRect and PhysicalShape layers* [PR 5670](https://github.com/flutter/engine/pull/5670): Add anti-alias switch to canvas clip calls* [PR 5853](https://github.com/flutter/engine/pull/5853): Rename clip mode to clip behavior* [PR 5868](https://github.com/flutter/engine/pull/5868): Rename clip to clipBehavior in compositing.dart* [PR 5973](https://github.com/flutter/engine/pull/5937): Call drawPaint instead of drawPath if there's clip* [PR 5952](https://github.com/flutter/engine/pull/5952): Call drawPath without clip if possible* [PR 20205](https://github.com/flutter/flutter/pull/20205): Set default clipBehavior to Clip.none and update tests* [PR 20538](https://github.com/flutter/flutter/pull/20538): Expose clipBehavior to more Material Buttons* [PR 20751](https://github.com/flutter/flutter/pull/20751): Add customBorder to InkWell so it can clip ShapeBorder* [PR 20752](https://github.com/flutter/flutter/pull/20752): Set the default clip to Clip.none again* [PR 21012](https://github.com/flutter/flutter/pull/21012): Add default-no-clip tests to more buttons* [PR 21703](https://github.com/flutter/flutter/pull/21703): Default clipBehavior of ClipRect to hardEdge* [PR 21826](https://github.com/flutter/flutter/pull/21826): Missing default hardEdge clip for ClipRectLayer

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clip-behavior/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clip-behavior.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clip-behavior/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clip-behavior.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clip-behavior.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/clip-behavior/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/clip-behavior.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   