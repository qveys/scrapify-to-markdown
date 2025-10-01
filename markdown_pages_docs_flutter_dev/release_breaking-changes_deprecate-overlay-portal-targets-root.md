Deprecate `OverlayPortal.targetsRootOverlay`
============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate `OverlayPortal.targetsRootOverlay`](/release/breaking-changes/deprecate-overlay-portal-targets-root)

Summary
-------

[#](#summary)

The `OverlayPortal.targetsRootOverlay` property was deprecated and replaced with `overlayLocation`.

Context
-------

[#](#context)

A parameter `overlayLocation` was added to the OverlayPortal default constructor to control where the overlay child renders. As the result, the constructor `OverlayPortal.targetsRootOverlay` was no longer useful.

Description of change
---------------------

[#](#description-of-change)

The `OverlayPortal.targetsRootOverlay` was deprecated.

Migration guide
---------------

[#](#migration-guide)

If you are using `OverlayPortal.targetsRootOverlay`, you can use `OverlayPortal` with `overlayLocation` instead.

### Case 1: trivial case

[#](#case-1-trivial-case)

Code before migration:

dart

```
Widget build(BuildContext context) {
  return OverlayPortal.targetsRootOverlay(
    controller: myController,
    overlayChildBuilder: _myBuilder,
    child: myChild,
  );
}
```

Code after migration:

dart

```
Widget build(BuildContext context) {
  return OverlayPortal(
    overlayLocation: OverlayChildLocation.rootOverlay,
    controller: myController,
    overlayChildBuilder: _myBuilder,
    child: myChild,
  );
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.35.0-0.0.pre  
 In stable release: TBD

References
----------

[#](#references)

API documentation:

* [`OverlayPortal`](https://api.flutter.dev/flutter/widgets/OverlayPortal-class.html)

Relevant issue:

* [Issue 168785](https://github.com/flutter/flutter/issues/168785)

Relevant PR:

* [PR 174239](https://github.com/flutter/flutter/pull/174239)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-overlay-portal-targets-root/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-overlay-portal-targets-root.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-overlay-portal-targets-root/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-overlay-portal-targets-root.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-overlay-portal-targets-root.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-overlay-portal-targets-root/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-overlay-portal-targets-root.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   