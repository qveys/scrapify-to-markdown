Use lists
=========

1. [Cookbook](/cookbook) chevron\_right- [Lists](/cookbook/lists) chevron\_right- [Use lists](/cookbook/lists/basic-list)

Displaying lists of data is a fundamental pattern for mobile apps. Flutter includes the [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html) widget to make working with lists a breeze.

Create a ListView
-----------------

[#](#create-a-listview)

Using the standard `ListView` constructor is perfect for lists that contain only a few items. The built-in [`ListTile`](https://api.flutter.dev/flutter/material/ListTile-class.html) widget is a way to give items a visual structure.

dart

```
ListView(
  children: const <Widget>[
    ListTile(leading: Icon(Icons.map), title: Text('Map')),
    ListTile(leading: Icon(Icons.photo_album), title: Text('Album')),
    ListTile(leading: Icon(Icons.phone), title: Text('Phone')),
  ],
),
```

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Basic List';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: ListView(
          children: const <Widget>[
            ListTile(leading: Icon(Icons.map), title: Text('Map')),
            ListTile(leading: Icon(Icons.photo_album), title: Text('Album')),
            ListTile(leading: Icon(Icons.phone), title: Text('Phone')),
          ],
        ),
      ),
    );
  }
}
```

 ![Basic List Demo](/assets/images/docs/cookbook/basic-list.png)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/basic-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/basic-list.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/basic-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/basic-list.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/lists/basic-list.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/lists/basic-list/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/lists/basic-list.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    