Report errors to a service
==========================

1. [Cookbook](/cookbook) chevron\_right- [Maintenance](/cookbook/maintenance) chevron\_right- [Report errors to a service](/cookbook/maintenance/error-reporting)

While one always tries to create apps that are free of bugs, they're sure to crop up from time to time. Since buggy apps lead to unhappy users and customers, it's important to understand how often your users experience bugs and where those bugs occur. That way, you can prioritize the bugs with the highest impact and work to fix them.

How can you determine how often your users experiences bugs? Whenever an error occurs, create a report containing the error that occurred and the associated stacktrace. You can then send the report to an error tracking service, such as [Bugsnag](https://www.bugsnag.com/platforms/flutter), [Datadog](https://docs.datadoghq.com/real_user_monitoring/flutter/), [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics), [Rollbar](https://rollbar.com/), or Sentry.

The error tracking service aggregates all of the crashes your users experience and groups them together. This allows you to know how often your app fails and where the users run into trouble.

In this recipe, learn how to report errors to the [Sentry](https://sentry.io/welcome/) crash reporting service using the following steps:

1. Get a DSN from Sentry.- Import the Flutter Sentry package- Initialize the Sentry SDK- Capture errors programmatically

1. Get a DSN from Sentry
------------------------

[#](#1-get-a-dsn-from-sentry)

Before reporting errors to Sentry, you need a "DSN" to uniquely identify your app with the Sentry.io service.

To get a DSN, use the following steps:

1. [Create an account with Sentry](https://sentry.io/signup/).- Log in to the account.- Create a new Flutter project.- Copy the code snippet that includes the DSN.

2. Import the Sentry package
----------------------------

[#](#2-import-the-sentry-package)

Import the [`sentry_flutter`](https://pub.dev/packages/sentry_flutter) package into the app. The sentry package makes it easier to send error reports to the Sentry error tracking service.

To add the `sentry_flutter` package as a dependency, run `flutter pub add`:

```
flutter pub add sentry_flutter
```

3. Initialize the Sentry SDK
----------------------------

[#](#3-initialize-the-sentry-sdk)

Initialize the SDK to capture different unhandled errors automatically:

dart

```
import 'package:flutter/widgets.dart';
import 'package:sentry_flutter/sentry_flutter.dart';

Future<void> main() async {
  await SentryFlutter.init(
    (options) => options.dsn = 'https://example@sentry.io/example',
    appRunner: () => runApp(const MyApp()),
  );
}
```

Alternatively, you can pass the DSN to Flutter using the `dart-define` tag:

sh

```
--dart-define SENTRY_DSN=https://example@sentry.io/example
```

### What does that give me?

[#](#what-does-that-give-me)

This is all you need for Sentry to capture unhandled errors in Dart and native layers.  
 This includes Swift, Objective-C, C, and C++ on iOS, and Java, Kotlin, C, and C++ on Android.

4. Capture errors programmatically
----------------------------------

[#](#4-capture-errors-programmatically)

Besides the automatic error reporting that Sentry generates by importing and initializing the SDK, you can use the API to report errors to Sentry:

dart

```
await Sentry.captureException(exception, stackTrace: stackTrace);
```

For more information, see the [Sentry API](https://pub.dev/documentation/sentry_flutter/latest/sentry_flutter/sentry_flutter-library.html) docs on pub.dev.

Learn more
----------

[#](#learn-more)

Extensive documentation about using the Sentry SDK can be found on [Sentry's site](https://docs.sentry.io/platforms/flutter/).

Complete example
----------------

[#](#complete-example)

To view a working example, see the [Sentry flutter example](https://github.com/getsentry/sentry-dart/tree/main/flutter/example) app.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/maintenance/error-reporting/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/maintenance/error-reporting.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/maintenance/error-reporting/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/maintenance/error-reporting.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-06. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/maintenance/error-reporting.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/maintenance/error-reporting/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/maintenance/error-reporting.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   