Removal of AssetManifest.json
=============================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Removal of AssetManifest.json](/release/breaking-changes/asset-manifest-dot-json)

Summary
-------

[#](#summary)

Flutter apps included an asset file named `AssetManifest.json`. This file effectively contains a list of assets. Application code can read it using the [`AssetBundle`](https://api.flutter.dev/flutter/services/AssetBundle-class.html) API to determine what assets are available at runtime.

The `AssetManifest.json` file is an undocumented implementation detail. It's no longer used by the framework, and it's planned to no longer generate it in a future release of Flutter. If your app's code needs to get a list of available assets, use the [`AssetManifest`](https://api.flutter.dev/flutter/services/AssetManifest-class.html) API instead.

Migration guide
---------------

[#](#migration-guide)

### Reading asset manifest from Flutter application code

[#](#reading-asset-manifest-from-flutter-application-code)

Before:

dart

```
import 'dart:convert';
import 'package:flutter/services.dart';

void readAssetList() async {
  final assetManifestContent = await rootBundle.loadString('AssetManifest.json');
  final decodedAssetManifest =
      json.decode(assetManifestContent) as Map<String, Object?>;
  final assets = decodedAssetManifest.keys.toList().cast<String>();
}
```

After:

dart

```
import 'package:flutter/services.dart';

void readAssetList() async {
  final assetManifest = await AssetManifest.loadFromAssetBundle(rootBundle);
  final assets = assetManifest.listAssets();
}
```

### Reading asset manifest information from Dart code outside of a Flutter app

[#](#reading-asset-manifest-information-from-dart-code-outside-of-a-flutter-app)

The `flutter` CLI tool generates a new file, `AssetManifest.bin`. This replaces `AssetManifest.json`. This file contains the same information as `AssetManifest.json`, but in a different format. If you need to read this file from code that isn't part of a Flutter app, and therefore can't use the [`AssetManifest`](https://api.flutter.dev/flutter/services/AssetManifest-class.html) API, you can still parse the file yourself.

The [`standard_message_codec`](https://pub.dev/packages/standard_message_codec) package can be used to parse the contents.

dart

```
import 'dart:io';
import 'dart:typed_data';

import 'package:standard_message_codec/standard_message_codec.dart';

void main() {
  // The path to AssetManifest.bin depends on the target platform.
  final pathToAssetManifest = './build/web/assets/AssetManifest.bin';
  final manifest = File(pathToAssetManifest).readAsBytesSync();
  final decoded = const StandardMessageCodec()
      .decodeMessage(ByteData.sublistView(manifest));
  final assets = decoded.keys.cast<String>().toList();
}
```

Keep in mind that `AssetManifest.bin` is an implementation detail of Flutter. Reading this file isn't an officially supported workflow. The contents or format of the file might change in a future Flutter release without an announcement.

Timeline
--------

[#](#timeline)

`AssetManifest.json` will no longer be generated starting with the fourth stable release after 3.19 or one year after the release of 3.19, whichever comes later.

References
----------

[#](#references)

Relevant issues:

* When building a Flutter app, the flutter tool generates an `AssetManifest.json` file that's unused by the framework [(Issue #143577)](https://github.com/flutter/flutter/issues/143577)

Relevant PR:

* [Remove deprecated `AssetManifest.json` file](https://github.com/flutter/flutter/pull/172594)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/asset-manifest-dot-json/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/asset-manifest-dot-json.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/asset-manifest-dot-json/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/asset-manifest-dot-json.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-11. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/asset-manifest-dot-json.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/asset-manifest-dot-json/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/asset-manifest-dot-json.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   