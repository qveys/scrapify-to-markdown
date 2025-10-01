Migration guide for RouteSettings copyWith
==========================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for RouteSettings copyWith](/release/breaking-changes/routesettings-copywith-migration)

Summary
-------

[#](#summary)

The `RouteSettings.copyWith` method is removed, and apps that use it need to use the constructor to create a new `RouteSettings` instance instead.

Context
-------

[#](#context)

With the introduction of the [`Page`](https://api.flutter.dev/flutter/widgets/Page-class.html) class, the `RouteSettings.copyWith` was no longer a viable API.

Description of change
---------------------

[#](#description-of-change)

`RouteSettings.copyWith` was removed

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
RouteSettings newSettings = oldSettings.copyWith(name: 'new name');
```

Code after migration:

dart

```
RouteSettings newSettings = RouteSettings(name: 'new name', arguments: oldSettings.arguments);
```

Timeline
--------

[#](#timeline)

Landed in version: 3.5.0-9.0.pre-137-gc6f6095acd  
 In stable release: 3.7

References
----------

[#](#references)

Relevant PRs:

* [PR 113860](https://github.com/flutter/flutter/pull/113860): Removes RouteSetting.copyWith.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/routesettings-copywith-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/routesettings-copywith-migration.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/routesettings-copywith-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/routesettings-copywith-migration.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/routesettings-copywith-migration.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/routesettings-copywith-migration/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/routesettings-copywith-migration.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   