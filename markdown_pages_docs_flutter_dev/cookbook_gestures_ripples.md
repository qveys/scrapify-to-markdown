Add Material touch ripples
==========================

1. [Cookbook](/cookbook) chevron\_right- [Gestures](/cookbook/gestures) chevron\_right- [Add Material touch ripples](/cookbook/gestures/ripples)

Widgets that follow the Material Design guidelines display a ripple animation when tapped.

Flutter provides the [`InkWell`](https://api.flutter.dev/flutter/material/InkWell-class.html) widget to perform this effect. Create a ripple effect using the following steps:

1. Create a widget that supports tap.- Wrap it in an `InkWell` widget to manage tap callbacks and ripple animations.

dart

```
// The InkWell wraps the custom flat button widget.
InkWell(
  // When the user taps the button, show a snackbar.
  onTap: () {
    ScaffoldMessenger.of(
      context,
    ).showSnackBar(const SnackBar(content: Text('Tap')));
  },
  child: const Padding(
    padding: EdgeInsets.all(12),
    child: Text('Flat Button'),
  ),
)
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
    const title = 'InkWell Demo';

    return const MaterialApp(
      title: title,
      home: MyHomePage(title: title),
    );
  }
}

class MyHomePage extends StatelessWidget {
  final String title;

  const MyHomePage({super.key, required this.title});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      body: const Center(child: MyButton()),
    );
  }
}

class MyButton extends StatelessWidget {
  const MyButton({super.key});

  @override
  Widget build(BuildContext context) {
    // The InkWell wraps the custom flat button widget.
    return InkWell(
      // When the user taps the button, show a snackbar.
      onTap: () {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(const SnackBar(content: Text('Tap')));
      },
      child: const Padding(
        padding: EdgeInsets.all(12),
        child: Text('Flat Button'),
      ),
    );
  }
}
```

 ![Ripples Demo](/assets/images/docs/cookbook/ripples.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/ripples/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/ripples.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/ripples/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/ripples.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-19. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/ripples.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/ripples/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/ripples.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    