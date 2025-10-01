Adding TextInputClient.currentAutofillScope property
====================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Adding TextInputClient.currentAutofillScope property](/release/breaking-changes/add-currentAutofillScope-to-TextInputClient)

Summary
-------

[#](#summary)

A new getter, `TextInputClient.currentAutofillScope`, was added to the `TextInputClient` interface; all `TextInputClient` subclasses must provide a concrete implementation of `currentAutofillScope`.

This getter allows the `TextInputClient` to trigger an autofill that involves multiple logically connected input fields. For example, a "username" field can trigger an autofill that fills both itself and the "password" field associated with it.

Context
-------

[#](#context)

On many platforms, autofill services are capable of autofilling multiple input fields in a single autofill attempt. For example, username fields and password fields can usually be autofilled in one go. For this reason, a Flutter input field that is about to trigger autofill should also provide the platform with information about other autofillable input fields logically connected to it. `TextInputClient.currentAutofillScope` defines the group of input fields that are logically connected to this `TextInputClient`, and can be autofilled together.

Description of change
---------------------

[#](#description-of-change)

`TextInputClient` now has an additional getter that returns the `AutofillScope` that this client belongs to. This getter is used by the input client to collect autofill related information from other autofillable input fields within the same scope.

dart

```
abstract class TextInputClient {
  AutofillScope get currentAutofillScope;
}
```

If you see the error message "missing concrete implementation of 'getter TextInputClient.currentAutofillScope'" while compiling a Flutter app, follow the migration steps listed below.

Migration guide
---------------

[#](#migration-guide)

If you're not planning to add multifield autofill support to your `TextInputClient` subclass, simply return `null` in the getter:

dart

```
class CustomTextField implements TextInputClient {
  // Not having an AutofillScope does not prevent the input field
  // from being autofilled. However, only this input field is
  // autofilled when autofill is triggered on it.
  AutofillScope get currentAutofillScope => null;
}
```

If multifield autofill support is desirable, a common `AutofillScope` to use is the `AutofillGroup` widget. To get the closest `AutofillGroup` widget to the text input, use `AutofillGroup.of(context)`:

dart

```
class CustomTextFieldState extends State<CustomTextField> implements TextInputClient {
  AutofillScope get currentAutofillScope => AutofillGroup.of(context);
}
```

For more information, check out [`AutofillGroup`](https://api.flutter.dev/flutter/widgets/AutofillGroup-class.html).

Timeline
--------

[#](#timeline)

Landed in version: 1.18.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`AutofillGroup`](https://api.flutter.dev/flutter/widgets/AutofillGroup-class.html)* [`TextInputClient.currentAutofillScope`](https://api.flutter.dev/flutter/services/TextInputClient/currentAutofillScope.html)

Relevant issue:

* [Issue 13015: Autofill support](https://github.com/flutter/flutter/issues/13015)

Relevant PR:

* [Framework PR that added autofill support](https://github.com/flutter/flutter/pull/52126)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-currentAutofillScope-to-TextInputClient/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-currentAutofillScope-to-TextInputClient.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-currentAutofillScope-to-TextInputClient/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-currentAutofillScope-to-TextInputClient.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-currentAutofillScope-to-TextInputClient.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/add-currentAutofillScope-to-TextInputClient/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/add-currentAutofillScope-to-TextInputClient.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   