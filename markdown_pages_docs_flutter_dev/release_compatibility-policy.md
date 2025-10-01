Flutter compatibility policy
============================

1. [Stay up to date](/release) chevron\_right- [Flutter compatibility policy](/release/compatibility-policy)

The Flutter team tries to balance the need for API stability with the need to keep evolving APIs to fix bugs, improve API ergonomics, and provide new features in a coherent manner.

To this end, we have created a test registry where you can provide unit tests for your own applications or libraries that we run on every change to help us track changes that would break existing applications. Our commitment is that we won't make any changes that break these tests without working with the developers of those tests to (a) determine if the change is sufficiently valuable, and (b) provide fixes for the code so that the tests continue to pass.

If you would like to provide tests as part of this program, please submit a PR to the [flutter/tests repository](https://github.com/flutter/tests). The [README](https://github.com/flutter/tests#adding-more-tests) on that repository describes the process in detail.

Announcements and migration guides
----------------------------------

[#](#announcements-and-migration-guides)

If we do make a breaking change (defined as a change that caused one or more of these submitted tests to require changes), we will announce the change on our [flutter-announce](https://groups.google.com/forum/#!forum/flutter-announce) mailing list as well as in our release notes.

We provide a list of [guides for migrating code](/release/breaking-changes) affected by breaking changes.

Deprecation policy
------------------

[#](#deprecation-policy)

We will, on occasion, deprecate certain APIs rather than outright break them overnight. This is independent of our compatibility policy which is exclusively based on whether submitted tests fail, as described above.

The Flutter team doesn't remove deprecated APIs on a scheduled basis. If the team removes a deprecated API, it follows the same procedures as those for breaking changes.

Dart and other libraries used by Flutter
----------------------------------------

[#](#dart-and-other-libraries-used-by-flutter)

The Dart language itself has a [separate breaking-change policy](https://github.com/dart-lang/sdk/blob/main/docs/process/breaking-changes.md), with announcements on [Dart announce](https://groups.google.com/a/dartlang.org/g/announce).

In general, the Flutter team doesn't currently have any commitment regarding breaking changes for other dependencies. For example, it's possible that a new version of Flutter using a new version of Skia (the graphics engine used by some platforms on Flutter) or Harfbuzz (the font shaping engine used by Flutter) would have changes that affect contributed tests. Such changes wouldn't necessarily be accompanied by a migration guide.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/compatibility-policy/&page-source=https://github.com/flutter/website/tree/main/src/content/release/compatibility-policy.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/compatibility-policy/&page-source=https://github.com/flutter/website/tree/main/src/content/release/compatibility-policy.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-07-06. [View source](https://github.com/flutter/website/tree/main/src/content/release/compatibility-policy.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/compatibility-policy/&page-source=https://github.com/flutter/website/tree/main/src/content/release/compatibility-policy.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   