Localized messages are generated into source, not a synthetic package.
======================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Localized messages are generated into source, not a synthetic package.](/release/breaking-changes/flutter-generate-i10n-source)

Summary
-------

[#](#summary)

The `flutter` tool will no longer generate a synthetic `package:flutter_gen` or modify the `package_config.json` of the app.

Applications or tools that referenced `package:flutter_gen` should instead reference source files generated into the app's source directory directly.

In addition, the property `generate: true` is now required when using generated l10n source.

Background
----------

[#](#background)

`flutter_gen` is a virtual (synthetic) package that is created by the `flutter` command-line tool to allow developers to import that package to access generated symbols and functionality, such as for [internationalization](/ui/accessibility-and-internationalization/internationalization#adding-your-own-localized-messages). As the package isn't listed in an app's `pubspec.yaml`, and is created via re-writing the generated `package_config.json` file, many problems have been created.

Migration guide
---------------

[#](#migration-guide)

This change only affects apps that have the following entry in their `pubspec.yaml`:

yaml

```
flutter:
  generate: true
```

If your app previously used `gen-l10n` without this property, it is now required.

A synthetic package (`package:flutter_gen`) is created and referenced by the app:

dart

```
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
// ...
const MaterialApp(
  title: 'Localizations Sample App',
  localizationsDelegates: AppLocalizations.localizationsDelegates,
  supportedLocales: AppLocalizations.supportedLocales,
);
```

There are two ways to migrate away from importing `package:flutter_gen`:

1. Specify `synthetic-package: false` in the accompanying [`l10n.yaml`](/ui/accessibility-and-internationalization/internationalization#configuring-the-l10n-yaml-file) file:

   l10n.yaml

   yaml

   ```
   synthetic-package: false

   # The files are generated into the path specified by `arb-dir`
   arb-dir: lib/i18n

   # Or, specifically provide an output path:
   output-dir: lib/src/generated/i18n
   ```

   - Enable the `explicit-package-dependencies` feature flag:

     sh

     ```
     flutter config --explicit-package-dependencies
     ```

Timeline
--------

[#](#timeline)

Landed in version: 3.28.0-0.0.pre  
 Stable release: 3.32.0

**In the next stable release after this change lands, `package:flutter_gen` support will be removed.**

References
----------

[#](#references)

Relevant Issues:

* [Issue 73870](https://github.com/flutter/flutter/issues/73870), where `package:flutter_gen` pub problems are first found.* [Issue 102983](https://github.com/flutter/flutter/issues/102983), where `package:flutter_gen` problems are outlined.* [Issue 157819](https://github.com/flutter/flutter/issues/157819), where `--implicit-pubspec-resolution` is discussed.

Relevant Articles:

* [Internationalizing Flutter apps](/ui/accessibility-and-internationalization/internationalization#adding-your-own-localized-messages), the canonical documentation for the feature.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-generate-i10n-source/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-generate-i10n-source.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-generate-i10n-source/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-generate-i10n-source.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-18. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-generate-i10n-source.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-generate-i10n-source/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-generate-i10n-source.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   