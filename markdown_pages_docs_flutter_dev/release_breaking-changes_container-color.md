Container with color optimization
=================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Container with color optimization](/release/breaking-changes/container-color)

Summary
-------

[#](#summary)

A new `ColoredBox` widget has been added to the framework, and the `Container` widget has been optimized to use it if a user specifies a `color` instead of a `decoration`.

Context
-------

[#](#context)

It is very common to use the `Container` widget as follows:

dart

```
return Container(color: Colors.red);
```

Previously, this code resulted in a widget hierarchy that used a `BoxDecoration` to actually paint the background color. The `BoxDecoration` widget covers many cases other than just painting a background color, and is not as efficient as the new `ColoredBox` widget, which only paints a background color.

Widget tests that wanted to assert based on the color of a container in the widget tree would previously have to find the `BoxDecoration` to actually get the color of the container. Now, they are able to check the `color` property on the `Container` itself, unless a `BoxDecoration` was explicitly provided as the `decoration` property. It is still an error to supply both `color` and `decoration` to `Container`.

Migration guide
---------------

[#](#migration-guide)

Tests that assert on the color of a `Container` or that expected it to create a `BoxDecoration` need to be modified.

Code before migration:

dart

```
testWidgets('Container color', (WidgetTester tester) async {
  await tester.pumpWidget(Container(color: Colors.red));

  final Container container = tester.widgetList<Container>().first;
  expect(container.decoration.color, Colors.red);
  // Or, a test may have specifically looked for the BoxDecoration, e.g.:
  expect(find.byType(BoxDecoration), findsOneWidget);
});
```

Code after migration:

dart

```
testWidgets('Container color', (WidgetTester tester) async {
  await tester.pumpWidget(Container(color: Colors.red));

  final Container container = tester.widgetList<Container>().first;
  expect(container.color, Colors.red);
  // If your test needed to work directly with the BoxDecoration, it should
  // instead look for the ColoredBox, e.g.:
  expect(find.byType(BoxDecoration), findsNothing);
  expect(find.byType(ColoredBox), findsOneWidget);
});
```

Timeline
--------

[#](#timeline)

Landed in version: 1.15.4  
 In stable release: 1.17

References
----------

[#](#references)

API documentation:

* [`Container`](https://api.flutter.dev/flutter/widgets/Container-class.html)* [`ColoredBox`](https://api.flutter.dev/flutter/widgets/ColoredBox-class.html)* [`BoxDecoration`](https://api.flutter.dev/flutter/painting/BoxDecoration-class.html)

Relevant issues:

* [Issue 9672](https://github.com/flutter/flutter/issues/9672)* [Issue 28753](https://github.com/flutter/flutter/issues/28753)

Relevant PR:

* [Colored box and container optimization #50979](https://github.com/flutter/flutter/pull/50979)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/container-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/container-color.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/container-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/container-color.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/container-color.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/container-color/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/container-color.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   