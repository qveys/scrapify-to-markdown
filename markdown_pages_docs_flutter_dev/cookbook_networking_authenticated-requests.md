Make authenticated requests
===========================

1. [Cookbook](/cookbook) chevron\_right- [Networking](/cookbook/networking) chevron\_right- [Make authenticated requests](/cookbook/networking/authenticated-requests)

To fetch data from most web services, you need to provide authorization. There are many ways to do this, but perhaps the most common uses the `Authorization` HTTP header.

Add authorization headers
-------------------------

[#](#add-authorization-headers)

The [`http`](https://pub.dev/packages/http) package provides a convenient way to add headers to your requests. Alternatively, use the [`HttpHeaders`](https://api.dart.dev/dart-io/HttpHeaders-class.html) class from the `dart:io` library.

dart

```
final response = await http.get(
  Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
  // Send authorization headers to the backend.
  headers: {HttpHeaders.authorizationHeader: 'Basic your_api_token_here'},
);
```

Complete example
----------------

[#](#complete-example)

This example builds upon the [Fetching data from the internet](/cookbook/networking/fetch-data) recipe.

dart

```
import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

Future<Album> fetchAlbum() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
    // Send authorization headers to the backend.
    headers: {HttpHeaders.authorizationHeader: 'Basic your_api_token_here'},
  );
  final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

  return Album.fromJson(responseJson);
}

class Album {
  final int userId;
  final int id;
  final String title;

  const Album({required this.userId, required this.id, required this.title});

  factory Album.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {'userId': int userId, 'id': int id, 'title': String title} => Album(
        userId: userId,
        id: id,
        title: title,
      ),
      _ => throw const FormatException('Failed to load album.'),
    };
  }
}
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/authenticated-requests/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/authenticated-requests.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/authenticated-requests/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/authenticated-requests.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/networking/authenticated-requests.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/authenticated-requests/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/authenticated-requests.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   