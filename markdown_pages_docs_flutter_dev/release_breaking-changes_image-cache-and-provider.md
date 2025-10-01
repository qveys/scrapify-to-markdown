ImageCache and ImageProvider changes
====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [ImageCache and ImageProvider changes](/release/breaking-changes/image-cache-and-provider)

Summary
-------

[#](#summary)

`ImageCache` now has a method called `containsKey`. `ImageProvider` subclasses should not override `resolve`, but instead should implement new methods on `ImageProvider`. These changes were submitted as a single commit to the framework.

Description of change
---------------------

[#](#description-of-change)

The sections below describe the changes to `containsKey` and `ImageProvider`.

### containsKey change

[#](#containskey-change)

Clients of the `ImageCache`, such as a custom `ImageProvider`, may want to know if the cache is already tracking an image. Adding the `containsKey` method allows callers to discover this without calling a method like `putIfAbsent`, which can trigger an undesired call to `ImageProvider.load`.

The default implementation checks both pending and cached image buckets.

dart

```
  bool containsKey(Object key) {
    return _pendingImages[key] != null || _cache[key] != null;
  }
```

### ImageProvider changes

[#](#imageprovider-changes)

The `ImageProvider.resolve` method does some complicated error handling work that should not normally be overridden. It also previously did work to load the image into the image cache, by way of `ImageProvider.obtainKey` and `ImageProvider.load`. Subclasses had no opportunity to override this behavior without overriding `resolve`, and the ability to compose `ImageProvider`s is limited if multiple `ImageProvider`s expect to override `resolve`.

To solve this issue, `resolve` is now marked as non-virtual, and two new protected methods have been added: `createStream()` and `resolveStreamForKey()`. These methods allow subclasses to control most of the behavior of `resolve`, without having to duplicate all the error handling work. It also allows subclasses that compose `ImageProvider`s to be more confident that there is only one public entrypoint to the various chained providers.

Migration guide
---------------

[#](#migration-guide)

### ImageCache change

[#](#imagecache-change)

Before migration, the code would not have an override of `containsKey`.

Code after migration:

dart

```
class MyImageCache implements ImageCache {
  @override
  bool containsKey(Object key) {
    // Check if your custom cache is tracking this key.
  }

  ...
}
```

### ImageProvider change

[#](#imageprovider-change)

Code before the migration:

dart

```
class MyImageProvider extends ImageProvider<Object> {
  @override
  ImageStream resolve(ImageConfiguration configuration) {
    // create stream
    // set up error handling
    // interact with ImageCache
    // call obtainKey/load, etc.
  }
  ...
}
```

Code after the migration:

dart

```
class MyImageProvider extends ImageProvider<Object> {
  @override
  ImageStream createStream(ImageConfiguration configuration) {
    // Return stream, or use super.createStream(),
    // which returns a new ImageStream.
  }

  @override
  void resolveStreamForKey(
    ImageConfiguration configuration,
    ImageStream stream,
    Object key,
    ImageErrorListener handleError,
  ) {
    // Interact with the cache, use the key, potentially call `load`,
    // and report any errors back through `handleError`.
  }
  ...
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

* [`ImageCache`](https://api.flutter.dev/flutter/painting/ImageCache-class.html)* [`ImageProvider`](https://api.flutter.dev/flutter/painting/ImageProvider-class.html)* [`ScrollAwareImageProvider`](https://api.flutter.dev/flutter/widgets/ScrollAwareImageProvider-class.html)

Relevant issues:

* [Issue #32143](https://github.com/flutter/flutter/issues/32143)* [Issue #44510](https://github.com/flutter/flutter/issues/44510)* [Issue #48305](https://github.com/flutter/flutter/issues/48305)* [Issue #48775](https://github.com/flutter/flutter/issues/48775)

Relevant PRs:

* [Defer image decoding when scrolling fast #49389](https://github.com/flutter/flutter/pull/49389)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-cache-and-provider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-cache-and-provider.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-cache-and-provider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-cache-and-provider.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-cache-and-provider.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-cache-and-provider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-cache-and-provider.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   