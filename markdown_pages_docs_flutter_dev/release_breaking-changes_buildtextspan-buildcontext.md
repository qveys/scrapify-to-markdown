Added BuildContext parameter to TextEditingController.buildTextSpan
===================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Added BuildContext parameter to TextEditingController.buildTextSpan](/release/breaking-changes/buildtextspan-buildcontext)

Summary
-------

[#](#summary)

A `BuildContext` parameter was added to `TextEditingController.buildTextSpan`.

Classes that extend or implement `TextEditingController` and override `buildTextSpan` need to add the `BuildContext` parameter to the signature to make it a valid override.

Callers of `TextEditingController.buildTextSpan` need to pass a `BuildContext` to the call.

Context
-------

[#](#context)

`TextEditingController.buildTextSpan` is called by `EditableText` on its controller to create the `TextSpan` that it renders. `buildTextSpan` can be overridden in custom classes that extend `TextEditingController`. This allows classes extending `TextEditingController` override `buildTextSpan` to change the style of parts of the text, for example, for rich text editing.

Any state that is required by `buildTextSpan` (other than the `TextStyle` and `withComposing` arguments) needed to be passed into the class that extends `TextEditingController`.

Description of change
---------------------

[#](#description-of-change)

With the `BuildContext` available, users can access `InheritedWidgets` inside `buildTextSpan` to retrieve state required to style the text, or otherwise manipulate the created `TextSpan`.

Consider the example where we have a `HighlightTextEditingController` that wants to highlight text by setting its color to `Theme.accentColor`.

Before this change the controller implementation would look like this:

dart

```
class HighlightTextEditingController extends TextEditingController {
  HighlightTextEditingController(this.highlightColor);

  final Color highlightColor;

  @override
  TextSpan buildTextSpan({TextStyle? style, required bool withComposing}) {
    return super.buildTextSpan(style: TextStyle(color: highlightColor), withComposing: withComposing);
  }
```

And users of the controller would need to pass the color when creating the controller.

With the `BuildContext` parameter available, the `HighlightTextEditingController` can directly access `Theme.accentColor` using `Theme.of(BuildContext)`:

dart

```
class HighlightTextEditingController extends TextEditingController {
  @override
  TextSpan buildTextSpan({required BuildContext context, TextStyle? style, required bool withComposing}) {
    final Color color = Theme.of(context).accentColor;
    return super.buildTextSpan(context: context, style: TextStyle(color: color), withComposing: withComposing);
  }
}
```

Migration guide
---------------

[#](#migration-guide)

### Overriding `TextEditingController.buildTextSpan`

[#](#overriding-texteditingcontroller-buildtextspan)

Add a `required BuildContext context` parameter to the signature of the `buildTextSpan` override.

Code before migration:

dart

```
class MyTextEditingController {
  @override
  TextSpan buildTextSpan({TextStyle? style, required bool withComposing}) {
    /* ... */
  }
}
```

Example error message before migration:

```
'MyTextEditingController.buildTextSpan' ('TextSpan Function({TextStyle? style, required bool withComposing})') isn't a valid override of 'TextEditingController.buildTextSpan' ('TextSpan Function({required BuildContext context, TextStyle? style, required bool withComposing})').
```

Code after migration:

dart

```
class MyTextEditingController {
  @override
  TextSpan buildTextSpan({required BuildContext context, TextStyle? style, required bool withComposing}) {
    /* ... */
  }
}
```

### Calling `TextEditingController.buildTextSpan`

[#](#calling-texteditingcontroller-buildtextspan)

Pass a named parameter 'context' of type `BuildContext` to the call.

Code before migration:

dart

```
TextEditingController controller = /* ... */;
TextSpan span = controller.buildTextSpan(withComposing: false);
```

Error message before migration:

```
The named parameter 'context' is required, but there's no corresponding argument.
Try adding the required argument.
```

Code after migration:

dart

```
BuildContext context = /* ... */;
TextEditingController controller = /* ... */;
TextSpan span = controller.buildTextSpan(context: context, withComposing: false);
```

Timeline
--------

[#](#timeline)

Landed in version: 1.26.0  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`TextEditingController.buildTextSpan`](https://api.flutter.dev/flutter/widgets/TextEditingController/buildTextSpan.html)

Relevant issues:

* [Issue #72343](https://github.com/flutter/flutter/issues/72343)

Relevant PRs:

* [Reland "Add BuildContext parameter to TextEditingController.buildTextSpan" #73510](https://github.com/flutter/flutter/pull/73510)* [Revert "Add BuildContext parameter to TextEditingController.buildTextSpan" #73503](https://github.com/flutter/flutter/pull/73503)* [Add BuildContext parameter to TextEditingController.buildTextSpan #72344](https://github.com/flutter/flutter/pull/72344)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/buildtextspan-buildcontext/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/buildtextspan-buildcontext.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/buildtextspan-buildcontext/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/buildtextspan-buildcontext.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/buildtextspan-buildcontext.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/buildtextspan-buildcontext/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/buildtextspan-buildcontext.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   