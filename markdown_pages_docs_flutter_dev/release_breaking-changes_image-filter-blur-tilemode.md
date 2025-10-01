ImageFilter.blur default tile mode automatic selection.
=======================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [ImageFilter.blur default tile mode automatic selection.](/release/breaking-changes/image-filter-blur-tilemode)

Summary
-------

[#](#summary)

The `ui.ImageFilter.blur`'s default tile mode is now automatically selected by the backend. Previously `TileMode.clamp` was used unless a different tile mode was specified. Now, the default is `null` and specifies automatic selection unless a specific tile mode is specified.

Background
----------

[#](#background)

`ImageFilter.blur`'s *tile mode* specifies what happens to edge pixels for the applied filter. There are four options:

* `TileMode.clamp` (the previous default)* `Tilemode.repeated`* `TileMode.mirror`* `TileMode.decal`

Previously, if the behavior wasn't specified, `ImageFilter` defaulted to `clamp` mode. This sometimes surprised developers as it didn't always match expectations.

As of this change, the filter automatically selects the following tile modes based on context:

* `decal` with save layers and when applied to individual shape draws (such as with `drawRect` and `drawPath`).* `mirror` with backdrop filters.* `clamp` for `drawImage`.

Migration guide
---------------

[#](#migration-guide)

Only blur image filters that don't specify an explicit tile mode are impacted by this change.

We believe that the new defaults are generally better and would recommend removing any specified blur tile modes.

Code before migration:

dart

```
final filter = ui.ImageFilter.blur(sigmaX: 4, sigmaY: 4, tileMode: TileMode.decal);
```

Code after migration:

dart

```
final filter = ui.ImageFilter.blur(sigmaX: 4, sigmaY: 4);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.28.0-0.1.pre  
 In stable release: 3.29

References
----------

[#](#references)

API documentation:

* [`ImageFilter`](https://api.flutter.dev/flutter/dart-ui/ImageFilter-class.html)* [`TileMode`](https://api.flutter.dev/flutter/dart-ui/TileMode.html)

Relevant issues:

* [Issue #154935](https://github.com/flutter/flutter/issues/154935)* [Issue #110318](https://github.com/flutter/flutter/issues/110318)* [Issue #157693](https://github.com/flutter/flutter/issues/157693)

Relevant PRs:

* [Change default TileMode for blur ImageFilter objects to null](https://github.com/flutter/engine/pull/55552)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-filter-blur-tilemode/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-filter-blur-tilemode.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-filter-blur-tilemode/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-filter-blur-tilemode.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-filter-blur-tilemode.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/image-filter-blur-tilemode/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/image-filter-blur-tilemode.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   