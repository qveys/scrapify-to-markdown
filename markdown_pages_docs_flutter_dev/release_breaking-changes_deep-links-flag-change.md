Deep links flag change
======================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Deep links flag change](/release/breaking-changes/deep-links-flag-change)

Summary
-------

[#](#summary)

**This breaking change only affects mobile apps that use a third party deep linking plugin package.**

The default value for Flutter's deep linking option has changed from `false` to `true`, meaning that deep linking is now opt-in by default.

Migration guide
---------------

[#](#migration-guide)

If you're using Flutter's default deep linking setup, this isn't a breaking change for you.

However, if you're using a third-party plugin for deep links, such as the following, this update introduces a breaking change:

* [Firebase dynamic links](https://firebase.google.com/docs/dynamic-links)* [`package:uni_link`](https://pub.dev/packages/uni_links)* [`package:app_links`](https://pub.dev/packages/app_links)* [`package:flutter_branch_sdk`](https://pub.dev/packages/flutter_branch_sdk)

In this case, you must manually reset the Flutter deep linking option to `false`.

Within your app's `AndroidManifest.xml` file for Android:

AndroidManifest.xml

xml

```
<manifest>
   <application
       <activity>
<meta-data android:name="flutter_deeplinking_enabled" android:value="false" />
       </activity>
   </application>
</manifest>
```

Within your app's `info.plist` file for iOS:

info.plist

xml

```
 <key>FlutterDeepLinkingEnabled</key>
 <false/>
```

Timeline
--------

[#](#timeline)

Landed in version: 3.25.0-0.1.pre  
 Stable release: 3.27

References
----------

[#](#references)

Design document:

* [flutter.dev/go/deep-link-flag-migration](https://flutter.dev/go/deep-link-flag-migration)

Relevant PR:

* [Set deep linking flag to true by default](https://github.com/flutter/engine/pull/52350)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deep-links-flag-change/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deep-links-flag-change.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deep-links-flag-change/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deep-links-flag-change.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-13. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deep-links-flag-change.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/deep-links-flag-change/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/deep-links-flag-change.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   