Migration guide for `RouteInformation.location`
===============================================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Migration guide for `RouteInformation.location`](/release/breaking-changes/route-information-uri)

Summary
-------

[#](#summary)

`RouteInformation.location` and related APIs were deprecated in the favor of `RouteInformation.uri`.

Context
-------

[#](#context)

The [`RouteInformation`](https://api.flutter.dev/flutter/widgets/RouteInformation-class.html) needs the authority information to handle mobile deeplinks from different web domains. The `uri` field was added to `RouteInformation` that captures the entire deeplink information and route-related parameters were converted to the full [`Uri`](https://api.flutter.dev/flutter/dart-core/Uri-class.html) format. This led to deprecation of incompatible APIs.

Description of change
---------------------

[#](#description-of-change)

* The `RouteInformation.location` was replaced by `RouteInformation.uri`.* The `WidgetBindingObserver.didPushRoute` was deprecated.* The `location` parameter of `SystemNavigator.routeInformationUpdated` was replaced by the newly added `uri` parameter.

Migration guide
---------------

[#](#migration-guide)

Code before migration:

dart

```
const RouteInformation myRoute = RouteInformation(location: '/myroute');
```

Code after migration:

dart

```
final RouteInformation myRoute = RouteInformation(uri: Uri.parse('/myroute'));
```

Code before migration:

dart

```
final String myPath = myRoute.location;
```

Code after migration:

dart

```
final String myPath = myRoute.uri.path;
```

Code before migration:

dart

```
class MyObserverState extends State<MyWidget> with WidgetsBindingObserver {
  @override
  Future<bool> didPushRoute(String route) => _handleRoute(route);
}
```

Code after migration:

dart

```
class MyObserverState extends State<MyWidget> with WidgetsBindingObserver {
  @override
  Future<bool> didPushRouteInformation(RouteInformation routeInformation) => _handleRoute(
    Uri.decodeComponent(
      Uri(
        path: uri.path.isEmpty ? '/' : uri.path,
        queryParameters: uri.queryParametersAll.isEmpty ? null : uri.queryParametersAll,
        fragment: uri.fragment.isEmpty ? null : uri.fragment,
      ).toString(),
    )
  );
}
```

Code before migration:

dart

```
SystemNavigator.routeInformationUpdated(location: '/myLocation');
```

Code after migration:

dart

```
SystemNavigator.routeInformationUpdated(uri: Uri.parse('/myLocation'));
```

Timeline
--------

[#](#timeline)

Landed in version: 3.10.0-13.0.pre  
 In stable release: 3.13.0

References
----------

[#](#references)

Relevant PRs:

* [PR 119968](https://github.com/flutter/flutter/pull/119968): Implement url support for RouteInformation and didPushRouteInformation.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-information-uri/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-information-uri.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-information-uri/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-information-uri.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-information-uri.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/route-information-uri/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/route-information-uri.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   