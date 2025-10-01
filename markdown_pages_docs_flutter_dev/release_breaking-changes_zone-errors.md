"Zone mismatch" message
=======================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- ["Zone mismatch" message](/release/breaking-changes/zone-errors)

Summary
-------

[#](#summary)

Starting with Flutter 3.10, the framework detects mismatches when using Zones and reports them to the console in debug builds.

Background
----------

[#](#background)

Zones are a mechanism for managing callbacks in Dart. While primarily useful for overriding `print` and `Timer` logic in tests, and for catching errors in tests, they are sometimes used for scoping global variables to certain parts of an application.

Flutter requires (and has always required) that all framework code be run in the same zone. Notably, this means that calls to `WidgetsFlutterBinding.ensureInitialized()` should be run in the same zone as calls to `runApp()`.

Historically, Flutter has not detected such mismatches. This sometimes leads to obscure and hard-to-debug issues. For example, a callback for keyboard input might be invoked using a zone that does not have access to the `zoneValues` that it expects. In our experience, most if not all code that uses Zones in a way that does not guarantee that all parts of the Flutter framework are working in the same Zone has some latent bug. Often these bugs appear unrelated to the use of Zones.

To help developers who have accidentally violated this invariant, starting with Flutter 3.10, a non-fatal warning is printed in debug builds when a mismatch is detected. The warning looks like the following:

```
════════ Exception caught by Flutter framework ════════════════════════════════════
The following assertion was thrown during runApp:
Zone mismatch.

The Flutter bindings were initialized in a different zone than is now being used.
This will likely cause confusion and bugs as any zone-specific configuration will
inconsistently use the configuration of the original binding initialization zone or
this zone based on hard-to-predict factors such as which zone was active when a
particular callback was set.
It is important to use the same zone when calling `ensureInitialized` on the
binding as when calling `runApp` later.
To make this warning fatal, set BindingBase.debugZoneErrorsAreFatal to true before
the bindings are initialized (i.e. as the first statement in `void main() { }`).
[...]
═══════════════════════════════════════════════════════════════════════════════════
```

The warning can be made fatal by setting [`BindingBase.debugZoneErrorsAreFatal`](https://api.flutter.dev/flutter/foundation/BindingBase/debugZoneErrorsAreFatal.html) to `true`. This flag might be changed to default to `true` in a future version of Flutter.

Migration guide
---------------

[#](#migration-guide)

The best way to silence this message is to remove use of Zones from within the application. Zones can be very hard to debug, because they are essentially global variables, and break encapsulation. Best practice is to avoid global variables and zones.

If removing zones is not an option (for example because the application depends on a third-party library that relies on zones for its configuration), then the various calls into the Flutter framework should be moved to all be in the same zone. Typically, this means moving the call to `WidgetsFlutterBinding.ensureInitialized()` to the same closure as the call to `runApp()`.

This can be awkward when the zone in which `runApp` is run is being initialized with `zoneValues` obtained from a plugin (which requires `WidgetsFlutterBinding.ensureInitialized()` to have been called).

One option in this kind of scenario is to place a mutable object in the `zoneValues`, and update that object with the value once the value is available.

dart

```
import 'dart:async';
import 'package:flutter/material.dart';

class Mutable<T> {
  Mutable(this.value);
  T value;
}

void main() {
  var myValue = Mutable<double>(0.0);
  Zone.current.fork(
    zoneValues: {
      'myKey': myValue,
    }
  ).run(() {
    WidgetsFlutterBinding.ensureInitialized();
    var newValue = ...; // obtain value from plugin
    myValue.value = newValue; // update value in Zone
    runApp(...);
  });
}
```

In code that needs to use `myKey`, it can be obtained indirectly using `Zone.current['myKey'].value`.

When such a solution does not work because a third-party dependency requires the use of a specific type for a specific `zoneValues` key, all calls into the dependency can be wrapped in `Zone` calls that provide suitable values.

It is strongly recommended that packages that use zones in this way migrate to more maintainable solutions.

Timeline
--------

[#](#timeline)

Landed in version: 3.9.0-9.0.pre  
 In stable release: 3.10.0

References
----------

[#](#references)

API documentation:

* [`Zone`](https://api.flutter.dev/flutter/dart-async/Zone-class.html)* [`BindingBase.debugZoneErrorsAreFatal`](https://api.flutter.dev/flutter/foundation/BindingBase/debugZoneErrorsAreFatal.html)

Relevant issues:

* [Issue 94123](https://github.com/flutter/flutter/issues/94123): Flutter framework does not warn when ensureInitialized is called in a different zone than runApp

Relevant PRs:

* [PR 122836](https://github.com/flutter/flutter/pull/122836): Assert that runApp is called in the same zone as binding.ensureInitialized

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/zone-errors/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/zone-errors.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/zone-errors/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/zone-errors.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/zone-errors.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/zone-errors/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/zone-errors.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   