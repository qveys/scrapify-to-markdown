Communicate with WebSockets
===========================

1. [Cookbook](/cookbook) chevron\_right- [Networking](/cookbook/networking) chevron\_right- [Communicate with WebSockets](/cookbook/networking/web-sockets)

In addition to normal HTTP requests, you can connect to servers using `WebSockets`. `WebSockets` allow for two-way communication with a server without polling.

In this example, connect to a [test WebSocket server sponsored by Lob.com](https://www.lob.com/blog/websocket-org-is-down-here-is-an-alternative). The server sends back the same message you send to it. This recipe uses the following steps:

1. Connect to a WebSocket server.- Listen for messages from the server.- Send data to the server.- Close the WebSocket connection.

1. Connect to a WebSocket server
--------------------------------

[#](#1-connect-to-a-websocket-server)

The [`web_socket_channel`](https://pub.dev/packages/web_socket_channel) package provides the tools you need to connect to a WebSocket server.

The package provides a `WebSocketChannel` that allows you to both listen for messages from the server and push messages to the server.

In Flutter, use the following line to create a `WebSocketChannel` that connects to a server:

dart

```
final channel = WebSocketChannel.connect(
  Uri.parse('wss://echo.websocket.events'),
);
```

2. Listen for messages from the server
--------------------------------------

[#](#2-listen-for-messages-from-the-server)

Now that you've established a connection, listen to messages from the server.

After sending a message to the test server, it sends the same message back.

In this example, use a [`StreamBuilder`](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html) widget to listen for new messages, and a [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) widget to display them.

dart

```
StreamBuilder(
  stream: channel.stream,
  builder: (context, snapshot) {
    return Text(snapshot.hasData ? '${snapshot.data}' : '');
  },
),
```

### How this works

[#](#how-this-works)

The `WebSocketChannel` provides a [`Stream`](https://api.flutter.dev/flutter/dart-async/Stream-class.html) of messages from the server.

The `Stream` class is a fundamental part of the `dart:async` package. It provides a way to listen to async events from a data source. Unlike `Future`, which returns a single async response, the `Stream` class can deliver many events over time.

The [`StreamBuilder`](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html) widget connects to a `Stream` and asks Flutter to rebuild every time it receives an event using the given `builder()` function.

3. Send data to the server
--------------------------

[#](#3-send-data-to-the-server)

To send data to the server, `add()` messages to the `sink` provided by the `WebSocketChannel`.

dart

```
channel.sink.add('Hello!');
```

### How this works

[#](#how-this-works-1)

The `WebSocketChannel` provides a [`StreamSink`](https://api.flutter.dev/flutter/dart-async/StreamSink-class.html) to push messages to the server.

The `StreamSink` class provides a general way to add sync or async events to a data source.

4. Close the WebSocket connection
---------------------------------

[#](#4-close-the-websocket-connection)

After you're done using the WebSocket, close the connection:

dart

```
channel.sink.close();
```

Complete example
----------------

[#](#complete-example)

dart

```
import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'WebSocket Demo';
    return const MaterialApp(
      title: title,
      home: MyHomePage(title: title),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _controller = TextEditingController();
  final _channel = WebSocketChannel.connect(
    Uri.parse('wss://echo.websocket.events'),
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Form(
              child: TextFormField(
                controller: _controller,
                decoration: const InputDecoration(labelText: 'Send a message'),
              ),
            ),
            const SizedBox(height: 24),
            StreamBuilder(
              stream: _channel.stream,
              builder: (context, snapshot) {
                return Text(snapshot.hasData ? '${snapshot.data}' : '');
              },
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _sendMessage,
        tooltip: 'Send message',
        child: const Icon(Icons.send),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  void _sendMessage() {
    if (_controller.text.isNotEmpty) {
      _channel.sink.add(_controller.text);
    }
  }

  @override
  void dispose() {
    _channel.sink.close();
    _controller.dispose();
    super.dispose();
  }
}
```

![Web sockets demo](/assets/images/docs/cookbook/web-sockets.webp)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/web-sockets/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/web-sockets.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/web-sockets/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/web-sockets.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-05-19. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/networking/web-sockets.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/networking/web-sockets/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/networking/web-sockets.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   