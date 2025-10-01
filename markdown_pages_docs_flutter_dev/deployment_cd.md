Continuous delivery with Flutter
================================

1. [Deployment](/deployment) chevron\_right- [Continuous delivery with Flutter](/deployment/cd)

Follow continuous delivery best practices with Flutter to make sure your application is delivered to your beta testers and validated on a frequent basis without resorting to manual workflows.

CI/CD Options
-------------

[#](#cicd-options)

There are a number of continuous integration (CI) and continuous delivery (CD) options available to help automate the delivery of your application.

### All-in-one options with built-in Flutter functionality

[#](#all-in-one-options-with-built-in-flutter-functionality)

* [Codemagic](https://blog.codemagic.io/getting-started-with-codemagic/)* [Bitrise](https://devcenter.bitrise.io/en/getting-started/quick-start-guides/getting-started-with-flutter-apps)* [Appcircle](https://appcircle.io/blog/guide-to-automated-mobile-ci-cd-for-flutter-projects-with-appcircle/)

### Integrating fastlane with existing workflows

[#](#integrating-fastlane-with-existing-workflows)

You can use fastlane with the following tooling:

* [GitHub Actions](https://github.com/features/actions)
  + Example: [Github Action in Flutter Project](https://github.com/nabilnalakath/flutter-githubaction)* [Cirrus](https://cirrus-ci.org)* [Travis](https://travis-ci.org/)* [GitLab](https://docs.gitlab.com/ee/ci/)* [CircleCI](https://circleci.com)
          + [Building and deploying Flutter apps with Fastlane](https://circleci.com/blog/deploy-flutter-android)

This guide shows how to set up fastlane and then integrate it with your existing testing and continuous integration (CI) workflows. For more information, see "Integrating fastlane with existing workflow".

fastlane
--------

[#](#fastlane)

[fastlane](https://docs.fastlane.tools) is an open-source tool suite to automate releases and deployments for your app.

### Local setup

[#](#local-setup)

It's recommended that you test the build and deployment process locally before migrating to a cloud-based system. You could also choose to perform continuous delivery from a local machine.

1. Install fastlane `gem install fastlane` or `brew install fastlane`. Visit the [fastlane docs](https://docs.fastlane.tools) for more info.- Create an environment variable named `FLUTTER_ROOT`, and set it to the root directory of your Flutter SDK. (This is required for the scripts that deploy for iOS.)- Create your Flutter project, and when ready, make sure that your project builds via
       * ![Android](/assets/images/docs/cd/android.png) `flutter build appbundle`; and* ![iOS](/assets/images/docs/cd/ios.png) `flutter build ipa`.- Initialize the fastlane projects for each platform.
         * ![Android](/assets/images/docs/cd/android.png) In your `[project]/android` directory, run `fastlane init`.* ![iOS](/assets/images/docs/cd/ios.png) In your `[project]/ios` directory, run `fastlane init`.- Edit the `Appfile`s to ensure they have adequate metadata for your app.
           * ![Android](/assets/images/docs/cd/android.png) Check that `package_name` in `[project]/android/fastlane/Appfile` matches your package name in AndroidManifest.xml.* ![iOS](/assets/images/docs/cd/ios.png) Check that `app_identifier` in `[project]/ios/fastlane/Appfile` also matches Info.plist's bundle identifier. Fill in `apple_id`, `itc_team_id`, `team_id` with your respective account info.- Set up your local login credentials for the stores.
             * ![Android](/assets/images/docs/cd/android.png) Follow the [Supply setup steps](https://docs.fastlane.tools/getting-started/android/setup/#setting-up-supply) and ensure that `fastlane supply init` successfully syncs data from your Play Store console. *Treat the .json file like your password and do not check it into any public source control repositories.** ![iOS](/assets/images/docs/cd/ios.png) Your iTunes Connect username is already in your `Appfile`'s `apple_id` field. Set the `FASTLANE_PASSWORD` shell environment variable with your iTunes Connect password. Otherwise, you'll be prompted when uploading to iTunes/TestFlight.- Set up code signing.
               * ![Android](/assets/images/docs/cd/android.png) Follow the [Android app signing steps](/deployment/android#signing-the-app).* ![iOS](/assets/images/docs/cd/ios.png) On iOS, create and sign using a distribution certificate instead of a development certificate when you're ready to test and deploy using TestFlight or App Store.
                   + Create and download a distribution certificate in your [Apple Developer Account console](https://developer.apple.com/account/ios/certificate/).+ `open [project]/ios/Runner.xcworkspace/` and select the distribution certificate in your target's settings pane.- Create a `Fastfile` script for each platform.
                 * ![Android](/assets/images/docs/cd/android.png) On Android, follow the [fastlane Android beta deployment guide](https://docs.fastlane.tools/getting-started/android/beta-deployment/). Your edit could be as simple as adding a `lane` that calls `upload_to_play_store`. Set the `aab` argument to `../build/app/outputs/bundle/release/app-release.aab` to use the app bundle `flutter build` already built.* ![iOS](/assets/images/docs/cd/ios.png) On iOS, follow the [fastlane iOS beta deployment guide](https://docs.fastlane.tools/getting-started/ios/beta-deployment/). You can specify the archive path to avoid rebuilding the project. For example:

                     ruby

                     ```
                     build_app(
                       skip_build_archive: true,
                       archive_path: "../build/ios/archive/Runner.xcarchive",
                     )
                     upload_to_testflight
                     ```

You're now ready to perform deployments locally or migrate the deployment process to a continuous integration (CI) system.

### Running deployment locally

[#](#running-deployment-locally)

1. Build the release mode app.
   * ![Android](/assets/images/docs/cd/android.png) `flutter build appbundle`.* ![iOS](/assets/images/docs/cd/ios.png) `flutter build ipa`.- Run the Fastfile script on each platform.
     * ![Android](/assets/images/docs/cd/android.png) `cd android` then `fastlane [name of the lane you created]`.* ![iOS](/assets/images/docs/cd/ios.png) `cd ios` then `fastlane [name of the lane you created]`.

### Cloud build and deploy setup

[#](#cloud-build-and-deploy-setup)

First, follow the local setup section described in 'Local setup' to make sure the process works before migrating onto a cloud system like Travis.

The main thing to consider is that since cloud instances are ephemeral and untrusted, you won't be leaving your credentials like your Play Store service account JSON or your iTunes distribution certificate on the server.

Continuous Integration (CI) systems generally support encrypted environment variables to store private data. You can pass these environment variables using `--dart-define MY_VAR=MY_VALUE` while building the app.

**Take precaution not to re-echo those variable values back onto the console in your test scripts**. Those variables are also not available in pull requests until they're merged to ensure that malicious actors cannot create a pull request that prints these secrets out. Be careful with interactions with these secrets in pull requests that you accept and merge.

1. Make login credentials ephemeral.
   * ![Android](/assets/images/docs/cd/android.png) On Android:
     + Remove the `json_key_file` field from `Appfile` and store the string content of the JSON in your CI system's encrypted variable. Read the environment variable directly in your `Fastfile`.

       ```
       upload_to_play_store(
         ...
         json_key_data: ENV['<variable name>']
       )
       ```

       + Serialize your upload key (for example, using base64) and save it as an encrypted environment variable. You can deserialize it on your CI system during the install phase with

         bash

         ```
         echo "$PLAY_STORE_UPLOAD_KEY" | base64 --decode > [path to your upload keystore]
         ```* ![iOS](/assets/images/docs/cd/ios.png) On iOS:
       + Move the local environment variable `FASTLANE_PASSWORD` to use encrypted environment variables on the CI system.+ The CI system needs access to your distribution certificate. fastlane's [Match](https://docs.fastlane.tools/actions/match/) system is recommended to synchronize your certificates across machines.- It's recommended to use a Gemfile instead of using an indeterministic `gem install fastlane` on the CI system each time to ensure the fastlane dependencies are stable and reproducible between local and cloud machines. However, this step is optional.
     * In both your `[project]/android` and `[project]/ios` folders, create a `Gemfile` containing the following content:

       ```
       source "https://rubygems.org"

       gem "fastlane"
       ```

       * In both directories, run `bundle update` and check both `Gemfile` and `Gemfile.lock` into source control.* When running locally, use `bundle exec fastlane` instead of `fastlane`.- Create the CI test script such as `.travis.yml` or `.cirrus.yml` in your repository root.
       * See [fastlane CI documentation](https://docs.fastlane.tools/best-practices/continuous-integration) for CI specific setup.* Shard your script to run on both Linux and macOS platforms.* During the setup phase of the CI task, do the following:
             + Ensure Bundler is available using `gem install bundler`.+ Run `bundle install` in `[project]/android` or `[project]/ios`.+ Make sure the Flutter SDK is available and set in `PATH`.+ For Android, ensure the Android SDK is available and the `ANDROID_SDK_ROOT` path is set.+ For iOS, you might have to specify a dependency on Xcode (for example, `osx_image: xcode9.2`).* In the script phase of the CI task:
               + Run `flutter build appbundle` or `flutter build ios --release --no-codesign --config-only`, depending on the platform.+ `cd android` or `cd ios`+ `bundle exec fastlane [name of the lane]`

Xcode Cloud
-----------

[#](#xcode-cloud)

[Xcode Cloud](https://developer.apple.com/xcode-cloud) is a continuous integration and delivery service for building, testing, and distributing apps and frameworks for Apple platforms.

### Requirements

[#](#requirements)

* Xcode 13.4.1 or higher.* Be enrolled in the [Apple Developer Program](https://developer.apple.com/programs).

### Custom build script

[#](#custom-build-script)

Xcode Cloud recognizes [custom build scripts](https://developer.apple.com/documentation/xcode/writing-custom-build-scripts) that can be used to perform additional tasks at a designated time. It also includes a set of [predefined environment variables](https://developer.apple.com/documentation/xcode/environment-variable-reference), such as `$CI_WORKSPACE`, which is the location of your cloned repository.

*info* Note

The temporary build environment that Xcode Cloud uses includes tools that are part of macOS and Xcode—for example, Python—and additionally Homebrew to support installing third-party dependencies and tools.

#### Post-clone script

[#](#post-clone-script)

Leverage the post-clone custom build script that runs after Xcode Cloud clones your Git repository using the following instructions:

Create a file at `ios/ci_scripts/ci_post_clone.sh` and add the content below.

sh

```
#!/bin/sh

# Fail this script if any subcommand fails.
set -e

# The default execution directory of this script is the ci_scripts directory.
cd $CI_PRIMARY_REPOSITORY_PATH # change working directory to the root of your cloned repo.

# Install Flutter using git.
git clone https://github.com/flutter/flutter.git --depth 1 -b stable $HOME/flutter
export PATH="$PATH:$HOME/flutter/bin"

# Install Flutter artifacts for iOS (--ios), or macOS (--macos) platforms.
flutter precache --ios

# Install Flutter dependencies.
flutter pub get

# Install CocoaPods using Homebrew.
HOMEBREW_NO_AUTO_UPDATE=1 # disable homebrew's automatic updates.
brew install cocoapods

# Install CocoaPods dependencies.
cd ios && pod install # run `pod install` in the `ios` directory.

exit 0
```

This file should be added to your git repository and marked as executable.

```
git add --chmod=+x ios/ci_scripts/ci_post_clone.sh
```

### Workflow configuration

[#](#workflow-configuration)

An [Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference) defines the steps performed in the CI/CD process when your workflow is triggered.

*info* Note

This requires that your project is already initialized with Git and linked to a remote repository.

To create a new workflow in Xcode, use the following instructions:

1. Choose **Product > Xcode Cloud > Create Workflow** to open the **Create Workflow** sheet.- Select the product (app) that the workflow should be attached to, then click the **Next** button.- The next sheet displays an overview of the default workflow provided by Xcode, and can be customized by clicking the **Edit Workflow** button.

#### Branch changes

[#](#branch-changes)

By default Xcode suggests the Branch Changes condition that starts a new build for every change to your Git repository's default branch.

For your app's iOS variant, it's reasonable that you would want Xcode Cloud to trigger your workflow after you've made changes to your flutter packages, or modified either the Dart or iOS source files within the `lib\` and `ios\` directories.

This can be achieved by using the following Files and Folders conditions:

![Xcode Workflow Branch Changes](/assets/images/docs/releaseguide/xcode_workflow_branch_changes.png)

### Next build number

[#](#next-build-number)

Xcode Cloud defaults the build number for new workflows to `1` and increments it per successful build. If you're using an existing app with a higher build number, you'll need to configure Xcode Cloud to use the correct build number for its builds by simply specifying the `Next Build Number` in your iteration.

Check out [Setting the next build number for Xcode Cloud builds](https://developer.apple.com/documentation/xcode/setting-the-next-build-number-for-xcode-cloud-builds#Set-the-next-build-number-to-a-custom-value) for more information.

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/cd/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/cd.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/cd/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/cd.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-07-09. [View source](https://github.com/flutter/website/tree/main/src/content/deployment/cd.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/deployment/cd/&page-source=https://github.com/flutter/website/tree/main/src/content/deployment/cd.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   