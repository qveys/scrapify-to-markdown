Dry layout support for RenderBox
================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Dry layout support for RenderBox](/release/breaking-changes/renderbox-dry-layout)

Summary
-------

[#](#summary)

A new method named `computeDryLayout` was added to the `RenderBox` protocol. Subclasses of `RenderBox` are expected to implement it to correctly report their desired size given a set of `BoxConstraints` during intrinsic calculations. Subclasses that implement `computeDryLayout` no longer need to override `performResize`.

Context
-------

[#](#context)

A new method, `computeDryLayout`, was added to the `RenderBox` protocol to correctly calculate the intrinsic sizes of a `RenderParagraph` with `WidgetSpan` children and a `RenderWrap`. The method receives a set of `BoxConstraints` and is expected to calculate the resulting size of the `RenderBox` without changing any internal state. It's essentially a dry run of `performLayout` that only calculates the resulting size and doesn't place the children. The `computeDryLayout` method is part of the intrinsics protocol (see also [`RenderBox.computeMinIntrinsicWidth`](https://api.flutter.dev/flutter/rendering/RenderBox/computeMinIntrinsicWidth.html) and friends).

Description of change
---------------------

[#](#description-of-change)

Subclasses of `RenderBox` need to override the new `computeDryLayout` method if they are used as a descendant of a `RenderObject` that may query the intrinsic size of its children. Examples of widgets that do this are `IntrinsicHeight` and `IntrinsicWidth`.

The default implementation of `RenderBox.performResize` also uses the size computed by `computeDryLayout` to perform the resize. Overriding `performResize` is therefore no longer necessary.

Migration guide
---------------

[#](#migration-guide)

Subclasses that already override `performResize` can be migrated by simply changing the function signature from `void performResize()` to `Size computeDryLayout(BoxConstraints constraints)` and by returning the calculated size instead of assigning it to the `size` setter. The old implementation of `performResize` can be removed.

Code before migration:

dart

```
  @override
  void performResize() {
     size = constraints.biggest;
  }
```

Code after migration:

dart

```
  // This replaces the old performResize method.
  @override
  Size computeDryLayout(BoxConstraints constraints) {
     return constraints.biggest;
  }
```

If the subclass doesn't override `performResize`, the implementation of `computeDryLayout` has to be extracted from the `performLayout` method. Basically, `computeDryLayout` needs to do all the work `performLayout` is doing to figure out the size of the `RenderBox`. However, instead of assigning it to the `size` setter, it returns the computed size. If `computeDryLayout` needs to know the size of its children, it must obtain that size by calling `getDryLayout` on the child instead of calling `layout`.

If for some reason it is impossible to calculate the dry layout, `computeDryLayout` must call `debugCannotComputeDryLayout` from within an assert and return a dummy size of `const Size(0, 0)`. Calculating a dry layout is, for example, impossible if the size of a `RenderBox` depends on the baseline metrics of its children.

dart

```
  @override
  Size computeDryLayout(BoxConstraints constraints) {
    assert(debugCannotComputeDryLayout(
      reason: 'Layout requires baseline metrics, which are only available after a full layout.'
    ));
    return const Size(0, 0);
  }
```

Timeline
--------

[#](#timeline)

Landed in version: 1.25.0-4.0.pre  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`RenderBox`](https://api.flutter.dev/flutter/rendering/RenderBox-class.html)* [`computeMinInstrinsicWidth`](https://api.flutter.dev/flutter/rendering/RenderBox/computeMinIntrinsicWidth.html)* [`computeDryLayout`](https://api.flutter.dev/flutter/rendering/RenderBox/computeDryLayout.html)* [`getDryLayout`](https://api.flutter.dev/flutter/rendering/RenderBox/getDryLayout.html)* [`performResize`](https://api.flutter.dev/flutter/rendering/RenderBox/performResize.html)* [`RenderWrap`](https://api.flutter.dev/flutter/rendering/RenderWrap-class.html)* [`RenderParagraph`](https://api.flutter.dev/flutter/rendering/RenderParagraph-class.html)

Relevant issues:

* [Issue 48679](https://github.com/flutter/flutter/issues/48679)

Relevant PRs:

* [Fixes Intrinsics for RenderParagraph and RenderWrap](https://github.com/flutter/flutter/pull/70656)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/renderbox-dry-layout/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/renderbox-dry-layout.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/renderbox-dry-layout/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/renderbox-dry-layout.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/renderbox-dry-layout.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/renderbox-dry-layout/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/renderbox-dry-layout.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   