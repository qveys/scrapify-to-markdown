ImageCache large images
=======================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [ImageCache large images](/release/breaking-changes/imagecache-large-images)

Summary
-------

[#](#summary)

The `maxByteSize` of the `ImageCache` is no longer automatically made larger to accommodate large images.

Context
-------

[#](#context)

Previously, when loading images into the `ImageCache` that had larger byte sizes than the `ImageCache`'s `maxByteSize`, Flutter permanently increased the `maxByteSize` value to accommodate those images. This logic sometimes led to bloated `maxByteSize` values that made working in memory-limited systems more difficult.

Description of change
---------------------

[#](#description-of-change)

The following "before" and "after" pseudocode demonstrates the changes made to the `ImageCache` algorithm:

dart

```
// Old logic pseudocode
void onLoadImage(Image image) {
  if (image.byteSize > _cache.maxByteSize) {
    _cache.maxByteSize = image.byteSize + 1000;
  }
  _cache.add(image);
  while (_cache.count > _cache.maxCount
      || _cache.byteSize > _cache.maxByteSize) {
    _cache.discardOldestImage();
  }
}
```

dart

```
// New logic pseudocode
void onLoadImage(Image image) {
  if (image.byteSize < _cache.maxByteSize) {
    _cache.add(image);
    while (_cache.count > _cache.maxCount
        || _cache.byteSize > cache.maxByteSize) {
      cache.discardOldestImage();
    }
  }
}
```

Migration guide
---------------

[#](#migration-guide)

There might be situations where the `ImageCache` is thrashing with the new logic where it wasn't previously, specifically if you load images that are larger than your `cache.maxByteSize` value. This can be remedied by one of the following approaches:

1. Increase the `ImageCache.maxByteSize` value to accommodate larger images.- Adjust your image loading logic to guarantee that the images fit nicely into the `ImageCache.maxByteSize` value of your choosing.- Subclass `ImageCache`, implement your desired logic, and create a new binding that serves up your subclass of `ImageCache` (see the [`image_cache.dart`](https://github.com/flutter/flutter/blob/72a3d914ee5db0033332711224e728b8a5281d89/packages/flutter/lib/src/painting/image_cache.dart#L34) source).

Timeline
--------

[#](#timeline)

The old algorithm is no longer supported.

Landed in version: 1.16.3  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`ImageCache`](https://api.flutter.dev/flutter/painting/ImageCache-class.html)

Relevant issue:

* [Issue 45643](https://github.com/flutter/flutter/issues/45643)

Relevant PR:

* [Stopped increasing the cache size to accommodate large images](https://github.com/flutter/flutter/pull/47387)

Other:

* [`ImageCache` source](https://github.com/flutter/flutter/blob/main/packages/flutter/lib/src/painting/image_cache.dart)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/imagecache-large-images/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/imagecache-large-images.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/imagecache-large-images/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/imagecache-large-images.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/imagecache-large-images.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/imagecache-large-images/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/imagecache-large-images.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   