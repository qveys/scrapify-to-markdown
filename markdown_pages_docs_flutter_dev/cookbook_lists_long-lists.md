Work with long lists
====================

1. [Cookbook](/cookbook) chevron\_right- [Lists](/cookbook/lists) chevron\_right- [Work with long lists](/cookbook/lists/long-lists)

The standard [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html) constructor works well for small lists. To work with lists that contain a large number of items, it's best to use the [`ListView.builder`](https://api.flutter.dev/flutter/widgets/ListView/ListView.builder.html) constructor.

In contrast to the default `ListView` constructor, which requires creating all items at once, the `ListView.builder()` constructor creates items as they're scrolled onto the screen.

1. Create a data source
-----------------------

[#](#1-create-a-data-source)

First, you need a data source. For example, your data source might be a list of messages, search results, or products in a store. Most of the time, this data comes from the internet or a database.

For this example, generate a list of 10,000 Strings using the [`List.generate`](https://api.flutter.dev/flutter/dart-core/List/List.generate.html) constructor.

dart

```
List<String>.generate(10000, (i) => 'Item $i'),
```

2. Convert the data source into widgets
---------------------------------------

[#](#2-convert-the-data-source-into-widgets)

To display the list of strings, render each String as a widget using `ListView.builder()`. In this example, display each String on its own line.

dart

```
ListView.builder(
  itemCount: items.length,
  prototypeItem: ListTile(title: Text(items.first)),
  itemBuilder: (context, index) {
    return ListTile(title: Text(items[index]));
  },
)
```

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MyApp(
      items: List<String>.generate(10000, (i) => 'Item $i'),
    ),
  );
}

class MyApp extends StatelessWidget {
  final List<String> items;

  const MyApp({super.key, required this.items});

  @override
  Widget build(BuildContext context) {
    const title = 'Long List';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: ListView.builder(
          itemCount: items.length,
          prototypeItem: ListTile(title: Text(items.first)),
          itemBuilder: (context, index) {
            return ListTile(title: Text(items[index]));
          },
        ),
      ),
    );
  }
}
```

Children's extent
-----------------

[#](#childrens-extent)

To specify each item's extent, you can use either [`prototypeItem`](https://api.flutter.dev/flutter/widgets/ListView/prototypeItem.html), [`itemExtent`](https://api.flutter.dev/flutter/widgets/ListView/itemExtent.html), or [`itemExtentBuilder`](https://api.flutter.dev/flutter/widgets/ListView/itemExtentBuilder.html).

Specifying either is more efficient than letting the children determine their own extent because the scrolling machinery can make use of the foreknowledge of the children's extent to save work, for example when the scroll position changes drastically.

Use [`prototypeItem`](https://api.flutter.dev/flutter/widgets/ListView/prototypeItem.html) or [`itemExtent`](https://api.flutter.dev/flutter/widgets/ListView/itemExtent.html) if your list has items of fixed size.

Use [`itemExtentBuilder`](https://api.flutter.dev/flutter/widgets/ListView/itemExtentBuilder.html) if your list has items of different sizes.

 ![Long Lists Demo](/assets/images/docs/cookbook/long-lists.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/long-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/long-lists.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/long-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/long-lists.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/lists/long-lists.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/long-lists/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/long-lists.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    