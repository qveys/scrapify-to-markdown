Flutter's fonts and typography
==============================

1. [UI](/ui) chevron\_right- [Design & theming](/ui/design) chevron\_right- [Text](/ui/design/text) chevron\_right- [Flutter's fonts and typography](/ui/design/text/typography)

[*Typography*](https://en.wikipedia.org/wiki/Typography) covers the style and appearance of type or fonts: it specifies how heavy the font is, the slant of the font, the spacing between the letters, and other visual aspects of the text.

All fonts are *not* created the same.

A font style is defined by, at minimum, a typeface, representing the set of common character rules describing fonts in the same type family, such as **Roboto** or **Noto**, a font weight (for example, Regular, Bold, or a numeric value), and a style (like Regular, *Italic*, etc). All of these and additional pre-set attributes come together to make up what we would call a static font.

Variable fonts allow some of these attributes to be modified at runtime and store what would normally be multiple static fonts in a single file.

Typographic Scale
-----------------

[#](#typographic-scale)

A typographical scale is a set of related text styles to provide balance, cohesion, and visual variety in your apps.

The common type scale in Flutter, provided by [`TextTheme`](https://api.flutter.dev/flutter/material/TextTheme-class.html), includes five categories of text indicating the function:

* Display* Headline* Title* Label* Body

There are also three size variations for each:

* Small* Medium* Large

Each of these fifteen combinations of a category and text size are represented by a single [`TextStyle`](https://api.flutter.dev/flutter/painting/TextStyle-class.html).

![Listing of typographical scale for Material TextTheme](/assets/images/docs/development/ui/typography/typographical-scale.png)

All the platform specific typographical scales that Flutter exposes are contained in the [`Typography`](https://api.flutter.dev/flutter/material/Typography-class.html) class. Usually, you will not need to reference this class directly as the `TextTheme` will be localized to your target platform.

Variable fonts
--------------

[#](#variable-fonts)

[Variable fonts](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts) allow you to control pre-defined aspects of text styling. Variable fonts support specific axes, such as width, weight, slant (to name a few). The user can select *any value along the continuous axis* when specifying the type.

### Using the Google Fonts type tester

[#](#using-the-google-fonts-type-tester)

A growing number of fonts on Google Fonts offer some variable font capabilities. You can see the range of options by using the Type Tester and see how you might vary a single font.

![Demonstration of varying aspects for Noto Sans with Lorem ipsum text](/assets/images/docs/development/ui/typography/google-fonts-type-tester.png)

In real time, move the slider on any of the axes to see how it affects the font. When programming a variable font, use the [`FontVariation`](https://api.flutter.dev/flutter/dart-ui/FontVariation-class.html) class to modify the font's design axes. The `FontVariation` class conforms to the [OpenType font variables spec](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview).

Static fonts
------------

[#](#static-fonts)

Google Fonts also contains static fonts. As with variable fonts, you need to know how the font is designed to know what options are available to you. Once again, the Google Fonts site can help.

### Using the Google Fonts package

[#](#using-the-google-fonts-package)

While you can download fonts from the site and install them manually in your apps, you can elect to use theme directly from the [google\_fonts](https://pub.dev/packages/google_fonts) package on [pub.dev](https://pub.dev).

They can be used as is by referencing simply the font name:

dart

```
Text(
  'This is Google Fonts',
  style: GoogleFonts.lato(),
),
```

or customized by setting properties on the resulting `TextStyle`:

dart

```
Text(
  'This is Google Fonts',
  style: GoogleFonts.lato(
    textStyle: Theme.of(context).textTheme.displayLarge,
    fontSize: 48,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
  ),
),
```

### Modifying fonts

[#](#modifying-fonts)

Use the following API to programmatically alter a static font (but remember that this only works if the font was *designed* to support the feature):

* [`FontFeature`](https://api.flutter.dev/flutter/dart-ui/FontFeature-class.html) to select glyphs* [`FontWeight`](https://api.flutter.dev/flutter/dart-ui/FontWeight-class.html) to modify weight* [`FontStyle`](https://api.flutter.dev/flutter/dart-ui/FontStyle.html) to italicize* [`FontVariation`](https://api.flutter.dev/flutter/dart-ui/FontVariation-class.html) to specify a range of values for a specific property.

A `FontFeature` corresponds to an [OpenType feature tag](https://learn.microsoft.com/en-us/typography/opentype/spec/featuretags) and can be thought of as a boolean flag to enable or disable a feature of a given font.

Other resources
---------------

[#](#other-resources)

The following video shows you some of the capabilities of Flutter's typography and combines it with the Material *and* Cupertino look and feel (depending on the platform the app runs on), animation, and custom fragment shaders:

[Watch on YouTube in a new tab: "Prototyping beautiful designs with Flutter"](https://www.youtube.com/watch/sA5MRFFUuOU)

To read one engineer's experience customizing variable fonts and animating them as they morph (and was the basis for the above video), check out [Playful typography with Flutter](https://blog.flutter.dev/playful-typography-with-flutter-f030385058b4), a free article on Medium. The associated example also uses a custom shader.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/text/typography/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/text/typography.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/text/typography/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/text/typography.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-31. [View source](https://github.com/flutter/website/tree/main/src/content/ui/design/text/typography.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/design/text/typography/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/design/text/typography.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   