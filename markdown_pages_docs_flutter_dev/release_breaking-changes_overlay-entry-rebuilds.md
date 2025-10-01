Rebuild optimization for OverlayEntries and Routes
==================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Rebuild optimization for OverlayEntries and Routes](/release/breaking-changes/overlay-entry-rebuilds)

Summary
-------

[#](#summary)

This optimization improves performance for route transitions, but it may uncover missing calls to `setState` in your app.

Context
-------

[#](#context)

Prior to this change, an `OverlayEntry` would rebuild when a new opaque entry was added on top of it or removed above it. These rebuilds were unnecessary because they were not triggered by a change in state of the affected `OverlayEntry`. This breaking change optimized how we handle the addition and removal of `OverlayEntry`s, and removes unnecessary rebuilds to improve performance.

Since the `Navigator` internally puts each `Route` into an `OverlayEntry` this change also applies to `Route` transitions: If an opaque `Route` is pushed on top or removed from above another `Route`, the `Route`s below the opaque `Route` no longer rebuilds unnecessarily.

Description of change
---------------------

[#](#description-of-change)

In most cases, this change doesn't require any changes to your code. However, if your app was erroneously relying on the implicit rebuilds you may see issues, which can be resolved by wrapping any state change in a `setState` call.

Furthermore, this change slightly modified the shape of the widget tree: Prior to this change, the `OverlayEntry`s were wrapped in a `Stack` widget. The explicit `Stack` widget was removed from the widget hierarchy.

Migration guide
---------------

[#](#migration-guide)

If you're seeing issues after upgrading to a Flutter version that included this change, audit your code for missing calls to `setState`. In the example below, assigning the return value of `Navigator.pushNamed` to `buttonLabel` is implicitly modifying the state and it should be wrapped in an explicit `setState` call.

Code before migration:

dart

```
class FooState extends State<Foo> {
  String buttonLabel = 'Click Me';
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        // Illegal state modification that should be wrapped in setState.
        buttonLabel = await Navigator.pushNamed(context, '/bar');
      },
      child: Text(buttonLabel),
    );
  }
}
```

Code after migration:

dart

```
class FooState extends State<Foo> {
  String buttonLabel = 'Click Me';
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        final newLabel = await Navigator.pushNamed(context, '/bar');
        setState(() {
          buttonLabel = newLabel;
        });
      },
      child: Text(buttonLabel),
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`setState`](https://api.flutter.dev/flutter/widgets/State/setState.html)* [`OverlayEntry`](https://api.flutter.dev/flutter/widgets/OverlayEntry-class.html)* [`Overlay`](https://api.flutter.dev/flutter/widgets/Overlay-class.html)* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`Route`](https://api.flutter.dev/flutter/widgets/Route-class.html)* [`OverlayRoute`](https://api.flutter.dev/flutter/widgets/OverlayRoute-class.html)

Relevant issues:

* [Issue 45797](https://github.com/flutter/flutter/issues/45797)

Relevant PRs:

* [Do not rebuild Routes when a new opaque Route is pushed on top](https://github.com/flutter/flutter/pull/48900)* [Reland "Do not rebuild Routes when a new opaque Route is pushed on top"](https://github.com/flutter/flutter/pull/49376)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/overlay-entry-rebuilds/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/overlay-entry-rebuilds.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/overlay-entry-rebuilds/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/overlay-entry-rebuilds.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/overlay-entry-rebuilds.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/overlay-entry-rebuilds/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/overlay-entry-rebuilds.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   