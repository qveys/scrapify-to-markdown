Build and release a Linux app to the Snap Store
===============================================

1. [Deployment](/deployment) chevron\_right- [Linux](/deployment/linux)

During a typical development cycle, you test an app using `flutter run` at the command line, or by using the **Run** and **Debug** options in your IDE. By default, Flutter builds a *debug* version of your app.

When you're ready to prepare a *release* version of your app, for example to [publish to the Snap Store](https://snapcraft.io/store) or an [alternative channel](#additional-deployment-resources), this page can help.

Prerequisites
-------------

[#](#prerequisites)

To build and publish to the Snap Store, you need the following components:

* [Ubuntu](https://ubuntu.com/download/desktop) OS, 18.04 LTS (or higher)* [Snapcraft](https://snapcraft.io/snapcraft) command line tool* [LXD container manager](https://linuxcontainers.org/lxd/downloads/)

Set up the build environment
----------------------------

[#](#set-up-the-build-environment)

Use the following instructions to set up your build environment.

### Install snapcraft

[#](#install-snapcraft)

At the command line, run the following:

```
sudo snap install snapcraft --classic
```

### Install LXD

[#](#install-lxd)

To install LXD, use the following command:

```
sudo snap install lxd
```

LXD is required during the snap build process. Once installed, LXD needs to be configured for use. The default answers are suitable for most use cases.

```
sudo lxd init
Would you like to use LXD clustering? (yes/no) [default=no]:
Do you want to configure a new storage pool? (yes/no) [default=yes]:
Name of the new storage pool [default=default]:
Name of the storage backend to use (btrfs, dir, lvm, zfs, ceph) [default=zfs]:
Create a new ZFS pool? (yes/no) [default=yes]:
Would you like to use an existing empty disk or partition? (yes/no) [default=no]:
Size in GB of the new loop device (1GB minimum) [default=5GB]:
Would you like to connect to a MAAS server? (yes/no) [default=no]:
Would you like to create a new local network bridge? (yes/no) [default=yes]:
What should the new bridge be called? [default=lxdbr0]:
What IPv4 address should be used? (CIDR subnet notation, "auto" or "none") [default=auto]:
What IPv6 address should be used? (CIDR subnet notation, "auto" or "none") [default=auto]:
Would you like LXD to be available over the network? (yes/no) [default=no]:
Would you like stale cached images to be updated automatically? (yes/no) [default=yes]
Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]:
```

On the first run, LXD might not be able to connect to its socket:

```
An error occurred when trying to communicate with the 'LXD'
provider: cannot connect to the LXD socket
('/var/snap/lxd/common/lxd/unix.socket').
```

This means you need to add your username to the LXD (lxd) group, so log out of your session and then log back in:

```
sudo usermod -a -G lxd <your username>
```

Overview of snapcraft
---------------------

[#](#overview-of-snapcraft)

The `snapcraft` tool builds snaps based on the instructions listed in a `snapcraft.yaml` file. To get a basic understanding of snapcraft and its core concepts, take a look at the [Snap documentation](https://snapcraft.io/docs) and the [Introduction to snapcraft](https://snapcraft.io/blog/introduction-to-snapcraft). Additional links and information are listed at the bottom of this page.

Flutter snapcraft.yaml example
------------------------------

[#](#flutter-snapcraft-yaml-example)

Place the YAML file in your Flutter project under `<project root>/snap/snapcraft.yaml`. (And remember that YAML files are sensitive to white space!) For example:

yaml

```
name: super-cool-app
version: 0.1.0
summary: Super Cool App
description: Super Cool App that does everything!

confinement: strict
base: core22
grade: stable

slots:
  dbus-super-cool-app: # adjust accordingly to your app name
    interface: dbus
    bus: session
    name: org.bar.super_cool_app # adjust accordingly to your app name and
    
apps:
  super-cool-app:
    command: super_cool_app
    extensions: [gnome] # gnome includes the libraries required by flutter
    plugs:
    - network
    slots:
      - dbus-super-cool-app
parts:
  super-cool-app:
    source: .
    plugin: flutter
    flutter-target: lib/main.dart # The main entry-point file of the application
```

The following sections explain the various pieces of the YAML file.

### Metadata

[#](#metadata)

This section of the `snapcraft.yaml` file defines and describes the application. The snap version is derived (adopted) from the build section.

yaml

```
name: super-cool-app
version: 0.1.0
summary: Super Cool App
description: Super Cool App that does everything!
```

### Grade, confinement, and base

[#](#grade-confinement-and-base)

This section defines how the snap is built.

yaml

```
confinement: strict
base: core22
grade: stable
```

**Grade**: Specifies the quality of the snap; this is relevant for the publication step later. **Confinement**: Specifies what level of system resource access the snap will have once installed on the end-user system. Strict confinement limits the application access to specific resources (defined by plugs in the `app` section). **Base**: Snaps are designed to be self-contained applications, and therefore, they require their own private core root filesystem known as `base`. The `base` keyword specifies the version used to provide the minimal set of common libraries, and mounted as the root filesystem for the application at runtime.

### Apps

[#](#apps)

This section defines the application(s) that exist inside the snap. There can be one or more applications per snap. This example has a single application—super\_cool\_app.

yaml

```
apps:
  super-cool-app:
    command: super_cool_app
    extensions: [gnome]
```

**Command**: Points to the binary, relative to the snap's root, and runs when the snap is invoked. **Extensions**: A list of one or more extensions. Snapcraft extensions are reusable components that can expose sets of libraries and tools to a snap at build and runtime, without the developer needing to have specific knowledge of included frameworks. The `gnome` extension exposes the GTK 3 libraries to the Flutter snap. This ensures a smaller footprint and better integration with the system. **Plugs**: A list of one or more plugs for system interfaces. These are required to provide necessary functionality when snaps are strictly confined. This Flutter snap needs access to the network. **DBus interface**: The [DBus interface](https://snapcraft.io/docs/dbus-interface) provides a way for snaps to communicate over DBus. The snap providing the DBus service declares a slot with the well-known DBus name and which bus it uses. Snaps wanting to communicate with the providing snap's service declare a plug for the providing snap. Note that a snap declaration is needed for your snap to be delivered via the snap store and claim this well-known DBus name (simply upload the snap to the store and request a manual review and a reviewer will take a look). When a providing snap is installed, snapd will generate security policy that will allow it to listen on the well-known DBus name on the specified bus. If the system bus is specified, snapd will also generate DBus bus policy that allows 'root' to own the name and any user to communicate with the service. Non-snap processes are allowed to communicate with the providing snap following traditional permissions checks. Other (consuming) snaps might only communicate with the providing snap by connecting the snaps' interface.

```
dbus-super-cool-app: # adjust accordingly to your app name
  interface: dbus
  bus: session
  name: dev.site.super_cool_app
```

### Parts

[#](#parts)

This section defines the sources required to assemble the snap.

Parts can be downloaded and built automatically using plugins. Similar to extensions, snapcraft can use various plugins (such as Python, C, Java, and Ruby) to assist in the building process. Snapcraft also has some special plugins.

**nil** plugin: Performs no action and the actual build process is handled using a manual override. **flutter** plugin: Provides the necessary Flutter SDK tools so you can use it without having to manually download and set up the build tools.

yaml

```
parts:
  super-cool-app:
    source: .
    plugin: flutter
    flutter-target: lib/main.dart # The main entry-point file of the application
```

Desktop file and icon
---------------------

[#](#desktop-file-and-icon)

Desktop entry files are used to add an application to the desktop menu. These files specify the name and icon of your application, the categories it belongs to, related search keywords and more. These files have the extension .desktop and follow the XDG Desktop Entry Specification version 1.1.

### Flutter super-cool-app.desktop example

[#](#flutter-super-cool-app-desktop-example)

Place the .desktop file in your Flutter project under `<project root>/snap/gui/super-cool-app.desktop`.

**Notice**: icon and .desktop file name must be the same as your app name in yaml file!

For example:

yaml

```
[Desktop Entry]
Name=Super Cool App
Comment=Super Cool App that does everything
Exec=super-cool-app 
Icon=${SNAP}/meta/gui/super-cool-app.png # Replace name with your app name.
Terminal=false
Type=Application
Categories=Education; # Adjust accordingly your snap category.
```

Place your icon with .png extension in your Flutter project under `<project root>/snap/gui/super-cool-app.png`.

Build the snap
--------------

[#](#build-the-snap)

Once the `snapcraft.yaml` file is complete, run `snapcraft` as follows from the root directory of the project.

To use the Multipass VM backend:

```
snapcraft
```

To use the LXD container backend:

```
snapcraft --use-lxd
```

Test the snap
-------------

[#](#test-the-snap)

Once the snap is built, you'll have a `<name>.snap` file in your root project directory.

$ sudo snap install ./super-cool-app\_0.1.0\_amd64.snap --dangerous

Publish
-------

[#](#publish)

You can now publish the snap. The process consists of the following:

1. Create a developer account at [snapcraft.io](https://snapcraft.io/), if you haven't already done so.- Register the app's name. Registration can be done either using the Snap Store Web UI portal, or from the command line, as follows:

     ```
     snapcraft login
     snapcraft register
     ```

     - Release the app. After reading the next section to learn about selecting a Snap Store channel, push the snap to the store:

       ```
       snapcraft upload --release=<channel> <file>.snap
       ```

### Snap Store channels

[#](#snap-store-channels)

The Snap Store uses channels to differentiate among different versions of snaps.

The `snapcraft upload` command uploads the snap file to the store. However, before you run this command, you need to learn about the different release channels. Each channel consists of three components:

**Track**: All snaps must have a default track called latest. This is the implied track unless specified otherwise. **Risk**: Defines the readiness of the application. The risk levels used in the snap store are: `stable`, `candidate`, `beta`, and `edge`. **Branch**: Allows creation of short-lived snap sequences to test bug-fixes.

### Snap Store automatic review

[#](#snap-store-automatic-review)

The Snap Store runs several automated checks against your snap. There might also be a manual review, depending on how the snap was built, and if there are any specific security concerns. If the checks pass without errors, the snap becomes available in the store.

Additional snapcraft resources
------------------------------

[#](#additional-snapcraft-resources)

You can learn more from the following links on the [snapcraft.io](https://snapcraft.io/) site:

* [Channels](https://docs.snapcraft.io/channels)* [Environment variables](https://snapcraft.io/docs/environment-variables)* [Interface management](https://snapcraft.io/docs/interface-management)* [Parts environment variables](https://snapcraft.io/docs/parts-environment-variables)* [Releasing to the Snap Store](https://snapcraft.io/docs/releasing-to-the-snap-store)* [Snapcraft extensions](https://snapcraft.io/docs/snapcraft-extensions)* [Supported plugins](https://snapcraft.io/docs/supported-plugins)

Additional deployment resources
-------------------------------

[#](#additional-deployment-resources)

### [fastforge](https://github.com/fastforgedev/fastforge)

[#](#fastforge)

> An all-in-one Flutter application packaging and distribution tool, providing you with a one-stop solution to meet various distribution needs.

Supports popular packaging formats like, appimage, deb, pacman, rpm, and more.

### [flatpak-flutter](https://github.com/TheAppgineer/flatpak-flutter)

[#](#flatpak-flutter)

> Flatpak manifest tooling for the offline build of Flutter apps.

Supports Flatpak preparation for publishing on [Flathub](https://flathub.org).

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/linux/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/linux.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/linux/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/linux.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-09-05. [View source](https://github.com/flutter/website/tree/main/src/content/deployment/linux.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/linux/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/linux.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   