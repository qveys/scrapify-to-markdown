Page transitions replaced by ZoomPageTransitionsBuilder
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Page transitions replaced by ZoomPageTransitionsBuilder](/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder)

Summary
-------

[#](#summary)

In order to ensure that libraries follow the latest OEM behavior, the default page transition builders now use `ZoomPageTransitionsBuilder` on all platforms (excluding iOS and macOS) instead of `FadeUpwardsPageTransitionsBuilder`.

Context
-------

[#](#context)

The `FadeUpwardsPageTransitionsBuilder` (provided with the first Flutter release), defined a page transition that's similar to the one provided by Android O. This page transitions builder will eventually be deprecated on Android, as per Flutter's [deprecation policy](/release/compatibility-policy#deprecation-policy).

`ZoomPageTransitionsBuilder`, the new page transition builder for Android, Linux, and Windows, defines a page transition that's similar to the one provided by Android Q and R.

According to the [Style guide for Flutter repo](https://github.com/flutter/flutter/blob/main/docs/contributing/Style-guide-for-Flutter-repo.md), the framework will follow the latest OEM behavior. Page transition builders using `FadeUpwardsPageTransitionsBuilder` are all switched to the `ZoomPageTransitionsBuilder`. When the current `TargetPlatform` doesn't have `PageTransitionsBuilder` defined in the `ThemeData.pageTransitionsTheme`, `ZoomPageTransitionsBuilder` is used as the default.

Description of change
---------------------

[#](#description-of-change)

`PageTransitionsBuilder`s defined in `PageTransitionsTheme._defaultBuilders` have changed from `FadeUpwardsPageTransitionsBuilder` to `ZoomPageTransitionsBuilder` for `TargetPlatform.android`, `TargetPlatform.linux` and `TargetPlatform.windows`.

Migration guide
---------------

[#](#migration-guide)

If you want to switch back to the previous page transition builder (`FadeUpwardsPageTransitionsBuilder`), you should define builders explicitly for the target platforms.

Code before migration:

dart

```
MaterialApp(
  theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple)),
)
```

Code after migration:

dart

```
MaterialApp(
  theme: ThemeData(
    pageTransitionsTheme: const PageTransitionsTheme(
      builders: <TargetPlatform, PageTransitionsBuilder>{
        TargetPlatform.android: FadeUpwardsPageTransitionsBuilder(), // Apply this to every platforms you need.
      },
    ),
  ),
)
```

If you want to apply the same page transition builder to all platforms:

dart

```
MaterialApp(
  theme: ThemeData(
    pageTransitionsTheme: PageTransitionsTheme(
      builders: Map<TargetPlatform, PageTransitionsBuilder>.fromIterable(
        TargetPlatform.values,
        value: (dynamic _) => const FadeUpwardsPageTransitionsBuilder(),
      ),
    ),
  ),
)
```

### Tests migration

[#](#tests-migration)

If you used to try to find widgets but failed with *Too many elements* using the new transition, and saw errors similar to the following:

```
══╡ EXCEPTION CAUGHT BY FLUTTER TEST FRAMEWORK ╞════════════════════════════════════════════════════
The following StateError was thrown running a test:
Bad state: Too many elements

When the exception was thrown, this was the stack:
#0      Iterable.single (dart:core/iterable.dart:656:24)
#1      WidgetController.widget (package:flutter_test/src/controller.dart:69:30)
#2      main.<anonymous closure> (file:///path/to/your/test.dart:1:2)
```

You should migrate your tests by using the `descendant` scope for `Finder`s with the specific widget type. Below is the example of `DataTable`'s test:

Test before migration:

dart

```
final Finder finder = find.widgetWithIcon(Transform, Icons.arrow_upward);
```

Test after migration:

dart

```
final Finder finder = find.descendant(
  of: find.byType(DataTable),
  matching: find.widgetWithIcon(Transform, Icons.arrow_upward),
);
```

Widgets that typically need to migrate the finder scope are: `Transform`, `FadeTransition`, `ScaleTransition`, and `ColoredBox`.

Timeline
--------

[#](#timeline)

Landed in version: 2.13.0-1.0.pre  
 In stable release: 3.0.0

References
----------

[#](#references)

API documentation:

* [`ZoomPageTransitionsBuilder`](https://api.flutter.dev/flutter/material/ZoomPageTransitionsBuilder-class.html)* [`FadeUpwardsPageTransitionsBuilder`](https://api.flutter.dev/flutter/material/FadeUpwardsPageTransitionsBuilder-class.html)* [`PageTransitionsTheme`](https://api.flutter.dev/flutter/material/PageTransitionsTheme-class.html)

Relevant issues:

* [Issue 43277](https://github.com/flutter/flutter/issues/43277)

Relevant PR:

* [PR 100812](https://github.com/flutter/flutter/pull/100812)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/page-transition-replaced-by-ZoomPageTransitionBuilder.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   