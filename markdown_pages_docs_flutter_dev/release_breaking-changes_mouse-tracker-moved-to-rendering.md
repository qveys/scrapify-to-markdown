MouseTracker moved to rendering
===============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [MouseTracker moved to rendering](/release/breaking-changes/mouse-tracker-moved-to-rendering)

Summary
-------

[#](#summary)

[`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html) and related symbols are moved from the `gestures` package, resulting in error messages such as undefined classes or methods. Import them from `rendering` package instead.

Context
-------

[#](#context)

Prior to this change [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html) was part of the `gestures` package. This brought troubles when we found out that code related to [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html) often wanted to import from the `rendering` package.

Since [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html) turned out to be more connected to `rendering` than `gestures`, we have moved it and its related code to `rendering`.

Description of change
---------------------

[#](#description-of-change)

The file `mouse_tracking.dart` has been moved from the `gestures` package to `rendering`. All symbols in the said file have been moved without keeping backward compatibility.

Migration guide
---------------

[#](#migration-guide)

If you see error of "Undefined class" or "Undefined name" of the following symbols:

* [`MouseDetectorAnnotationFinder`](https://api.flutter.dev/flutter/gestures/MouseDetectorAnnotationFinder.html)* [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html)* [`MouseTrackerAnnotation`](https://api.flutter.dev/flutter/gestures/MouseTrackerAnnotation-class.html)* [`PointerEnterEventListener`](https://api.flutter.dev/flutter/gestures/PointerEnterEventListener.html)* [`PointerExitEventListener`](https://api.flutter.dev/flutter/gestures/PointerExitEventListener.html)* [`PointerHoverEventListener`](https://api.flutter.dev/flutter/gestures/PointerHoverEventListener.html)

You should add the following import:

dart

```
import 'package:flutter/rendering.dart';
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

* [`MouseDetectorAnnotationFinder`](https://api.flutter.dev/flutter/gestures/MouseDetectorAnnotationFinder.html)* [`MouseTracker`](https://api.flutter.dev/flutter/gestures/MouseTracker-class.html)* [`MouseTrackerAnnotation`](https://api.flutter.dev/flutter/gestures/MouseTrackerAnnotation-class.html)* [`PointerEnterEventListener`](https://api.flutter.dev/flutter/gestures/PointerEnterEventListener.html)* [`PointerExitEventListener`](https://api.flutter.dev/flutter/gestures/PointerExitEventListener.html)* [`PointerHoverEventListener`](https://api.flutter.dev/flutter/gestures/PointerHoverEventListener.html)

Relevant issues:

* [Transform mouse events to the local coordinate system](https://github.com/flutter/flutter/issues/33675)* [Move annotations to a separate tree](https://github.com/flutter/flutter/issues/49568)

Relevant PR:

* [Move mouse\_tracking.dart to rendering](https://github.com/flutter/flutter/pull/52781)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-moved-to-rendering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-moved-to-rendering.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-moved-to-rendering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-moved-to-rendering.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-moved-to-rendering.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/mouse-tracker-moved-to-rendering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/mouse-tracker-moved-to-rendering.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   