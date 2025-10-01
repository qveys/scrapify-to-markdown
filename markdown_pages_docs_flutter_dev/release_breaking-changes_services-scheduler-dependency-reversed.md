Reversing the dependency between the scheduler and services layer
=================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Reversing the dependency between the scheduler and services layer](/release/breaking-changes/services-scheduler-dependency-reversed)

Summary
-------

[#](#summary)

The services layer now depends on the scheduler layer. Previously, the opposite was true. This may affect you if you have defined custom bindings overriding Flutter's `SchedulerBinding` or `ServicesBinding`.

Context
-------

[#](#context)

Prior to this change, the scheduler layer was dependent on the services layer. This change reverses the dependency chain and allows the services layer to make use of the scheduling primitives in the scheduler layer. For example, services in the services layer can now schedule tasks by using `SchedulerBinding.scheduleTask`.

Description of change
---------------------

[#](#description-of-change)

The change only affects users who are defining their own custom bindings based on Flutter's `SchedulerBinding` and `ServicesBinding`.

Migration guide
---------------

[#](#migration-guide)

Prior to this change, the `ServiceBinding` had to be defined before the `SchedulerBinding`. With this change, it is the other way around:

Code before migration:

dart

```
class FooBinding extends BindingBase with ServicesBinding, SchedulerBinding {
 // ...
}
```

Code after migration:

dart

```
class FooBinding extends BindingBase with SchedulerBinding, ServicesBinding {
 // ...
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.18.0  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`ServicesBinding`](https://api.flutter.dev/flutter/scheduler/ServicesBinding-mixin.html)* [`SchedulerBinding`](https://api.flutter.dev/flutter/scheduler/SchedulerBinding-mixin.html)

Relevant PRs:

* [Reverse dependency between services and scheduler](https://github.com/flutter/flutter/pull/54212)* [Revert bindings dependency workaround](https://github.com/flutter/flutter/pull/54286)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/services-scheduler-dependency-reversed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/services-scheduler-dependency-reversed.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/services-scheduler-dependency-reversed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/services-scheduler-dependency-reversed.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/services-scheduler-dependency-reversed.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/services-scheduler-dependency-reversed/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/services-scheduler-dependency-reversed.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   