Obfuscate Dart code
===================

1. [Deployment](/deployment) chevron\_right- [Obfuscate Dart code](/deployment/obfuscate)

What is code obfuscation?
-------------------------

[#](#what-is-code-obfuscation)

[Code obfuscation](https://en.wikipedia.org/wiki/Obfuscation_(software)) is the process of modifying an app's binary to make it harder for humans to understand. Obfuscation hides function and class names in your compiled Dart code, replacing each symbol with another symbol, making it difficult for an attacker to reverse engineer your proprietary app.

Limitations and warnings
------------------------

[#](#limitations)

**Flutter's code obfuscation works only on a [release build](/testing/build-modes#release).**

*warning* Warning

It is a **poor security practice** to store secrets in an app.

Obfuscating your code does *not* encrypt resources nor does it protect against reverse engineering. It only renames symbols with more obscure names.

Web apps don't support obfuscation. A web app can be [minified](https://en.wikipedia.org/wiki/Minification_(programming)), which provides a similar result. When you build a release version of a Flutter web app, the web compiler minifies the app. To learn more, see [Build and release a web app](/deployment/web).

Supported targets
-----------------

[#](#supported-targets)

The following build targets support the obfuscation process described on this page:

* `aar`* `apk`* `appbundle`* `ios`* `ios-framework`* `ipa`* `linux`* `macos`* `macos-framework`* `windows`

For detailed information about the command line options available for a build target, run the following command. The `--obfuscate` and `--split-debug-info` options should be listed in the output. If they aren't, you'll need to install a newer version of Flutter to obfuscate your code.

```
flutter build <build-target> -h
```

* `<build-target>`: The build target. For example, `apk`.

Obfuscate your app
------------------

[#](#obfuscate-your-app)

To obfuscate your app and create a symbol map, use the `flutter build` command in release mode with the `--obfuscate` and `--split-debug-info` options. If you want to debug your obfuscated app in the future, you will need the symbol map.

1. Run the following command to obfuscate your app and generate a SYMBOLS file:

   ```
   flutter build <build-target> \ 
      --obfuscate \ 
      --split-debug-info=/<symbols-directory>
   ```

   * `<build-target>`: The build target. For example, `apk`.* `<symbols-directory>`: The directory where the SYMBOLS file should be placed. For example, `out/android`.- Once you've obfuscated your binary, **backup the SYMBOLS file**. You might need this if you lose your original SYMBOLs file and you want to de-obfuscate a stack trace.

Read an obfuscated stack trace
------------------------------

[#](#read-an-obfuscated-stack-trace)

To debug a stack trace created by an obfuscated app, use the following steps to make it human readable:

1. Find the matching SYMBOLS file. For example, a crash from an Android arm64 device would need `app.android-arm64.symbols`.- Provide both the stack trace (stored in a file) and the SYMBOLS file to the `flutter symbolize` command.

     ```
     flutter symbolize \
        -i <stack-trace-file> \
        -d <obfuscated-symbols-file>
     ```

     * `<stack-trace-file>`: The file path for the stacktrace. For example, `???`.* `<obfuscated-symbols-file>`: The file path for the symbols file that contains the obfuscated symbols. For example, `out/android/app.android-arm64.symbols`.

     For more information about the `symbolize` command, run `flutter symbolize -h`.

Read an obfuscated name
-----------------------

[#](#read-an-obfuscated-name)

You can generate a JSON file that contains an obfuscation map. An obfuscation map is a JSON array with pairs of original names and obfuscated names. For example, `["MaterialApp", "ex", "Scaffold", "ey"]`, where `ex` is the obfuscated name of `MaterialApp`.

To generate an obfuscation map, use the following command:

```
flutter build <build-target> \
   --obfuscate \
   --split-debug-info=/<symbols-directory> \
   --extra-gen-snapshot-options=--save-obfuscation-map=/<obfuscation-map-file>
```

* `<build-target>`: The build target. For example, `apk`.* `<symbols-directory>`: The directory where the symbols should be placed. For example, `out/android`* `<obfuscation-map-file>`: The file path where the JSON obfuscation map should be placed. For example, `out/android/map.json`

Caveat
------

[#](#caveat)

Be aware of the following when coding an app that will eventually be an obfuscated binary.

* Code that relies on matching specific class, function, or library names will fail. For example, the following call to `expect()` won't work in an obfuscated binary:

  dart

  ```
  expect(foo.runtimeType.toString(), equals('Foo'));
  ```

  * Enum names are not obfuscated currently.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/obfuscate/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/obfuscate.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/obfuscate/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/obfuscate.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-10. [View source](https://github.com/flutter/website/tree/main/src/content/deployment/obfuscate.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/obfuscate/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/obfuscate.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   