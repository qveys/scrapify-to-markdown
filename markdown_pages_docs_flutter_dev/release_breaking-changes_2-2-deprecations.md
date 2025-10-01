Deprecated API removed after v2.2
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deprecated API removed after v2.2](/release/breaking-changes/2-2-deprecations)

Summary
-------

[#](#summary)

In accordance with Flutter's [Deprecation Policy](https://github.com/flutter/flutter/blob/main/docs/contributing/Tree-hygiene.md#deprecations), deprecated APIs that reached end of life after the 2.2 stable release have been removed.

All affected APIs have been compiled into this primary source to aid in migration. A [quick reference sheet](/go/deprecations-removed-after-2-2) is available as well.

Changes
-------

[#](#changes)

This section lists the deprecations, listed by the affected class.

### `hasFloatingPlaceholder` of `InputDecoration` & `InputDecorationTheme`

[#](#hasfloatingplaceholder-of-inputdecoration-inputdecorationtheme)

Supported by Flutter Fix: yes

`hasFloatingPlaceholder` was deprecated in v1.13.2. Use `floatingLabelBehavior` instead. Where `useFloatingPlaceholder` was true, replace with `FloatingLabelBehavior.auto`. Where `useFloatingPlaceholder` was false, replace with `FloatingLabelBehavior.never`. This change allows more behaviors to be specified beyond the original binary choice, adding `FloatingLabelBehavior.always` as an additional option.

**Migration guide**

Code before migration:

dart

```
// InputDecoration
// Base constructor
InputDecoration(hasFloatingPlaceholder: true);
InputDecoration(hasFloatingPlaceholder: false);

// collapsed constructor
InputDecoration.collapsed(hasFloatingPlaceholder: true);
InputDecoration.collapsed(hasFloatingPlaceholder: false);

// Field access
inputDecoration.hasFloatingPlaceholder;

// InputDecorationTheme
// Base constructor
InputDecorationTheme(hasFloatingPlaceholder: true);
InputDecorationTheme(hasFloatingPlaceholder: false);

// Field access
inputDecorationTheme.hasFloatingPlaceholder;

// copyWith
inputDecorationTheme.copyWith(hasFloatingPlaceholder: false);
inputDecorationTheme.copyWith(hasFloatingPlaceholder: true);
```

Code after migration:

dart

```
// InputDecoration
// Base constructor
InputDecoration(floatingLabelBehavior: FloatingLabelBehavior.auto);
InputDecoration(floatingLabelBehavior: FloatingLabelBehavior.never);

// collapsed constructor
InputDecoration.collapsed(floatingLabelBehavior: FloatingLabelBehavior.auto);
InputDecoration.collapsed(floatingLabelBehavior: FloatingLabelBehavior.never);

// Field access
inputDecoration.floatingLabelBehavior;

// InputDecorationTheme
// Base constructor
InputDecorationTheme(floatingLabelBehavior: FloatingLabelBehavior.auto);
InputDecorationTheme(floatingLabelBehavior: FloatingLabelBehavior.never);

// Field access
inputDecorationTheme.floatingLabelBehavior;

// copyWith
inputDecorationTheme.copyWith(floatingLabelBehavior: FloatingLabelBehavior.never);
inputDecorationTheme.copyWith(floatingLabelBehavior: FloatingLabelBehavior.auto);
```

**References**

API documentation:

* [`InputDecoration`](https://api.flutter.dev/flutter/material/InputDecoration-class.html)* [`InputDecorationTheme`](https://api.flutter.dev/flutter/material/InputDecorationTheme-class.html)* [`FloatingLabelBehavior`](https://api.flutter.dev/flutter/material/FloatingLabelBehavior-class.html)

Relevant issues:

* [InputDecoration: option to always float label](https://github.com/flutter/flutter/issues/30664)

Relevant PRs:

* Deprecated in [#46115](https://github.com/flutter/flutter/pull/46115)* Removed in [#83923](https://github.com/flutter/flutter/pull/83923)

---

### `TextTheme`

[#](#texttheme)

Supported by Flutter Fix: yes

Several `TextStyle` properties of `TextTheme` were deprecated in v1.13.8. They are listed in the following table alongside the appropriate replacement in the new API.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Deprecation New API|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | display4 headline1|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | display3 headline2|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | display2 headline3|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | display1 headline4|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | headline headline5|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | title headline6|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | subhead subtitle1|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | body2 bodyText1|  |  |  |  | | --- | --- | --- | --- | | body1 bodyText2|  |  | | --- | --- | | subtitle subtitle2 | | | | | | | | | | | | | | | | | | | | | |

**Migration guide**

Code before migration:

dart

```
// TextTheme
// Base constructor
TextTheme(
  display4: displayStyle4,
  display3: displayStyle3,
  display2: displayStyle2,
  display1: displayStyle1,
  headline: headlineStyle,
  title: titleStyle,
  subhead: subheadStyle,
  body2: body2Style,
  body1: body1Style,
  caption: captionStyle,
  button: buttonStyle,
  subtitle: subtitleStyle,
  overline: overlineStyle,
);

// copyWith
TextTheme.copyWith(
  display4: displayStyle4,
  display3: displayStyle3,
  display2: displayStyle2,
  display1: displayStyle1,
  headline: headlineStyle,
  title: titleStyle,
  subhead: subheadStyle,
  body2: body2Style,
  body1: body1Style,
  caption: captionStyle,
  button: buttonStyle,
  subtitle: subtitleStyle,
  overline: overlineStyle,
);

// Getters
TextStyle style;
style = textTheme.display4;
style = textTheme.display3;
style = textTheme.display2;
style = textTheme.display1;
style = textTheme.headline;
style = textTheme.title;
style = textTheme.subhead;
style = textTheme.body2;
style = textTheme.body1;
style = textTheme.caption;
style = textTheme.button;
style = textTheme.subtitle;
style = textTheme.overline;
```

Code after migration:

dart

```
// TextTheme
// Base constructor
TextTheme(
  headline1: displayStyle4,
  headline2: displayStyle3,
  headline3: displayStyle2,
  headline4: displayStyle1,
  headline5: headlineStyle,
  headline6: titleStyle,
  subtitle1: subheadStyle,
  bodyText1: body2Style,
  bodyText2: body1Style,
  caption: captionStyle,
  button: buttonStyle,
  subtitle2: subtitleStyle,
  overline: overlineStyle,
);

TextTheme.copyWith(
  headline1: displayStyle4,
  headline2: displayStyle3,
  headline3: displayStyle2,
  headline4: displayStyle1,
  headline5: headlineStyle,
  headline6: titleStyle,
  subtitle1: subheadStyle,
  bodyText1: body2Style,
  bodyText2: body1Style,
  caption: captionStyle,
  button: buttonStyle,
  subtitle2: subtitleStyle,
  overline: overlineStyle,
);

TextStyle style;
style = textTheme.headline1;
style = textTheme.headline2;
style = textTheme.headline3;
style = textTheme.headline4;
style = textTheme.headline5;
style = textTheme.headline6;
style = textTheme.subtitle1;
style = textTheme.bodyText1;
style = textTheme.bodyText2;
style = textTheme.caption;
style = textTheme.button;
style = textTheme.subtitle2;
style = textTheme.overline;
```

**References**

Design document:

* [Update the TextTheme API](/go/update-text-theme-api)

API documentation:

* [`TextTheme`](https://api.flutter.dev/flutter/material/TextTheme-class.html)

Relevant issues:

* [Migrate TextTheme to 2018 APIs](https://github.com/flutter/flutter/issues/45745)

Relevant PRs:

* Deprecated in [#48547](https://github.com/flutter/flutter/pull/48547)* Removed in [#83924](https://github.com/flutter/flutter/pull/83924)

---

### Default `Typography`

[#](#default-typography)

Supported by Flutter Fix: no

The default `Typography` was deprecated in v1.13.8. The prior default returned the text styles of the 2014 Material Design specification. This will now result in `TextStyle`s reflecting the 2018 Material Design specification. For the former, use the `material2014` constructor.

**Migration guide**

Code before migration:

dart

```
// Formerly returned 2014 TextStyle spec
Typography();
```

Code after migration:

dart

```
// Use 2018 TextStyle spec, either by default or explicitly.
Typography();
Typography.material2018();

// Use 2014 spec from former API
Typography.material2014();
```

**References**

Design document:

* [Update the TextTheme API](/go/update-text-theme-api)

API documentation:

* [`Typography`](https://api.flutter.dev/flutter/material/Typography-class.html)

Relevant issues:

* [Migrate TextTheme to 2018 APIs](https://github.com/flutter/flutter/issues/45745)

Relevant PRs:

* Deprecated in [#48547](https://github.com/flutter/flutter/pull/48547)* Removed in [#83924](https://github.com/flutter/flutter/pull/83924)

---

Timeline
--------

[#](#timeline)

In stable release: 2.5

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-2-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-2-deprecations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-2-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-2-deprecations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-01-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-2-deprecations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/2-2-deprecations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/2-2-deprecations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   