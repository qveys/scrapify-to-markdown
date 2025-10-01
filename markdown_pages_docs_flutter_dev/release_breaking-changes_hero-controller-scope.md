More Strict Assertions in the Navigator and the Hero Controller Scope
=====================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [More Strict Assertions in the Navigator and the Hero Controller Scope](/release/breaking-changes/hero-controller-scope)

Summary
-------

[#](#summary)

The framework throws an assertion error when it detects there are multiple navigators registered with one hero controller scope.

Context
-------

[#](#context)

The hero controller scope hosts a hero controller for its widget subtree. The hero controller can only support one navigator at a time. Previously, there was no assertion to guarantee that.

Description of change
---------------------

[#](#description-of-change)

If the code starts throwing assertion errors after this change, it means the code was already broken even before this change. Multiple navigators may be registered under the same hero controller scope, and they can not trigger hero animations when their route changes. This change only surfaced this problem.

Migration guide
---------------

[#](#migration-guide)

An example application that starts to throw exceptions.

dart

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      builder: (BuildContext context, Widget child) {
        // Builds two parallel navigators. This throws
        // error because both of navigators are under the same
        // hero controller scope created by MaterialApp.
        return Stack(
          children: <Widget>[
            Navigator(
              onGenerateRoute: (RouteSettings settings) {
                return MaterialPageRoute<void>(
                  settings: settings,
                  builder: (BuildContext context) {
                    return const Text('first Navigator');
                  }
                );
              },
            ),
            Navigator(
              onGenerateRoute: (RouteSettings settings) {
                return MaterialPageRoute<void>(
                  settings: settings,
                  builder: (BuildContext context) {
                    return const Text('Second Navigator');
                  }
                );
              },
            ),
          ],
        );
      }
    )
  );
}
```

You can fix this application by introducing your own hero controller scopes.

dart

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      builder: (BuildContext context, Widget child) {
        // Builds two parallel navigators.
        return Stack(
          children: <Widget>[
            HeroControllerScope(
              controller: MaterialApp.createMaterialHeroController(),
              child: Navigator(
                onGenerateRoute: (RouteSettings settings) {
                  return MaterialPageRoute<void>(
                    settings: settings,
                    builder: (BuildContext context) {
                      return const Text('first Navigator');
                    }
                  );
                },
              ),
            ),
            HeroControllerScope(
              controller: MaterialApp.createMaterialHeroController(),
              child: Navigator(
                onGenerateRoute: (RouteSettings settings) {
                  return MaterialPageRoute<void>(
                    settings: settings,
                    builder: (BuildContext context) {
                      return const Text('second Navigator');
                    }
                  );
                },
              ),
            ),
          ],
        );
      }
    )
  );
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.20.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html)* [`HeroController`](https://api.flutter.dev/flutter/widgets/HeroController-class.html)* [`HeroControllerScope`](https://api.flutter.dev/flutter/widgets/HeroControllerScope-class.html)

Relevant issue:

* [Issue 45938](https://github.com/flutter/flutter/issues/45938)

Relevant PR:

* [Clean up hero controller scope](https://github.com/flutter/flutter/pull/60655)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/hero-controller-scope/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/hero-controller-scope.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/hero-controller-scope/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/hero-controller-scope.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/hero-controller-scope.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/hero-controller-scope/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/hero-controller-scope.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   