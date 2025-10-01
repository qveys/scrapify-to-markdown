Migrate useDeleteButtonTooltip to deleteButtonTooltipMessage of Chips
=====================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migrate useDeleteButtonTooltip to deleteButtonTooltipMessage of Chips](/release/breaking-changes/chip-usedeletebuttontooltip-migration)

Summary
-------

[#](#summary)

Using `useDeleteButtonTooltip` of any chip that has a delete button gives a deprecation warning, or no longer exists when referenced. This includes the `Chip`, `InputChip`, and `RawChip` widgets.

Context
-------

[#](#context)

The `useDeleteButtonTooltip` of `Chip`, `InputChip`, and `RawChip` widgets is deprecated in favor of `deleteButtonTooltipMessage`, as the latter can be used to disable the tooltip of the chip's delete button.

Description of change
---------------------

[#](#description-of-change)

The `deleteButtonTooltipMessage` property provides a message to the tooltip on the delete button of the chip widgets. Subsequently, a change was made such that providing an empty string to this property disables the tooltip.

To avoid redundancy of the API, this change deprecated `useDeleteButtonTooltip`, which was introduced for this exact functionality. A [Flutter fix](/tools/flutter-fix) is available to help you migrate existing code from `useDeleteButtonTooltip` to `deleteButtonTooltipMessage`, if you explicitly disabled the tooltip.

Migration guide
---------------

[#](#migration-guide)

By default, the tooltip of the delete button is always enabled. To explicitly disable the tooltip, provide an empty string to the `deleteButtonTooltipMessage` property. The following code snippets show the migration changes, which are applicable for `Chip`, `InputChip`, and `RawChip` widgets:

Code before migration:

dart

```
Chip(
  label: const Text('Disabled delete button tooltip'),
  onDeleted: _handleDeleteChip,
  useDeleteButtonTooltip: false,
);

RawChip(
  label: const Text('Enabled delete button tooltip'),
  onDeleted: _handleDeleteChip,
  useDeleteButtonTooltip: true,
);
```

Code after migration:

dart

```
Chip(
  label: const Text('Disabled delete button tooltip'),
  onDeleted: _handleDeleteChip,
  deleteButtonTooltipMessage: '',
);

RawChip(
  label: const Text('Enabled delete button tooltip'),
  onDeleted: _handleDeleteChip,
);
```

Timeline
--------

[#](#timeline)

Landed in version: 2.11.0-0.1.pre  
 In stable release: 3.0.0

References
----------

[#](#references)

API documentation:

* [`Chip`](https://api.flutter.dev/flutter/material/Chip-class.html)* [`InputChip`](https://api.flutter.dev/flutter/material/InputChip-class.html)* [`RawChip`](https://api.flutter.dev/flutter/material/RawChip-class.html)

Relevant PR:

* [Deprecate `useDeleteButtonTooltip` for Chips](https://github.com/flutter/flutter/pull/96174)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/chip-usedeletebuttontooltip-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/chip-usedeletebuttontooltip-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/chip-usedeletebuttontooltip-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/chip-usedeletebuttontooltip-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/chip-usedeletebuttontooltip-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/chip-usedeletebuttontooltip-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/chip-usedeletebuttontooltip-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   