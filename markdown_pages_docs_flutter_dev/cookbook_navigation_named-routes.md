Navigate with named routes
==========================

1. [Cookbook](/cookbook) chevron\_right- [Navigation](/cookbook/navigation) chevron\_right- [Navigate with named routes](/cookbook/navigation/named-routes)

*info* Note

Named routes are no longer recommended for most applications. For more information, see [Limitations](/ui/navigation#limitations) in the [navigation overview](/ui/navigation) page.

In the [Navigate to a new screen and back](/cookbook/navigation/navigation-basics) recipe, you learned how to navigate to a new screen by creating a new route and pushing it to the [`Navigator`](https://api.flutter.dev/flutter/widgets/Navigator-class.html).

However, if you need to navigate to the same screen in many parts of your app, this approach can result in code duplication. The solution is to define a *named route*, and use the named route for navigation.

To work with named routes, use the [`Navigator.pushNamed()`](https://api.flutter.dev/flutter/widgets/Navigator/pushNamed.html) function. This example replicates the functionality from the original recipe, demonstrating how to use named routes using the following steps:

1. Create two screens.- Define the routes.- Navigate to the second screen using `Navigator.pushNamed()`.- Return to the first screen using `Navigator.pop()`.

1. Create two screens
---------------------

[#](#1-create-two-screens)

First, create two screens to work with. The first screen contains a button that navigates to the second screen. The second screen contains a button that navigates back to the first.

dart

```
import 'package:flutter/material.dart';

class FirstScreen extends StatelessWidget {
  const FirstScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('First Screen')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Navigate to the second screen when tapped.
          },
          child: const Text('Launch screen'),
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  const SecondScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Second Screen')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Navigate back to first screen when tapped.
          },
          child: const Text('Go back!'),
        ),
      ),
    );
  }
}
```

2. Define the routes
--------------------

[#](#2-define-the-routes)

Next, define the routes by providing additional properties to the [`MaterialApp`](https://api.flutter.dev/flutter/material/MaterialApp-class.html) constructor: the `initialRoute` and the `routes` themselves.

The `initialRoute` property defines which route the app should start with. The `routes` property defines the available named routes and the widgets to build when navigating to those routes.

dart

```
MaterialApp(
  title: 'Named Routes Demo',
  // Start the app with the "/" named route. In this case, the app starts
  // on the FirstScreen widget.
  initialRoute: '/',
  routes: {
    // When navigating to the "/" route, build the FirstScreen widget.
    '/': (context) => const FirstScreen(),
    // When navigating to the "/second" route, build the SecondScreen widget.
    '/second': (context) => const SecondScreen(),
  },
)
```

*warning* Warning

When using `initialRoute`, **don't** define a `home` property.

3. Navigate to the second screen
--------------------------------

[#](#3-navigate-to-the-second-screen)

With the widgets and routes in place, trigger navigation by using the [`Navigator.pushNamed()`](https://api.flutter.dev/flutter/widgets/Navigator/pushNamed.html) method. This tells Flutter to build the widget defined in the `routes` table and launch the screen.

In the `build()` method of the `FirstScreen` widget, update the `onPressed()` callback:

dart

```
// Within the `FirstScreen` widget
onPressed: () {
  // Navigate to the second screen using a named route.
  Navigator.pushNamed(context, '/second');
}
```

4. Return to the first screen
-----------------------------

[#](#4-return-to-the-first-screen)

To navigate back to the first screen, use the [`Navigator.pop()`](https://api.flutter.dev/flutter/widgets/Navigator/pop.html) function.

dart

```
// Within the SecondScreen widget
onPressed: () {
  // Navigate back to the first screen by popping the current route
  // off the stack.
  Navigator.pop(context);
}
```

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Named Routes Demo',
      // Start the app with the "/" named route. In this case, the app starts
      // on the FirstScreen widget.
      initialRoute: '/',
      routes: {
        // When navigating to the "/" route, build the FirstScreen widget.
        '/': (context) => const FirstScreen(),
        // When navigating to the "/second" route, build the SecondScreen widget.
        '/second': (context) => const SecondScreen(),
      },
    ),
  );
}

class FirstScreen extends StatelessWidget {
  const FirstScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('First Screen')),
      body: Center(
        child: ElevatedButton(
          // Within the `FirstScreen` widget
          onPressed: () {
            // Navigate to the second screen using a named route.
            Navigator.pushNamed(context, '/second');
          },
          child: const Text('Launch screen'),
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  const SecondScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Second Screen')),
      body: Center(
        child: ElevatedButton(
          // Within the SecondScreen widget
          onPressed: () {
            // Navigate back to the first screen by popping the current route
            // off the stack.
            Navigator.pop(context);
          },
          child: const Text('Go back!'),
        ),
      ),
    );
  }
}
```

 ![Navigation Basics Demo](/assets/images/docs/cookbook/navigation-basics.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/named-routes/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/named-routes.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/named-routes/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/named-routes.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-04-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/named-routes.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/named-routes/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/named-routes.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    