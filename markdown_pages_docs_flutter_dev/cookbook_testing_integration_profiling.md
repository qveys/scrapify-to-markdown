Measure performance with an integration test
============================================

1. [Cookbook](/cookbook) chevron\_right- [Testing](/cookbook/testing) chevron\_right- [Integration](/cookbook/testing/integration) chevron\_right- [Measure performance with an integration test](/cookbook/testing/integration/profiling)

When it comes to mobile apps, performance is critical to user experience. Users expect apps to have smooth scrolling and meaningful animations free of stuttering or skipped frames, known as "jank." How to ensure that your app is free of jank on a wide variety of devices?

There are two options: first, manually test the app on different devices. While that approach might work for a smaller app, it becomes more cumbersome as an app grows in size. Alternatively, run an integration test that performs a specific task and records a performance timeline. Then, examine the results to determine whether a specific section of the app needs to be improved.

In this recipe, learn how to write a test that records a performance timeline while performing a specific task and saves a summary of the results to a local file.

*info* Note

Recording performance timelines isn't supported on web. For performance profiling on web, see [Debugging performance for web apps](/perf/web-performance)

This recipe uses the following steps:

1. Write a test that scrolls through a list of items.- Record the performance of the app.- Save the results to disk.- Run the test.- Review the results.

1. Write a test that scrolls through a list of items
----------------------------------------------------

