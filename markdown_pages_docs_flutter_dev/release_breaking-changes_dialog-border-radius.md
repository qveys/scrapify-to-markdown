Dialogs' Default BorderRadius
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Dialogs' Default BorderRadius](/release/breaking-changes/dialog-border-radius)

Summary
-------

[#](#summary)

Instances of `Dialog`, as well as `SimpleDialog`, `AlertDialog`, and `showTimePicker`, now have a default shape of a `RoundedRectangleBorder` with a `BorderRadius` of 4.0 pixels. This matches the current specifications of Material Design. Prior to this change, the default behavior for `Dialog.shape`'s `BorderRadius` was 2.0 pixels.

Context
-------

[#](#context)

`Dialog`s and their associated subclasses (`SimpleDialog`, `AlertDialog`, and `showTimePicker`), appears slightly different as the border radius is larger. If you have master golden file images that have the prior rendering of the `Dialog` with a 2.0 pixel border radius, your widget tests will fail. These golden file images can be updated to reflect the new rendering, or you can update your code to maintain the original behavior.

The `showDatePicker` dialog already matched this specification and is unaffected by this change.

Migration guide
---------------

[#](#migration-guide)

If you prefer to maintain the old shape, you can use the shape property of your `Dialog` to specify the original 2 pixel radius.

Setting the Dialog shape to the original radius:

dart

```
import 'package:flutter/material.dart';

void main() => runApp(Foo());

class Foo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        floatingActionButton: FloatingActionButton(onPressed: () {
          showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                content: Text('Alert!'),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(2))),
              );
            },
          );
        }),
      ),
    );
  }
}
```

If you prefer the new behavior and have failing golden file tests, you can update your master golden files using this command:

```
flutter test --update-goldens
```

Timeline
--------

[#](#timeline)

Landed in version: 1.20.0-0.0.pre  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`Dialog`](https://api.flutter.dev/flutter/material/Dialog-class.html)* [`SimpleDialog`](https://api.flutter.dev/flutter/material/SimpleDialog-class.html)* [`AlertDialog`](https://api.flutter.dev/flutter/material/AlertDialog-class.html)* [`showTimePicker`](https://api.flutter.dev/flutter/material/showTimePicker.html)* [`showDatePicker`](https://api.flutter.dev/flutter/material/showDatePicker.html)

Relevant PR:

* [PR 58829: Matching Material Spec for Dialog shape](https://github.com/flutter/flutter/pull/58829)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dialog-border-radius/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dialog-border-radius.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dialog-border-radius/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dialog-border-radius.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dialog-border-radius.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/dialog-border-radius/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/dialog-border-radius.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   