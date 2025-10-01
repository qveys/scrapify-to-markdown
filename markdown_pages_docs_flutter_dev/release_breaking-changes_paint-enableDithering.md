Paint.enableDithering is now true by default.
=============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Paint.enableDithering is now true by default.](/release/breaking-changes/paint-enableDithering)

Summary
-------

[#](#summary)

[`Paint.enableDithering`](https://api.flutter.dev/flutter/dart-ui/Paint/enableDithering.html) is now `true` by default (previously, `false`), and is *deprecated* pending removal - Flutter no longer supports user-configurable dithering settings.

In addition, the dithering documentation states support is *only* for gradients.

Background
----------

[#](#background)

[`Paint.enableDithering`](https://api.flutter.dev/flutter/dart-ui/Paint/enableDithering.html) was added as a global option in [PR 13868](https://github.com/flutter/engine/pull/13868) as a response to [Issue 44134](https://github.com/flutter/flutter/issues/44134), which reported that gradients in Flutter had visible banding artifacts:
> Gradients currently have a lot of color banding on all devices, and it looks very weird when using the pulse animation too. A solution is to make the gradients opaque, and to use dithered gradients with Skia. Dithered gradients aren't currently exposed, so adding a dither parameter to dart:ui's Paint class would be nice. We'd be able to manually draw our gradients with a CustomPainter.

![Example of banding](https://user-images.githubusercontent.com/30870216/210907719-4f4a1a8d-e28a-4d39-9e99-3635a26a0c74.png)

[Issue 118073](https://github.com/flutter/flutter/issues/118073) reported that gradients in our new [Impeller](/perf/impeller) backend displayed visible banding artifacts in some gradients. It was later discovered that Impeller didn't support the (rarely used) [`Paint.enableDithering`](https://api.flutter.dev/flutter/dart-ui/Paint/enableDithering.html) property.

After adding dithering support to Impeller ([PR 44181](https://github.com/flutter/engine/pull/44181), [PR 44331](https://github.com/flutter/engine/pull/44331), [PR 44522](https://github.com/flutter/engine/pull/44522)), and reviewing the performance impact of dithering (negligible), the following observations were made:

1. Consensus that gradients look good by default: [Issue 112498](https://github.com/flutter/flutter/issues/112498).- Having a global option was intended to be deprecated: [PR 13868](https://github.com/flutter/engine/pull/13868).

This resulted in the following decisions:

1. Make dithering enabled by default.- Deprecate the global option.- Remove the global option in a future release.

As part of that process, the ability for dithering to affect anything other than gradients was removed in [PR 44730](https://github.com/flutter/engine/pull/44730) and [PR 44912](https://github.com/flutter/engine/pull/44912). That was done to ease the process of migrating, because Impeller will never support dithering for anything but gradients.

Migration guide
---------------

[#](#migration-guide)

Most users and libraries will not need to make any changes.

For users that maintain golden tests, you might need to update your golden images to reflect the new default. For example, if you use [`matchesGoldenFile`](https://api.flutter.dev/flutter_test/matchesGoldenFile.html) to test a widget that contains a gradient:

```
flutter test --update-goldens
```

While this is not expected to be a common case, you can disable dithering temporarily by setting the `enableDithering` property in your `main()` method (either in an app or test):

dart

```
void main() {
  // TODO: Remove this after XYZ.
  Paint.enableDithering = false;

  runApp(MyApp());
}
```

As the plan is to *permanently* remove the `enableDithering` property, please provide feedback in [Issue 112498](https://github.com/flutter/flutter/issues/112498) if you have a use case that requires disabling dithering (due to performance, crashes).

If for some reason you *must* draw gradients without dithering, you'll need to write your own custom shader. Describing that is out of the scope of this migration guide, but you can find some resources and examples:

* [Writing and using fragment shaders](/ui/design/graphics/fragment-shaders)* [`hsl_linear_gradient.frag`](https://github.com/jonahwilliams/awesome_gradients/blob/a4e09c47ef1760bd7073beb60f49dad8ede5bb2e/shaders/hsl_linear_gradient.frag)

**NOTE**: Flutter web does not support dithering: [Issue 134250](https://github.com/flutter/flutter/issues/134250).

Timeline
--------

[#](#timeline)

Landed in version: 3.14.0-0.1.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`Paint.enableDithering`](https://api.flutter.dev/flutter/dart-ui/Paint/enableDithering.html)* [`matchesGoldenFile`](https://api.flutter.dev/flutter_test/matchesGoldenFile.html)

Relevant issues:

* [Issue 44134](https://github.com/flutter/flutter/issues/44134)* [Issue 112498](https://github.com/flutter/flutter/issues/112498)* [Issue 118073](https://github.com/flutter/flutter/issues/118073)

Relevant PRs:

* [PR 13868](https://github.com/flutter/engine/pull/13868)* [PR 44181](https://github.com/flutter/engine/pull/44181)* [PR 44331](https://github.com/flutter/engine/pull/44331)* [PR 44522](https://github.com/flutter/engine/pull/44522)* [PR 44730](https://github.com/flutter/engine/pull/44730)* [PR 44912](https://github.com/flutter/engine/pull/44912)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/paint-enableDithering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/paint-enableDithering.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/paint-enableDithering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/paint-enableDithering.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-16. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/paint-enableDithering.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/paint-enableDithering/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/paint-enableDithering.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   