Find widgets
============

1. [Cookbook](/cookbook) chevron\_right- [Testing](/cookbook/testing) chevron\_right- [Widget](/cookbook/testing/widget) chevron\_right- [Find widgets](/cookbook/testing/widget/finders)

To locate widgets in a test environment, use the [`Finder`](https://api.flutter.dev/flutter/flutter_test/Finder-class.html) classes. While it's possible to write your own `Finder` classes, it's generally more convenient to locate widgets using the tools provided by the [`flutter_test`](https://api.flutter.dev/flutter/flutter_test/flutter_test-library.html) package.

During a `flutter run` session on a widget test, you can also interactively tap parts of the screen for the Flutter tool to print the suggested `Finder`.

This recipe looks at the [`find`](https://api.flutter.dev/flutter/flutter_test/find-constant.html) constant provided by the `flutter_test` package, and demonstrates how to work with some of the `Finders` it provides. For a full list of available finders, see the [`CommonFinders` documentation](https://api.flutter.dev/flutter/flutter_test/CommonFinders-class.html).

If you're unfamiliar with widget testing and the role of `Finder` classes, review the [Introduction to widget testing](/cookbook/testing/widget/introduction) recipe.

This recipe uses the following steps:

1. Find a `Text` widget.- Find a widget with a specific `Key`.- Find a specific widget instance.

1. Find a `Text` widget
-----------------------

[#](#1-find-a-text-widget)

In testing, you often need to find widgets that contain specific text. This is exactly what the `find.text()` method is for. It creates a `Finder` that searches for widgets that display a specific `String` of text.

dart

```
testWidgets('finds a Text widget', (tester) async {
  // Build an App with a Text widget that displays the letter 'H'.
  await tester.pumpWidget(const MaterialApp(home: Scaffold(body: Text('H'))));

  // Find a widget that displays the letter 'H'.
  expect(find.text('H'), findsOneWidget);
});
```

2. Find a widget with a specific `Key`
--------------------------------------

[#](#2-find-a-widget-with-a-specific-key)

In some cases, you might want to find a widget based on the Key that has been provided to it. This can be handy if displaying multiple instances of the same widget. For example, a `ListView` might display several `Text` widgets that contain the same text.

In this case, provide a `Key` to each widget in the list. This allows an app to uniquely identify a specific widget, making it easier to find the widget in the test environment.

dart

```
testWidgets('finds a widget using a Key', (tester) async {
  // Define the test key.
  const testKey = Key('K');

  // Build a MaterialApp with the testKey.
  await tester.pumpWidget(MaterialApp(key: testKey, home: Container()));

  // Find the MaterialApp widget using the testKey.
  expect(find.byKey(testKey), findsOneWidget);
});
```

3. Find a specific widget instance
----------------------------------

[#](#3-find-a-specific-widget-instance)

Finally, you might be interested in locating a specific instance of a widget. For example, this can be useful when creating widgets that take a `child` property and you want to ensure you're rendering the `child` widget.

dart

```
testWidgets('finds a specific instance', (tester) async {
  const childWidget = Padding(padding: EdgeInsets.zero);

  // Provide the childWidget to the Container.
  await tester.pumpWidget(Container(child: childWidget));

  // Search for the childWidget in the tree and verify it exists.
  expect(find.byWidget(childWidget), findsOneWidget);
});
```

Summary
-------

[#](#summary)

The `find` constant provided by the `flutter_test` package provides several ways to locate widgets in the test environment. This recipe demonstrated three of these methods, and several more methods exist for different purposes.

If the above examples do not work for a particular use-case, see the [`CommonFinders` documentation](https://api.flutter.dev/flutter/flutter_test/CommonFinders-class.html) to review all available methods.

Complete example
----------------

[#](#complete-example)

dart

```
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('finds a Text widget', (tester) async {
    // Build an App with a Text widget that displays the letter 'H'.
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: Text('H'))));

    // Find a widget that displays the letter 'H'.
    expect(find.text('H'), findsOneWidget);
  });

  testWidgets('finds a widget using a Key', (tester) async {
    // Define the test key.
    const testKey = Key('K');

    // Build a MaterialApp with the testKey.
    await tester.pumpWidget(MaterialApp(key: testKey, home: Container()));

    // Find the MaterialApp widget using the testKey.
    expect(find.byKey(testKey), findsOneWidget);
  });

  testWidgets('finds a specific instance', (tester) async {
    const childWidget = Padding(padding: EdgeInsets.zero);

    // Provide the childWidget to the Container.
    await tester.pumpWidget(Container(child: childWidget));

    // Search for the childWidget in the tree and verify it exists.
    expect(find.byWidget(childWidget), findsOneWidget);
  });
}
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/widget/finders/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/widget/finders.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/widget/finders/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/widget/finders.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-22. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/testing/widget/finders.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/widget/finders/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/widget/finders.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   