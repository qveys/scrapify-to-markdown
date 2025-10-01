Animate a widget across screens
===============================

1. [Cookbook](/cookbook) chevron\_right- [Navigation](/cookbook/navigation) chevron\_right- [Animate a widget across screens](/cookbook/navigation/hero-animations)

It's often helpful to guide users through an app as they navigate from screen to screen. A common technique to lead users through an app is to animate a widget from one screen to the next. This creates a visual anchor connecting the two screens.

Use the [`Hero`](https://api.flutter.dev/flutter/widgets/Hero-class.html) widget to animate a widget from one screen to the next. This recipe uses the following steps:

1. Create two screens showing the same image.- Add a `Hero` widget to the first screen.- Add a `Hero` widget to the second screen.

1. Create two screens showing the same image
--------------------------------------------

[#](#1-create-two-screens-showing-the-same-image)

In this example, display the same image on both screens. Animate the image from the first screen to the second screen when the user taps the image. For now, create the visual structure; handle animations in the next steps.

*info* Note

This example builds upon the [Navigate to a new screen and back](/cookbook/navigation/navigation-basics) and [Handle taps](/cookbook/gestures/handling-taps) recipes.

dart

```
import 'package:flutter/material.dart';

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Main Screen')),
      body: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute<void>(
              builder: (context) {
                return const DetailScreen();
              },
            ),
          );
        },
        child: Image.network('https://picsum.photos/250?image=9'),
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  const DetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: GestureDetector(
        onTap: () {
          Navigator.pop(context);
        },
        child: Center(
          child: Image.network('https://picsum.photos/250?image=9'),
        ),
      ),
    );
  }
}
```

2. Add a `Hero` widget to the first screen
------------------------------------------

[#](#2-add-a-hero-widget-to-the-first-screen)

To connect the two screens together with an animation, wrap the `Image` widget on both screens in a `Hero` widget. The `Hero` widget requires two arguments:

`tag`: An object that identifies the `Hero`. It must be the same on both screens. `child`: The widget to animate across screens.

dart

```
Hero(
  tag: 'imageHero',
  child: Image.network('https://picsum.photos/250?image=9'),
)
```

3. Add a `Hero` widget to the second screen
-------------------------------------------

[#](#3-add-a-hero-widget-to-the-second-screen)

To complete the connection with the first screen, wrap the `Image` on the second screen with a `Hero` widget that has the same `tag` as the `Hero` in the first screen.

After applying the `Hero` widget to the second screen, the animation between screens just works.

dart

```
Hero(
  tag: 'imageHero',
  child: Image.network('https://picsum.photos/250?image=9'),
)
```

*info* Note

This code is identical to what you have on the first screen. As a best practice, create a reusable widget instead of repeating code. This example uses identical code for both widgets, for simplicity.

Interactive example
-------------------

[#](#interactive-example)

```
import 'package:flutter/material.dart';

void main() => runApp(const HeroApp());

class HeroApp extends StatelessWidget {
  const HeroApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(title: 'Transition Demo', home: MainScreen());
  }
}

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Main Screen')),
      body: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute<void>(
              builder: (context) {
                return const DetailScreen();
              },
            ),
          );
        },
        child: Hero(
          tag: 'imageHero',
          child: Image.network('https://picsum.photos/250?image=9'),
        ),
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  const DetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: GestureDetector(
        onTap: () {
          Navigator.pop(context);
        },
        child: Center(
          child: Hero(
            tag: 'imageHero',
            child: Image.network('https://picsum.photos/250?image=9'),
          ),
        ),
      ),
    );
  }
}
```

 ![Hero demo](/assets/images/docs/cookbook/hero.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/hero-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/hero-animations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/hero-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/hero-animations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-19. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/hero-animations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/navigation/hero-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/navigation/hero-animations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    