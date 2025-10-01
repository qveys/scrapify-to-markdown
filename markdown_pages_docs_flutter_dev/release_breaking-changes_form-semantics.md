The Form widget no longer supports being a sliver.
==================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [The Form widget no longer supports being a sliver.](/release/breaking-changes/form-semantics)

Summary
-------

[#](#summary)

Previously, the Form widget essentially acted as a direct wrapper around its child. This design allowed a Form containing a sliver child (e.g., Form(child: other sliver)) to be treated as a sliver itself within a CustomScrollView or similar scrollable parent.

However, This PR introduced a new semantics widget within the Form widget's internal structure. This change alters its rendering behavior, meaning Form can no longer directly function as a sliver.

Context
-------

[#](#context)

This change is part of an ongoing effort to improve the accessibility and semantic understanding of Flutter widgets. By embedding a semantics widget directly within Form, the framework can provide better information to accessibility services.

Description of change
---------------------

[#](#description-of-change)

The core change is the integration of a semantics widget into the Form widget's build method.

Migration guide
---------------

[#](#migration-guide)

If your app does not currently use the Form widget directly as a sliver within a scrollable list (e.g., as a direct child of CustomScrollView's slivers property), then no changes are required.

If your app use Form as a sliver, you will need to wrap the Form widget within a SliverToBoxAdapter. SliverToBoxAdapter is a sliver that contains a single box widget, converting a regular widget into a sliver that can be placed in a CustomScrollView.

Code before migration:

dart

```
sliver: Form(
    key: controller.formKey,
    child: SomeWidgetWithFormFields(),
)
```

Code after migration:

dart

```
sliver: SliverToBoxAdapter(
    child: Form(
        key: controller.formKey,
        child: SomeWidgetWithFormFields(),
    )
)
```

Timeline
--------

[#](#timeline)

Landed in version: 3.35.0-pre  
 In stable release: 3.35

References
----------

[#](#references)

API documentation:

* [`Form`](https://api.flutter.dev/flutter/widgets/Form-class.html)

Relevant issues:

* [Issue 161628](https://github.com/flutter/flutter/issues/161628)

Relevant PRs:

* [PR 170709: Add semantics role for form](https://github.com/flutter/pull/170709)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-semantics.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-semantics.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-semantics.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/form-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/form-semantics.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   