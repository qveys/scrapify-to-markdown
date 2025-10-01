TextField requires a MaterialLocalizations widget
=================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [TextField requires a MaterialLocalizations widget](/release/breaking-changes/text-field-material-localizations)

Summary
-------

[#](#summary)

Instances of `TextField` must have a `MaterialLocalizations` present in the widget tree. Trying to instantiate a `TextField` without the proper localizations results in an assertion such as the following:

```
No MaterialLocalizations found.
TextField widgets require MaterialLocalizations to be provided by a Localizations widget ancestor.
The material library uses Localizations to generate messages, labels, and abbreviations.
To introduce a MaterialLocalizations, either use a MaterialApp at the root of your application to
include them automatically, or add a Localization widget with a MaterialLocalizations delegate.
The specific widget that could not find a MaterialLocalizations ancestor was:
  TextField
```

Context
-------

[#](#context)

If the `TextField` descends from a `MaterialApp`, the `DefaultMaterialLocalizations` is already instantiated and won't require any changes to your existing code.

If the `TextField` doesn't descend from `MaterialApp`, you can use a `Localizations` widget to provide your own localizations.

Migration guide
---------------

[#](#migration-guide)

If you see an assertion error, make sure that locale information is available to the `TextField`, either through an ancestor `MaterialApp` (that automatically provides `Localizations`), or by creating your own `Localizations` widget.

Code before migration:

dart

```
import 'package:flutter/material.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MediaQuery(
      data: const MediaQueryData(),
      child: Directionality(
        textDirection: TextDirection.ltr,
        child: Material(
          child: TextField(),
        ),
      ),
    );
  }
}
```

Code after migration (Providing localizations using the `MaterialApp`):

dart

```
import 'package:flutter/material.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Material(
        child: TextField(),
      ),
    );
  }
}
```

Code after migration (Providing localizations via the `Localizations` widget):

dart

```
import 'package:flutter/material.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Localizations(
      locale: const Locale('en', 'US'),
      delegates: const <LocalizationsDelegate<dynamic>>[
        DefaultWidgetsLocalizations.delegate,
        DefaultMaterialLocalizations.delegate,
      ],
      child: MediaQuery(
        data: const MediaQueryData(),
        child: Directionality(
          textDirection: TextDirection.ltr,
          child: Material(
            child: TextField(),
          ),
        ),
      ),
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.20.0-1.0.pre  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html)* [`Localizations`](https://api.flutter.dev/flutter/widgets/Localizations-class.html)* [`MaterialLocalizations`](https://api.flutter.dev/flutter/material/MaterialLocalizations-class.html)* [`DefaultMaterialLocalizations`](https://api.flutter.dev/flutter/material/DefaultMaterialLocalizations-class.html)* [`MaterialApp`](https://api.flutter.dev/flutter/material/MaterialApp-class.html)* [Internationalizing Flutter apps](/ui/accessibility-and-internationalization/internationalization)

Relevant PR:

* [PR 58831: Assert debugCheckHasMaterialLocalizations on TextField](https://github.com/flutter/flutter/pull/58831)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-field-material-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-field-material-localizations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-field-material-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-field-material-localizations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-field-material-localizations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/text-field-material-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/text-field-material-localizations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   