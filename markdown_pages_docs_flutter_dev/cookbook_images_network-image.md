Display images from the internet
================================

1. [Cookbook](/cookbook) chevron\_right- [Images](/cookbook/images) chevron\_right- [Display images from the internet](/cookbook/images/network-image)

Displaying images is fundamental for most mobile apps. Flutter provides the [`Image`](https://api.flutter.dev/flutter/widgets/Image-class.html) widget to display different types of images.

To work with images from a URL, use the [`Image.network()`](https://api.flutter.dev/flutter/widgets/Image/Image.network.html) constructor.

dart

```
Image.network('https://picsum.photos/250?image=9'),
```

Bonus: animated gifs
--------------------

[#](#bonus-animated-gifs)

One useful thing about the `Image` widget: It supports animated gifs.

dart

```
Image.network(
  'https://docs.flutter.dev/assets/images/dash/dash-fainting.gif',
);
```

Image fade in with placeholders
-------------------------------

[#](#image-fade-in-with-placeholders)

The default `Image.network` constructor doesn't handle more advanced functionality, such as fading images in after loading. To accomplish this task, check out [Fade in images with a placeholder](/cookbook/images/fading-in-images).

* [Fade in images with a placeholder](/cookbook/images/fading-in-images)

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
    var title = 'Web Images';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: Text(title)),
        body: Image.network('https://picsum.photos/250?image=9'),
      ),
    );
  }
}
```

 ![Network image demo](/assets/images/docs/cookbook/network-image.png)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/network-image/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/network-image.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/network-image/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/network-image.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/images/network-image.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/network-image/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/network-image.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    