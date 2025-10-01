Implicit animations
===================

1. [Codelabs](/codelabs) chevron\_right- [Implicit animations](/codelabs/implicit-animations)

Welcome to the implicit animations codelab, where you learn how to use Flutter widgets that make it easy to create animations for a specific set of properties.

*info* Note

This codelab uses embedded DartPads to display examples and exercises. If you see empty boxes instead of DartPads, check out [Troubleshooting DartPad](https://dart.dev/tools/dartpad/troubleshoot).

To get the most out of this codelab, you should have basic knowledge about:

* How to [make a Flutter app](https://codelabs.developers.google.com/codelabs/flutter-codelab-first).* How to use [stateful widgets](/ui/interactivity#stateful-and-stateless-widgets).

This codelab covers the following material:

* Using `AnimatedOpacity` to create a fade-in effect.* Using `AnimatedContainer` to animate transitions in size, color, and margin.* Overview of implicit animations and techniques for using them.

**Estimated time to complete this codelab: 15-30 minutes.**

What are implicit animations?
-----------------------------

[#](#what-are-implicit-animations)

With Flutter's [animation library](https://api.flutter.dev/flutter/animation/animation-library.html), you can add motion and create visual effects for the widgets in your UI. One widget set in the library manages animations for you. These widgets are collectively referred to as *implicit animations*, or *implicitly animated widgets*, deriving their name from the [ImplicitlyAnimatedWidget](https://api.flutter.dev/flutter/widgets/ImplicitlyAnimatedWidget-class.html) class that they implement. With implicit animations, you can animate a widget property by setting a target value; whenever that target value changes, the widget animates the property from the old value to the new one. In this way, implicit animations trade control for convenience—they manage animation effects so that you don't have to.

Example: Fade-in text effect
----------------------------

[#](#example-fade-in-text-effect)

The following example shows how to add a fade-in effect to existing UI using an implicitly animated widget called [AnimatedOpacity](https://api.flutter.dev/flutter/widgets/AnimatedOpacity-class.html). **The example begins with no animation code**—it consists of a [Material App](https://api.flutter.dev/flutter/material/MaterialApp-class.html) home screen containing:

* A photograph of an owl.* One **Show details** button that does nothing when clicked.* Description text of the owl in the photograph.

### Fade-in (starter code)

[#](#fade-in-starter-code)

To view the example, Click **Run**:

```
// Copyright 2019 the Dart project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

import 'package:flutter/material.dart';

const owlUrl =
    'https://raw.githubusercontent.com/flutter/website/main/src/content/assets/images/docs/owl.jpg';

class FadeInDemo extends StatefulWidget {
  const FadeInDemo({super.key});

  @override
  State<FadeInDemo> createState() => _FadeInDemoState();
}

class _FadeInDemoState extends State<FadeInDemo> {
  @override
  Widget build(BuildContext context) {
    return ListView(children: <Widget>[
      Image.network(owlUrl),
      TextButton(
        child: const Text(
          'Show Details',
          style: TextStyle(color: Colors.blueAccent),
        ),
        onPressed: () => {},
      ),
      const Column(
        children: [
          Text('Type: Owl'),
          Text('Age: 39'),
          Text('Employment: None'),
        ],
      )
    ]);
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: FadeInDemo(),
        ),
      ),
    );
  }
}

void main() {
  runApp(
    const MyApp(),
  );
}
```

### Animate opacity with AnimatedOpacity widget

[#](#animate-opacity-with-animatedopacity-widget)

This section contains a list of steps you can use to add an implicit animation to the [fade-in starter code](#fade-in-starter-code). After the steps, you can also run the [fade-in complete](#fade-in-complete) code with the changes already made. The steps outline how to use the `AnimatedOpacity` widget to add the following animation feature:

* The owl's description text remains hidden until the user clicks **Show details**.* When the user clicks **Show details**, the owl's description text fades in.

#### 1. Pick a widget property to animate

[#](#1-pick-a-widget-property-to-animate)

To create a fade-in effect, you can animate the `opacity` property using the`AnimatedOpacity` widget. Wrap the `Column` widget in an `AnimatedOpacity` widget:

dart

```
@override
Widget build(BuildContext context) {
  return ListView(children: <Widget>[
    Image.network(owlUrl),
    TextButton(
      child: const Text(
        'Show Details',
        style: TextStyle(color: Colors.blueAccent),
      ),
      onPressed: () => {},
    ),
    const Column(
      children: [
        Text('Type: Owl'),
        Text('Age: 39'),
        Text('Employment: None'),
      ],
    ),
    AnimatedOpacity(
      child: const Column(
        children: [
          Text('Type: Owl'),
          Text('Age: 39'),
          Text('Employment: None'),
        ],
      ),
    ),
  ]);
}
```

*info* Note

You can reference the line numbers in the example code to help track where to make these changes in the [fade-in starter code](#fade-in-starter-code).

#### 2. Initialize a state variable for the animated property

[#](#2-initialize-a-state-variable-for-the-animated-property)

To hide the text before the user clicks **Show details**, set the starting value for `opacity` to zero:

dart

```
class _FadeInDemoState extends State<FadeInDemo> {
  double opacity = 0;

  @override
  Widget build(BuildContext context) {
    return ListView(children: <Widget>[
      // ...
      AnimatedOpacity(
        opacity: opacity,
        child: const Column(
```

#### 3. Set the duration of the animation

[#](#3-set-the-duration-of-the-animation)

In addition to an `opacity` parameter, `AnimatedOpacity` requires a [duration](https://api.flutter.dev/flutter/widgets/ImplicitlyAnimatedWidget/duration.html) to use for its animation. For this example, you can start with 2 seconds:

dart

```
AnimatedOpacity(
  duration: const Duration(seconds: 2),
  opacity: opacity,
  child: const Column(
```

#### 4. Set up a trigger for animation and choose an end value

[#](#4-set-up-a-trigger-for-animation-and-choose-an-end-value)

Configure the animation to trigger when the user clicks **Show details**. To do this, change `opacity` state using the `onPressed()` handler for `TextButton`. To make the `FadeInDemo` widget become fully visible when the user clicks **Show details**, use the `onPressed()` handler to set `opacity` to 1:

dart

```
TextButton(
  child: const Text(
    'Show Details',
    style: TextStyle(color: Colors.blueAccent),
  ),
  onPressed: () => {},
  onPressed: () => setState(() {
    opacity = 1;
  }),
),
```

*info* Note

You only need to set the start and end values of `opacity`. The `AnimatedOpacity` widget manages everything in between.

### Fade-in (complete)

[#](#fade-in-complete)

Here's the example with the completed changes you've made. Run this example then click **Show details** to trigger the animation.

```
// Copyright 2019 the Dart project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

import 'package:flutter/material.dart';

const owlUrl =
    'https://raw.githubusercontent.com/flutter/website/main/src/content/assets/images/docs/owl.jpg';

class FadeInDemo extends StatefulWidget {
  const FadeInDemo({super.key});

  @override
  State<FadeInDemo> createState() => _FadeInDemoState();
}

class _FadeInDemoState extends State<FadeInDemo> {
  double opacity = 0;

  @override
  Widget build(BuildContext context) {
    return ListView(children: <Widget>[
      Image.network(owlUrl),
      TextButton(
        child: const Text(
          'Show Details',
          style: TextStyle(color: Colors.blueAccent),
        ),
        onPressed: () => setState(() {
          opacity = 1;
        }),
      ),
      AnimatedOpacity(
        duration: const Duration(seconds: 2),
        opacity: opacity,
        child: const Column(
          children: [
            Text('Type: Owl'),
            Text('Age: 39'),
            Text('Employment: None'),
          ],
        ),
      )
    ]);
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: FadeInDemo(),
        ),
      ),
    );
  }
}

void main() {
  runApp(
    const MyApp(),
  );
}
```

### Putting it all together

[#](#putting-it-all-together)

The [Fade-in text effect](#example-fade-in-text-effect) example demonstrates the following features of the `AnimatedOpacity` widget.

* It listens for state changes to its `opacity` property.* When the `opacity` property changes, it animates the transition to the new value for `opacity`.* It requires a `duration` parameter to define how long the transition between the values should take.

*info* Note

* Implicit animations can only animate the properties of a parent stateful widget. The preceding example enables this with the `FadeInDemo` widget that extends `StatefulWidget`.* The `AnimatedOpacity` widget only animates the `opacity` property. Some implicitly animated widgets can animate many properties at the same time. The following example showcases this.

Example: Shape-shifting effect
------------------------------

[#](#example-shape-shifting-effect)

The following example shows how to use the [`AnimatedContainer`](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html) widget to animate multiple properties (`margin`, `borderRadius`, and `color`) with different types (`double` and `Color`). **The example begins with no animation code**. It starts with a [Material App](https://api.flutter.dev/flutter/material/MaterialApp-class.html) home screen that contains:

* A `Container` widget configured with a `borderRadius`, `margin`, and `color`. These properties are setup to be regenerated each time you run the example.* A **Change** button that does nothing when clicked.

### Shape-shifting (starter code)

[#](#shape-shifting-starter-code)

To start the example, click **Run**.

```
// Copyright 2019 the Dart project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

import 'dart:math';

import 'package:flutter/material.dart';

double randomBorderRadius() {
  return Random().nextDouble() * 64;
}

double randomMargin() {
  return Random().nextDouble() * 64;
}

Color randomColor() {
  return Color(0xFFFFFFFF & Random().nextInt(0xFFFFFFFF));
}

class AnimatedContainerDemo extends StatefulWidget {
  const AnimatedContainerDemo({super.key});

  @override
  State<AnimatedContainerDemo> createState() => _AnimatedContainerDemoState();
}

class _AnimatedContainerDemoState extends State<AnimatedContainerDemo> {
  late Color color;
  late double borderRadius;
  late double margin;

  @override
  void initState() {
    super.initState();
    color = randomColor();
    borderRadius = randomBorderRadius();
    margin = randomMargin();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: <Widget>[
            SizedBox(
              width: 128,
              height: 128,
              child: Container(
                margin: EdgeInsets.all(margin),
                decoration: BoxDecoration(
                  color: color,
                  borderRadius: BorderRadius.circular(borderRadius),
                ),
              ),
            ),
            ElevatedButton(
              child: const Text('Change'),
              onPressed: () => {},
            ),
          ],
        ),
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: AnimatedContainerDemo(),
    );
  }
}

void main() {
  runApp(
    const MyApp(),
  );
}
```

### Animate color, borderRadius, and margin with AnimatedContainer

[#](#animate-color-borderradius-and-margin-with-animatedcontainer)

This section contains a list of steps you can use to add an implicit animation to the [shape-shifting starter code](#shape-shifting-starter-code). After completing each step, you can also run the [complete shape-shifting example](#shape-shifting-complete) with the changes already made.

The [shape-shifting starter code](#shape-shifting-starter-code) assigns each property in the `Container` widget a random value. Associated functions generate the relevant values:

* The `randomColor()` function generates a `Color` for the `color` property* The `randomBorderRadius()` function generates a `double` for the `borderRadius` property.* The `randomMargin()` function generates a `double` for the `margin` property.

The following steps use the `AnimatedContainer` widget to:

* Transition to new values for `color`, `borderRadius`, and `margin` whenever the user clicks **Change**.* Animate the transition to the new values for `color`, `borderRadius`, and `margin` whenever they are set.

#### 1. Add an implicit animation

[#](#1-add-an-implicit-animation)

Change the `Container` widget to an `AnimatedContainer` widget:

dart

```
SizedBox(
  width: 128,
  height: 128,
  child: Container(
  child: AnimatedContainer(
    margin: EdgeInsets.all(margin),
    decoration: BoxDecoration(
      color: color,
      borderRadius: BorderRadius.circular(borderRadius),
    ),
  ),
),
```

*info* Note

You can reference the line numbers in the example code to help track where to make these changes in the [shape-shifting starter code](#shape-shifting-starter-code).

#### 2. Set starting values for animated properties

[#](#2-set-starting-values-for-animated-properties)

The `AnimatedContainer` widget transitions between old and new values of its properties when they change. To contain the behavior triggered when the user clicks **Change**, create a `change()` method. The `change()` method can use the `setState()` method to set new values for the `color`, `borderRadius`, and `margin` state variables:

dart

```
void change() {
  setState(() {
    color = randomColor();
    borderRadius = randomBorderRadius();
    margin = randomMargin();
  });
}

@override
Widget build(BuildContext context) {
  // ...
```

#### 3. Set up a trigger for the animation

[#](#3-set-up-a-trigger-for-the-animation)

To set the animation to trigger whenever the user presses **Change**, invoke the `change()` method in the `onPressed()` handler:

dart

```
ElevatedButton(
  child: const Text('Change'),
  onPressed: () => {},
  onPressed: () => change(),
),
```

#### 4. Set duration

[#](#4-set-duration)

Set the `duration` of the animation that powers the transition between the old and new values:

dart

```
SizedBox(
  width: 128,
  height: 128,
  child: AnimatedContainer(
    margin: EdgeInsets.all(margin),
    decoration: BoxDecoration(
      color: color,
      borderRadius: BorderRadius.circular(borderRadius),
    ),
    duration: const Duration(milliseconds: 400),
  ),
),
```

### Shape-shifting (complete)

[#](#shape-shifting-complete)

Here's the example with the completed changes you've made. Run the code and click **Change** to trigger the animation. Each time you click **Change**, the shape animates to its new values for `margin`, `borderRadius`, and `color`.

```
// Copyright 2019 the Dart project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

import 'dart:math';

import 'package:flutter/material.dart';

const _duration = Duration(milliseconds: 400);

double randomBorderRadius() {
  return Random().nextDouble() * 64;
}

double randomMargin() {
  return Random().nextDouble() * 64;
}

Color randomColor() {
  return Color(0xFFFFFFFF & Random().nextInt(0xFFFFFFFF));
}

class AnimatedContainerDemo extends StatefulWidget {
  const AnimatedContainerDemo({super.key});

  @override
  State<AnimatedContainerDemo> createState() => _AnimatedContainerDemoState();
}

class _AnimatedContainerDemoState extends State<AnimatedContainerDemo> {
  late Color color;
  late double borderRadius;
  late double margin;

  @override
  void initState() {
    super.initState();
    color = randomColor();
    borderRadius = randomBorderRadius();
    margin = randomMargin();
  }

  void change() {
    setState(() {
      color = randomColor();
      borderRadius = randomBorderRadius();
      margin = randomMargin();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: <Widget>[
            SizedBox(
              width: 128,
              height: 128,
              child: AnimatedContainer(
                margin: EdgeInsets.all(margin),
                decoration: BoxDecoration(
                  color: color,
                  borderRadius: BorderRadius.circular(borderRadius),
                ),
                duration: _duration,
              ),
            ),
            ElevatedButton(
              child: const Text('Change'),
              onPressed: () => change(),
            ),
          ],
        ),
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: AnimatedContainerDemo(),
    );
  }
}

void main() {
  runApp(
    const MyApp(),
  );
}
```

### Using animation curves

[#](#using-animation-curves)

The preceding examples show how:

* Implicit animations allow you to animate the transition between values for specific widget properties.* The `duration` parameter allows you to set how long the animation takes to complete.

Implicit animations also allow you to control changes to **the rate** of an animation that occurs during the set `duration`. To define this change in rate, set the value of the `curve` parameter to a [`Curve`](https://api.flutter.dev/flutter/animation/Curve-class.html), such as one declared in the [`Curves`](https://api.flutter.dev/flutter/animation/Curves-class.html) class.

The preceding examples did not specify a value for the `curve` parameter. Without a specified curve value, the implicit animations apply a [linear animation curve](https://api.flutter.dev/flutter/animation/Curves/linear-constant.html).

Specify a value for the `curve` parameter in the [complete shape-shifting example](#shape-shifting-complete). The animation changes when you pass the [`easeInOutBack`](https://api.flutter.dev/flutter/animation/Curves/easeInOutBack-constant.html) constant for `curve`,

dart

```
SizedBox(
  width: 128,
  height: 128,
  child: AnimatedContainer(
    margin: EdgeInsets.all(margin),
    decoration: BoxDecoration(
      color: color,
      borderRadius: BorderRadius.circular(borderRadius),
    ),
    duration: _duration,
    curve: Curves.easeInOutBack,
  ),
),
```

When you pass the `Curves.easeInOutBack` constant to the `curve` property of the `AnimatedContainer` widget, watch how the rates of change for `margin`, `borderRadius`, and `color` follow the curve that constant defined.

[  ](https://flutter.github.io/assets-for-api-docs/assets/animation/curve_ease_in_out_back.mp4)

### Putting it all together

[#](#putting-it-all-together-1)

The [complete shape-shifting example](#shape-shifting-complete) animates transitions between values for `margin`, `borderRadius`, and `color` properties. The `AnimatedContainer` widget animates changes to any of its properties. These include those you didn't use such as `padding`, `transform`, and even `child` and `alignment`! By showing additional capabilities of implicit animations, the [complete shape-shifting example](#shape-shifting-complete) builds upon [fade-in complete](#fade-in-complete) example.

To summarize implicit animations:

* Some implicit animations, like the `AnimatedOpacity` widget, only animate one property. Others, like the `AnimatedContainer` widget, can animate many properties.* Implicit animations animate the transition between the old and new value of a property when it changes using the provided `curve` and `duration`.* If you do not specify a `curve`, implicit animations default to a [linear curve](https://api.flutter.dev/flutter/animation/Curves/linear-constant.html).

What's next?
------------

[#](#whats-next)

Congratulations, you've finished the codelab! To learn more, check out these suggestions:

* Try the [animations tutorial](/ui/animations/tutorial).* Learn about [hero animations](/ui/animations/hero-animations) and [staggered animations](/ui/animations/staggered-animations).* Checkout the [animation library](https://api.flutter.dev/flutter/animation/animation-library.html).* Explore other [Flutter learning resources](/reference/learning-resources).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/codelabs/implicit-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/codelabs/implicit-animations.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/codelabs/implicit-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/codelabs/implicit-animations.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-02. [View source](https://github.com/flutter/website/tree/main/src/content/codelabs/implicit-animations.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/codelabs/implicit-animations/&page-source=https://github.com/flutter/website/tree/main/src/content/codelabs/implicit-animations.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    