Add achievements and leaderboards to your mobile game
=====================================================

1. [Cookbook](/cookbook) chevron\_right- [Games](/cookbook/games) chevron\_right- [Add achievements and leaderboards to your mobile game](/cookbook/games/achievements-leaderboard)

Gamers have various motivations for playing games. In broad strokes, there are four major motivations: [immersion, achievement, cooperation, and competition](https://meditations.metavert.io/p/game-player-motivations). No matter the game you build, some players want to *achieve* in it. This could be trophies won or secrets unlocked. Some players want to *compete* in it. This could be hitting high scores or accomplishing speedruns. These two ideas map to the concepts of *achievements* and *leaderboards*.

![A simple graphic representing the four types of motivation explained above](/assets/images/docs/cookbook/types-of-gamer-motivations.png)

Ecosystems such as the App Store and Google Play provide centralized services for achievements and leaderboards. Players can view achievements from all their games in one place and developers don't need to re-implement them for every game.

This recipe demonstrates how to use the [`games_services` package](https://pub.dev/packages/games_services) to add achievements and leaderboard functionality to your mobile game.

1. Enable platform services
---------------------------

[#](#1-enable-platform-services)

To enable games services, set up *Game Center* on iOS and *Google Play Games Services* on Android.

### iOS

[#](#ios)

To enable Game Center (GameKit) on iOS:

1. Open your Flutter project in Xcode. Open `ios/Runner.xcworkspace`- Select the root **Runner** project.- Go to the **Signing & Capabilities** tab.- Click the `+` button to add **Game Center** as a capability.- Close Xcode.- If you haven't already, register your game in [App Store Connect](https://appstoreconnect.apple.com/) and from the **My App** section press the `+` icon.

             ![Screenshot of the + button in App Store Connect](/assets/images/docs/cookbook/app-store-add-app-button.png)- Still in App Store Connect, look for the *Game Center* section. You can find it in **Services** as of this writing. On the **Game Center** page, you might want to set up a leaderboard and several achievements, depending on your game. Take note of the IDs of the leaderboards and achievements you create.

### Android

[#](#android)

To enable *Play Games Services* on Android:

1. If you haven't already, go to [Google Play Console](https://play.google.com/console/) and register your game there.

   ![Screenshot of the 'Create app' button in Google Play Console](/assets/images/docs/cookbook/google-play-create-app.png)- Still in Google Play Console, select *Play Games Services* → *Setup and management* → *Configuration* from the navigation menu and follow their instructions.
     * This takes a significant amount of time and patience. Among other things, you'll need to set up an OAuth consent screen in Google Cloud Console. If at any point you feel lost, consult the official [Play Games Services guide](https://developers.google.com/games/services/console/enabling).

       ![Screenshot showing the Games Services section in Google Play Console](/assets/images/docs/cookbook/play-console-play-games-services.png)- When done, you can start adding leaderboards and achievements in **Play Games Services** → **Setup and management**. Create the exact same set as you did on the iOS side. Make note of IDs.- Go to **Play Games Services → Setup and management → Publishing**.- Click **Publish**. Don't worry, this doesn't actually publish your game. It only publishes the achievements and leaderboard. Once a leaderboard, for example, is published this way, it cannot be unpublished.- Go to **Play Games Services** **→ Setup and management → Configuration → Credentials**.- Find the **Get resources** button. It returns an XML file with the Play Games Services IDs.

               xml

               ```
               <!-- THIS IS JUST AN EXAMPLE -->
               <?xml version="1.0" encoding="utf-8"?>
               <resources>
                   <!--app_id-->
                   <string name="app_id" translatable="false">424242424242</string>
                   <!--package_name-->
                   <string name="package_name" translatable="false">dev.flutter.tictactoe</string>
                   <!--achievement First win-->
                   <string name="achievement_first_win" translatable="false">sOmEiDsTrInG</string>
                   <!--leaderboard Highest Score-->
                   <string name="leaderboard_highest_score" translatable="false">sOmEiDsTrInG</string>
               </resources>
               ```

               - Add a file at `android/app/src/main/res/values/games-ids.xml` containing the XML you received in the previous step.

2. Sign in to the game service
------------------------------

[#](#2-sign-in-to-the-game-service)

Now that you have set up *Game Center* and *Play Games Services*, and have your achievement & leaderboard IDs ready, it's finally Dart time.

1. Add a dependency on the [`games_services` package](https://pub.dev/packages/games_services).

   ```
   flutter pub add games_services
   ```

   - Before you can do anything else, you have to sign the player into the game service.

     dart

     ```
     try {
       await GamesServices.signIn();
     } on PlatformException catch (e) {
       // ... deal with failures ...
     }
     ```

The sign in happens in the background. It takes several seconds, so don't call `signIn()` before `runApp()` or the players will be forced to stare at a blank screen every time they start your game.

The API calls to the `games_services` API can fail for a multitude of reasons. Therefore, every call should be wrapped in a try-catch block as in the previous example. The rest of this recipe omits exception handling for clarity.

*lightbulb* Tip

It's a good practice to create a controller. This would be a `ChangeNotifier`, a bloc, or some other piece of logic that wraps around the raw functionality of the `games_services` plugin.

3. Unlock achievements
----------------------

[#](#3-unlock-achievements)

1. Register achievements in Google Play Console and App Store Connect, and take note of their IDs. Now you can award any of those achievements from your Dart code:

   dart

   ```
   await GamesServices.unlock(
     achievement: Achievement(
       androidID: 'your android id',
       iOSID: 'your ios id',
     ),
   );
   ```

   The player's account on Google Play Games or Apple Game Center now lists the achievement.- To display the achievements UI from your game, call the `games_services` API:

     dart

     ```
     await GamesServices.showAchievements();
     ```

     This displays the platform achievements UI as an overlay on your game.- To display the achievements in your own UI, use [`GamesServices.loadAchievements()`](https://pub.dev/documentation/games_services/latest/games_services/GamesServices/loadAchievements.html).

4. Submit scores
----------------

[#](#4-submit-scores)

When the player finishes a play-through, your game can submit the result of that play session into one or more leaderboards.

For example, a platformer game like Super Mario can submit both the final score and the time taken to complete the level, to two separate leaderboards.

1. In the first step, you registered a leaderboard in Google Play Console and App Store Connect, and took note of its ID. Using this ID, you can submit new scores for the player:

   dart

   ```
   await GamesServices.submitScore(
     score: Score(
       iOSLeaderboardID: 'some_id_from_app_store',
       androidLeaderboardID: 'sOmE_iD_fRoM_gPlAy',
       value: 100,
     ),
   );
   ```

   You don't need to check whether the new score is the player's highest. The platform game services handle that for you.- To display the leaderboard as an overlay over your game, make the following call:

     dart

     ```
     await GamesServices.showLeaderboards(
       iOSLeaderboardID: 'some_id_from_app_store',
       androidLeaderboardID: 'sOmE_iD_fRoM_gPlAy',
     );
     ```

     - If you want to display the leaderboard scores in your own UI, you can fetch them with [`GamesServices.loadLeaderboardScores()`](https://pub.dev/documentation/games_services/latest/games_services/GamesServices/loadLeaderboardScores.html).

5. Next steps
-------------

[#](#5-next-steps)

There's more to the `games_services` plugin. With this plugin, you can:

* Get the player's icon, name or unique ID* Save and load game states* Sign out of the game service

Some achievements can be incremental. For example: "You have collected all 10 pieces of the McGuffin."

Each game has different needs from game services.

To start, you might want to create this controller in order to keep all achievements & leaderboards logic in one place:

dart

```
import 'dart:async';

import 'package:games_services/games_services.dart';
import 'package:logging/logging.dart';

/// Allows awarding achievements and leaderboard scores,
/// and also showing the platforms' UI overlays for achievements
/// and leaderboards.
///
/// A facade of `package:games_services`.
class GamesServicesController {
  static final Logger _log = Logger('GamesServicesController');

  final Completer<bool> _signedInCompleter = Completer();

  Future<bool> get signedIn => _signedInCompleter.future;

  /// Unlocks an achievement on Game Center / Play Games.
  ///
  /// You must provide the achievement ids via the [iOS] and [android]
  /// parameters.
  ///
  /// Does nothing when the game isn't signed into the underlying
  /// games service.
  Future<void> awardAchievement({
    required String iOS,
    required String android,
  }) async {
    if (!await signedIn) {
      _log.warning('Trying to award achievement when not logged in.');
      return;
    }

    try {
      await GamesServices.unlock(
        achievement: Achievement(androidID: android, iOSID: iOS),
      );
    } catch (e) {
      _log.severe('Cannot award achievement: $e');
    }
  }

  /// Signs into the underlying games service.
  Future<void> initialize() async {
    try {
      await GamesServices.signIn();
      // The API is unclear so we're checking to be sure. The above call
      // returns a String, not a boolean, and there's no documentation
      // as to whether every non-error result means we're safely signed in.
      final signedIn = await GamesServices.isSignedIn;
      _signedInCompleter.complete(signedIn);
    } catch (e) {
      _log.severe('Cannot log into GamesServices: $e');
      _signedInCompleter.complete(false);
    }
  }

  /// Launches the platform's UI overlay with achievements.
  Future<void> showAchievements() async {
    if (!await signedIn) {
      _log.severe('Trying to show achievements when not logged in.');
      return;
    }

    try {
      await GamesServices.showAchievements();
    } catch (e) {
      _log.severe('Cannot show achievements: $e');
    }
  }

  /// Launches the platform's UI overlay with leaderboard(s).
  Future<void> showLeaderboard() async {
    if (!await signedIn) {
      _log.severe('Trying to show leaderboard when not logged in.');
      return;
    }

    try {
      await GamesServices.showLeaderboards(
        // TODO: When ready, change both these leaderboard IDs.
        iOSLeaderboardID: 'some_id_from_app_store',
        androidLeaderboardID: 'sOmE_iD_fRoM_gPlAy',
      );
    } catch (e) {
      _log.severe('Cannot show leaderboard: $e');
    }
  }

  /// Submits [score] to the leaderboard.
  Future<void> submitLeaderboardScore(int score) async {
    if (!await signedIn) {
      _log.warning('Trying to submit leaderboard when not logged in.');
      return;
    }

    _log.info('Submitting $score to leaderboard.');

    try {
      await GamesServices.submitScore(
        score: Score(
          // TODO: When ready, change these leaderboard IDs.
          iOSLeaderboardID: 'some_id_from_app_store',
          androidLeaderboardID: 'sOmE_iD_fRoM_gPlAy',
          value: score,
        ),
      );
    } catch (e) {
      _log.severe('Cannot submit leaderboard score: $e');
    }
  }
}
```

More information
----------------

[#](#more-information)

The Flutter Casual Games Toolkit includes the following templates:

* [basic](https://github.com/flutter/games/tree/main/templates/basic#readme): basic starter game* [card](https://github.com/flutter/games/tree/main/templates/card#readme): starter card game* [endless runner](https://github.com/flutter/games/tree/main/templates/endless_runner#readme): starter game (using Flame) where the player endlessly runs, avoiding pitfalls and gaining rewards

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/games/achievements-leaderboard/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/games/achievements-leaderboard.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/games/achievements-leaderboard/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/games/achievements-leaderboard.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2025-02-12. [View source](https://github.com/flutter/website/tree/main/src/content/cookbook/games/achievements-leaderboard.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/cookbook/games/achievements-leaderboard/&page-source=https://github.com/flutter/website/tree/main/src/content/cookbook/games/achievements-leaderboard.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   