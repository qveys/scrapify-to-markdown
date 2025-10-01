Retrieve the value of a text field
==================================

1. [Cookbook](/cookbook) chevron\_right- [Forms](/cookbook/forms) chevron\_right- [Retrieve the value of a text field](/cookbook/forms/retrieve-input)

In this recipe, learn how to retrieve the text a user has entered into a text field using the following steps:

1. Create a `TextEditingController`.- Supply the `TextEditingController` to a `TextField`.- Display the current value of the text field.

1. Create a `TextEditingController`
-----------------------------------

[#](#1-create-a-texteditingcontroller)

To retrieve the text a user has entered into a text field, create a [`TextEditingController`](https://api.flutter.dev/flutter/widgets/TextEditingController-class.html) and supply it to a `TextField` or `TextFormField`.

*error* Important

Call `dispose` of the `TextEditingController` when you've finished using it. This ensures that you discard any resources used by the object.

dart

```
// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  State<MyCustomForm> createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds the data related to the Form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final myController = TextEditingController();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Fill this out in the next step.
  }
}
```

2. Supply the `TextEditingController` to a `TextField`
------------------------------------------------------

[#](#2-supply-the-texteditingcontroller-to-a-textfield)

Now that you have a `TextEditingController`, wire it up to a text field using the `controller` property:

dart

```
return TextField(controller: myController);
```

3. Display the current value of the text field
----------------------------------------------

[#](#3-display-the-current-value-of-the-text-field)

After supplying the `TextEditingController` to the text field, begin reading values. Use the [`text`](https://api.flutter.dev/flutter/widgets/TextEditingController/text.html) property provided by the `TextEditingController` to retrieve the String that the user has entered into the text field.

The following code displays an alert dialog with the current value of the text field when the user taps a floating action button.

dart

```
FloatingActionButton(
  // When the user presses the button, show an alert dialog containing
  // the text that the user has entered into the text field.
  onPressed: () {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          // Retrieve the text that the user has entered by using the
          // TextEditingController.
          content: Text(myController.text),
        );
      },
    );
  },
  tooltip: 'Show me the value!',
  child: const Icon(Icons.text_fields),
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
    return const MaterialApp(
      title: 'Retrieve Text Input',
      home: MyCustomForm(),
    );
  }
}

// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  State<MyCustomForm> createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds the data related to the Form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final myController = TextEditingController();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Retrieve Text Input')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: TextField(controller: myController),
      ),
      floatingActionButton: FloatingActionButton(
        // When the user presses the button, show an alert dialog containing
        // the text that the user has entered into the text field.
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                // Retrieve the text the that user has entered by using the
                // TextEditingController.
                content: Text(myController.text),
              );
            },
          );
        },
        tooltip: 'Show me the value!',
        child: const Icon(Icons.text_fields),
      ),
    );
  }
}
```

 ![Retrieve Text Input Demo](/assets/images/docs/cookbook/retrieve-input.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/retrieve-input/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/retrieve-input.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/retrieve-input/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/retrieve-input.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/forms/retrieve-input.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/forms/retrieve-input/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/forms/retrieve-input.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

    