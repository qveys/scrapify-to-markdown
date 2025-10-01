Migration guide for wide gamut Color
====================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for wide gamut Color](/release/breaking-changes/wide-gamut-framework)

Summary
-------

[#](#summary)

The API for the [`Color`](https://api.flutter.dev/flutter/dart-ui/Color-class.html) class in `dart:ui` is changing to support [wide gamut color spaces](https://en.wikipedia.org/wiki/RGB_color_spaces).

Context
-------

[#](#context)

The Flutter engine [already supports wide gamut color](https://github.com/flutter/flutter/issues/55092) with [Impeller](https://api.flutter.dev/perf/impeller), and the support is now being added [to the framework](https://github.com/flutter/flutter/issues/127855).

The iOS devices that Flutter supports render to a larger array of colors, specifically in the [DisplayP3](https://en.wikipedia.org/wiki/DCI-P3) color space. After this change, the Flutter framework can render all of those colors on iOS Impeller, and the `Color` class is better prepared for future color spaces or changes to color component bit depth.

Description of change
---------------------

[#](#description-of-change)

Changes to [`Color`](https://api.flutter.dev/flutter/dart-ui/Color-class.html):

1. Adds an enum field that specifies its [`ColorSpace`](https://api.flutter.dev/flutter/dart-ui/ColorSpace.html).- Adds API to use normalized floating-point color components.- Removes API that uses 8-bit unsigned integer color components that can lead to data loss.

Changes to [`ColorSpace`](https://api.flutter.dev/flutter/dart-ui/ColorSpace.html):

1. Adds a `displayP3` property.

Migration guide
---------------

[#](#migration-guide)

### 8-bit unsigned integer constructors

[#](#8-bit-unsigned-integer-constructors)

Constructors like `Color.fromARGB` remain unchanged and have continued support. To take advantage of Display P3 colors, you must use the new `Color.from` constructor that takes normalized floating-point color components.

dart

```
// Before: Constructing an sRGB color from the lower 8 bits of four integers.
final magenta = Color.fromARGB(0xff, 0xff, 0x0, 0xff);

// After: Constructing a color with normalized floating-point components.
final magenta = Color.from(alpha: 1.0, red: 1.0, green: 0.0, blue: 1.0);
```

### Implementors of `Color`

[#](#implementors-of-color)

There are new methods being added to `Color` so any class that `implements Color` will break and have to implement the new methods, such as `Color.a` and `Color.b`.

Ultimately, implementors should migrate to take advantage of the new API. In the short-term, these methods can easily be implemented without changing the underlying structure of your class.

For example:

dart

```
class Foo implements Color {
  int _red;

  @override
  double get r => _red / 255.0;
}
```

*info* Note

Flutter plans to eventually lock the `Color` class down and make it `sealed`.

Now might be a good opportunity to switch from [inheritance to composition](https://en.wikipedia.org/wiki/Composition_over_inheritance) and stop reimplementing `Color`.

### Color space support

[#](#color-space-support)

Clients that use `Color` and perform any sort of calculation on the color components should now first check the color space component before performing calculations. To help with that, you can use the new `Color.withValues` method to perform color space conversions.

Example migration:

dart

```
// Before
double redRatio(Color x, Color y) => x.red / y.red;

// After
double redRatio(Color x, Color y) {
  final xPrime = x.withValues(colorSpace: ColorSpace.extendedSRGB);
  final yPrime = y.withValues(colorSpace: ColorSpace.extendedSRGB);
  return xPrime.r / yPrime.r;
}
```

Performing calculations with color components without aligning color spaces can lead to subtle unexpected results. In the preceding example, the `redRatio` would have the difference of `0.09` when calculated with differing color spaces versus aligned color spaces.

### Access color components

[#](#access-color-components)

If your app ever accesses a `Color` component, consider taking advantage of the floating-point components. In the short term, you can scale the components themselves.

dart

```
extension IntColorComponents on Color {
  int get intAlpha => _floatToInt8(this.a);
  int get intRed => _floatToInt8(this.r);
  int get intGreen => _floatToInt8(this.g);
  int get intBlue => _floatToInt8(this.b);

  int _floatToInt8(double x) {
    return (x * 255.0).round() & 0xff;
  }
}
```

### Opacity

[#](#opacity)

Before Flutter 3.27, Color had the concept of "opacity" which showed up in the methods `opacity` and `withOpacity()`. Opacity was introduced as a way to communicate with `Color` about its alpha channel with floating-point values ([0.0, 1.0]). Opacity methods were convenience methods for setting the 8-bit alpha value ([0, 255]), but never offered the full expression of a floating-point number. This was sufficient when color components were stored as 8-bit integers.

Since Flutter 3.27, alpha is stored as a floating-point value. Using `.a` and `.withValues()` will give the full expression of a floating-point value and won't be quantized (restricted to a limited range). That means "alpha" expresses the intent of "opacity" more correctly. Opacity is different in a subtle way where its usage can result in unexpected data loss, so `.withOpacity()` and `.opacity` have been deprecated and their semantics have been maintained to avoid breaking anyone.

For example:

dart

```
// Prints 0.5019607843137255.
print(Colors.black.withOpacity(0.5).a);
// Prints 0.5.
print(Colors.black.withValues(alpha: 0.5).a);
```

Practically all usage will directly benefit from the more accurate colors. In the rare case where it doesn't, care can be taken to quantize opacity to [0, 255] using `.alpha` and `.withAlpha()` to match the behavior before Flutter 3.27.

#### Migrate `opacity`

[#](#migrate-opacity)

dart

```
// Before: Access the alpha channel as a (converted) floating-point value.
final x = color.opacity;

// After: Access the alpha channel directly.
final x = color.a;
```

#### Migrate `withOpacity`

[#](#migrate-withopacity)

dart

```
// Before: Create a new color with the specified opacity.
final x = color.withOpacity(0.0);

// After: Create a new color with the specified alpha channel value,
// accounting for the current or specified color space.
final x = color.withValues(alpha: 0.0);
```

### Equality

[#](#equality)

Once `Color` stores its color components as floating-point numbers, equality works slightly differently. When calculating colors, there might be a tiny difference in values that could be considered equal. To accommodate this use the [`closeTo`](https://api.flutter.dev/documentation/matcher/latest/matcher/closeTo.html) or [`isColorSameAs`](https://api.flutter.dev/flutter/flutter_test/isSameColorAs.html) matchers.

dart

```
// Before: Check exact equality of int-based color.
expect(calculateColor(), const Color(0xffff00ff));

// After: Check rough equality of floating-point-based color.
expect(calculateColor(), isSameColorAs(const Color(0xffff00ff)));
```

Timeline
--------

[#](#timeline)

### Phase 1 - New API introduction, old API deprecation

[#](#phase-1-new-api-introduction-old-api-deprecation)

Landed in version: 3.26.0-0.1.pre  
 In stable release: 3.27.0

### Phase 2 - Old API removal

[#](#phase-2-old-api-removal)

Landed in version: Not yet  
 In stable release: Not yet

References
----------

[#](#references)

Relevant issue:

* [issue 127855](https://github.com/flutter/flutter/issues/127855): Implement wide gamut color support in the Framework

Relevant PRs:

* [PR 54737](https://github.com/flutter/engine/pull/54737): Framework wide color

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-framework/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-framework.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-framework/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-framework.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-10. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-framework.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-framework/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-framework.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   