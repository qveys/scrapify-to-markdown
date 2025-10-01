The new Form, FormField auto-validation API
===========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [The new Form, FormField auto-validation API](/release/breaking-changes/form-field-autovalidation-api)

Summary
-------

[#](#summary)

The previous auto validation API for the `Form` and `FormField` widgets didn't control when auto validation should occur. So the auto validation for these widgets always happened on first build when the widget was first visible to the user, and you weren't able to control when the auto validation should happen.

Context
-------

[#](#context)

Due to the original API not allowing developers to change the auto validation behavior for validating only when the user interacts with the form field, we added new API that allows developers to configure how they want auto validation to behave for the `Form` and `FormField` widgets.

Description of change
---------------------

[#](#description-of-change)

The following changes were made:

* The `autovalidate` parameter is deprecated.* A new parameter called `autovalidateMode`, an Enum that accepts values from the `AutovalidateMode` Enum class, is added.

Migration guide
---------------

[#](#migration-guide)

To migrate to the new auto validation API you need to replace the usage of the deprecated `autovalidate` parameter to the new `autovalidateMode` parameter. If you want the same behavior as before you can use: `autovalidateMode = AutovalidateMode.always`. This makes your `Form` and `FormField` widgets auto validate on first build and every time it changes.

Code before migration:

dart

```
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FormField(
      autovalidate: true,
      builder: (FormFieldState state) {
        return Container();
      },
    );
  }
}
```

Code after migration:

dart

```
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FormField(
      autovalidateMode: AutovalidateMode.always,
      builder: (FormFieldState state) {
        return Container();
      },
    );
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.21.0-5.0.pre  
 In stable release: 1.22

References
----------

[#](#references)

API documentation:

* [`AutovalidateMode`](https://api.flutter.dev/flutter/widgets/AutovalidateMode.html)

Relevant issues:

* [Issue 56363](https://github.com/flutter/flutter/issues/56363)* [Issue 18885](https://github.com/flutter/flutter/issues/18885)* [Issue 15404](https://github.com/flutter/flutter/issues/15404)* [Issue 36154](https://github.com/flutter/flutter/issues/36154)* [Issue 48876](https://github.com/flutter/flutter/issues/48876)

Relevant PRs:

* [PR 56365: FormField should autovalidate only if its content was changed](https://github.com/flutter/pull/56365)* [PR 59766: FormField should autovalidate only if its content was changed (fixed)](https://github.com/flutter/flutter/pull/59766)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-field-autovalidation-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-field-autovalidation-api.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-field-autovalidation-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-field-autovalidation-api.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-field-autovalidation-api.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-field-autovalidation-api/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-field-autovalidation-api.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   