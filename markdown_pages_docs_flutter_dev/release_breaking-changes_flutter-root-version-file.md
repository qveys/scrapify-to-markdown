$FLUTTER\_ROOT/bin/cache/flutter.version.json replaces $FLUTTER\_ROOT/version
=============================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [$FLUTTER\_ROOT/bin/cache/flutter.version.json replaces $FLUTTER\_ROOT/version](/release/breaking-changes/flutter-root-version-file)

Summary
-------

[#](#summary)

The `flutter` tool will no longer output the `$FLUTTER_ROOT/version` metadata file, and only output `$FLUTTER_ROOT/bin/cache/flutter.version.json`.

Tools and build scripts that rely on the presence of `$FLUTTER_ROOT/version` need to be updated.

Background
----------

[#](#background)

[In 2023](https://github.com/flutter/flutter/pull/124558), `$FLUTTER_ROOT/bin/cache/fluttter.version.json` was added as a newer file format that replaces `$FLUTTER_ROOT/version`.

So a file that looked something like this:

version

```
3.33.0-1.0.pre-1070
```

Was replaced by something like this:

flutter.version.json

json

```
{
  "frameworkVersion": "3.33.0-1.0.pre-1070",
  "channel": "master",
  "repositoryUrl": "unknown source",
  "frameworkRevision": "be9526fbaaaab9474e95d196b70c41297eeda2d0",
  "frameworkCommitDate": "2025-07-22 11:34:11 -0700",
  "engineRevision": "be9526fbaaaab9474e95d196b70c41297eeda2d0",
  "engineCommitDate": "2025-07-22 18:34:11.000Z",
  "engineContentHash": "70fb28dde094789120421d4e807a9c37a0131296",
  "engineBuildDate": "2025-07-22 11:47:42.829",
  "dartSdkVersion": "3.10.0 (build 3.10.0-15.0.dev)",
  "devToolsVersion": "2.48.0",
  "flutterVersion": "3.33.0-1.0.pre-1070"
}
```

Generating both files is a source of technical debt.

Migration guide
---------------

[#](#migration-guide)

Most Flutter developers don't parse or use this file, but custom tools or CI configurations might.

For example, the Flutter team's own `api.flutter.dev` generation script:

post\_processe\_docs.dart

dart

```
final File versionFile = File('version');
final String version = versionFile.readAsStringSync();
```

Was updated in [172601](https://github.com/flutter/flutter/pull/172601) to:

dart

```
final File versionFile = File(path.join(checkoutPath, 'bin', 'cache', 'flutter.version.json'));
final String version = () {
  final Map<String, Object?> json =
      jsonDecode(versionFile.readAsStringSync()) as Map<String, Object?>;
  return json['flutterVersion']! as String;
}();
```

To temporarily opt-out of `$FLUTTER_ROOT/version` no longer being emitted:

sh

```
flutter config --no-enable-omit-legacy-version-file
```

Timeline
--------

[#](#timeline)

Landed in version: 3.33.0-1.0.pre-1416  
 Stable release: *Not published yet*

One stable release after this change lands, `--no-enable-omit-legacy-version-file` will be removed.

References
----------

[#](#references)

Relevant Issues:

* [Issue 171900](https://github.com/flutter/flutter/issues/171900), where `FLUTTER_ROOT/version` was slated for removal

Relevant PRs:

* [PR 124558](https://github.com/flutter/flutter/pull/124558), where `flutter.version.json` was added as the new format* [PR 172601](https://github.com/flutter/flutter/pull/172601), an example of migrating a script to use `flutter.version.json`

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-root-version-file/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-root-version-file.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-root-version-file/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-root-version-file.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-18. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-root-version-file.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/flutter-root-version-file/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/flutter-root-version-file.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   