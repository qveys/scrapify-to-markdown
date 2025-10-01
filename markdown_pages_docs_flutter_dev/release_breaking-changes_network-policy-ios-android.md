Insecure HTTP connections are disabled by default on iOS and Android
====================================================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Insecure HTTP connections are disabled by default on iOS and Android](/release/breaking-changes/network-policy-ios-android)

Summary
-------

[#](#summary)

If your code tries to open an HTTP connection to a host on iOS or Android, a `StateException` is now thrown with the following message:

```
Insecure HTTP is not allowed by platform: <host>
```

Use HTTPS instead.

*error* Important

This change over-restricted HTTP access on local networks beyond the restrictions imposed by mobile platforms ([flutter/flutter#72723](https://github.com/flutter/flutter/issues/72723)).

This change has since been reverted.

Context
-------

[#](#context)

Starting with Android [API 28](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted) and [iOS 9](https://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity), these platforms disable insecure HTTP connections by default.

With this change Flutter also disables insecure connections on mobile platforms. Other platforms (desktop, web, etc) are not affected.

You can override this behavior by following the platform-specific guidelines to define a domain-specific network policy. See the migration guide below for details.

Much like the platforms, the application can still open insecure socket connections. Flutter does not enforce any policy at socket level; you would be responsible for securing the connection.

Migration guide
---------------

[#](#migration-guide)

On iOS, you can add [NSExceptionDomains](https://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity/nsexceptiondomains) to your application's Info.plist.

On Android, you can add a [network security config](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted) XML. For Flutter to find your XML file, you need to also add a `metadata` entry to the `<application>` tag in your manifest. This metadata entry should carry the name: `io.flutter.network-policy` and should contain the resource identifier of the XML.

For instance, if you put your XML configuration under `res/xml/network_security_config.xml`, your manifest would contain the following:

xml

```
<application ...>
  ...
  <meta-data android:name="io.flutter.network-policy"
             android:resource="@xml/network_security_config"/>
</application>
```

### Allowing cleartext connection for debug builds

[#](#allowing-cleartext-connection-for-debug-builds)

If you would like to allow HTTP connections for Android debug builds, you can add the following snippet to your $project\_path\android\app\src\debug\AndroidManifest.xml:

xml

```
<application android:usesCleartextTraffic="true"/>
```

For iOS, you can follow [these instructions](/add-to-app/ios/project-setup/?tab=embed-using-cocoapods#set-local-network-privacy-permissions) to create a `Info-debug.plist` and put this in:

xml

```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

We **do not** recommend you do this for your release builds.

Additional Information
----------------------

[#](#additional-information)

* Build time configuration is the only way to change network policy. It cannot be modified at runtime.* Localhost connections are always allowed.* You can allow insecure connections only to domains. Specific IP addresses are not accepted as input. This is in line with what platforms support. If you would like to allow IP addresses, the only option is to allow cleartext connections in your app.

Timeline
--------

[#](#timeline)

Landed in version: 1.23  
 In stable release: 2.0.0  
 Reverted in version: 2.2.0 (proposed)

References
----------

[#](#references)

API documentation: There's no API for this change since the modification to network policy is done through the platform specific configuration as detailed above.

Relevant PRs:

* [PR 20218: Plumbing for setting domain network policy](https://github.com/flutter/engine/pull/20218)* [Introduce per-domain policy for strict secure connections](https://github.com/dart-lang/sdk/commit/d878cfbf20375befa09f9bf85f0ba2b87b319427)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/network-policy-ios-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/network-policy-ios-android.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/network-policy-ios-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/network-policy-ios-android.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-06-17. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/network-policy-ios-android.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/network-policy-ios-android/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/network-policy-ios-android.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   