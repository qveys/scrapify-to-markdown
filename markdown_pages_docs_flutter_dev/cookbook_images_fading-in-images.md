Fade in images with a placeholder
=================================

1. [Cookbook](/cookbook) chevron\_right- [Images](/cookbook/images) chevron\_right- [Fade in images with a placeholder](/cookbook/images/fading-in-images)

When displaying images using the default `Image` widget, you might notice they simply pop onto the screen as they're loaded. This might feel visually jarring to your users.

Instead, wouldn't it be nice to display a placeholder at first, and images would fade in as they're loaded? Use the [`FadeInImage`](https://api.flutter.dev/flutter/widgets/FadeInImage-class.html) widget for exactly this purpose.

`FadeInImage` works with images of any type: in-memory, local assets, or images from the internet.

In-Memory
---------

[#](#in-memory)

In this example, use the [`transparent_image`](https://pub.dev/packages/transparent_image) package for a simple transparent placeholder.

dart

```
FadeInImage.memoryNetwork(
  placeholder: kTransparentImage,
  image: 'https://picsum.photos/250?image=9',
),
```

### Complete example

[#](#complete-example)

dart

```
import 'package:flutter/material.dart';
import 'package:transparent_image/transparent_image.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Fade in images';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: Stack(
          children: <Widget>[
            const Center(child: CircularProgressIndicator()),
            Center(
              child: FadeInImage.memoryNetwork(
                placeholder: kTransparentImage,
                image: 'https://picsum.photos/250?image=9',
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

![Fading In Image Demo](/assets/images/docs/cookbook/fading-in-images.webp)

From asset bundle
-----------------

[#](#from-asset-bundle)

You can also consider using local assets for placeholders. First, add the asset to the project's `pubspec.yaml` file (for more details, see [Adding assets and images](/ui/assets/assets-and-images)):

yaml

```
flutter:
  assets:
    - assets/loading.gif
```

Then, use the [`FadeInImage.assetNetwork()`](https://api.flutter.dev/flutter/widgets/FadeInImage/FadeInImage.assetNetwork.html) constructor:

dart

```
FadeInImage.assetNetwork(
  placeholder: 'assets/loading.gif',
  image: 'https://picsum.photos/250?image=9',
),
```

### Complete example

[#](#complete-example-1)

dart

```
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Fade in images';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(title: const Text(title)),
        body: Center(
          child: FadeInImage.assetNetwork(
            placeholder: 'assets/loading.gif',
            image: 'https://picsum.photos/250?image=9',
          ),
        ),
      ),
    );
  }
}
```

![Asset fade-in](/assets/images/docs/cookbook/fading-in-asset-demo.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/fading-in-images/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/fading-in-images.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/fading-in-images/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/fading-in-images.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/images/fading-in-images.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/images/fading-in-images/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/images/fading-in-images.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   