Using Flutter in China
======================

1. [Using Flutter in China](/community/china)

*info* Note

如果你正在中国的网络环境下配置 Flutter， 请参考 [在中国网络环境下使用 Flutter](https://docs.flutter.cn/community/china) 文档.

To speed the download and installation of Flutter in China, consider using a [mirror site](https://en.wikipedia.org/wiki/Mirror_site) or *mirror*.

*error* Important

Use mirror sites *only* if you *trust* the provider. The Flutter team can't verify their reliability or security.

Use a Flutter mirror site
-------------------------

[#](#use-a-flutter-mirror-site)

The [China Flutter User Group](https://github.com/cfug) (CFUG) maintains a Simplified Chinese Flutter website <https://flutter.cn> and a mirror. Other mirrors can be found at the [end of this guide](#known-trusted-community-run-mirror-sites).

### Configure your machine to use a mirror site

[#](#configure-your-machine-to-use-a-mirror-site)

To install or use Flutter in China, use a trustworthy Flutter mirror. This requires setting two environment variables on your machine.

*All examples that follow presume that you are using the CFUG mirror.*

To set your machine to use a mirror site:

* [Windows](#57-tab-panel)* [macOS](#58-tab-panel)* [Linux](#59-tab-panel)* [ChromeOS](#60-tab-panel)

This procedure requires using Powershell.

1. Open a new window in Powershell to prepare running scripts.- Set `PUB_HOSTED_URL` to your mirror site.

     ```
     C:> $env:PUB_HOSTED_URL="https://pub.flutter-io.cn"
     ```

     - Set `FLUTTER_STORAGE_BASE_URL` to your mirror site.

       ```
       C:> $env:FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
       ```

       - Download the Flutter archive from your mirror site. In your preferred browser, go to [Flutter SDK archive](https://docs.flutter.cn/release/archive?tab=windows).- Create a folder where you can install Flutter. then change into it.

           Consider a path like `%USERPROFILE%dev`.

           ```
           C:> New-Item -Path '`%USERPROFILE%dev`' -ItemType Directory; cd `%USERPROFILE%dev`
           ```

           - Extract the SDK from the zip archive file.

             This example assumes you downloaded the Windows version of the Flutter SDK.

             ```
             C:> Expand-Archive .\flutter_windows_3.13.0-stable.zip
             ```

             - Add Flutter to your `PATH` environment variable.

               ```
               C:> $env:PATH = $pwd.PATH + "/flutter/bin",$env:PATH -join ";"
               ```

               - Run Flutter Doctor to verify your installation.

                 ```
                 C:> flutter doctor
                 ```

From this example, `flutter pub get` fetches packages from `flutter-io.cn`, in any terminal where you set `PUB_HOSTED_URL` and `FLUTTER_STORAGE_BASE_URL`.

Any environment variables set using `$env:` in this procedure only apply to the current window.

To set these values on a permanent basis, set the environment variables as in the following example:

```
# cd to flutter dir
$currentDirectory = Get-Location   
$newPath = "$currentDirectory\bin;$env:PATH"
[System.Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
[System.Environment]::SetEnvironmentVariable('PUB_HOSTED_URL', 'https://pub.flutter-io.cn', 'User')
[System.Environment]::SetEnvironmentVariable('FLUTTER_STORAGE_BASE_URL', 'https://storage.flutter-io.cn', 'User')

Write-Host ". $PROFILE"
```

This procedure requires using your terminal.

1. Open a new window in your terminal to prepare running scripts.- Set `PUB_HOSTED_URL` to your mirror site.

     ```
     export PUB_HOSTED_URL="https://pub.flutter-io.cn"
     ```

     - Set `FLUTTER_STORAGE_BASE_URL` to your mirror site.

       ```
       export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
       ```

       - Download the Flutter archive from your mirror site. In your preferred browser, go to [Flutter SDK archive](https://docs.flutter.cn/release/archive?tab=macos).- Create a folder where you can install Flutter. then change into it.

           Consider a path like `~/dev`.

           ```
           mkdir ~/dev; cd `~/dev`
           ```

           - Extract the SDK from the zip archive file.

             This example assumes you downloaded the macOS version of the Flutter SDK.

             ```
             unzip flutter_macos_3.13.0-stable.zip
             ```

             - Add Flutter to your `PATH` environment variable.

               ```
               export PATH="$PWD/flutter/bin:$PATH"
               ```

               - Run Flutter Doctor to verify your installation.

                 ```
                 flutter doctor
                 ```

From this example, `flutter pub get` fetches packages from `flutter-io.cn`, in any terminal where you set `PUB_HOSTED_URL` and `FLUTTER_STORAGE_BASE_URL`.

Any environment variables set using `export` in this procedure only apply to the current window.

To set these values on a permanent basis, append those three `export` commands to the `*rc` or `*profile` file that your preferred shell uses. This would resemble the following:

```
cat &#x3C;<eot>> ~/.zprofile
export PUB_HOSTED_URL="https://pub.flutter-io.cn"
export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
export PATH="$PWD/flutter/bin:$PATH"
EOT
```

This procedure requires using your terminal.

1. Open a new window in your terminal to prepare running scripts.- Set `PUB_HOSTED_URL` to your mirror site.

     ```
     export PUB_HOSTED_URL="https://pub.flutter-io.cn"
     ```

     - Set `FLUTTER_STORAGE_BASE_URL` to your mirror site.

       ```
       export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
       ```

       - Download the Flutter archive from your mirror site. In your preferred browser, go to [Flutter SDK archive](https://docs.flutter.cn/release/archive?tab=linux).- Create a folder where you can install Flutter. then change into it.

           Consider a path like `~/dev`.

           ```
           mkdir ~/dev; cd `~/dev`
           ```

           - Extract the SDK from the tar.xz archive file.

             This example assumes you downloaded the Linux version of the Flutter SDK.

             ```
             tar -xf flutter_linux_3.13.0-stable.tar.xz
             ```

             - Add Flutter to your `PATH` environment variable.

               ```
               export PATH="$PWD/flutter/bin:$PATH"
               ```

               - Run Flutter Doctor to verify your installation.

                 ```
                 flutter doctor
                 ```

From this example, `flutter pub get` fetches packages from `flutter-io.cn`, in any terminal where you set `PUB_HOSTED_URL` and `FLUTTER_STORAGE_BASE_URL`.

Any environment variables set using `export` in this procedure only apply to the current window.

To set these values on a permanent basis, append those three `export` commands to the `*rc` or `*profile` file that your preferred shell uses. This would resemble the following:

```
cat &#x3C;<eot>> ~/.zprofile
export PUB_HOSTED_URL="https://pub.flutter-io.cn"
export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
export PATH="$PWD/flutter/bin:$PATH"
EOT
```

This procedure requires using your terminal.

1. Open a new window in your terminal to prepare running scripts.- Set `PUB_HOSTED_URL` to your mirror site.

     ```
     export PUB_HOSTED_URL="https://pub.flutter-io.cn"
     ```

     - Set `FLUTTER_STORAGE_BASE_URL` to your mirror site.

       ```
       export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
       ```

       - Download the Flutter archive from your mirror site. In your preferred browser, go to [Flutter SDK archive](https://docs.flutter.cn/release/archive?tab=chromeos).- Create a folder where you can install Flutter. then change into it.

           Consider a path like `~/dev`.

           ```
           mkdir ~/dev; cd `~/dev`
           ```

           - Extract the SDK from the tar.xz archive file.

             This example assumes you downloaded the ChromeOS version of the Flutter SDK.

             ```
             tar -xf flutter_linux_3.13.0-stable.tar.xz
             ```

             - Add Flutter to your `PATH` environment variable.

               ```
               export PATH="$PWD/flutter/bin:$PATH"
               ```

               - Run Flutter Doctor to verify your installation.

                 ```
                 flutter doctor
                 ```

From this example, `flutter pub get` fetches packages from `flutter-io.cn`, in any terminal where you set `PUB_HOSTED_URL` and `FLUTTER_STORAGE_BASE_URL`.

Any environment variables set using `export` in this procedure only apply to the current window.

To set these values on a permanent basis, append those three `export` commands to the `*rc` or `*profile` file that your preferred shell uses. This would resemble the following:

```
cat &#x3C;<eot>> ~/.zprofile
export PUB_HOSTED_URL="https://pub.flutter-io.cn"
export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
export PATH="$PWD/flutter/bin:$PATH"
EOT
```

### Download Flutter archives based on a mirror site

[#](#download-flutter-archives-based-on-a-mirror-site)

To download Flutter from the [SDK archive](/install/archive) from a mirror, replace `storage.googleapis.com` with the URL of your trusted mirror. Use your mirror site in the browser or in other applications like IDM or Thunder. This should improve download speed.

The following example shows how to change the URL for Flutter's download site from Google's archive to CFUG's mirror.

* [Windows](#61-tab-panel)* [macOS](#62-tab-panel)* [Linux](#63-tab-panel)* [ChromeOS](#64-tab-panel)

To download the Windows 3.13 version of the Flutter SDK, you would change the original URL from:

```
https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.13.0-stable.zip
```

to the mirror URL:

```
https://storage.flutter-io.cn/flutter_infra_release/releases/stable/windows/flutter_windows_3.13.0-stable.zip
```

To download the macOS 3.13 version of the Flutter SDK, you would change the original URL from:

```
https://storage.googleapis.com/flutter_infra_release/releases/stable/macos/flutter_macos_3.13.0-stable.zip
```

to the mirror URL:

```
https://storage.flutter-io.cn/flutter_infra_release/releases/stable/macos/flutter_macos_3.13.0-stable.zip
```

To download the Linux 3.13 version of the Flutter SDK, you would change the original URL from:

```
https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.13.0-stable.tar.xz
```

to the mirror URL:

```
https://storage.flutter-io.cn/flutter_infra_release/releases/stable/linux/flutter_linux_3.13.0-stable.tar.xz
```

To download the ChromeOS 3.13 version of the Flutter SDK, you would change the original URL from:

```
https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.13.0-stable.tar.xz
```

to the mirror URL:

```
https://storage.flutter-io.cn/flutter_infra_release/releases/stable/linux/flutter_linux_3.13.0-stable.tar.xz
```

*info* Note

Not every mirror supports downloading artifacts using their direct URL.

Configure your machine to publish your package
----------------------------------------------

[#](#configure-your-machine-to-publish-your-package)

To publish your packages to `pub.dev`, you need to be able to access both Google Auth and the `pub.dev` site.

To enable access to `pub.dev`:

* [Windows](#65-tab-panel)* [macOS](#66-tab-panel)* [Linux](#67-tab-panel)* [ChromeOS](#68-tab-panel)

1. Configure a proxy. To configure a proxy, check out the [Dart documentation on proxies](https://dart.dev/tools/pub/troubleshoot#pub-get-fails-from-behind-a-corporate-firewall).- Verify that your `PUB_HOSTED_URL` environment variable is either unset or empty.

     ```
     echo $env:PUB_HOSTED_URL
     ```

     If this command returns any value, unset it.

     ```
     Remove-Item $env:PUB_HOSTED_URL
     ```

1. Configure a proxy. To configure a proxy, check out the [Dart documentation on proxies](https://dart.dev/tools/pub/troubleshoot#pub-get-fails-from-behind-a-corporate-firewall).- Verify that your `PUB_HOSTED_URL` environment variable is either unset or empty.

     ```
     echo $PUB_HOSTED_URL
     ```

     If this command returns any value, unset it.

     ```
     unset $PUB_HOSTED_URL
     ```

To learn more about publishing packages, check out the [Dart documentation on publishing packages](https://dart.dev/tools/pub/publishing).

Known, trusted community-run mirror sites
-----------------------------------------

[#](#known-trusted-community-run-mirror-sites)

The Flutter team can't guarantee long-term availability of any mirrors. You can use other mirrors if they become available.

---

### China Flutter User Group

[#](#china-flutter-user-group)

[China Flutter User Group](https://github.com/cfug) maintains the `flutter-io.cn` mirror. It includes the Flutter SDK and pub packages.

#### Configure your machine to use this mirror

[#](#configure-your-machine-to-use-this-mirror)

To set your machine to use this mirror, use these commands.

On macOS, Linux, or ChromeOS:

```
export PUB_HOSTED_URL=https://pub.flutter-io.cn;
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```

On Windows:

```
$env:PUB_HOSTED_URL="https://pub.flutter-io.cn";
$env:FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
```

#### Get support for this mirror

[#](#get-support-for-this-mirror)

If you're running into issues that only occur when using the `flutter-io.cn` mirror, report the issue to their [issue tracker](https://github.com/cfug/flutter.cn/issues/new/choose).

---

### Shanghai Jiao Tong University \*nix User Group

[#](#shanghai-jiao-tong-university-nix-user-group)

[Shanghai Jiao Tong University \*nix User Group](https://github.com/sjtug) maintains the `mirror.sjtu.edu.cn` mirror. It includes the Flutter SDK and pub packages.

#### Configure your machine to use this mirror

[#](#configure-your-machine-to-use-this-mirror-1)

To set your machine to use this mirror, use these commands.

On macOS, Linux, or ChromeOS:

```
export PUB_HOSTED_URL=https://mirror.sjtu.edu.cn/dart-pub;
export FLUTTER_STORAGE_BASE_URL=https://mirror.sjtu.edu.cn
```

On Windows:

```
$env:PUB_HOSTED_URL="https://mirror.sjtu.edu.cn/dart-pub";
$env:FLUTTER_STORAGE_BASE_URL="https://mirror.sjtu.edu.cn"
```

#### Get support for this mirror

[#](#get-support-for-this-mirror-1)

If you're running into issues that only occur when using the `mirror.sjtu.edu.cn` mirror, report the issue to their [issue tracker](https://github.com/sjtug/mirror-requests).

---

### Tsinghua University TUNA Association

[#](#tsinghua-university-tuna-association)

[Tsinghua University TUNA Association](https://tuna.moe) maintains the `mirrors.tuna.tsinghua.edu.cn` mirror. It includes the Flutter SDK and pub packages.

#### Configure your machine to use this mirror

[#](#configure-your-machine-to-use-this-mirror-2)

To set your machine to use this mirror, use these commands.

On macOS, Linux, or ChromeOS:

```
export PUB_HOSTED_URL=https://mirrors.tuna.tsinghua.edu.cn/dart-pub;
export FLUTTER_STORAGE_BASE_URL=https://mirrors.tuna.tsinghua.edu.cn/flutter
```

On Windows:

```
$env:PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub";
$env:FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"
```

#### Get support for this mirror

[#](#get-support-for-this-mirror-2)

If you're running into issues that only occur when using the `mirrors.tuna.tsinghua.edu.cn` mirror, report the issue to their [issue tracker](https://github.com/tuna/issues).

Offer to host a new mirror site
-------------------------------

[#](#offer-to-host-a-new-mirror-site)

If you're interested in setting up your own mirror, contact [flutter-dev@googlegroups.com](mailto:flutter-dev@googlegroups.com) for assistance.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/community/china/&page-source=https://github.com/flutter/website/tree/main/src/content/community/china/index.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/community/china/&page-source=https://github.com/flutter/website/tree/main/src/content/community/china/index.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-08-25. [View source](https://github.com/flutter/website/tree/main/src/content/community/china/index.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/community/china/&page-source=https://github.com/flutter/website/tree/main/src/content/community/china/index.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   