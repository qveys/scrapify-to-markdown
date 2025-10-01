Migration guide for describeEnum and EnumProperty
=================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for describeEnum and EnumProperty](/release/breaking-changes/describe-enum)

Summary
-------

[#](#summary)

The global method `describeEnum` has been deprecated. Previous uses of `describeEnum(Enum.something)` should use `Enum.something.name` instead.

The class `EnumProperty` was modified to extend `<T extends Enum?>` instead of `<T>`. Existing uses of `EnumProperty<NotAnEnum>` should use `DiagnosticsProperty<NotAnEnum>` instead.

Context
-------

[#](#context)

Dart 2.17 introduced [enhanced enums](https://dart.dev/language/enums#declaring-enhanced-enums), which added `Enum` as a type. As a result, all enums got a `name` getter, which made `describeEnum` redundant. Before that, enum classes were often analyzed using an `EnumProperty`.

The `describeEnum` method was used to convert an enum value to a string, since `Enum.something.toString()` would produce `Enum.something` instead of `something`, which a lot of users wanted. Now, the `name` getter does this.

The `describeEnum` function is being deprecated, so the `EnumProperty` class is updated to only accept `Enum` objects.

Description of change
---------------------

[#](#description-of-change)

Remove `describeEnum`.

* Replace `describeEnum(Enum.something)` with `Enum.something.name`.

The `EnumProperty` now expects null or an `Enum`; you can no longer pass it a non-`Enum` class.

Migration guide
---------------

[#](#migration-guide)

If you previously used `describeEnum(Enum.field)` to access the string value from an enum, you can now call `Enum.field.name`.

If you previously used `EnumProperty<NotAnEnum>`, you can now use the generic `DiagnosticsProperty<NotAnEnum>`.

Code before migration:

dart

```
enum MyEnum { paper, rock }

print(describeEnum(MyEnum.paper)); // output: paper

// TextInputType is not an Enum
properties.add(EnumProperty<TextInputType>( ... ));
```

Code after migration:

dart

```
enum MyEnum { paper, rock }

print(MyEnum.paper.name); // output: paper

// TextInputType is not an Enum
properties.add(DiagnosticsProperty<TextInputType>( ... ));
```

Timeline
--------

[#](#timeline)

Landed in version: 3.14.0-2.0.pre  
 In stable release: 3.16

References
----------

[#](#references)

API documentation:

* [`describeEnum`](https://api.flutter.dev/flutter/foundation/describeEnum.html)* [`EnumProperty`](https://api.flutter.dev/flutter/foundation/EnumProperty-class.html)

Relevant issues:

* [Cleanup SemanticsFlag and SemanticsAction issue](https://github.com/flutter/flutter/issues/123346)

Relevant PRs:

* [Deprecate `describeEnum` PR](https://github.com/flutter/flutter/pull/125016)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/describe-enum/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/describe-enum.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/describe-enum/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/describe-enum.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-03-18. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/describe-enum.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/describe-enum/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/describe-enum.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   