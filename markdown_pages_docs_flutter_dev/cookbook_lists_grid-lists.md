Create a grid list
==================

1. [Cookbook](/cookbook) chevron\_right- [Lists](/cookbook/lists) chevron\_right- [Create a grid list](/cookbook/lists/grid-lists)

In some cases, you might want to display your items as a grid rather than a normal list of items that come one after the next. For this task, use the [`GridView`](https://api.flutter.dev/flutter/widgets/GridView-class.html) widget.

The simplest way to get started using grids is by using the [`GridView.count()`](https://api.flutter.dev/flutter/widgets/GridView/GridView.count.html) constructor, because it allows you to specify how many rows or columns you'd like.

To visualize how `GridView` works, generate a list of 100 widgets that display their index in the list.

dart

```
GridView.count(
  // Create a grid with 2 columns.
  // If you change the scrollDirection to horizontal,
  // this produces 2 rows.
  crossAxisCount: 2,
  // Generate 100 widgets that display their index in the list.
  children: List.generate(100, (index) {
    return Center(
      child: Text(
        'Item $index',
        style: TextTheme.of(context).headlineSmall,
      ),
    );
  }),
),
```

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Grid List';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: GridView.count(
          // Create a grid with 2 columns.
          // If you change the scrollDirection to horizontal,
          // this produces 2 rows.
          crossAxisCount: 2,
          // Generate 100 widgets that display their index in the list.
          children: List.generate(100, (index) {
            return Center(
              child: Text(
                'Item $index',
                style: TextTheme.of(context).headlineSmall,
              ),
            );
          }),
        ),
      ),
    );
  }
}
```

 ![Grid List Demo](/assets/images/docs/cookbook/grid-list.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/grid-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/grid-lists.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/grid-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/grid-lists.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/lists/grid-lists.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/grid-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/grid-lists.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    