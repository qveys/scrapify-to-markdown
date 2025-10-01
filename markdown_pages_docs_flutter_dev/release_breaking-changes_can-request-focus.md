Deprecated TextField.canRequestFocus
====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated TextField.canRequestFocus](/release/breaking-changes/can-request-focus)

Summary
-------

[#](#summary)

`TextField.canRequestFocus` is deprecated. The same functionality can be achieved by setting the `canRequestFocus` parameter of the `TextField`'s `FocusNode`.

Background
----------

[#](#background)

`TextField.canRequestFocus` was added to support `DropdownMenu`, which has a `TextField` that sometimes isn't interactive. However, the same functionality can be achieved by setting the `canRequestFocus` parameter of a `TextField`'s `FocusNode`. `DropdownMenu` has been migrated to this approach, and other use cases should follow the same pattern.

Apps that use `TextField.canRequestFocus` display the following error when run in debug mode: "Use `focusNode` instead.". Specifically, this means that users should pass a `FocusNode` to `TextField.focusNode` with the `FocusNode.canRequestFocus` parameter set.

Migration guide
---------------

[#](#migration-guide)

To migrate, remove the `TextField.canRequestFocus` parameter. Create a `FocusNode` with the `FocusNode.canRequestFocus` parameter set to the desired value, and pass that to `TextField.focusNode`.

Code before migration:

dart

```
class _MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return TextField(
      canRequestFocus: false,
    );
  }
}
```

Code after migration:

dart

```
class _MyWidgetState extends State<MyWidget> {
  final FocusNode _focusNode = FocusNode(canRequestFocus: false);

  @override
  Widget build(BuildContext context) {
    return TextField(
      focusNode: _focusNode,
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: Reverted, waiting to reland  
 In stable release: Not yet

References
----------

[#](#references)

API documentation:

* [`DropdownMenu`](https://api.flutter.dev/flutter/material/DropdownMenu-class.html)* [`FocusNode.canRequestFocus`](https://api.flutter.dev/flutter/widgets/FocusNode/canRequestFocus.html)* [`TextField.canRequestFocus`](https://api.flutter.dev/flutter/material/TextField/canRequestFocus.html)* [`TextField.focusNode`](https://api.flutter.dev/flutter/material/TextField/focusNode.html)

Relevant issues:

* [Broken selection on TextField if canRequestFocus: false](https://github.com/flutter/flutter/issues/130011)* [DropdownMenu Disable text input](https://github.com/flutter/flutter/issues/116587)

Relevant PRs:

* [Add requestFocusOnTap to DropdownMenu](https://github.com/flutter/flutter/pull/117504)* [Replace TextField.canRequestFocus with TextField.focusNode.canRequestFocus](https://github.com/flutter/flutter/pull/130164)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/can-request-focus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/can-request-focus.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/can-request-focus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/can-request-focus.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/can-request-focus.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/can-request-focus/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/can-request-focus.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   