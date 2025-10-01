Writing and using fragment shaders
==================================

1. [UI](/ui) chevron\_right- [Design & theming](/ui/design) chevron\_right- [Drawing & graphics](/ui/design/graphics) chevron\_right- [Fragment shaders](/ui/design/graphics/fragment-shaders)

*info* Note

Both the Skia and [Impeller](/perf/impeller) backends support writing a custom shader. Except where noted, the same instructions apply to both.

Custom shaders can be used to provide rich graphical effects beyond those provided by the Flutter SDK. A shader is a program authored in a small, Dart-like language, known as GLSL, and executed on the user's GPU.

Custom shaders are added to a Flutter project by listing them in the `pubspec.yaml` file, and obtained using the [`FragmentProgram`](https://api.flutter.dev/flutter/dart-ui/FragmentProgram-class.html) API.

Adding shaders to an application
--------------------------------

[#](#adding-shaders-to-an-application)

Shaders, in the form of GLSL files with the `.frag` extension, must be declared in the `shaders` section of your project's `pubspec.yaml` file. The Flutter command-line tool compiles the shader to its appropriate backend format, and generates its necessary runtime metadata. The compiled shader is then included in the application just like an asset.

yaml

```
flutter:
  shaders:
    - shaders/myshader.frag
```

When running in debug mode, changes to a shader program trigger recompilation and update the shader during hot reload or hot restart.

Shaders from packages are added to a project with `packages/$pkgname` prefixed to the shader program's name (where `$pkgname` is the name of the package).

### Loading shaders at runtime

[#](#loading-shaders-at-runtime)

To load a shader into a `FragmentProgram` object at runtime, use the [`FragmentProgram.fromAsset`](https://api.flutter.dev/flutter/dart-ui/FragmentProgram/fromAsset.html) constructor. The asset's name is the same as the path to the shader given in the `pubspec.yaml` file.

dart

```
void loadMyShader() async {
  var program = await FragmentProgram.fromAsset('shaders/myshader.frag');
}
```

The `FragmentProgram` object can be used to create one or more [`FragmentShader`](https://api.flutter.dev/flutter/dart-ui/FragmentShader-class.html) instances. A `FragmentShader` object represents a fragment program along with a particular set of *uniforms* (configuration parameters). The available uniforms depends on how the shader was defined.

dart

```
void updateShader(Canvas canvas, Rect rect, FragmentProgram program) {
  var shader = program.fragmentShader();
  shader.setFloat(0, 42.0);
  canvas.drawRect(rect, Paint()..shader = shader);
}
```

### Canvas API

[#](#canvas-api)

Fragment shaders can be used with most Canvas APIs by setting [`Paint.shader`](https://api.flutter.dev/flutter/dart-ui/Paint/shader.html). For example, when using [`Canvas.drawRect`](https://api.flutter.dev/flutter/dart-ui/Canvas/drawRect.html) the shader is evaluated for all fragments within the rectangle. For an API like [`Canvas.drawPath`](https://api.flutter.dev/flutter/dart-ui/Canvas/drawPath.html) with a stroked path, the shader is evaluated for all fragments within the stroked line. Some APIs, such as [`Canvas.drawImage`](https://api.flutter.dev/flutter/dart-ui/Canvas/drawImage.html), ignore the value of the shader.

dart

```
void paint(Canvas canvas, Size size, FragmentShader shader) {
  // Draws a rectangle with the shader used as a color source.
  canvas.drawRect(
    Rect.fromLTWH(0, 0, size.width, size.height),
    Paint()..shader = shader,
  );

  // Draws a stroked rectangle with the shader only applied to the fragments
  // that lie within the stroke.
  canvas.drawRect(
    Rect.fromLTWH(0, 0, size.width, size.height),
    Paint()
      ..style = PaintingStyle.stroke
      ..shader = shader,
  )
}
```

Authoring shaders
-----------------

[#](#authoring-shaders)

Fragment shaders are authored as GLSL source files. By convention, these files have the `.frag` extension. (Flutter doesn't support vertex shaders, which would have the `.vert` extension.)

Any GLSL version from 460 down to 100 is supported, though some available features are restricted. The rest of the examples in this document use version `460 core`.

Shaders are subject to the following limitations when used with Flutter:

* UBOs and SSBOs aren't supported* `sampler2D` is the only supported sampler type* Only the two-argument version of `texture` (sampler and uv) is supported* No additional varying inputs can be declared* All precision hints are ignored when targeting Skia* Unsigned integers and booleans aren't supported

### Uniforms

[#](#uniforms)

A fragment program can be configured by defining `uniform` values in the GLSL shader source and then setting these values in Dart for each fragment shader instance.

Floating point uniforms with the GLSL types `float`, `vec2`, `vec3`, and `vec4` are set using the [`FragmentShader.setFloat`](https://api.flutter.dev/flutter/dart-ui/FragmentShader/setFloat.html) method. GLSL sampler values, which use the `sampler2D` type, are set using the [`FragmentShader.setImageSampler`](https://api.flutter.dev/flutter/dart-ui/FragmentShader/setImageSampler.html) method.

The correct index for each `uniform` value is determined by the order that the uniform values are defined in the fragment program. For data types composed of multiple floats, such as a `vec4`, you must call [`FragmentShader.setFloat`](https://api.flutter.dev/flutter/dart-ui/FragmentShader/setFloat.html) once for each value.

For example, given the following uniforms declarations in a GLSL fragment program:

glsl

```
uniform float uScale;
uniform sampler2D uTexture;
uniform vec2 uMagnitude;
uniform vec4 uColor;
```

The corresponding Dart code to initialize these `uniform` values is as follows:

dart

```
void updateShader(FragmentShader shader, Color color, Image image) {
  shader.setFloat(0, 23);  // uScale
  shader.setFloat(1, 114); // uMagnitude x
  shader.setFloat(2, 83);  // uMagnitude y

  // Convert color to premultiplied opacity.
  shader.setFloat(3, color.red / 255 * color.opacity);   // uColor r
  shader.setFloat(4, color.green / 255 * color.opacity); // uColor g
  shader.setFloat(5, color.blue / 255 * color.opacity);  // uColor b
  shader.setFloat(6, color.opacity);                     // uColor a

  // Initialize sampler uniform.
  shader.setImageSampler(0, image);
 }
```

Observe that the indices used with [`FragmentShader.setFloat`](https://api.flutter.dev/flutter/dart-ui/FragmentShader/setFloat.html) do not count the `sampler2D` uniform. This uniform is set separately with [`FragmentShader.setImageSampler`](https://api.flutter.dev/flutter/dart-ui/FragmentShader/setImageSampler.html), with the index starting over at 0.

Any float uniforms that are left uninitialized will default to `0.0`.

#### Current position

[#](#current-position)

The shader has access to a `varying` value that contains the local coordinates for the particular fragment being evaluated. Use this feature to compute effects that depend on the current position, which can be accessed by importing the `flutter/runtime_effect.glsl` library and calling the `FlutterFragCoord` function. For example:

glsl

```
#include <flutter/runtime_effect.glsl>

void main() {
  vec2 currentPos = FlutterFragCoord().xy;
}
```

The value returned from `FlutterFragCoord` is distinct from `gl_FragCoord`. `gl_FragCoord` provides the screen space coordinates and should generally be avoided to ensure that shaders are consistent across backends. When targeting a Skia backend, the calls to `gl_FragCoord` are rewritten to access local coordinates but this rewriting isn't possible with Impeller.

#### Colors

[#](#colors)

There isn't a built-in data type for colors. Instead they are commonly represented as a `vec4` with each component corresponding to one of the RGBA color channels.

The single output `fragColor` expects that the color value is normalized to be in the range of `0.0` to `1.0` and that it has premultiplied alpha. This is different than typical Flutter colors which use a `0-255` value encoding and have unpremultipled alpha.

#### Samplers

[#](#samplers)

A sampler provides access to a `dart:ui` `Image` object. This image can be acquired either from a decoded image or from part of the application using [`Scene.toImageSync`](https://api.flutter.dev/flutter/dart-ui/Scene/toImageSync.html) or [`Picture.toImageSync`](https://api.flutter.dev/flutter/dart-ui/Picture/toImageSync.html).

glsl

```
#include <flutter/runtime_effect.glsl>

uniform vec2 uSize;
uniform sampler2D uTexture;

out vec4 fragColor;

void main() {
  vec2 uv = FlutterFragCoord().xy / uSize;
  fragColor = texture(uTexture, uv);
}
```

By default, the image uses [`TileMode.clamp`](https://api.flutter.dev/flutter/dart-ui/TileMode.html) to determine how values outside of the range of `[0, 1]` behave. Customization of the tile mode is not supported and needs to be emulated in the shader.

### Performance considerations

[#](#performance-considerations)

When targeting the Skia backend, loading the shader might be expensive since it must be compiled to the appropriate platform-specific shader at runtime. If you intend to use one or more shaders during an animation, consider precaching the fragment program objects before starting the animation.

You can reuse a `FragmentShader` object across frames; this is more efficient than creating a new `FragmentShader` for each frame.

For a more detailed guide on writing performant shaders, check out [Writing efficient shaders](https://github.com/flutter/flutter/blob/main/engine/src/flutter/impeller/docs/shader_optimization.md) on GitHub.

### Other resources

[#](#other-resources)

For more information, here are a few resources.

* [The Book of Shaders](https://thebookofshaders.com/) by Patricio Gonzalez Vivo and Jen Lowe* [Shader toy](https://www.shadertoy.com/), a collaborative shader playground* [`simple_shader`](https://github.com/flutter/samples/tree/main/simple_shader), a simple Flutter fragment shaders sample project* [`flutter_shaders`](https://pub.dev/packages/flutter_shaders), a package that simplifies using fragment shaders in Flutter

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/graphics/fragment-shaders/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/graphics/fragment-shaders.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/graphics/fragment-shaders/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/graphics/fragment-shaders.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/ui/design/graphics/fragment-shaders.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/graphics/fragment-shaders/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/graphics/fragment-shaders.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   