[#](#1-write-a-test-that-scrolls-through-a-list-of-items)

In this recipe, record the performance of an app as it scrolls through a list of items. To focus on performance profiling, this recipe builds on the [Scrolling](/cookbook/testing/widget/scrolling) recipe in widget tests.

Follow the instructions in that recipe to create an app and write a test to verify that everything works as expected.

2. Record the performance of the app
------------------------------------

[#](#2-record-the-performance-of-the-app)

Next, record the performance of the app as it scrolls through the list. Perform this task using the [`traceAction()`](https://api.flutter.dev/flutter/flutter_driver/FlutterDriver/traceAction.html) method provided by the [`IntegrationTestWidgetsFlutterBinding`](https://api.flutter.dev/flutter/package-integration_test_integration_test/IntegrationTestWidgetsFlutterBinding-class.html) class.

This method runs the provided function and records a [`Timeline`](https://api.flutter.dev/flutter/flutter_driver/Timeline-class.html) with detailed information about the performance of the app. This example provides a function that scrolls through the list of items, ensuring that a specific item is displayed. When the function completes, the `traceAction()` creates a report data `Map` that contains the `Timeline`.

Specify the `reportKey` when running more than one `traceAction`. By default all `Timelines` are stored with the key `timeline`, in this example the `reportKey` is changed to `scrolling_timeline`.

dart

```
await binding.traceAction(() async {
  // Scroll until the item to be found appears.
  await tester.scrollUntilVisible(
    itemFinder,
    500.0,
    scrollable: listFinder,
  );
}, reportKey: 'scrolling_timeline');
```

3. Save the results to disk
---------------------------

[#](#3-save-the-results-to-disk)

Now that you've captured a performance timeline, you need a way to review it. The `Timeline` object provides detailed information about all of the events that took place, but it doesn't provide a convenient way to review the results.

Therefore, convert the `Timeline` into a [`TimelineSummary`](https://api.flutter.dev/flutter/flutter_driver/TimelineSummary-class.html). The `TimelineSummary` can perform two tasks that make it easier to review the results:

1. Writing a json document on disk that summarizes the data contained within the `Timeline`. This summary includes information about the number of skipped frames, slowest build times, and more.- Saving the complete `Timeline` as a json file on disk. This file can be opened with the Chrome browser's tracing tools found at `chrome://tracing`.

To capture the results, create a file named `perf_driver.dart` in the `test_driver` folder and add the following code:

dart

```
import 'package:flutter_driver/flutter_driver.dart' as driver;
import 'package:integration_test/integration_test_driver.dart';

Future<void> main() {
  return integrationDriver(
    responseDataCallback: (data) async {
      if (data != null) {
        final timeline = driver.Timeline.fromJson(
          data['scrolling_timeline'] as Map<String, dynamic>,
        );

        // Convert the Timeline into a TimelineSummary that's easier to
        // read and understand.
        final summary = driver.TimelineSummary.summarize(timeline);

        // Then, write the entire timeline to disk in a json format.
        // This file can be opened in the Chrome browser's tracing tools
        // found by navigating to chrome://tracing.
        // Optionally, save the summary to disk by setting includeSummary
        // to true
        await summary.writeTimelineToFile(
          'scrolling_timeline',
          pretty: true,
          includeSummary: true,
        );
      }
    },
  );
}
```

The `integrationDriver` function has a `responseDataCallback` which you can customize. By default, it writes the results to the `integration_response_data.json` file, but you can customize it to generate a summary like in this example.

4. Run the test
---------------

[#](#4-run-the-test)

After configuring the test to capture a performance `Timeline` and save a summary of the results to disk, run the test with the following command:

```
flutter drive \
  --driver=test_driver/perf_driver.dart \
  --target=integration_test/scrolling_test.dart \
  --profile
```

The `--profile` option means to compile the app for the "profile mode" rather than the "debug mode", so that the benchmark result is closer to what will be experienced by end users.

*info* Note

Run the command with `--no-dds` when running on a mobile device or emulator. This option disables the Dart Development Service (DDS), which won't be accessible from your computer.

5. Review the results
---------------------

[#](#5-review-the-results)

After the test completes successfully, the `build` directory at the root of the project contains two files:

1. `scrolling_summary.timeline_summary.json` contains the summary. Open the file with any text editor to review the information contained within. With a more advanced setup, you could save a summary every time the test runs and create a graph of the results.- `scrolling_timeline.timeline.json` contains the complete timeline data. Open the file using the Chrome browser's tracing tools found at `chrome://tracing`. The tracing tools provide a convenient interface for inspecting the timeline data to discover the source of a performance issue.

### Summary example

[#](#summary-example)

json

```
{
  "average_frame_build_time_millis": 4.2592592592592595,
  "worst_frame_build_time_millis": 21.0,
  "missed_frame_build_budget_count": 2,
  "average_frame_rasterizer_time_millis": 5.518518518518518,
  "worst_frame_rasterizer_time_millis": 51.0,
  "missed_frame_rasterizer_budget_count": 10,
  "frame_count": 54,
  "frame_build_times": [
    6874,
    5019,
    3638
  ],
  "frame_rasterizer_times": [
    51955,
    8468,
    3129
  ]
}
```

Complete example
----------------

[#](#complete-example)

**integration\_test/scrolling\_test.dart**

dart

```
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:your_package/main.dart';

void main() {
  final binding = IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('Counter increments smoke test', (tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      MyApp(items: List<String>.generate(10000, (i) => 'Item $i')),
    );

    final listFinder = find.byType(Scrollable);
    final itemFinder = find.byKey(const ValueKey('item_50_text'));

    await binding.traceAction(() async {
      // Scroll until the item to be found appears.
      await tester.scrollUntilVisible(
        itemFinder,
        500.0,
        scrollable: listFinder,
      );
    }, reportKey: 'scrolling_timeline');
  });
}
```

**test\_driver/perf\_driver.dart**

dart

```
import 'package:flutter_driver/flutter_driver.dart' as driver;
import 'package:integration_test/integration_test_driver.dart';

Future<void> main() {
  return integrationDriver(
    responseDataCallback: (data) async {
      if (data != null) {
        final timeline = driver.Timeline.fromJson(
          data['scrolling_timeline'] as Map<String, dynamic>,
        );

        // Convert the Timeline into a TimelineSummary that's easier to
        // read and understand.
        final summary = driver.TimelineSummary.summarize(timeline);

        // Then, write the entire timeline to disk in a json format.
        // This file can be opened in the Chrome browser's tracing tools
        // found by navigating to chrome://tracing.
        // Optionally, save the summary to disk by setting includeSummary
        // to true
        await summary.writeTimelineToFile(
          'scrolling_timeline',
          pretty: true,
          includeSummary: true,
        );
      }
    },
  );
}
```

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/profiling/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/profiling.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/profiling/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/profiling.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/profiling.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/testing/integration/profiling/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/testing/integration/profiling.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   