Replace AnimationSheetBuilder.display with collate
==================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Replace AnimationSheetBuilder.display with collate](/release/breaking-changes/animation-sheet-builder-display)

Summary
-------

[#](#summary)

The `AnimationSheetBuilder.display` and `sheetSize` methods are deprecated, and should be replaced with `AnimationSheetBuilder.collate`.

Context
-------

[#](#context)

[`AnimationSheetBuilder`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder-class.html) is a testing utility class that records frames of an animating widget, and later composes the frames into a single animation sheet for [golden testing](https://api.flutter.dev/flutter/flutter_test/matchesGoldenFile.html). The old way of composing involves `display` to list the images into a table-like widget, adjusting the testing surface with `sheetSize`, and capturing the table widget for comparison. A new way, `collate`, has been added that directly puts the frames together into an image for comparison, which requires less boilerplate code and outputs a smaller image without compromise in quality. APIs for the old way are thus deprecated.

The reason why `collate` outputs a smaller image, is because the old way captures on a testing surface with pixel ratio 3.0, which means it uses a 3x3 pixel block of the exactly same color to represent 1 actual pixel, making the image 9 times as large as necessary (before PNG compression).

Description of change
---------------------

[#](#description-of-change)

The following changes have been made to the [`AnimationSheetBuilder`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder-class.html) class:

* 'display' is deprecated and shouldn't be used* 'sheetSize' is deprecated and shouldn't be used

Migration guide
---------------

[#](#migration-guide)

To migrate to the new API, change the process of setting surface size and displaying the widget into [`AnimationSheetBuilder.collate`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder/collate.html).

### Derive cells per row

[#](#derive-cells-per-row)

The `collate` requires an explicit `cellsPerRow` argument, which is the number of frames per row in the output image. It can be manually counted, or calculated as follows:

* Find the width of frame, specified when constructing `AnimationSheetBuilder`. For example, in the following snippet it's 80:

dart

```
final AnimationSheetBuilder animationSheet = AnimationSheetBuilder(frameSize: const Size(80, 30));
```

* Find the width of surface size, specified when setting the surface size; the default is 800. For example, in the following snippet it's 600:

dart

```
tester.binding.setSurfaceSize(animationSheet.sheetSize(600));
```

* The frames per row should be the result of the two numbers divided, rounded down. For example, 600 / 80 = 7 (rounded down), therefore

dart

```
animationSheet.collate(7)
```

### Migrate code

[#](#migrate-code)

Code before migration:

dart

```
  testWidgets('Indeterminate CircularProgressIndicator', (WidgetTester tester) async {
    final AnimationSheetBuilder animationSheet = AnimationSheetBuilder(frameSize: const Size(40, 40));

    await tester.pumpFrames(animationSheet.record(
      const Directionality(
        textDirection: TextDirection.ltr,
        child: Padding(
          padding: EdgeInsets.all(4),
          child: CircularProgressIndicator(),
        ),
      ),
    ), const Duration(seconds: 2));

    // The code starting here needs migration.

    tester.binding.setSurfaceSize(animationSheet.sheetSize());

    final Widget display = await animationSheet.display();
    await tester.pumpWidget(display);

    await expectLater(
      find.byWidget(display),
      matchesGoldenFile('material.circular_progress_indicator.indeterminate.png'),
    );
  }, skip: isBrowser); // https://github.com/flutter/flutter/issues/42767
```

Code after migration (`cellsPerRow` is 20, derived from 800 / 40):

dart

```
  testWidgets('Indeterminate CircularProgressIndicator', (WidgetTester tester) async {
    final AnimationSheetBuilder animationSheet = AnimationSheetBuilder(frameSize: const Size(40, 40));

    await tester.pumpFrames(animationSheet.record(
      const Directionality(
        textDirection: TextDirection.ltr,
        child: Padding(
          padding: EdgeInsets.all(4),
          child: CircularProgressIndicator(),
        ),
      ),
    ), const Duration(seconds: 2));

    await expectLater(
      animationSheet.collate(20),
      matchesGoldenFile('material.circular_progress_indicator.indeterminate.png'),
    );
  }, skip: isBrowser); // https://github.com/flutter/flutter/issues/42767
```

It's expected that related golden test reference images are invalidated, which should all be updated. The new images should be identical to the old ones except 1/3 in scale.

Timeline
--------

[#](#timeline)

Landed in version: v2.3.0-13.0.pre  
 In stable release: 2.5

References
----------

[#](#references)

API documentation:

* [`AnimationSheetBuilder`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder-class.html)* [`AnimationSheetBuilder.collate`](https://api.flutter.dev/flutter/flutter_test/AnimationSheetBuilder/collate.html)

Relevant PR:

* [Test WidgetTester handling test pointers](https://github.com/flutter/flutter/pull/83337)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/animation-sheet-builder-display/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/animation-sheet-builder-display.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/animation-sheet-builder-display/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/animation-sheet-builder-display.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-06-01. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/animation-sheet-builder-display.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/animation-sheet-builder-display/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/animation-sheet-builder-display.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   