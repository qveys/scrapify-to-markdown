Handle taps
===========

1. [Cookbook](/cookbook) chevron\_right- [Gestures](/cookbook/gestures) chevron\_right- [Handle taps](/cookbook/gestures/handling-taps)

You not only want to display information to users, you want users to interact with your app. Use the [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html) widget to respond to fundamental actions, such as tapping and dragging.

*info* Note

To learn more, watch this short Widget of the Week video on the `GestureDetector` widget:

[Watch on YouTube in a new tab: "GestureDetector | Flutter widget of the week"](https://www.youtube.com/watch/WhVXkCFPmK4)

This recipe shows how to make a custom button that shows a snackbar when tapped with the following steps:

1. Create the button.- Wrap it in a `GestureDetector` and provide an `onTap()` callback.

dart

```
// The GestureDetector wraps the button.
GestureDetector(
  // When the child is tapped, show a snackbar.
  onTap: () {
    const snackBar = SnackBar(content: Text('Tap'));

    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  },
  // The custom button
  child: Container(
    padding: const EdgeInsets.all(12),
    decoration: BoxDecoration(
      color: Colors.lightBlue,
      borderRadius: BorderRadius.circular(8),
    ),
    child: const Text('My Button'),
  ),
)
```

Notes
-----

[#](#notes)

1. For information on adding the Material ripple effect to your button, see the [Add Material touch ripples](/cookbook/gestures/ripples) recipe.- Although this example creates a custom button, Flutter includes a handful of button implementations, such as: [`ElevatedButton`](https://api.flutter.dev/flutter/material/ElevatedButton-class.html), [`TextButton`](https://api.flutter.dev/flutter/material/TextButton-class.html), and [`CupertinoButton`](https://api.flutter.dev/flutter/cupertino/CupertinoButton-class.html).

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
    const title = 'Gesture Demo';

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
    // The GestureDetector wraps the button.
    return GestureDetector(
      // When the child is tapped, show a snackbar.
      onTap: () {
        const snackBar = SnackBar(content: Text('Tap'));

        ScaffoldMessenger.of(context).showSnackBar(snackBar);
      },
      // The custom button
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.lightBlue,
          borderRadius: BorderRadius.circular(8),
        ),
        child: const Text('My Button'),
      ),
    );
  }
}
```

 ![Handle taps demo](/assets/images/docs/cookbook/handling-taps.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/handling-taps/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/handling-taps.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/handling-taps/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/handling-taps.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-06-20. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/handling-taps.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/gestures/handling-taps/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/gestures/handling-taps.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    