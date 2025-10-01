GestureRecognizer cleanup
=========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [GestureRecognizer cleanup](/release/breaking-changes/gesture-recognizer-add-allowed-pointer)

Summary
-------

[#](#summary)

`OneSequenceGestureRecognizer.addAllowedPointer()` was changed to take a `PointerDownEvent`, like its superclass. Previously, it accepted the more general `PointerEvent` type, which was incorrect.

Context
-------

[#](#context)

The framework only ever passes `PointerDownEvent` objects to `addAllowedPointer()`. Declaring `OneSequenceGestureRecognizer.addAllowedPointer()` to take the more general type was confusing, and caused `OneSequenceGestureRecognizer` subclasses to have to cast their argument to the right class.

Description of change
---------------------

[#](#description-of-change)

The previous declaration forced `OneSequenceGestureRecognizer` descendants to override `addAllowedPointer()` like so:

dart

```
class CustomGestureRecognizer extends ScaleGestureRecognizer {
  @override
  void addAllowedPointer(PointerEvent event) {
    // insert custom handling of event here...
    super.addAllowedPointer(event);
  }
}
```

The new method declaration will cause this code to fail with the following error message:

```
super.addAllowedPointer(event); The argument type 'PointerEvent' can't be assigned to the parameter type 'PointerDownEvent'.
                                #argument_type_not_assignable
```

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
class CustomGestureRecognizer extends ScaleGestureRecognizer {
  @override
  void addAllowedPointer(PointerEvent event) {
    // insert custom handling of event here...
    super.addAllowedPointer(event);
  }
}
```

Code after migration:

dart

```
class CustomGestureRecognizer extends ScaleGestureRecognizer {
  @override
  void addAllowedPointer(PointerDownEvent event) {
    // insert custom handling of event here...
    super.addAllowedPointer(event);
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 2.3.0-13.0.pre  
 In stable release: 2.5

References
----------

[#](#references)

API documentation:

* [`OneSequenceGestureRecognizer`](https://api.flutter.dev/flutter/gestures/OneSequenceGestureRecognizer-class.html)

Relevant PR:

* [Fix addAllowedPointer() overrides](https://github.com/flutter/flutter/pull/82834)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/gesture-recognizer-add-allowed-pointer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/gesture-recognizer-add-allowed-pointer.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/gesture-recognizer-add-allowed-pointer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/gesture-recognizer-add-allowed-pointer.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/gesture-recognizer-add-allowed-pointer.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/gesture-recognizer-add-allowed-pointer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/gesture-recognizer-add-allowed-pointer.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   