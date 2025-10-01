New APIs for Android plugins that render to a Surface
=====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [New APIs for Android plugins that render to a Surface](/release/breaking-changes/android-surface-plugins)

Summary
-------

[#](#summary)

The Android embedder for Flutter introduces a new API, [`SurfaceProducer`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.SurfaceProducer.html), which allows plugins to render to a `Surface` without needing to manage what the backing implementation is. Plugins using the older [`createSurfaceTexture`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.html#createSurfaceTexture()) API will continue to work with [Impeller](/perf/impeller) after the *next* stable release, but are recommended to migrate to the new API.

Background
----------

[#](#background)

An Android [`SurfaceTexture`](https://source.android.com/docs/core/graphics/arch-st) is a backing implementation for a [`Surface`](https://developer.android.com/reference/android/view/Surface) that uses an [OpenGLES](https://www.khronos.org/opengles/) texture as the backing store.

For example, a plugin might display frames from a *camera* plugin:

![Flowchart](https://camo.githubusercontent.com/cdb52c5d371b4f1d5573b650a0eddb0871e5e8be1012d290e008f41bc71b2580/68747470733a2f2f736f757263652e616e64726f69642e636f6d2f7374617469632f646f63732f636f72652f67726170686963732f696d616765732f636f6e74696e756f75735f636170747572655f61637469766974792e706e67)

In newer versions of the Android API (>= 29), Android introduced a backend-agnostic [`HardwareBuffer`](https://developer.android.com/reference/android/hardware/HardwareBuffer), which coincides with the minimum version that Flutter will attempt to use the [Vulkan](https://source.android.com/docs/core/graphics/arch-vulkan) renderer. The Android embedding API needed to be updated to support a more generic `Surface` creation API that doesn't rely on OpenGLES.

Migration guide
---------------

[#](#migration-guide)

If you are using the older [`createSurfaceTexture`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.html#createSurfaceTexture()) API, you should migrate to the new [`createSurfaceProducer`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.html#createSurfaceProducer()) API. The new API is more flexible and allows the Flutter engine to opaquely pick the best implementation for the current platform and API level.

1. Instead of creating a `SurfaceTextureEntry`, create a `SurfaceProducer`:

   java

   ```
   TextureRegistry.SurfaceTextureEntry entry = textureRegistry.createSurfaceTexture();
   TextureRegistry.SurfaceProducer producer = textureRegistry.createSurfaceProducer();
   ```

   - Instead of creating a `new Surface(...)`, call [`getSurface()`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.SurfaceProducer.html#getSurface()) on the `SurfaceProducer`:

     java

     ```
     Surface surface = new Surface(entry.surfaceTexture());
     Surface surface = producer.getSurface();
     ```

In order to conserve memory when the application is suspended in the background, Android and Flutter *may* destroy a surface when it is no longer visible. To ensure that the surface is recreated when the application is resumed, you should use the provided [`setCallback`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.SurfaceProducer.html#setCallback(io.flutter.view.TextureRegistry.SurfaceProducer.Callback)) method to listen to surface lifecycle events:

java

```
surfaceProducer.setCallback(
   new TextureRegistry.SurfaceProducer.Callback() {
      @Override
      public void onSurfaceAvailable() {
         // Do surface initialization here, and draw the current frame.
      }

      @Override
      public void onSurfaceDestroyed() {
         // Do surface cleanup here, and stop drawing frames.
      }
   }
);
```

A full example of using this new API can be found in [PR 6989](https://github.com/flutter/packages/pull/6989) for the `video_player_android` plugin.

*info* Note

In early versions of this API, the callback was named `onSurfaceCreated`, and was invoked even if the original surface was not destroyed. This has been fixed in the latest (pending 3.27) version of the API.

Note on camera previews
-----------------------

[#](#note-on-camera-previews)

If your plugin implements a camera preview, your migration might also require fixing the rotation of that preview. This is because `Surface`s produced by the `SurfaceProducer` might not contain the transformation information that Android libraries need to correctly rotate the preview automatically.

In order to correct the rotation, you need to rotate the preview with respect to the camera sensor orientation and the device orientation according to the equation:

```
rotation = (sensorOrientationDegrees - deviceOrientationDegrees * sign + 360) % 360
```

where `deviceOrientationDegrees` is counterclockwise degrees and `sign` is 1 for front-facing cameras and -1 for back-facing cameras.

To calculate this rotation,

* Use [`SurfaceProducer.handlesCropAndRotation`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.SurfaceProducer.html#handlesCropAndRotation()) to check if the underlying `Surface` handles rotation (if `false`, you may need to handle the rotation).* Retrieve the sensor orientation degrees by retrieving the value of [`CameraCharacteristics.SENSOR_ORIENTATION`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SENSOR_ORIENTATION).* Retrieve the device orientation degrees in one of the ways that the [Android orientation calculation documentation](https://developer.android.com/media/camera/camera2/camera-preview#orientation_calculation) details.

To apply this rotation, you can use a [`RotatedBox`](https://api.flutter.dev/flutter/widgets/RotatedBox-class.html) widget.

For more information on this calculation, check out the [Android orientation calculation documentation](https://developer.android.com/media/camera/camera2/camera-preview#orientation_calculation). For a full example of making this fix, check out [this `camera_android_camerax` PR](https://github.com/flutter/packages/pull/7044).

Timeline
--------

[#](#timeline)

Landed in version: 3.22

*info* Note

This feature landed in the *previous* version of the SDK but was non-functional; plugins that migrate to this API should set `3.24` as a minimum version constraint.

In stable release: 3.24

In the upcoming stable release, 3.27, `onSurfaceCreated` is deprecated, and `onSurfaceAvailable` and `handlesCropAndRotation` are added.

References
----------

[#](#references)

API documentation:

* [`SurfaceProducer`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.SurfaceProducer.html)* [`createSurfaceProducer`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.html#createSurfaceProducer())* [`createSurfaceTexture`](https://api.flutter.dev/javadoc/io/flutter/view/TextureRegistry.html#createSurfaceTexture())

Relevant issues:

* [Issue 139702](https://github.com/flutter/flutter/issues/139702)* [Issue 145930](https://github.com/flutter/flutter/issues/145930)

Relevant PRs:

* [PR 51061](https://github.com/flutter/engine/pull/51061), where we test the new API in the engine tests.* [PR 6456](https://github.com/flutter/packages/pull/6456), where we migrate the `video_player` plugin to use the new API.* [PR 6461](https://github.com/flutter/packages/pull/6461), where we migrate the `camera_android` plugin to use the new API.* [PR 6989](https://github.com/flutter/packages/pull/6989), where we add a full example of using the new API in the `video_player_android` plugin.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-surface-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-surface-plugins.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-surface-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-surface-plugins.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-10-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-surface-plugins.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/android-surface-plugins/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/android-surface-plugins.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   