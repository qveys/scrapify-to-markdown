Updated Material 3 `Slider`
===========================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Updated Material 3 `Slider`](/release/breaking-changes/updated-material-3-slider)

Summary
-------

[#](#summary)

The `Slider` has been updated to match the Material 3 Design specifications.

The `Slider` changes include an updated height, a gap between the active and inactive track, and a stop indicator to show the end value of the inactive track. Pressing the thumb adjusts its width, and the track adjusts its shape. The new value indicator shape is a rounded rectangle. New color mappings have also been introduced for some of the `Slider` shapes.

Context
-------

[#](#context)

The Material 3 Design specs for the `Slider` were updated in December 2023. To opt into the 2024 design spec, set the `Slider.year2023` flag to `false`. This is done to ensure that existing apps aren't affected by the updated design specifications.

Description of change
---------------------

[#](#description-of-change)

The `Slider` widget has a `year2023` flag that can be set to `false` to opt in to the updated design spec. The default value for the `year2023` flag is `true`, which means that the `Slider` uses the previous 2023 design specifications.

When [`Slider.year2023`](https://main-api.flutter.dev/flutter/material/Slider/year2023.html) is set to `false`, the slider uses the updated design specifications.

Migration guide
---------------

[#](#migration-guide)

To opt into the updated design spec for the `Slider`, set the `year2023` flag to `false`:

dart

```
Slider(
  year2023: false,
  value: _value,
  onChanged: (value) {
    setState(() {
      _value = value;
    });
  },
),
```

To update your entire app to use the updated `Slider` design, set the `SliderThemeData.year2023` property to `false` in your `MaterialApp`:

dart

```
return MaterialApp(
  theme: ThemeData(sliderTheme: const SliderThemeData(year2023: false)),
        // ...
        Slider(
          value: _value,
          onChanged: (value) {
            setState(() {
              _value = value;
            });
          },
        ),
        // ...
```

Timeline
--------

[#](#timeline)

Landed in version: 3.28.0-0.1.pre  
 In stable release: 3.29

References
----------

[#](#references)

API documentation:

* [`Slider`](https://main-api.flutter.dev/flutter/material/Slider-class.html)* [`Slider.year2023`](https://main-api.flutter.dev/flutter/material/Slider/year2023.html)

Relevant issues:

* [Update `Slider` for Material 3 redesign](https://github.com/flutter/flutter/issues/141842)

Relevant PRs:

* [Introduce new Material 3 `Slider` shapes](https://github.com/flutter/flutter/pull/152237)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-slider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-slider.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-slider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-slider.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-26. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-slider.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-slider/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-slider.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   