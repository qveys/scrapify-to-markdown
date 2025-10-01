Accessibility traversal order of tooltip changed
================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Accessibility traversal order of tooltip changed](/release/breaking-changes/tooltip-semantics-order)

Summary
-------

[#](#summary)

During accessibility focus traversal, `Tooltip.message` is visited immediately after `Tooltip.child`.

Background
----------

[#](#background)

The `Tooltip` widget usually wraps an interactive UI component such as a button, and shows a help message when long pressed. When the message is visible, assistive technologies should announce it after the button.

The `Tooltip` widget originally put `Tooltip.message` on an `OverlayEntry` when long pressed. As a result, `Tooltip.message` was not immediately after `Tooltip.child` in the semantics tree.

Migration guide
---------------

[#](#migration-guide)

This change moved the tooltip message in the semantics tree. You might see accessibility test failures if your tests expect a tooltip message to appear in a specific location in the semantics tree, when it is visible. Update any failing accessibility tests to adopt the new tooltip semantics order.

For example, if you constructed the following widget tree in your test:

dart

```
Directionality(
  textDirection: TextDirection.ltr,
  child: Overlay(
    initialEntries: <OverlayEntry>[
      OverlayEntry(
        builder: (BuildContext context) {
          return ListView(
            children: <Widget>[
              const Text('before'),
              Tooltip(
                key: tooltipKey,
                showDuration: const Duration(days: 365),
                message: 'message',
                child: const Text('child'),
              ),
              const Text('after'),
            ],
          );
        },
      ),
    ],
  ),
);
```

When the tooltip message is visible, the corresponding semantics tree before this change should look like this:

dart

```
SemanticsNode#0
 │
 ├─SemanticsNode#1
 │ │
 │ └─SemanticsNode#5
 │   │ flags: hasImplicitScrolling
 │   │ scrollChildren: 3
 │   │
 │   ├─SemanticsNode#2
 │   │   tags: RenderViewport.twoPane
 │   │   label: "before"
 │   │   textDirection: ltr
 │   │
 │   ├─SemanticsNode#3
 │   │   tags: RenderViewport.twoPane
 │   │   label: "child"
 │   │   tooltip: "message"
 │   │   textDirection: ltr
 │   │
 │   └─SemanticsNode#4
 │       tags: RenderViewport.twoPane
 │       label: "after"
 │       textDirection: ltr
 │
 └─SemanticsNode#6
     label: "message"
     textDirection: ltr
```

After this change, the same widget tree generates a slightly different semantics tree, as shown below. Node #6 becomes a child of node #3, instead of node #0.

dart

```
SemanticsNode#0
 │
 └─SemanticsNode#1
   │
   └─SemanticsNode#5
     │ flags: hasImplicitScrolling
     │ scrollChildren: 3
     │
     ├─SemanticsNode#2
     │   tags: RenderViewport.twoPane
     │   label: "before"
     │   textDirection: ltr
     │
     ├─SemanticsNode#3
     │ │ tags: RenderViewport.twoPane
     │ │ label: "child"
     │ │ tooltip: "message"
     │ │ textDirection: ltr
     │ │
     │ └─SemanticsNode#6
     │     label: "message"
     │     textDirection: ltr
     │
     └─SemanticsNode#4
         tags: RenderViewport.twoPane
         label: "after"
         textDirection: ltr
```

Timeline
--------

[#](#timeline)

Landed in version: 3.16.0-11.0.pre  
 In stable release: 3.19.0

References
----------

[#](#references)

API documentation:

* [`Tooltip`](https://api.flutter.dev/flutter/material/Tooltip-class.html)

Relevant PRs:

* [OverlayPortal.overlayChild contributes semantics to OverlayPortal instead of Overlay](https://github.com/flutter/flutter/pull/134921)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tooltip-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tooltip-semantics-order.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tooltip-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tooltip-semantics-order.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tooltip-semantics-order.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/tooltip-semantics-order/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/tooltip-semantics-order.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   