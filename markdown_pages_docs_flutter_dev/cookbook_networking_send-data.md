Send data to the internet
=========================

1. [Cookbook](/cookbook) chevron\_right- [Networking](/cookbook/networking) chevron\_right- [Send data to the internet](/cookbook/networking/send-data)

Sending data to the internet is necessary for most apps. The `http` package has got that covered, too.

This recipe uses the following steps:

1. Add the `http` package.- Send data to a server using the `http` package.- Convert the response into a custom Dart object.- Get a `title` from user input.- Display the response on screen.

1. Add the `http` package
-------------------------

[#](#1-add-the-http-package)

To add the `http` package as a dependency, run `flutter pub add`:

```
flutter pub add http
```

Import the `http` package.

dart

```
import 'package:http/http.dart' as http;
```

If you are deploying to Android, edit your `AndroidManifest.xml` file to add the Internet permission.

xml

```
<!-- Required to fetch data from the internet. -->
<uses-permission android:name="android.permission.INTERNET" />
```

Likewise, if you are deploying to macOS, edit your `macos/Runner/DebugProfile.entitlements` and `macos/Runner/Release.entitlements` files to include the network client entitlement.

xml

```
<!-- Required to fetch data from the internet. -->
<key>com.apple.security.network.client</key>
<true/>
```

2. Sending data to server
-------------------------

[#](#2-sending-data-to-server)

This recipe covers how to create an `Album` by sending an album title to the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) using the [`http.post()`](https://pub.dev/documentation/http/latest/http/post.html) method.

Import `dart:convert` for access to `jsonEncode` to encode the data:

dart

```
import 'dart:convert';
```

Use the `http.post()` method to send the encoded data:

dart

```
Future<http.Response> createAlbum(String title) {
  return http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/albums'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );
}
```

The `http.post()` method returns a `Future` that contains a `Response`.

* [`Future`](https://api.flutter.dev/flutter/dart-async/Future-class.html) is a core Dart class for working with asynchronous operations. A Future object represents a potential value or error that will be available at some time in the future.* The `http.Response` class contains the data received from a successful http call.* The `createAlbum()` method takes an argument `title` that is sent to the server to create an `Album`.

3. Convert the `http.Response` to a custom Dart object
------------------------------------------------------

[#](#3-convert-the-http-response-to-a-custom-dart-object)

While it's easy to make a network request, working with a raw `Future<http.Response>` isn't very convenient. To make your life easier, convert the `http.Response` into a Dart object.

### Create an Album class

[#](#create-an-album-class)

First, create an `Album` class that contains the data from the network request. It includes a factory constructor that creates an `Album` from JSON.

Converting JSON with [pattern matching](https://dart.dev/language/patterns) is only one option. For more information, see the full article on [JSON and serialization](/data-and-backend/serialization/json).

dart

```
class Album {
  final int id;
  final String title;

  const Album({required this.id, required this.title});

  factory Album.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {'id': int id, 'title': String title} => Album(id: id, title: title),
      _ => throw const FormatException('Failed to load album.'),
    };
  }
}
```

### Convert the `http.Response` to an `Album`

[#](#convert-the-http-response-to-an-album)

Use the following steps to update the `createAlbum()` function to return a `Future<Album>`:

1. Convert the response body into a JSON `Map` with the `dart:convert` package.- If the server returns a `CREATED` response with a status code of 201, then convert the JSON `Map` into an `Album` using the `fromJson()` factory method.- If the server doesn't return a `CREATED` response with a status code of 201, then throw an exception. (Even in the case of a "404 Not Found" server response, throw an exception. Do not return `null`. This is important when examining the data in `snapshot`, as shown below.)

dart

```
Future<Album> createAlbum(String title) async {
  final response = await http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/albums'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );

  if (response.statusCode == 201) {
    // If the server did return a 201 CREATED response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 201 CREATED response,
    // then throw an exception.
    throw Exception('Failed to create album.');
  }
}
```

Hooray! Now you've got a function that sends the title to a server to create an album.

4. Get a title from user input
------------------------------

[#](#4-get-a-title-from-user-input)

Next, create a `TextField` to enter a title and a `ElevatedButton` to send data to server. Also define a `TextEditingController` to read the user input from a `TextField`.

When the `ElevatedButton` is pressed, the `_futureAlbum` is set to the value returned by `createAlbum()` method.

dart

```
Column(
  mainAxisAlignment: MainAxisAlignment.center,
  children: <Widget>[
    TextField(
      controller: _controller,
      decoration: const InputDecoration(hintText: 'Enter Title'),
    ),
    ElevatedButton(
      onPressed: () {
        setState(() {
          _futureAlbum = createAlbum(_controller.text);
        });
      },
      child: const Text('Create Data'),
    ),
  ],
)
```

On pressing the **Create Data** button, make the network request, which sends the data in the `TextField` to the server as a `POST` request. The Future, `_futureAlbum`, is used in the next step.

5. Display the response on screen
---------------------------------

[#](#5-display-the-response-on-screen)

To display the data on screen, use the [`FutureBuilder`](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html) widget. The `FutureBuilder` widget comes with Flutter and makes it easy to work with asynchronous data sources. You must provide two parameters:

1. The `Future` you want to work with. In this case, the future returned from the `createAlbum()` function.- A `builder` function that tells Flutter what to render, depending on the state of the `Future`: loading, success, or error.

Note that `snapshot.hasData` only returns `true` when the snapshot contains a non-null data value. This is why the `createAlbum()` function should throw an exception even in the case of a "404 Not Found" server response. If `createAlbum()` returns `null`, then `CircularProgressIndicator` displays indefinitely.

dart

```
FutureBuilder<Album>(
  future: _futureAlbum,
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      return Text(snapshot.data!.title);
    } else if (snapshot.hasError) {
      return Text('${snapshot.error}');
    }

    return const CircularProgressIndicator();
  },
)
```

Complete example
----------------

[#](#complete-example)

dart

```
import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

Future<Album> createAlbum(String title) async {
  final response = await http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/albums'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );

  if (response.statusCode == 201) {
    // If the server did return a 201 CREATED response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 201 CREATED response,
    // then throw an exception.
    throw Exception('Failed to create album.');
  }
}

class Album {
  final int id;
  final String title;

  const Album({required this.id, required this.title});

  factory Album.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {'id': int id, 'title': String title} => Album(id: id, title: title),
      _ => throw const FormatException('Failed to load album.'),
    };
  }
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() {
    return _MyAppState();
  }
}

class _MyAppState extends State<MyApp> {
  final TextEditingController _controller = TextEditingController();
  Future<Album>? _futureAlbum;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Create Data Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Scaffold(
        appBar: AppBar(title: const Text('Create Data Example')),
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(8),
          child: (_futureAlbum == null) ? buildColumn() : buildFutureBuilder(),
        ),
      ),
    );
  }

  Column buildColumn() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        TextField(
          controller: _controller,
          decoration: const InputDecoration(hintText: 'Enter Title'),
        ),
        ElevatedButton(
          onPressed: () {
            setState(() {
              _futureAlbum = createAlbum(_controller.text);
            });
          },
          child: const Text('Create Data'),
        ),
      ],
    );
  }

  FutureBuilder<Album> buildFutureBuilder() {
    return FutureBuilder<Album>(
      future: _futureAlbum,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text(snapshot.data!.title);
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }
}
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/send-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/send-data.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/send-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/send-data.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/networking/send-data.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/send-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/send-data.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   