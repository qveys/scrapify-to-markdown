AnnotatedRegionLayers return local position relative to clipping region
=======================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [AnnotatedRegionLayers return local position relative to clipping region](/release/breaking-changes/annotations-return-local-position-relative-to-object)

Summary
-------

[#](#summary)

The local position returned by `AnnotatedRegionLayers` in an annotation search has been changed to be relative to the clipping region instead of the layer. This makes the local position more meaningful and reliable, but breaks code that directly performs annotation searches and uses the local position.

Context
-------

[#](#context)

Annotations are metadata that are assigned during the rendering phase to regions on the screen. Searching the annotations with a location gives the contextual information that contains that location. They are used to detect mouse events and the theme of app bars.

When `localPosition` was first added to the search result, it was defined as relative to the layer that owned the annotation, which turned out to be a design mistake. The offset from the layer is meaningless and unreliable. For example, a `Transform` widget draws on the same layer with an offset if the transform matrix is a simple translation, or push a dedicated `TransformLayer` if the matrix is non-trivial. The former case keeps the previous coordinate origin (for example, the top left corner of the app), while the latter case moves the position origin since it's on a new layer. The two cases might not produce noticeable visual differences, since the extra layer might just be a scale of 99%, despite that the annotation search returns different results. In order to make this local position reliable, we have to choose one of the results to stick to.

Description of change
---------------------

[#](#description-of-change)

The `localPosition` returned by an `AnnotatedRegionLayer` is now the local position it received subtracted by `offset`, where `offset` is the location of the clipping area relative to the layer.

dart

```
class AnnotatedRegionLayer<T> extends ContainerLayer {
  @override
  bool findAnnotations<S>(AnnotationResult<S> result, Offset localPosition, { required bool onlyFirst }) {
    ...
    if (/* shouldAddAnnotation */) {
      result.add(AnnotationEntry<S>(
        annotation: typedValue,
        // Used to be:
        // localPosition: localPosition,
        localPosition: localPosition - offset,
      ));
    }
    ...
  }
}
```

Conceptually, this has changed how `AnnotatedRegionLayer.offset` and `size` are defined. They used to mean "the clipping rectangle that restricts the annotation search", while they now jointly represent "the region of the annotation object".

Migration guide
---------------

[#](#migration-guide)

Code that is actively using this local position is probably directly interacting with layers, since using render objects or widgets have already made this result unreliable. In order to preserve the previous behavior, you can reimplement `AnnotatedRegionLayer` to return a local position without subtracting the offset.

Timeline
--------

[#](#timeline)

Landed in version: 1.15.2  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`AnnotatedRegionLayer`](https://api.flutter.dev/flutter/rendering/AnnotatedRegionLayer-class.html)* [`AnnotationEntry`](https://api.flutter.dev/flutter/rendering/AnnotationEntry-class.html)

Relevant issues:

* [Issue #49568](https://github.com/flutter/flutter/issues/49568)

Relevant PR:

* [Make Annotation's localPosition relative to object](https://github.com/flutter/flutter/pull/50157)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/annotations-return-local-position-relative-to-object/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/annotations-return-local-position-relative-to-object.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/annotations-return-local-position-relative-to-object/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/annotations-return-local-position-relative-to-object.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/annotations-return-local-position-relative-to-object.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/annotations-return-local-position-relative-to-object/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/annotations-return-local-position-relative-to-object.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   