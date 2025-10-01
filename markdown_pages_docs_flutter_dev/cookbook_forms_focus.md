Focus and text fields
=====================

1. [Cookbook](/cookbook) chevron\_right- [Forms](/cookbook/forms) chevron\_right- [Focus and text fields](/cookbook/forms/focus)

When a text field is selected and accepting input, it is said to have "focus." Generally, users shift focus to a text field by tapping, and developers shift focus to a text field programmatically by using the tools described in this recipe.

Managing focus is a fundamental tool for creating forms with an intuitive flow. For example, say you have a search screen with a text field. When the user navigates to the search screen, you can set the focus to the text field for the search term. This allows the user to start typing as soon as the screen is visible, without needing to manually tap the text field.

In this recipe, learn how to give the focus to a text field as soon as it's visible, as well as how to give focus to a text field when a button is tapped.

Focus a text field as soon as it's visible
------------------------------------------

[#](#focus-a-text-field-as-soon-as-its-visible)

To give focus to a text field as soon as it's visible, use the `autofocus` property.

dart

```
TextField(
  autofocus: true,
);
```

For more information on handling input and creating text fields, see the [Forms](/cookbook/forms) section of the cookbook.

Focus a text field when a button is tapped
------------------------------------------

[#](#focus-a-text-field-when-a-button-is-tapped)

Rather than immediately shifting focus to a specific text field, you might need to give focus to a text field at a later point in time. In the real world, you might also need to give focus to a specific text field in response to an API call or a validation error. In this example, give focus to a text field after the user presses a button using the following steps:

1. Create a `FocusNode`.- Pass the `FocusNode` to a `TextField`.- Give focus to the `TextField` when a button is tapped.

### 1. Create a `FocusNode`

[#](#1-create-a-focusnode)

First, create a [`FocusNode`](https://api.flutter.dev/flutter/widgets/FocusNode-class.html). Use the `FocusNode` to identify a specific `TextField` in Flutter's "focus tree." This allows you to give focus to the `TextField` in the next steps.

Since focus nodes are long-lived objects, manage the lifecycle using a `State` object. Use the following instructions to create a `FocusNode` instance inside the `initState()` method of a `State` class, and clean it up in the `dispose()` method:

dart

```
// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  State<MyCustomForm> createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds data related to the form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Define the focus node. To manage the lifecycle, create the FocusNode in
  // the initState method, and clean it up in the dispose method.
  late FocusNode myFocusNode;

  @override
  void initState() {
    super.initState();

    myFocusNode = FocusNode();
  }

  @override
  void dispose() {
    // Clean up the focus node when the Form is disposed.
    myFocusNode.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Fill this out in the next step.
  }
}
```

### 2. Pass the `FocusNode` to a `TextField`

[#](#2-pass-the-focusnode-to-a-textfield)

Now that you have a `FocusNode`, pass it to a specific `TextField` in the `build()` method.

dart

```
@override
Widget build(BuildContext context) {
  return TextField(focusNode: myFocusNode);
}
```

### 3. Give focus to the `TextField` when a button is tapped

[#](#3-give-focus-to-the-textfield-when-a-button-is-tapped)

Finally, focus the text field when the user taps a floating action button. Use the [`requestFocus()`](https://api.flutter.dev/flutter/widgets/FocusNode/requestFocus.html) method to perform this task.

dart

```
FloatingActionButton(
  // When the button is pressed,
  // give focus to the text field using myFocusNode.
  onPressed: () => myFocusNode.requestFocus(),
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
    return const MaterialApp(title: 'Text Field Focus', home: MyCustomForm());
  }
}

// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  State<MyCustomForm> createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds data related to the form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Define the focus node. To manage the lifecycle, create the FocusNode in
  // the initState method, and clean it up in the dispose method.
  late FocusNode myFocusNode;

  @override
  void initState() {
    super.initState();

    myFocusNode = FocusNode();
  }

  @override
  void dispose() {
    // Clean up the focus node when the Form is disposed.
    myFocusNode.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Text Field Focus')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // The first text field is focused on as soon as the app starts.
            const TextField(autofocus: true),
            // The second text field is focused on when a user taps the
            // FloatingActionButton.
            TextField(focusNode: myFocusNode),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        // When the button is pressed,
        // give focus to the text field using myFocusNode.
        onPressed: () => myFocusNode.requestFocus(),
        tooltip: 'Focus Second Text Field',
        child: const Icon(Icons.edit),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
```

 ![Text Field Focus Demo](/assets/images/docs/cookbook/focus.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/focus/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/focus.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/focus/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/focus.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-02. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/forms/focus.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/focus/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/focus.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    