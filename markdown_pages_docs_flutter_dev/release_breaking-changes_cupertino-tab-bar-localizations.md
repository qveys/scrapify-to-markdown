CupertinoTabBar requires Localizations parent
=============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [CupertinoTabBar requires Localizations parent](/release/breaking-changes/cupertino-tab-bar-localizations)

Summary
-------

[#](#summary)

Instances of `CupertinoTabBar` must have a `Localizations`parent in order to provide a localized `Semantics` hint. Trying to instantiate a `CupertinoTabBar` without localizations results in an assertion such as the following:

```
CupertinoTabBar requires a Localizations parent in order to provide an appropriate Semantics hint
for tab indexing. A CupertinoApp provides the DefaultCupertinoLocalizations, or you can
instantiate your own Localizations.
'package:flutter/src/cupertino/bottom_tab_bar.dart':
Failed assertion: line 213 pos 7: 'localizations != null'
```

Context
-------

[#](#context)

To support localized semantics information, the `CupertinoTabBar` requires localizations.

Before this change, the `Semantics` hint provided to the `CupertinoTabBar` was a hard-coded String, 'tab, $index of $total'. The content of the semantics hint was also updated from this original String to 'Tab $index of $total' in English.

If your `CupertinoTabBar` is within the scope of a `CupertinoApp`, the `DefaultCupertinoLocalizations` is already instantiated and may suit your needs without having to make a change to your existing code.

If your `CupertinoTabBar` is not within a `CupertinoApp`, you may provide the localizations of your choosing using the `Localizations` widget.

Migration guide
---------------

[#](#migration-guide)

If you are seeing a `'localizations != null'` assertion error, make sure locale information is being provided to your `CupertinoTabBar`.

Code before migration:

dart

```
import 'package:flutter/cupertino.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MediaQuery(
      data: const MediaQueryData(),
      child: CupertinoTabBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.add_circled),
            label: 'Tab 1',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.add_circled_solid),
            label: 'Tab 2',
          ),
        ],
        currentIndex: 1,
      ),
    );
  }
}
```

Code after migration (Providing localizations via the `CupertinoApp`):

dart

```
import 'package:flutter/cupertino.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CupertinoApp(
      home: CupertinoTabBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.add_circled),
            label: 'Tab 1',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.add_circled_solid),
            label: 'Tab 2',
          ),
        ],
        currentIndex: 1,
      ),
    );
  }
}
```

Code after migration (Providing localizations by using the `Localizations` widget):

dart

```
import 'package:flutter/cupertino.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Localizations(
      locale: const Locale('en', 'US'),
      delegates: <LocalizationsDelegate<dynamic>>[
        DefaultWidgetsLocalizations.delegate,
        DefaultCupertinoLocalizations.delegate,
      ],
      child: MediaQuery(
        data: const MediaQueryData(),
        child: CupertinoTabBar(
          items: const <BottomNavigationBarItem>[
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.add_circled),
              label: 'Tab 1',
            ),
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.add_circled_solid),
              label: 'Tab 2',
            ),
          ],
          currentIndex: 1,
        ),
      ),
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.18.0-9.0.pre  
 In stable release: 1.20.0

References
----------

[#](#references)

API documentation:

* [`CupertinoTabBar`](https://api.flutter.dev/flutter/cupertino/CupertinoTabBar-class.html)* [`Localizations`](https://api.flutter.dev/flutter/widgets/Localizations-class.html)* [`DefaultCupertinoLocalizations`](https://api.flutter.dev/flutter/cupertino/DefaultCupertinoLocalizations-class.html)* [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html)* [`CupertinoApp`](https://api.flutter.dev/flutter/cupertino/CupertinoApp-class.html)* [Internationalizing Flutter Apps](/ui/accessibility-and-internationalization/internationalization)

Relevant PR:

* [PR 55336: Adding tabSemanticsLabel to CupertinoLocalizations](https://github.com/flutter/flutter/pull/55336)* [PR 56582: Update Tab semantics in Cupertino to be the same as Material](https://github.com/flutter/flutter/pull/56582#issuecomment-625497951)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-tab-bar-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-tab-bar-localizations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-tab-bar-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-tab-bar-localizations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-tab-bar-localizations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/cupertino-tab-bar-localizations/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/cupertino-tab-bar-localizations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   