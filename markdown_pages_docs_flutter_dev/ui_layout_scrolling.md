Scrolling
=========

1. [UI](/ui) chevron\_right- [Layout](/ui/layout) chevron\_right- [Scrolling](/ui/layout/scrolling)

Flutter has many built-in widgets that automatically scroll and also offers a variety of widgets that you can customize to create specific scrolling behavior.

Basic scrolling
---------------

[#](#basic-scrolling)

Many Flutter widgets support scrolling out of the box and do most of the work for you. For example, [`SingleChildScrollView`](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) automatically scrolls its child when necessary. Other useful widgets include [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html) and [`GridView`](https://api.flutter.dev/flutter/widgets/GridView-class.html). You can check out more of these widgets on the [scrolling page](/ui/widgets/scrolling) of the Widget catalog.

[Watch on YouTube in a new tab: "Scrollbar | Flutter widget of the week"](https://www.youtube.com/watch/DbkIQSvwnZc)

 

[Watch on YouTube in a new tab: "ListView | Flutter widget of the week"](https://www.youtube.com/watch/KJpkjHGiI5A)

### Infinite scrolling

[#](#infinite-scrolling)

When you have a long list of items in your `ListView` or `GridView` (including an *infinite* list), you can build the items on demand as they scroll into view. This provides a much more performant scrolling experience. For more information, check out [`ListView.builder`](https://api.flutter.dev/flutter/widgets/ListView/ListView.builder.html) or [`GridView.builder`](https://api.flutter.dev/flutter/widgets/GridView/GridView.builder.html).

### Specialized scrollable widgets

[#](#specialized-scrollable-widgets)

The following widgets provide more specific scrolling behavior.

A video on using [`DraggableScrollableSheet`](https://api.flutter.dev/flutter/widgets/DraggableScrollableSheet-class.html):

[Watch on YouTube in a new tab: "DraggableScrollableSheet | Flutter widget of the week"](https://www.youtube.com/watch/Hgw819mL_78)

Turn the scrollable area into a wheel with [`ListWheelScrollView`](https://api.flutter.dev/flutter/widgets/ListWheelScrollView-class.html)!

[Watch on YouTube in a new tab: "ListWheelScrollView | Flutter widget of the week"](https://www.youtube.com/watch/dUhmWAz4C7Y)

Fancy scrolling
---------------

[#](#fancy-scrolling)

Perhaps you want to implement *elastic* scrolling, also called *scroll bouncing*. Or maybe you want to implement other dynamic scrolling effects, like parallax scrolling. Or perhaps you want a scrolling header with very specific behavior, such as shrinking or disappearing.

You can achieve all this and more using the Flutter `Sliver*` classes. A *sliver* refers to a piece of the scrollable area. You can define and insert a sliver into a [`CustomScrollView`](https://api.flutter.dev/flutter/widgets/CustomScrollView-class.html) to have finer-grained control over that area.

For more information, check out [Using slivers to achieve fancy scrolling](/ui/layout/scrolling/slivers) and the [Sliver classes](/ui/widgets/layout#sliver-widgets).

Nested scrolling widgets
------------------------

[#](#nested-scrolling-widgets)

How do you nest a scrolling widget inside another scrolling widget without hurting scrolling performance? Do you set the `ShrinkWrap` property to true, or do you use a sliver?

Check out the "ShrinkWrap vs Slivers" video:

[Watch on YouTube in a new tab: "ShrinkWrap vs Slivers | Decoding Flutter"](https://www.youtube.com/watch/LUqDNnv_dh0)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/layout/scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/layout/scrolling/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/layout/scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/layout/scrolling/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-08-05. [View source](https://github.com/flutter/website/tree/main/src/content/ui/layout/scrolling/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/ui/layout/scrolling/&page-source=https://github.com/flutter/website/tree/main/src/content/ui/layout/scrolling/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   