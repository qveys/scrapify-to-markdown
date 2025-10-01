SnackBar with action no longer auto-dismisses
=============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [SnackBar with action no longer auto-dismisses](/release/breaking-changes/snackbar-with-action-behavior-update)

Summary
-------

[#](#summary)

The default behavior of a [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html) with an action has changed. Previously, a `SnackBar` with an action would not auto-dismiss if talkback was enabled. Now, all `SnackBar`s with an action default to a non-dismissible state until the user interacts with the action button.

Context
-------

[#](#context)

A `SnackBar` with an action button is now treated as a more persistent notification that requires user interaction. This change improves accessibility and user experience by ensuring that critical notifications remain on the screen until they are acknowledged.

Description of change
---------------------

[#](#description-of-change)

This change aligns with the Material 3 design specifications for `SnackBar`s:

* Old behavior: A `SnackBar` with an action button would auto-dismiss after a duration unless talkback was enabled.* New behavior: A `SnackBar` with an action button won't auto-dismiss; it remains on screen until dismissed by the user.

To override this behavior, an optional `persist` property has been added to `SnackBar`. When `persist` is true, the `SnackBar` won't auto-dismiss  
 and remains on screen until manually dismissed by the user. When false, the `SnackBar` auto-dismisses after its standard duration, regardless of the presence of an action. When null, the `SnackBar` follows the default behavior, which won't auto-dismiss if an action is present.

Migration guide
---------------

[#](#migration-guide)

To restore the old auto-dismiss behavior for a SnackBar with an action, set `persist` to false.

Code before migration:

dart

```
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: const Text('This is a snackbar with an action.'),
    action: SnackBarAction(
      label: 'Action',
      onPressed: () {
        // Perform some action
      },
    ),
  ),
);
```

Code after migration:

dart

```
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: const Text('This is a snackbar with an action.'),
    persist: false, // Add this line to restore auto-dismiss behavior
    action: SnackBarAction(
      label: 'Action',
      onPressed: () {
        // Perform some action
      },
    ),
  ),
);
```

Timeline
--------

[#](#timeline)

Landed in version: TBD In stable release: TBD

References
----------

[#](#references)

API documentation:

* [`SnackBar`](https://api.flutter.dev/flutter/material/SnackBar-class.html)

Relevant PRs:

* [SnackBar with action no longer auto-dismisses](https://github.com/flutter/flutter/pull/173084)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/snackbar-with-action-behavior-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/snackbar-with-action-behavior-update.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/snackbar-with-action-behavior-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/snackbar-with-action-behavior-update.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-25. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/snackbar-with-action-behavior-update.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/snackbar-with-action-behavior-update/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/snackbar-with-action-behavior-update.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   