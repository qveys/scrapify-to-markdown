The generic type of ParentDataWidget changed to ParentData
==========================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [The generic type of ParentDataWidget changed to ParentData](/release/breaking-changes/parent-data-widget-generic-type)

Summary
-------

[#](#summary)

The generic type of `ParentDataWidget` has changed from `RenderObjectWidget` to `ParentData`.

Context
-------

[#](#context)

Prior to this change, a `ParentDataWidget` was bound to a specific `RenderObjectWidget` type as ancestor. For example, a `Positioned` widget could only be used within a `Stack` widget. With this change, a `ParentDataWidget` can be used with any `RenderObjectWidget` type as ancestor as long as the `RenderObject` of said `RenderObjectWidget` sets up the correct `ParentData` type. In this new world, the `Positioned` widget can be reused with a hypothetical new `SuperStack` widget.

Description of change
---------------------

[#](#description-of-change)

The generic type argument of `ParentDataWidget` has changed from `RenderObjectWidget` to `ParentData`, and a new debug property, `debugTypicalAncestorWidgetClass`, is added to `ParentDataWidget`. The latter is used for error messages to give users a better idea of the context a given `ParentDataWidget` is supposed to be used in.

Migration guide
---------------

[#](#migration-guide)

You must migrate your code as described in this section if you're subclassing or implementing `ParentDataWidget`. If you do, the analyzer shows the following warnings when you upgrade to the Flutter version that includes this change:

```
  error • Missing concrete implementation of 'getter ParentDataWidget.debugTypicalAncestorWidgetClass' • lib/main.dart:114:7 • non_abstract_class_inherits_abstract_member
  error • 'FrogJar' doesn't extend 'ParentData' • lib/main.dart:114:41 • type_argument_not_matching_bounds
```

Code before migration:

dart

```
class FrogSize extends ParentDataWidget<FrogJar> {
  FrogSize({
    Key key,
    required this.size,
    required Widget child,
  }) : assert(child != null),
        assert(size != null),
        super(key: key, child: child);

  final Size size;

  @override
  void applyParentData(RenderObject renderObject) {
    final FrogJarParentData parentData = renderObject.parentData;
    if (parentData.size != size) {
      parentData.size = size;
      final RenderFrogJar targetParent = renderObject.parent;
      targetParent.markNeedsLayout();
    }
  }
}

class FrogJarParentData extends ParentData {
  Size size;
}

class FrogJar extends RenderObjectWidget {
  // ...
}
```

Code after migration:

dart

```
class FrogSize extends ParentDataWidget<FrogJarParentData> { // FrogJar changed to FrogJarParentData
  FrogSize({
    Key key,
    required this.size,
    required Widget child,
  }) : assert(child != null),
        assert(size != null),
        super(key: key, child: child);

  final Size size;

  @override
  void applyParentData(RenderObject renderObject) {
    final FrogJarParentData parentData = renderObject.parentData;
    if (parentData.size != size) {
      parentData.size = size;
      final RenderFrogJar targetParent = renderObject.parent;
      targetParent.markNeedsLayout();
    }
  }

  @override
  Type get debugTypicalAncestorWidgetClass => FrogJar; // Newly added
}
```

The generic type of the `ParentDataWidget` superclass changes from `FrogJar` (a `RenderObjectWidget`) to `FrogJarParentData` (the `ParentData` type that `FrogSize.applyParentData` wants to operate on). Additionally, the new `debugTypicalAncestorWidgetClass` is implemented for this `ParentDataWidget` subclass. It returns the type of a typical ancestor `RenderObjectWidget` for this `ParentDataWidget`. Most of the time, you just want to return the old generic type here (`FrogJar` in this example).

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`ParentDataWidget`](https://api.flutter.dev/flutter/widgets/ParentDataWidget-class.html)

Relevant PR:

* [Make ParentDataWidget usable with different ancestor RenderObjectWidget types](https://github.com/flutter/flutter/pull/48541)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/parent-data-widget-generic-type/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/parent-data-widget-generic-type.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/parent-data-widget-generic-type/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/parent-data-widget-generic-type.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/parent-data-widget-generic-type.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/parent-data-widget-generic-type/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/parent-data-widget-generic-type.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   