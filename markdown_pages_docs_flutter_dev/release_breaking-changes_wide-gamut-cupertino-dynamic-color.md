Migration guide for wide gamut CupertinoDynamicColor
====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for wide gamut CupertinoDynamicColor](/release/breaking-changes/wide-gamut-cupertino-dynamic-color)

Summary
-------

[#](#summary)

Certain properties and methods in [`CupertinoDynamicColor`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor-class.html) were deprecated to align with the [`Color`](https://api.flutter.dev/flutter/dart-ui/Color-class.html) class due to [wide gamut color spaces](https://en.wikipedia.org/wiki/RGB_color_spaces) support added in [Flutter 3.27](/release/breaking-changes/wide-gamut-framework).

Context
-------

[#](#context)

The `Color` class was updated to support wide gamut color spaces, but some corresponding deprecations were not initially applied to `CupertinoDynamicColor` due to its implementation rather than due to the extension of `Color`.

Description of change
---------------------

[#](#description-of-change)

1. The [`CupertinoDynamicColor.red`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/red.html) field is deprecated in favor of [`CupertinoDynamicColor.r`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/r.html).- The [`CupertinoDynamicColor.green`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/green.html) is deprecated in favor of [`CupertinoDynamicColor.g`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/g.html).- The [`CupertinoDynamicColor.blue`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/blue.html) is deprecated in favor of [`CupertinoDynamicColor.b`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/b.html).- The [`CupertinoDynamicColor.opacity`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/opacity.html) is deprecated in favor of [`CupertinoDynamicColor.a`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/a.html).- The [`CupertinoDynamicColor.withOpacity()`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/withOpacity.html) is deprecated in favor of [`CupertinoDynamicColor.withValues()`](https://api.flutter.dev/flutter/cupertino/CupertinoDynamicColor/withValues.html).

Migration guide
---------------

[#](#migration-guide)

### Access color components

[#](#access-color-components)

If your app accesses a single color component, consider taking advantage of the floating-point components. In the short term, you can scale the components themselves.

dart

```
int _floatToInt8(double x) {
  return (x * 255.0).round().clamp(0, 255);
}

const CupertinoDynamicColor color = CupertinoColors.systemBlue;
final intRed = _floatToInt8(color.r);
final intGreen = _floatToInt8(color.g);
final intBlue = _floatToInt8(color.b);
```

### Opacity

[#](#opacity)

Before Flutter 3.27, `Color` had the concept of "opacity", which showed up in the methods `opacity` and `withOpacity()`. Since Flutter 3.27, alpha is stored as a floating-point value. Using `.a` and `.withValues()` will give the full expression of a floating-point value and won't be quantized (restricted to a limited range). That means "alpha" expresses the intent of "opacity" more correctly.

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
final x = color.withOpacity(0.5);

// After: Create a new color with the specified alpha channel value,
// accounting for the current or specified color space.
final x = color.withValues(alpha: 0.5);
```

Timeline
--------

[#](#timeline)

Landed in version: Not yet  
 Stable release: Not yet

References
----------

[#](#references)

Relevant guides:

* [Migration guide for wide gamut Color](/release/breaking-changes/wide-gamut-framework)

Relevant issues:

* [Implement wide gamut color support in the Framework](https://github.com/flutter/flutter/issues/127855)* [CupertinoDynamicColor is missing deprecation notices](https://github.com/flutter/flutter/issues/171059)

Relevant PRs:

* [Add missing deprecations to CupertinoDynamicColor](https://github.com/flutter/flutter/pull/171160)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-cupertino-dynamic-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-cupertino-dynamic-color.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-cupertino-dynamic-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-cupertino-dynamic-color.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-cupertino-dynamic-color.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/wide-gamut-cupertino-dynamic-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/wide-gamut-cupertino-dynamic-color.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   