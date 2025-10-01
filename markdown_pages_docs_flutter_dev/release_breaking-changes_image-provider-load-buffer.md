Adding ImageProvider.loadBuffer
===============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Adding ImageProvider.loadBuffer](/release/breaking-changes/image-provider-load-buffer)

Summary
-------

[#](#summary)

* `ImageProvider` now has a method called `loadBuffer` that functions similarly to `load`, except that it decodes from an `ui.ImmutableBuffer`.* `ui.ImmutableBuffer` can now be created directly from an asset key.* The `AssetBundle` classes can now load an `ui.ImmutableBuffer`.* The `PaintingBinding` now has a method called `instantiateImageCodecFromBuffer`, which functions similarly to `instantiateImageCodec`.* `ImageProvider.load` is now deprecated, it will be removed in a future release.* `PaintingBinding.instantiateImageCodec` is now deprecated, it will be removed in a future release.

Context
-------

[#](#context)

`ImageProvider.loadBuffer` is a new method that must be implemented in order to load images. This API allows asset-based image loading to be performed faster and with less memory impact on application.

Description of change
---------------------

[#](#description-of-change)

When loading asset images, previously the image provider API required multiple copies of the compressed data. First, when opening the asset the data was copied into the external heap and exposed to Dart as a typed data array. Then that typed data array was eventually converted into an `ui.ImmutableBuffer`, which internally copies the data into a second structure for decoding.

With the addition of `ui.ImmutableBuffer.fromAsset`, compressed image bytes can be loaded directly into the structure used for decoding. Using this approach requires changes to the byte loading pipeline of `ImageProvider`. This process is also faster, because it bypasses some additional scheduling overhead of the previous method channel based loader.

`ImageProvider.loadBuffer` otherwise has the same contract as `ImageProvider.load`, except it provides a new decoding callback that expects an `ui.ImmutableBuffer` instead of a `Uint8List`. For `ImageProvider` classes that acquire bytes from places other than assets, the convenience method `ui.ImmutableBuffer.fromUint8List` can be used for compatibility.

Migration guide
---------------

[#](#migration-guide)

Classes that subclass `ImageProvider` must implement the `loadBuffer` method for loading assets. Classes that delegate to or call the methods of an `ImageProvider` directly must use `loadBuffer` instead of `load`.

Code before migration:

dart

```
class MyImageProvider extends ImageProvider<MyImageProvider> {
  @override
  ImageStreamCompleter load(MyImageProvider key, DecoderCallback decode) {
    return MultiFrameImageStreamCompleter(
        codec: _loadData(key, decode),
    );
  }

  Future<ui.Codec> _loadData(MyImageProvider key, DecoderCallback decode) async {
    final Uint8List bytes = await bytesFromSomeApi();
    return decode(bytes);
  }
}

class MyDelegatingProvider extends ImageProvider<MyDelegatingProvider> {
  MyDelegatingProvider(this.provider);

  final ImageProvder provider;

  @override
  ImageStreamCompleter load(MyDelegatingProvider key, DecoderCallback decode) {
    return provider.load(key, decode);
  }
}
```

Code after migration:

dart

```
class MyImageProvider extends ImageProvider<MyImageProvider> {
  @override
  ImageStreamCompleter loadBuffer(MyImageProvider key, DecoderBufferCallback decode) {
    return MultiFrameImageStreamCompleter(
        codec: _loadData(key, decode),
    );
  }

  Future<ui.Codec> _loadData(MyImageProvider key, DecoderBufferCallback decode) async {
    final Uint8List bytes = await bytesFromSomeApi();
    final ui.ImmutableBuffer buffer = await ui.ImmutableBuffer.fromUint8List(bytes);
    return decode(buffer);
  }
}

class MyDelegatingProvider extends ImageProvider<MyDelegatingProvider> {
  MyDelegatingProvider(this.provider);

  final ImageProvder provider;

  @override
  ImageStreamCompleter loadBuffer(MyDelegatingProvider key, DecoderCallback decode) {
    return provider.loadBuffer(key, decode);
  }
}
```

In both cases you might choose to keep the previous implementation of `ImageProvider.load` to give users of your code time to migrate as well.

Timeline
--------

[#](#timeline)

Landed in version: 3.1.0-0.0.pre.976  
 In stable release: 3.3.0

References
----------

[#](#references)

API documentation:

* [`ImmutableBuffer`](https://api.flutter.dev/flutter/dart-ui/ImmutableBuffer-class.html)* [`ImageProvider`](https://api.flutter.dev/flutter/painting/ImageProvider-class.html)

Relevant PR:

* [Use immutable buffer for loading asset images](https://github.com/flutter/flutter/pull/103496)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-provider-load-buffer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-provider-load-buffer.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-provider-load-buffer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-provider-load-buffer.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-provider-load-buffer.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-provider-load-buffer/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-provider-load-buffer.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   