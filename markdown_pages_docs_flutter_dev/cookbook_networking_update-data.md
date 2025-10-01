Update data over the internet
=============================

1. [Cookbook](/cookbook) chevron\_right- [Networking](/cookbook/networking) chevron\_right- [Update data over the internet](/cookbook/networking/update-data)

Updating data over the internet is necessary for most apps. The `http` package has got that covered!

This recipe uses the following steps:

1. Add the `http` package.- Update data over the internet using the `http` package.- Convert the response into a custom Dart object.- Get the data from the internet.- Update the existing `title` from user input.- Update and display the response on screen.

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

2. Updating data over the internet using the `http` package
-----------------------------------------------------------

[#](#2-updating-data-over-the-internet-using-the-http-package)

This recipe covers how to update an album title to the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) using the [`http.put()`](https://pub.dev/documentation/http/latest/http/put.html) method.

dart

```
Future<http.Response> updateAlbum(String title) {
  return http.put(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );
}
```

The `http.put()` method returns a `Future` that contains a `Response`.

* [`Future`](https://api.flutter.dev/flutter/dart-async/Future-class.html) is a core Dart class for working with async operations. A `Future` object represents a potential value or error that will be available at some time in the future.* The `http.Response` class contains the data received from a successful http call.* The `updateAlbum()` method takes an argument, `title`, which is sent to the server to update the `Album`.

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

Now, use the following steps to update the `updateAlbum()` function to return a `Future<Album>`:

1. Convert the response body into a JSON `Map` with the `dart:convert` package.- If the server returns an `UPDATED` response with a status code of 200, then convert the JSON `Map` into an `Album` using the `fromJson()` factory method.- If the server doesn't return an `UPDATED` response with a status code of 200, then throw an exception. (Even in the case of a "404 Not Found" server response, throw an exception. Do not return `null`. This is important when examining the data in `snapshot`, as shown below.)

dart

```
Future<Album> updateAlbum(String title) async {
  final response = await http.put(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to update album.');
  }
}
```

Hooray! Now you've got a function that updates the title of an album.

### Get the data from the internet

[#](#get-the-data-from-the-internet)

Get the data from internet before you can update it. For a complete example, see the [Fetch data](/cookbook/networking/fetch-data) recipe.

dart

```
Future<Album> fetchAlbum() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
  );

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}
```

Ideally, you will use this method to set `_futureAlbum` during `initState` to fetch the data from the internet.

4. Update the existing title from user input
--------------------------------------------

[#](#4-update-the-existing-title-from-user-input)

Create a `TextField` to enter a title and a `ElevatedButton` to update the data on server. Also define a `TextEditingController` to read the user input from a `TextField`.

When the `ElevatedButton` is pressed, the `_futureAlbum` is set to the value returned by `updateAlbum()` method.

dart

```
Column(
  mainAxisAlignment: MainAxisAlignment.center,
  children: <Widget>[
    Padding(
      padding: const EdgeInsets.all(8),
      child: TextField(
        controller: _controller,
        decoration: const InputDecoration(hintText: 'Enter Title'),
      ),
    ),
    ElevatedButton(
      onPressed: () {
        setState(() {
          _futureAlbum = updateAlbum(_controller.text);
        });
      },
      child: const Text('Update Data'),
    ),
  ],
);
```

On pressing the **Update Data** button, a network request sends the data in the `TextField` to the server as a `PUT` request. The `_futureAlbum` variable is used in the next step.

5. Display the response on screen
---------------------------------

[#](#5-display-the-response-on-screen)

To display the data on screen, use the [`FutureBuilder`](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html) widget. The `FutureBuilder` widget comes with Flutter and makes it easy to work with async data sources. You must provide two parameters:

1. The `Future` you want to work with. In this case, the future returned from the `updateAlbum()` function.- A `builder` function that tells Flutter what to render, depending on the state of the `Future`: loading, success, or error.

Note that `snapshot.hasData` only returns `true` when the snapshot contains a non-null data value. This is why the `updateAlbum` function should throw an exception even in the case of a "404 Not Found" server response. If `updateAlbum` returns `null` then `CircularProgressIndicator` will display indefinitely.

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
);
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

Future<Album> fetchAlbum() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
  );

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

Future<Album> updateAlbum(String title) async {
  final response = await http.put(
    Uri.parse('https://jsonplaceholder.typicode.com/albums/1'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{'title': title}),
  );

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to update album.');
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
  late Future<Album> _futureAlbum;

  @override
  void initState() {
    super.initState();
    _futureAlbum = fetchAlbum();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Update Data Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Scaffold(
        appBar: AppBar(title: const Text('Update Data Example')),
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(8),
          child: FutureBuilder<Album>(
            future: _futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                if (snapshot.hasData) {
                  return Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text(snapshot.data!.title),
                      TextField(
                        controller: _controller,
                        decoration: const InputDecoration(
                          hintText: 'Enter Title',
                        ),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            _futureAlbum = updateAlbum(_controller.text);
                          });
                        },
                        child: const Text('Update Data'),
                      ),
                    ],
                  );
                } else if (snapshot.hasError) {
                  return Text('${snapshot.error}');
                }
              }

              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/update-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/update-data.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/update-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/update-data.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/networking/update-data.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/update-data/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/update-data.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   