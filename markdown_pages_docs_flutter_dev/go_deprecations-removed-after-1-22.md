
Deze browserversie wordt niet meer ondersteund. Upgrade naar een ondersteunde browser.

Flutter Deprecations removed after 1.22

Tab

Extern

Delen

[Inloggen](https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&osid=1&continue=https://docs.google.com/spreadsheets/d/1kZOej-h4AiRW2Td3NUnVMSb8PYLB63mpj-oFYqb_4tc/edit?usp%3Dsharing&followup=https://docs.google.com/spreadsheets/d/1kZOej-h4AiRW2Td3NUnVMSb8PYLB63mpj-oFYqb_4tc/edit?usp%3Dsharing&ltmpl=sheets&ec=GAZAmwI)

Bestand

Bewerken

Bekijken

Invoegen

Opmaak

Gegevens

Extra

Uitbreidingen

Hulp

Toegankelijkheid

Foutopsporing

Niet-opgeslagen wijzigingen in Drive

Toegankelijkheid

Alleen reageren

Bezig met laden...

|  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Publicly Shared |  | flutter.dev/go/deprecations-removed-after-1-22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | Deprecations removed from Flutter after 1.22 Release |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Deprecation Policy: | https://github.com/flutter/flutter/wiki/Tree-hygiene#deprecation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | More Info: | https://flutter.dev/go/deprecation-lifetime |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 |  | https://medium.com/flutter/deprecation-lifetime-in-flutter-e4d76ee738ad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Evaluation PR: | https://github.com/flutter/flutter/pull/67789 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Library/Package | Deprecated | API |  | Fix | PR | Notes | dart fix support |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Cupertino | v0.2.3 | CupertinoDialog |  | Use CupertinoAlertDialog or CupertinoPopupSurface | https://github.com/flutter/flutter/pull/73604 | Landed, dart fix testing not supported | Y - only in IDE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 |  | v1.1.2 | CupertinoNavigationBar.actionsForegroundColor |  | Use CupertinoTheme.primaryColor | https://github.com/flutter/flutter/pull/73745 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 |  | v1.1.2 | CupertinoSliverNavigationBar.actionsForegroundColor |  | Use CupertinoTheme.primaryColor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  | v1.10.14 | CupertinoTextThemeData.brightness |  | Does nothing, no replacement. | https://github.com/flutter/flutter/pull/72017 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 | Gestures | v1.4.3 | PointerEnterEvent.fromHoverEvent |  | Use PointerEnterEvent.fromMouseEvent | https://github.com/flutter/flutter/pull/72395 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | v1.4.3 | PointerExitEvent.fromHoverEvent |  | Use PointerExitEvent.fromMouseEvent |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 | Material | v0.2.3 | showDialog(child) |  | Instead of 'child', use 'builder' | https://github.com/flutter/flutter/pull/72532/ | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  | v1.1.9 | Scaffold.resizeToAvoidBottomPadding |  | Use Scaffold.resizeToAvoidBottomInset | https://github.com/flutter/flutter/pull/72890 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  | v1.9.1 | ButtonTheme.bar |  | Use ButtonBarTheme | https://github.com/flutter/flutter/pull/73746 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | Painting | v1.7.3 | InlineSpan.text |  | Use TextSpan.text | https://github.com/flutter/flutter/pull/73747 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  | v1.7.3 | InlineSpan.children |  | UseTextSpan.children |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 |  | v1.7.3 | InlineSpan.visitTextSpan |  | Use InlineSpan.visitChildren |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 |  | v1.7.3 | InlineSpan.recognizer |  | Use TextSpan.recognizer |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 |  | v1.7.3 | InlineSpan.describeSemantics |  | Use InlineSpan.computeSemanticsInformation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 |  | v1.7.3 | PlaceholderSpan.visitTextSpan |  | Use PlaceHolderSpan.visitChildren |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 |  | v1.7.3 | TextSpan.visitTextSpan |  | Use TextSpan.visitChildren |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | Rendering | v1.10.0 | RenderView.scheduleInitialFrame |  | Call RenderView.prepareInitialFrame() followed by RenderView.owner!.requestVisualUpdate() | https://github.com/flutter/flutter/pull/73748 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 |  | v1.10.14 | Layer.findAll |  | Use Layer.findAllAnnotations(...).annotations | https://github.com/flutter/flutter/pull/73749 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | Services | v1.6.5 | BinaryMessenger get defaultBinaryMessenger |  | Use ServicesBinding.instance.defaultBinaryMessenger | https://github.com/flutter/flutter/pull/73750 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 |  | v1.6.5 | BinaryMessages |  | Use BinaryMessenger & defaultBinaryMessenger |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 |  | v1.6.5 | static BinaryMessages.handlePlatformMessage |  | Use defaultBinaryMessenger.handlePlatformMessage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 |  | v1.6.5 | static BinaryMessages.send |  | Use defaultBinaryMessenger.send |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 |  | v1.6.5 | static BinaryMessages.setMessageHandler |  | Use defaultBinaryMessenger.setMessageHandler |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  | v1.6.5 | static BinaryMessages.setMockMessageHandler |  | Use defaultBinaryMessenger.setMockMessageHandler |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | Widgets | v1.12.1 | TypeMatcher |  | Not in use, no replacement. | https://github.com/flutter/flutter/pull/73751 | In progress, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 |  | v1.12.1 | BuildContext.inheritFromElement |  | Use dependOnInheritedElement | https://github.com/flutter/flutter/pull/69620 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 |  | v1.12.1 | BuildContext.inheritFromWidgetOfExactType |  | Use dependonInheritedWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 |  | v1.12.1 | BuildContext.ancestorInheritedElementForWidgetOfExactType |  | Use getElementForInheritedWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 |  | v1.12.1 | BuildContext.ancestorWidgetOfExactType |  | Use findAncestorWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 |  | v1.12.1 | BuildContext.ancestorStateOfType |  | Use findAncestorStateOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 |  | v1.12.1 | BuildContext.rootAncestorStateOfType |  | Use findRootAncestorStateOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 |  | v1.12.1 | BuildContext.ancestorRenderObjectOfType |  | Use findAncestorRenderObjectOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 |  | v1.12.1 | Element.inheritFromElement |  | Use dependOnInheritedElement | https://github.com/flutter/flutter/pull/72903 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 |  | v1.12.1 | Element.inheritFromWidgetOfExactType |  | Use dependOnInheritedWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 45 |  | v1.12.1 | Element.ancestorInheritedElementForWidgetOfExactType |  | Use getElementForInheritedWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 46 |  | v1.12.1 | Element.ancestorWidgetOfExactType |  | Use findAncestorWidgetOfExactType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 |  | v1.12.1 | Element.ancestorStateOfType |  | Use findAncestorStateOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 |  | v1.12.1 | Element.rootAncestorStateOfType |  | Use findRootAncestorStateOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 49 |  | v1.12.1 | Element.ancestorRenderObjectOfType |  | Use findAncestorRenderObjectOfType |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 |  | v1.12.1 | StatefulElement.inheritFromElement |  | Use dependOnInheritedElement | https://github.com/flutter/flutter/pull/72901 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 51 |  | v1.12.4 | WidgetsBinding.deferFirstFrameReport |  | Use deferFirstFrame | https://github.com/flutter/flutter/pull/72893 | Landed | Y |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 52 |  | v1.12.4 | WidgetsBinding.allowFirstFrameReport |  | Use allowFirstFrame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 | flutter\_driver | v1.9.3 | WaitUntilNoTransientCallbacks |  | Use WaitForCondition command with NoTransientCallbacks | https://github.com/flutter/flutter/pull/73754 | Landed, dart fix not supported | N |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 54 |  | v1.9.3 | WaitUntilNoPendingFrame |  | Use WaitForCondition command with NoPendingFrame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 |  | v1.9.3 | WaitUntilFirstFrameRasterized |  | Use WaitForCondition command with FirstFrameRasterized |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 56 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 57 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 58 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 61 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 62 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 63 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 65 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 66 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 67 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 68 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 69 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 70 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 71 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 72 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 73 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 74 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 76 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| De koersen zijn niet voor alle markten beschikbaar en kunnen met 20 minuten vertraging worden weergegeven. De informatie wordt in de huidige staat aangeboden en is alleen bedoeld ter informatie, niet voor handelsdoeleinden of advies. [Disclaimer](http://www.google.com/googlefinance/disclaimer/) | | | | |
|  |  | Sheet1 |  |  |

Er is een browserfout opgetreden.  
 Houd de Shift-toets ingedrukt en druk op de knop 'Vernieuwen' om het nogmaals te proberen.