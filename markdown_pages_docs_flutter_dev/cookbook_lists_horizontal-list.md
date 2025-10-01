Create a horizontal list
========================

1. [Cookbook](/cookbook) chevron\_right- [Lists](/cookbook/lists) chevron\_right- [Create a horizontal list](/cookbook/lists/horizontal-list)

You might want to create a list that scrolls horizontally rather than vertically. The [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html) widget supports horizontal lists.

Use the standard `ListView` constructor, passing in a horizontal `scrollDirection`, which overrides the default vertical direction.

dart

```
ListView(
  // This next line does the trick.
  scrollDirection: Axis.horizontal,
  children: <Widget>[
    Container(width: 160, color: Colors.red),
    Container(width: 160, color: Colors.blue),
    Container(width: 160, color: Colors.green),
    Container(width: 160, color: Colors.yellow),
    Container(width: 160, color: Colors.orange),
  ],
),
```

Interactive example
-------------------

[#](#interactive-example)

*info* Desktop and web note

This example works in the browser and on the desktop. However, as this list scrolls on the horizontal axis (left to right or right to left), hold `Shift` while using the mouse scroll wheel to scroll the list.

To learn more, read the [breaking change](/release/breaking-changes/default-scroll-behavior-drag) page on the default drag for scrolling devices.

```
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Horizontal List';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: Container(
          margin: const EdgeInsets.symmetric(vertical: 20),
          height: 200,
          child: ListView(
            // This next line does the trick.
            scrollDirection: Axis.horizontal,
            children: <Widget>[
              Container(width: 160, color: Colors.red),
              Container(width: 160, color: Colors.blue),
              Container(width: 160, color: Colors.green),
              Container(width: 160, color: Colors.yellow),
              Container(width: 160, color: Colors.orange),
            ],
          ),
        ),
      ),
    );
  }
}
```

 ![Horizontal List Demo](/assets/images/docs/cookbook/horizontal-list.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/horizontal-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/horizontal-list.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/horizontal-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/horizontal-list.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/lists/horizontal-list.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/horizontal-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/horizontal-list.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    