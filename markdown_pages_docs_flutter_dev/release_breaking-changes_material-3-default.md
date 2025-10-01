The ThemeData.useMaterial3 flag is true by default
==================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [The ThemeData.useMaterial3 flag is true by default](/release/breaking-changes/material-3-default)

Summary
-------

[#](#summary)

The Material library has been updated to match the latest Material Design spec. Changes include new components, new component themes, and updated component visuals. As of this release, [`ThemeData.useMaterial3`](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html) is set `true` by default.

Background
----------

[#](#background)

Flutter's Material widgets now fully support Material 3 and, as of Flutter 3.16, Material 3 is now the default style.

The appearance of Material 3 components are primarily determined by the values for [`ThemeData.colorScheme`](https://api.flutter.dev/flutter/material/ThemeData/colorScheme.html) and [`ThemeData.textTheme`](https://api.flutter.dev/flutter/material/ThemeData/textTheme.html). ColorScheme makes it easier to create dark and light schemes so that your app is both aesthetically pleasing and compliant with accessibility requirements. To further customize the appearance of Material 3 components, add component themes to your `ThemeData`, such as [`ThemeData.segmentedButtonTheme`](https://api.flutter.dev/flutter/material/ThemeData/segmentedButtonTheme.html) or [`ThemeData.snackBarTheme`](https://api.flutter.dev/flutter/material/ThemeData/snackBarTheme.html).

Additionally, Material 3 improves motion by using easing and duration tokens. This means that Material 2 curves have been renamed to include the word "legacy" and will eventually be deprecated and removed.

Check out the [Material 3 gallery](https://github.com/flutter/samples/tree/main/material_3_demo) to test out all the new components and compare them with Material 2.

Migration guide
---------------

[#](#migration-guide)

Prior to the 3.16 release, the changes were "opt-in" using the `useMaterial3` theme property on `ThemeData`. As of this release, `useMaterial3` is `true` by default. You can still opt out of the Material 3 version of the Material library by specifying `useMaterial3: false` in your `MaterialApp` theme.

*info* Note

Support for Material 2 and configuring the `useMaterial3` property will eventually be deprecated and removed.

Also, some of the widgets couldn't merely be updated, but needed a whole new implementation. For this reason, your UI might look a little strange when you see it running with Material 3. To fix this, manually migrate to the new widgets, such as [`NavigationBar`](https://api.flutter.dev/flutter/material/NavigationBar-class.html).

For more details, check out the [Material 3 umbrella issue](https://github.com/flutter/flutter/issues/91605) on GitHub.

Timeline
--------

[#](#timeline)

Landed in version: 3.13.0-4.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

Documentation:

* [Material Design for Flutter](/ui/design/material)

API documentation:

* [`ThemeData.useMaterial3`](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html)

Relevant issues:

* [Material 3 umbrella issue](https://github.com/flutter/flutter/issues/91605)* [Add support for M3 motion](https://github.com/flutter/flutter/issues/129942)

Relevant PRs:

* [Change the default for `ThemeData.useMaterial3` to true](https://github.com/flutter/flutter/pull/129724)* [Updated `ThemeData.useMaterial3` API doc, default is true](https://github.com/flutter/flutter/pull/130764)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-3-default/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-3-default.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-3-default/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-3-default.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-10. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-3-default.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-3-default/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-3-default.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   