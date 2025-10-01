Deprecate textScaleFactor in favor of TextScaler
================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecate textScaleFactor in favor of TextScaler](/release/breaking-changes/deprecate-textscalefactor)

Summary
-------

[#](#summary)

In preparation for adopting the [Android 14 nonlinear font scaling](https://developer.android.com/about/versions/14/features#non-linear-font-scaling) feature, all occurrences of `textScaleFactor` in the Flutter framework have been deprecated and replaced by `TextScaler`.

Context
-------

[#](#context)

Many platforms allow users to scale textual contents up or down globally in system preferences. In the past, the scaling strategy was captured as a single `double` value named `textScaleFactor`, as text scaling was proportional: `scaledFontSize = textScaleFactor x unScaledFontSize`. For example, when `textScaleFactor` is 2.0 and the developer-specified font size is 14.0, the actual font size is 2.0 x 14.0 = 28.0.

With the introduction of [Android 14 nonlinear font scaling](https://developer.android.com/about/versions/14/features#non-linear-font-scaling), larger text gets scaled at a lesser rate as compared to smaller text, to prevent excessive scaling of text that is already large. The `textScaleFactor` scalar value used by "proportional" scaling is not enough to represent this new scaling strategy. The [Replaces `textScaleFactor` with `TextScaler`](https://github.com/flutter/flutter/pull/128522) pull request introduced a new class `TextScaler` to replace `textScaleFactor` in preparation for this new feature. Nonlinear text scaling is introduced in a different pull request.

Description of change
---------------------

[#](#description-of-change)

Introducing a new interface `TextScaler`, which represents a text scaling strategy.

dart

```
abstract class TextScaler { 
  double scale(double fontSize);
  double get textScaleFactor; // Deprecated. 
}
```

Use the `scale` method to scale font sizes instead of `textScaleFactor`. The `textScaleFactor` getter provides an estimated `textScaleFactor` value, it is for backward compatibility purposes and is already marked as deprecated, and will be removed in a future version of Flutter.

The new class has replaced `double textScaleFactor` (`double textScaleFactor` -> `TextScaler textScaler`), in the following APIs:

### Painting library

[#](#painting-library)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Affected APIs Error Message|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `InlineSpan.build({ double textScaleFactor = 1.0 })` argument The named parameter 'textScaleFactor' isn't defined.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `TextStyle.getParagraphStyle({ double TextScaleFactor = 1.0 })` argument The named parameter 'textScaleFactor' isn't defined.|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `TextStyle.getTextStyle({ double TextScaleFactor = 1.0 })` argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `TextPainter({ double TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `TextPainter.textScaleFactor` getter and setter 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  | | --- | --- | --- | --- | | `TextPainter.computeWidth({ double TextScaleFactor = 1.0 })` argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  | | --- | --- | | `TextPainter.computeMaxIntrinsicWidth({ double TextScaleFactor = 1.0 })` argument 'textScaleFactor' is deprecated and shouldn't be used. | | | | | | | | | | | | | | | |

### Rendering library

[#](#rendering-library)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Affected APIs Error Message|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `RenderEditable({ double TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `RenderEditable.textScaleFactor` getter and setter 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  | | --- | --- | --- | --- | | `RenderParagraph({ double TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  | | --- | --- | | `RenderParagraph.textScaleFactor` getter and setter 'textScaleFactor' is deprecated and shouldn't be used. | | | | | | | | | |

### Widgets library

[#](#widgets-library)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Affected APIs Error Message|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MediaQueryData({ double TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MediaQueryData.textScaleFactor` getter 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MediaQueryData.copyWith({ double? TextScaleFactor })` argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MediaQuery.maybeTextScaleFactorOf(BuildContext context)` static method 'maybeTextScaleFactorOf' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `MediaQuery.textScaleFactorOf(BuildContext context)` static method 'textScaleFactorOf' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `RichText({ double TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `RichText.textScaleFactor` getter 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `Text({ double? TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `Text.rich({ double? TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `Text.textScaleFactor` getter 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  | | --- | --- | --- | --- | | `EditableText({ double? TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  | | --- | --- | | `EditableText.textScaleFactor` getter 'textScaleFactor' is deprecated and shouldn't be used. | | | | | | | | | | | | | | | | | | | | | | | | | |

### Material library

[#](#material-library)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Affected APIs Error Message|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `SelectableText({ double? TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  |  |  | | --- | --- | --- | --- | | `SelectableText.rich({ double? TextScaleFactor = 1.0 })` constructor argument 'textScaleFactor' is deprecated and shouldn't be used.|  |  | | --- | --- | | `SelectableText.textScaleFactor` getter 'textScaleFactor' is deprecated and shouldn't be used. | | | | | | | |

Migration guide
---------------

[#](#migration-guide)

Widgets provided by the Flutter framework are already migrated. Migration is needed only if you're using any of the deprecated symbols listed in the previous tables.

### Migrating your APIs that expose `textScaleFactor`

[#](#migrating-your-apis-that-expose-textscalefactor)

Before:

dart

```
abstract class _MyCustomPaintDelegate { 
  void paint(PaintingContext context, Offset offset, double textScaleFactor) { 
  }
}
```

After:

dart

```
abstract class _MyCustomPaintDelegate { 
  void paint(PaintingContext context, Offset offset, TextScaler textScaler) { 
  }
}
```

### Migrating code that consumes `textScaleFactor`

[#](#migrating-code-that-consumes-textscalefactor)

If you're not currently using `textScaleFactor` directly, but rather passing it to a different API that receives a `textScaleFactor`, and the receiver API has already been migrated, then it's relatively straightforward:

Before:

dart

```
RichText( 
  textScaleFactor: MediaQuery.textScaleFactorOf(context),
  ...
)
```

After:

dart

```
RichText( 
  textScaler: MediaQuery.textScalerOf(context),
  ...
)
```

If the API that provides `textScaleFactor` hasn't been migrated, consider waiting for the migrated version.

If you wish to compute the scaled font size yourself, use `TextScaler.scale` instead of the `*` binary operator:

Before:

dart

```
final scaledFontSize = textStyle.fontSize * MediaQuery.textScaleFactorOf(context);
```

After:

dart

```
final scaledFontSize = MediaQuery.textScalerOf(context).scale(textStyle.fontSize);
```

If you are using `textScaleFactor` to scale dimensions that are not font sizes, there are no generic rules for migrating the code to nonlinear scaling, and it might require the UI to be implemented differently. Reusing the `MyTooltipBox`example:

dart

```
MyTooltipBox( 
  size: chatBoxSize * textScaleFactor,
  child: RichText(..., style: TextStyle(fontSize: 20)),
)
```

You could choose to use the "effective" text scale factor by applying the `TextScaler` on the font size 20: `chatBoxSize * textScaler.scale(20) / 20`, or redesign the UI and let the widget assume its own intrinsic size.

### Overriding the text scaling strategy in a widget subtree

[#](#overriding-the-text-scaling-strategy-in-a-widget-subtree)

To override the existing `TextScaler` used in a widget subtree, override the `MediaQuery` like so:

Before:

dart

```
MediaQuery( 
  data: MediaQuery.of(context).copyWith(textScaleFactor: 2.0),
  child: child,
)
```

After:

dart

```
MediaQuery( 
  data: MediaQuery.of(context).copyWith(textScaler: _myCustomTextScaler),
  child: child,
)
```

However, it's rarely needed to create a custom `TextScaler` subclass. `MediaQuery.withNoTextScaling` (which creates a widget that disables text scaling altogether for its child subtree), and `MediaQuery.withClampedTextScaling` (which creates a widget that restricts the scaled font size to within the range `[minScaleFactor * fontSize, maxScaleFactor * fontSize]`), are convenience methods that cover common cases where the text scaling strategy needs to be overridden.

#### Examples

[#](#examples)

**Disabling Text Scaling For Icon Fonts**

Before:

dart

```
MediaQuery(
  data: MediaQuery.of(context).copyWith(textScaleFactor: 1.0),
  child: IconTheme(
    data: ..,
    child: icon,
  ),
)
```

After:

dart

```
MediaQuery.withNoTextScaling(
  child: IconTheme(
    data: ...
    child: icon,
  ),
)
```

**Preventing Contents From Overscaling**

Before:

dart

```
final mediaQueryData = MediaQuery.of(context);
MediaQuery(
  data: mediaQueryData.copyWith(textScaleFactor: math.min(mediaQueryData.textScaleFactor, _kMaxTitleTextScaleFactor),
  child: child,
)
```

After:

dart

```
MediaQuery.withClampedTextScaling(
  maxScaleFactor: _kMaxTitleTextScaleFactor,
  child: title,
)
```

**Disabling Nonlinear Text Scaling**

If you want to temporarily opt-out of nonlinear text scaling on Android 14 until your app is fully migrated, put a modified `MediaQuery` at the top of your app's widget tree:

dart

```
runApp(
  Builder(builder: (context) {
    final mediaQueryData = MediaQuery.of(context);
    final mediaQueryDataWithLinearTextScaling = mediaQueryData
      .copyWith(textScaler: TextScaler.linear(mediaQueryData.textScaler.textScaleFactor));
    return MediaQuery(data: mediaQueryDataWithLinearTextScaling, child: realWidgetTree);
  }),
);
```

This trick uses the deprecated `textScaleFactor` API and will stop working once it's removed from the Flutter API.

Timeline
--------

[#](#timeline)

Landed in version: 3.13.0-4.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`TextScaler`](https://api.flutter.dev/flutter/painting/TextScaler-class.html)* [`MediaQuery.textScalerOf`](https://api.flutter.dev/flutter/widgets/MediaQuery/textScalerOf.html)* [`MediaQuery.maybeTextScalerOf`](https://api.flutter.dev/flutter/widgets/MediaQuery/maybeTextScalerOf.html)* [`MediaQuery.withNoTextScaling`](https://api.flutter.dev/flutter/widgets/MediaQuery/withNoTextScaling.html)* [`MediaQuery.withClampedTextScaling`](https://api.flutter.dev/flutter/widgets/MediaQuery/withClampedTextScaling.html)

Relevant issues:

* [New font scaling system (Issue 116231)](https://github.com/flutter/flutter/issues/116231)

Relevant PRs:

* [Replaces `textScaleFactor` with `TextScaler`](https://github.com/flutter/flutter/pull/128522)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-textscalefactor.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-textscalefactor.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-textscalefactor.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deprecate-textscalefactor.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   