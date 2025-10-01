Work with tabs
==============

1. [Cookbook](/cookbook) chevron\_right- [Design](/cookbook/design) chevron\_right- [Work with tabs](/cookbook/design/tabs)

Working with tabs is a common pattern in apps that follow the Material Design guidelines. Flutter includes a convenient way to create tab layouts as part of the [material library](https://api.flutter.dev/flutter/material/material-library.html).

This recipe creates a tabbed example using the following steps;

1. Create a `TabController`.- Create the tabs.- Create content for each tab.

1. Create a `TabController`
---------------------------

[#](#1-create-a-tabcontroller)

For tabs to work, you need to keep the selected tab and content sections in sync. This is the job of the [`TabController`](https://api.flutter.dev/flutter/material/TabController-class.html).

Either create a `TabController` manually, or automatically by using a [`DefaultTabController`](https://api.flutter.dev/flutter/material/DefaultTabController-class.html) widget.

Using `DefaultTabController` is the simplest option, since it creates a `TabController` and makes it available to all descendant widgets.

dart

```
return MaterialApp(
  home: DefaultTabController(length: 3, child: Scaffold()),
);
```

2. Create the tabs
------------------

[#](#2-create-the-tabs)

When a tab is selected, it needs to display content. You can create tabs using the [`TabBar`](https://api.flutter.dev/flutter/material/TabBar-class.html) widget. In this example, create a `TabBar` with three [`Tab`](https://api.flutter.dev/flutter/material/Tab-class.html) widgets and place it within an [`AppBar`](https://api.flutter.dev/flutter/material/AppBar-class.html).

dart

```
return MaterialApp(
  home: DefaultTabController(
    length: 3,
    child: Scaffold(
      appBar: AppBar(
        bottom: const TabBar(
          tabs: [
            Tab(icon: Icon(Icons.directions_car)),
            Tab(icon: Icon(Icons.directions_transit)),
            Tab(icon: Icon(Icons.directions_bike)),
          ],
        ),
      ),
    ),
  ),
);
```

By default, the `TabBar` looks up the widget tree for the nearest `DefaultTabController`. If you're manually creating a `TabController`, pass it to the `TabBar`.

3. Create content for each tab
------------------------------

[#](#3-create-content-for-each-tab)

Now that you have tabs, display content when a tab is selected. For this purpose, use the [`TabBarView`](https://api.flutter.dev/flutter/material/TabBarView-class.html) widget.

*info* Note

Order is important and must correspond to the order of the tabs in the `TabBar`.

dart

```
body: const TabBarView(
  children: [
    Icon(Icons.directions_car),
    Icon(Icons.directions_transit),
    Icon(Icons.directions_bike),
  ],
),
```

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() {
  runApp(const TabBarDemo());
}

class TabBarDemo extends StatelessWidget {
  const TabBarDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: AppBar(
            bottom: const TabBar(
              tabs: [
                Tab(icon: Icon(Icons.directions_car)),
                Tab(icon: Icon(Icons.directions_transit)),
                Tab(icon: Icon(Icons.directions_bike)),
              ],
            ),
            title: const Text('Tabs Demo'),
          ),
          body: const TabBarView(
            children: [
              Icon(Icons.directions_car),
              Icon(Icons.directions_transit),
              Icon(Icons.directions_bike),
            ],
          ),
        ),
      ),
    );
  }
}
```

 ![Tabs Demo](/assets/images/docs/cookbook/tabs.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/design/tabs/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/design/tabs.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/design/tabs/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/design/tabs.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/design/tabs.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/design/tabs/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/design/tabs.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    