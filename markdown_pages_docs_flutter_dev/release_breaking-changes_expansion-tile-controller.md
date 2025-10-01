Deprecated ExpansionTileController
==================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated ExpansionTileController](/release/breaking-changes/expansion-tile-controller)

Summary
-------

[#](#summary)

`ExpansionTileController` is deprecated. The same functionality can be achieved by using `ExpansibleController` instead.

Background
----------

[#](#background)

`ExpansionTileController` programmatically expands and collapses an `ExpansionTile`. A new `Expansible` widget has been added to the widgets library, which contains logic for expanding and collapsing behavior without being tied to the Material library. `ExpansibleController` complements `Expansible` and has the same functionality as `ExpansionTileController`. Additionally, `ExpansibleController` also supports adding and notifying listeners when its expansion state changes.

Apps that use `ExpansionTileController` display the following error when run in debug mode: "Use `ExpansibleController` instead.". Specifically, this means that users should replace usage of `ExpansionTileController` with `ExpansibleController`.

Migration guide
---------------

[#](#migration-guide)

To migrate, replace the `controller` parameter of an `ExpansionTile` from an `ExpansionTileController` to an `ExpansibleController`. Unlike `ExpansionTileController`, `ExpansibleController` is a `ChangeNotifier`, so remember to dispose the new `ExpansibleController`.

Code before migration:

dart

```
class _MyWidgetState extends State<MyWidget> {
  final ExpansionTileController controller = ExpansionTileController();
  
  @override
  Widget build(BuildContext context) {
    return ExpansionTile(
      controller: controller,
    );
  }
}
```

Code after migration:

dart

```
class _MyWidgetState extends State<MyWidget> {
  final ExpansibleController controller = ExpansibleController();
  
  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ExpansionTile(
      controller: controller,
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.31.0-0.1.pre  
 In stable release: 3.32

References
----------

[#](#references)

API documentation:

* [`ExpansionTileController`](https://api.flutter.dev/flutter/material/ExpansionTileController-class.html)* [`ExpansibleController`](https://api.flutter.dev/flutter/widgets/ExpansibleController-class.html)* [`ExpansionTile.controller`](https://api.flutter.dev/flutter/material/ExpansionTile/controller.html)* [`Expansible.controller`](https://api.flutter.dev/flutter/widgets/Expansible/controller.html)

Relevant issues:

* [Codeshare between ExpansionTile and its Cupertino variant](https://github.com/flutter/flutter/issues/163552)* [Deprecate ExpansionTileController in favor of ExpansibleController](https://github.com/flutter/flutter/issues/165511)

Relevant PRs:

* [Introduce Expansible, a base widget for ExpansionTile](https://github.com/flutter/flutter/pull/164049)* [Deprecate ExpansionTileController](https://github.com/flutter/flutter/pull/166368)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/expansion-tile-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/expansion-tile-controller.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/expansion-tile-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/expansion-tile-controller.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-20. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/expansion-tile-controller.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/expansion-tile-controller/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/expansion-tile-controller.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   