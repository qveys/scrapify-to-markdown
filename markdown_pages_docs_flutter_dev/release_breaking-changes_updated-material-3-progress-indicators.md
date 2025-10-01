Updated Material 3 progress indicators
======================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Updated Material 3 progress indicators](/release/breaking-changes/updated-material-3-progress-indicators)

Summary
-------

[#](#summary)

The `LinearProgressIndicator` and `CircularProgressIndicator` have been updated to match the Material 3 Design specifications.

The `LinearProgressIndicator`changes include a gap between the active and inactive tracks, a stop indicator, and rounded corners. The `CircularProgressIndicator` changes include a gap between the active and inactive tracks, and rounded stroke cap.

Context
-------

[#](#context)

The Material 3 Design specifications for the `LinearProgressIndicator` and `CircularProgressIndicator` were updated in December 2023.

To opt into the 2024 design specifications, set the `LinearProgressIndicator.year2023` and `CircularProgressIndicator.year2023` flags to `false`. This is done to ensure that existing apps aren't affected by the updated design spec.

Description of change
---------------------

[#](#description-of-change)

The `LinearProgressIndicator` and `CircularProgressIndicator` widgets each have a `year2023` flag that can be set to `false` to opt in to the updated design specification. The default value for the `year2023` flag is `true`, which means that the progress indicators use the 2023 design spec.

When [`LinearProgressIndicator.year2023`](https://main-api.flutter.dev/flutter/material/LinearProgressIndicator/year2023.html) is set to `false`, the progress indicator have gaps between active and inactive tracks, a stop indicator, and rounded corners. If the `LinearProgressIndicator` is indeterminate, the stop indicator isn't shown.

When [`CircularProgressIndicator.year2023`](https://main-api.flutter.dev/flutter/material/CircularProgressIndicator/year2023.html) is set to `false`, the progress indicator has a track gap and rounded stroke cap.

Migration guide
---------------

[#](#migration-guide)

To opt into the updated design spec for the `LinearProgressIndicator`, set the `year2023` flag to `false`:

dart

```
LinearProgressIndicator(
  year2023: false,
  value: 0.5,
),
```

To update your entire app to use the updated `LinearProgressIndicator` design, set the `ProgressIndicatorThemeData.year2023` property to `false` in your `MaterialApp`:

dart

```
return MaterialApp(
  theme: ThemeData(progressIndicatorTheme: const ProgressIndicatorThemeData(year2023: false)),
        // ...
        LinearProgressIndicator(
          year2023: false,
          value: 0.5,
        ),
        // ...
```

To opt into the updated design spec for the `CircularProgressIndicator`, set the `year2023` flag to `false`:

dart

```
CircularProgressIndicator(
  year2023: false,
  value: 0.5,
),
```

To update your entire app to use the updated `CircularProgressIndicator` design, set the `ProgressIndicatorThemeData.year2023` property to `false` in your `MaterialApp`:

dart

```
return MaterialApp(
  theme: ThemeData(progressIndicatorTheme: const ProgressIndicatorThemeData(year2023: false)),
        // ...
        CircularProgressIndicator(
          year2023: false,
          value: 0.5,
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

* [`LinearProgressIndicator`](https://main-api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)* [`CircularProgressIndicator`](https://main-api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)* [`LinearProgressIndicator.year2023`](https://main-api.flutter.dev/flutter/material/LinearProgressIndicator/year2023.html)* [`CircularProgressIndicator.year2023`](https://main-api.flutter.dev/flutter/material/CircularProgressIndicator/year2023.html)

Relevant issues:

* [Update both `ProgressIndicator` for Material 3 redesign](https://github.com/flutter/flutter/issues/141340)

Relevant PRs:

* [Update Material 3 `LinearProgressIndicator` for new visual style](https://github.com/flutter/flutter/pull/154817)* [Update Material 3 `CircularProgressIndicator` for new visual style](https://github.com/flutter/flutter/pull/158104)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-progress-indicators/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-progress-indicators.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-progress-indicators/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-progress-indicators.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-26. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-progress-indicators.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/updated-material-3-progress-indicators/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/updated-material-3-progress-indicators.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   