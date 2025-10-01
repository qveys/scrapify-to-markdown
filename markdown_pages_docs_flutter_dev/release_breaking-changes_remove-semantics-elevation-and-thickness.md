Removed semantics elevation and thickness
=========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Removed semantics elevation and thickness](/release/breaking-changes/remove-semantics-elevation-and-thickness)

Summary
-------

[#](#summary)

Both elevation and thickness semantics properties and their related APIs were removed.

Context
-------

[#](#context)

Both elevation and thickness semantics properties were created for Fuchsia's 3D rendering. They were never implemented and thus remained unused. There was also no other known usage for these properties. These properties added unnecessary code complexity and have been removed.

Description of change
---------------------

[#](#description-of-change)

The following properties are removed `SemanticsConfiguration.elevation`, `SemanticsConfiguration.thickness`, `SemanticsNode.thickness`, `SemanticsNode.elevation`, and `SemanticsNode.elevationAdjustment`.

Migration guide
---------------

[#](#migration-guide)

If you previously assigned these properties, remove the assignments.

Code before migration:

dart

```
void describeSemanticsConfiguration(SemanticsConfiguration config) {
  config.label = 'my label';
  config.elevation = 1;
  config.thickness = 1;
}
```

Code after migration:

dart

```
void describeSemanticsConfiguration(SemanticsConfiguration config) {
  config.label = 'my label';
}
```

Timeline
--------

[#](#timeline)

Landed in version: 3.34.0-0.0.pre  
 In stable release: 3.35

References
----------

[#](#references)

API documentation:

* [`SemanticsConfiguration`](https://api.flutter.dev/flutter/semantics/SemanticsConfiguration-class.html)* [`SemanticsNode`](https://api.flutter.dev/flutter/semantics/SemanticsNode-class.html)

Relevant issue:

* [Issue 166092](https://github.com/flutter/flutter/issues/166092)

Relevant PR:

* [PR 169382](https://github.com/flutter/flutter/pull/169382)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/remove-semantics-elevation-and-thickness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/remove-semantics-elevation-and-thickness.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/remove-semantics-elevation-and-thickness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/remove-semantics-elevation-and-thickness.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/remove-semantics-elevation-and-thickness.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/remove-semantics-elevation-and-thickness/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/remove-semantics-elevation-and-thickness.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   