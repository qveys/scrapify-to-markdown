Material Chip button semantics
==============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Material Chip button semantics](/release/breaking-changes/material-chip-button-semantics)

Summary
-------

[#](#summary)

Flutter now applies the semantic label of `button` to all interactive [Material Chips](https://m3.material.io/components/chips) for accessibility purposes.

Context
-------

[#](#context)

Interactive Material Chips (namely [`ActionChip`](https://api.flutter.dev/flutter/material/ActionChip-class.html), [`ChoiceChip`](https://api.flutter.dev/flutter/material/ChoiceChip-class.html), [`FilterChip`](https://api.flutter.dev/flutter/material/FilterChip-class.html), and [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html)) are now semantically marked as being buttons. However, the non-interactive information [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html) is not.

Marking Chips as buttons helps accessibility tools, search engines, and other semantic analysis software understand the meaning of an app. For example, it allows screen readers (such as TalkBack on Android and VoiceOver on iOS) to announce a tappable Chip as a "button", which can assist users in navigating your app. Prior to this change, users of accessibility tools may have had a subpar experience, unless you implemented a workaround by manually adding the missing semantics to the Chip widgets in your app.

Description of change
---------------------

[#](#description-of-change)

The outermost [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget that wraps all Chip classes to describe their semantic properties is modified.

The following changes apply to [`ActionChip`](https://api.flutter.dev/flutter/material/ActionChip-class.html), [`ChoiceChip`](https://api.flutter.dev/flutter/material/ChoiceChip-class.html), [`FilterChip`](https://api.flutter.dev/flutter/material/FilterChip-class.html), and [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html):

* The [`button`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/button.html) property is set to `true`.* The [`enabled`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/enabled.html) property reflects whether the Chip is *currently* tappable (by having a callback set).

These property changes bring interactive Chips' semantic behavior in-line with that of other [Material Buttons](https://m3.material.io/components/all-buttons).

For the non-interactive information [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html):

* The [`button`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/button.html) property is set to `false`.* The [`enabled`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/enabled.html) property is set to `null`.

Migration guide
---------------

[#](#migration-guide)

**You might not need to perform any migration.** This change only affects you if you worked around the issue of Material Chips missing `button` semantics by wrapping the widget given to the `label` field of a `Chip` with a `Semantics` widget marked as `button: true`. **In this case, the inner and outer `button` semantics conflict, resulting in the tappable area of the button shrinking down to the size of the label after this change is introduced.** Fix this issue either by deleting that `Semantics` widget and replacing it with its child, or by removing the `button: true` property if other semantic properties still need to be applied to the `label` widget of the Chip.

The following snippets use [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html) as an example, but the same process applies to [`ActionChip`](https://api.flutter.dev/flutter/material/ActionChip-class.html), [`ChoiceChip`](https://api.flutter.dev/flutter/material/ChoiceChip-class.html), and [`FilterChip`](https://api.flutter.dev/flutter/material/FilterChip-class.html) as well.

**Case 1: Remove the `Semantics` widget.**

Code before migration:

dart

```
Widget myInputChip = InputChip(
  onPressed: () {},
  label: Semantics(
    button: true,
    child: Text('My Input Chip'),
  ),
);
```

Code after migration:

dart

```
Widget myInputChip = InputChip(
  onPressed: () {},
  label: Text('My Input Chip'),
);
```

**Case 2: Remove `button:true` from the `Semantics` widget.**

Code before migration:

dart

```
Widget myInputChip = InputChip(
  onPressed: () {},
  label: Semantics(
    button: true,
    hint: 'Example Hint',
    child: Text('My Input Chip'),
  ),
);
```

Code after migration:

dart

```
Widget myInputChip = InputChip(
  onPressed: () {},
  label: Semantics(
    hint: 'Example Hint',
    child: Text('My Input Chip'),
  ),
);
```

Timeline
--------

[#](#timeline)

Landed in version: 1.23.0-7.0.pre  
 In stable release: 2.0.0

References
----------

[#](#references)

API documentation:

* [`ActionChip`](https://api.flutter.dev/flutter/material/ActionChip-class.html)* [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html)* [`ChoiceChip`](https://api.flutter.dev/flutter/material/ChoiceChip-class.html)* [`FilterChip`](https://api.flutter.dev/flutter/material/FilterChip-class.html)* [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html)* [Material Buttons](https://m3.material.io/components/all-buttons)* [Material Chips](https://m3.material.io/components/chips)* [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html)* [`SemanticsProperties.button`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/button.html)* [`SemanticsProperties.enabled`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/enabled.html)

Relevant issue:

* [Issue 58010](https://github.com/flutter/flutter/issues/58010): InputChip doesn't announce any action for a11y on iOS

Relevant PRs:

* [PR 60141](https://github.com/flutter/flutter/pull/60141): Tweaking Material Chip a11y semantics to match buttons* [PR 60645](https://github.com/flutter/flutter/pull/60645): Revert "Tweaking Material Chip a11y semantics to match buttons (#60141)* [PR 61048](https://github.com/flutter/flutter/pull/61048): Re-land "Tweaking Material Chip a11y semantics to match buttons (#60141)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-chip-button-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-chip-button-semantics.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-chip-button-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-chip-button-semantics.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-chip-button-semantics.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/material-chip-button-semantics/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/material-chip-button-semantics.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   