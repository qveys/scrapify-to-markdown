Migration guide for ignoringSemantics in IgnorePointer and related classes
==========================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for ignoringSemantics in IgnorePointer and related classes](/release/breaking-changes/ignoringsemantics-migration)

Summary
-------

[#](#summary)

The `IgnoringPointer` widget allows you to designate an area of the UI where you don't want to accept pointer events, for example, when you don't want to allow the user to enter text in a text field.

Previously, the `IgnorePointer` not only blocked pointer events but also dropped its subtree from the semantics tree. The `ignoreSemantics` parameter was introduced as a workaround to preserve the semantics tree when using `IgnorePointer`s.

The `IgnorePointer` behavior has changed in that it no longer drops the entire semantics subtree but merely blocks semantics actions in the subtree. The `ignoringSemantics` workaround is no longer needed and is deprecated.

This change also applies to the `AbsorbPointer` and `SliverIgnorePointer` widgets.

Description of change
---------------------

[#](#description-of-change)

`ignoringSemantics` was removed.

Migration guide
---------------

[#](#migration-guide)

If you set this parameter to true in these widgets, consider using `ExcludeSemantics` instead.

Code before migration:

dart

```
IgnorePointer(
  ignoringSemantics: true,
  child: const PlaceHolder(),
);

AbsorbPointer(
  ignoringSemantics: true,
  child: const PlaceHolder(),
);

SliverIgnorePointer(
  ignoringSemantics: true,
  child: const PlaceHolder(),
);
```

Code after migration:

dart

```
ExcludeSemantics(
  child: IgnorePointer(
    child: const PlaceHolder(),
  ),
);

ExcludeSemantics(
  child: AbsorbPointer(
    child: const PlaceHolder(),
  ),
);

SliverIgnorePointer(
  child: ExcludeSemantics(
    child: const PlaceHolder(),
  ),
);
```

If you are previously using `IgnorePointer`s with `ignoringSemantics` set to `false`, you can achieve the same behavior by copying the follow widgets directly into your code and use.

dart

```
/// A widget ignores pointer events without modifying the semantics tree.
class _IgnorePointerWithSemantics extends SingleChildRenderObjectWidget {
  const _IgnorePointerWithSemantics({
    super.child,
  });

  @override
  _RenderIgnorePointerWithSemantics createRenderObject(BuildContext context) {
    return _RenderIgnorePointerWithSemantics();
  }
}

class _RenderIgnorePointerWithSemantics extends RenderProxyBox {
  _RenderIgnorePointerWithSemantics();

  @override
  bool hitTest(BoxHitTestResult result, { required Offset position }) => false;
}

/// A widget absorbs pointer events without modifying the semantics tree.
class _AbsorbPointerWithSemantics extends SingleChildRenderObjectWidget {
  const _AbsorbPointerWithSemantics({
    super.child,
  });

  @override
  _RenderAbsorbPointerWithSemantics createRenderObject(BuildContext context) {
    return _RenderAbsorbPointerWithSemantics();
  }
}

class _RenderAbsorbPointerWithSemantics extends RenderProxyBox {
  _RenderAbsorbPointerWithSemantics();

  @override
  bool hitTest(BoxHitTestResult result, { required Offset position }) {
    return size.contains(position);
  }
}

/// A sliver ignores pointer events without modifying the semantics tree.
class _SliverIgnorePointerWithSemantics extends SingleChildRenderObjectWidget {
  const _SliverIgnorePointerWithSemantics({
    super.child,
  });

  @override
  _RenderSliverIgnorePointerWithSemantics createRenderObject(BuildContext context) {
    return _RenderSliverIgnorePointerWithSemantics();
  }
}

class _RenderSliverIgnorePointerWithSemantics extends RenderProxySliver {
  _RenderSliverIgnorePointerWithSemantics();

  @override
  bool hitTest(BoxHitTestResult result, { required Offset position }) => false;
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.10.0-2.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

Relevant PRs:

* [PR 120619](https://github.com/flutter/flutter/pull/120619): Fixes IgnorePointer and AbsorbPointer to only block user interactions in a11y.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ignoringsemantics-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ignoringsemantics-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ignoringsemantics-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ignoringsemantics-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ignoringsemantics-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/ignoringsemantics-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/ignoringsemantics-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   