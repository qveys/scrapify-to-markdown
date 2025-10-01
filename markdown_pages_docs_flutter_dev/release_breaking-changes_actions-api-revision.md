Actions API revision
====================

1. [Stay up to date](/release) chevron\_right- [Breaking changes](/release/breaking-changes) chevron\_right- [Actions API revision](/release/breaking-changes/actions-api-revision)

Summary
-------

[#](#summary)

In Flutter an [`Intent`](https://api.flutter.dev/flutter/widgets/Intent-class.html) is an object that's typically bound to a keyboard key combination using the [`Shortcuts`](https://api.flutter.dev/flutter/widgets/Shortcuts-class.html) widget. An `Intent` can be bound to an [`Action`](https://api.flutter.dev/flutter/widgets/Action-class.html), which can update the application's state or perform other operations. In the course of using this API, we identified several drawbacks in the design, so we have updated the Actions API to make it easier to use and understand.

In the previous Actions API design, actions were mapped from a [`LocalKey`](https://api.flutter.dev/flutter/foundation/LocalKey-class.html) to an `ActionFactory` that created a new `Action` each time the `invoke` method was called. In the current API, actions are mapped from the type of the `Intent` to an `Action` instance (with a `Map<Type, Action>`), and they are not created anew for each invocation.

Context
-------

[#](#context)

The original Actions API design was oriented towards invoking actions from widgets, and having those actions act in the context of the widget. Teams have been using actions, and found several limitations in that design that needed to be addressed:

1. Actions couldn't be invoked from outside of the widget hierarchy. Examples of this include processing a script of commands, some undo architectures, and some controller architectures.- The mapping from shortcut key to `Intent` and then to `Action` wasn't always clear, since the data structures mapped LogicalKeySet =>Intent and then `LocalKey` => `ActionFactory`. The new mapping is still `LogicalKeySet` to `Intent` but then it maps `Type` (`Intent` type) to `Action`, which is more direct and readable, since the type of the intent is written in the mapping.- If the key binding for an action was in another part of the widget hierarchy, it was not always possible for the `Intent` to have access to the state necessary to decide if the intent/action should be enabled or not.

To address these issues, we made some significant changes to the API. The mapping of actions was made more intuitive, and the enabled interface was moved to the `Action` class. Some unnecessary arguments were removed from the `Action`'s `invoke` method and its constructor, and actions were allowed to return results from their invoke method. Actions were made into generics, accepting the type of `Intent` they handle, and `LocalKeys` were no longer used for identifying which action to run, and the type of the `Intent` is used instead.

The majority of these changes were made in the PRs for [Revise Action API](https://github.com/flutter/flutter/pull/42940) and [Make Action.enabled be isEnabled(Intent intent) instead](https://github.com/flutter/flutter/pull/55230), and are described in detail in [the design doc](/go/actions-and-shortcuts-design-revision).

Description of change
---------------------

[#](#description-of-change)

Here are the changes made to address the above problems:

1. The `Map<LocalKey, ActionFactory>` that was given to the [`Actions`](https://api.flutter.dev/flutter/widgets/Actions-class.html) widget is now a `Map<Type, Action<Intent>>` (the type is the type of the Intent to be passed to the Action).- The `isEnabled` method was moved from the `Intent` class to the `Action` class.- The `FocusNode` argument to `Action.invoke` and `Actions.invoke` methods was removed.- Invoking an action no longer creates a new instance of the `Action`.- The `LocalKey` argument to the `Intent` constructor was removed.- The `LocalKey` argument to `CallbackAction` was removed.- The `Action` class is now a generic (`Action<T extends Intent>`) for better type safety.- The `OnInvokeCallback` used by `CallbackAction` no longer takes a `FocusNode` argument.- The `ActionDispatcher.invokeAction` signature has changed to not accept an optional `FocusNode`, but instead take an optional `BuildContext`.- The `LocalKey` static constants (named key by convention) in `Action` subclasses have been removed.- The `Action.invoke` and `ActionDispatcher.invokeAction` methods now return the result of invoking the action as an `Object`.- The `Action` class may now be listened to for state changes.- The `ActionFactory` typedef has been removed, as it is no longer used.

Example analyzer failures
-------------------------

[#](#example-analyzer-failures)

Here are some example analyzer failures that might be encountered where an outdated use of the Actions API might be the cause of the problem. The specifics of the error might differ, and there may be other failures caused by these changes.

```
error: MyActionDispatcher.invokeAction' ('bool Function(Action<Intent>, Intent, {FocusNode focusNode})') isn't a valid override of 'ActionDispatcher.invokeAction' ('Object Function(Action<Intent>, Intent, [BuildContext])'). (invalid_override at [main] lib/main.dart:74)

error: MyAction.invoke' ('void Function(FocusNode, Intent)') isn't a valid override of 'Action.invoke' ('Object Function(Intent)'). (invalid_override at [main] lib/main.dart:231)

error: The method 'isEnabled' isn't defined for the type 'Intent'. (undefined_method at [main] lib/main.dart:97)

error: The argument type 'Null Function(FocusNode, Intent)' can't be assigned to the parameter type 'Object Function(Intent)'. (argument_type_not_assignable at [main] lib/main.dart:176)

error: The getter 'key' isn't defined for the type 'NextFocusAction'. (undefined_getter at [main] lib/main.dart:294)

error: The argument type 'Map<LocalKey, dynamic>' can't be assigned to the parameter type 'Map<Type, Action<Intent>>'. (argument_type_not_assignable at [main] lib/main.dart:418)
```

Migration guide
---------------

[#](#migration-guide)

Significant changes area required to update existing code to the new API.

### Actions mapping for pre-defined actions

[#](#actions-mapping-for-pre-defined-actions)

To update the action maps in the `Actions` widget for predefined actions in Flutter, like `ActivateAction` and `SelectAction`, do the following:

* Update the argument type of the `actions` argument* Use an instance of a specific `Intent` class in the `Shortcuts` mapping, rather than an `Intent(TheAction.key)` instance.

Code before migration:

dart

```
class MyWidget extends StatelessWidget {
  // ...
  @override
  Widget build(BuildContext context) {
    return Shortcuts(
      shortcuts: <LogicalKeySet, Intent> {
        LogicalKeySet(LogicalKeyboardKey.enter): Intent(ActivateAction.key),
      },
      child: Actions(
        actions: <LocalKey, ActionFactory>{
          Activate.key: () => ActivateAction(),
        },
        child: Container(),
      )
    );
  }
}
```

Code after migration:

dart

```
class MyWidget extends StatelessWidget {
  // ...
  @override
  Widget build(BuildContext context) {
    return Shortcuts(
      shortcuts: <LogicalKeySet, Intent> {
        LogicalKeySet(LogicalKeyboardKey.enter): ActivateIntent,
      },
      child: Actions(
        actions: <Type, Action<Intent>>{
          ActivateIntent: ActivateAction(),
        },
        child: Container(),
      )
    );
  }
}
```

### Custom actions

[#](#custom-actions)

To migrate your custom actions, eliminate the `LocalKeys` you've defined, and replace them with `Intent` subclasses, as well as changing the type of the argument to the `actions` argument of the `Actions` widget.

Code before migration:

dart

```
class MyAction extends Action {
  MyAction() : super(key);

  /// The [LocalKey] that uniquely identifies this action to an [Intent].
  static const LocalKey key = ValueKey<Type>(RequestFocusAction);

  @override
  void invoke(FocusNode node, MyIntent intent) {
    // ...
  }
}

class MyWidget extends StatelessWidget {
  // ...
  @override
  Widget build(BuildContext context) {
    return Shortcuts(
      shortcuts: <LogicalKeySet, Intent> {
        LogicalKeySet(LogicalKeyboardKey.enter): Intent(MyAction.key),
      },
      child: Actions(
        actions: <LocalKey, ActionFactory>{
          MyAction.key: () => MyAction(),
        },
        child: Container(),
      )
    );
  }
}
```

Code after migration:

dart

```
// You may need to create new Intent subclasses if you used
// a bare LocalKey before.
class MyIntent extends Intent {
  const MyIntent();
}

class MyAction extends Action<MyIntent> {
  @override
  Object invoke(MyIntent intent) {
    // ...
  }
}

class MyWidget extends StatelessWidget {
  // ...
  @override
  Widget build(BuildContext context) {
    return Shortcuts(
      shortcuts: <LogicalKeySet, Intent> {
        LogicalKeySet(LogicalKeyboardKey.enter): MyIntent,
      },
      child: Actions(
        actions: <Type, Action<Intent>>{
          MyIntent: MyAction(),
        },
        child: Container(),
      )
    );
  }
}
```

### Custom `Actions` and `Intents` with arguments

[#](#custom-actions-and-intents-with-arguments)

To update actions that use intent arguments or hold state, you need to modify the arguments to the `invoke` method. In the example below, the code keeps the value of the argument in the intent as part of the action instance. This is because in the old design there is a new instance of the action created each time it's executed, and the resulting action could be kept by the [`ActionDispatcher`](https://api.flutter.dev/flutter/widgets/ActionDispatcher-class.html) to record the state.

In the example of post migration code below, the new `MyAction` returns the state as the result of calling `invoke`, since a new instance isn't created for each invocation. This state is returned to the caller of `Actions.invoke`, or `ActionDispatcher.invokeAction`, depending on how the action is invoked.

Code before migration:

dart

```
class MyIntent extends Intent {
  const MyIntent({this.argument});

  final int argument;
}

class MyAction extends Action {
  MyAction() : super(key);

  /// The [LocalKey] that uniquely identifies this action to an [Intent].
  static const LocalKey key = ValueKey<Type>(RequestFocusAction);

  int state;

  @override
  void invoke(FocusNode node, MyIntent intent) {
    // ...
    state = intent.argument;
  }
}
```

Code after migration:

dart

```
class MyIntent extends Intent {
  const MyIntent({this.argument});

  final int argument;
}

class MyAction extends Action<MyIntent> {
  @override
  int invoke(Intent intent) {
    // ...
    return intent.argument;
  }
}
```

Timeline
--------

[#](#timeline)

Landed in version: 1.18  
 In stable release: 1.20

References
----------

[#](#references)

API documentation:

* [`Action`](https://api.flutter.dev/flutter/widgets/Action-class.html)* [`ActionDispatcher`](https://api.flutter.dev/flutter/widgets/ActionDispatcher-class.html)* [`Actions`](https://api.flutter.dev/flutter/widgets/Actions-class.html)* [`Intent`](https://api.flutter.dev/flutter/widgets/Intent-class.html)* [`Shortcuts`](https://api.flutter.dev/flutter/widgets/Shortcuts-class.html)

Relevant issue:

* [Issue 53276](https://github.com/flutter/flutter/issues/53276)

Relevant PRs:

* [Revise Action API](https://github.com/flutter/flutter/pull/42940)* [Make Action.enabled be isEnabled(Intent intent) instead](https://github.com/flutter/flutter/pull/55230)

Was this page's content helpful?

thumb\_up thumb\_down

Thank you for your feedback!

 [feedback Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/actions-api-revision/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/actions-api-revision.md)

Thank you for your feedback! Please let us know what we can do to improve.

 [bug\_report Provide details](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/actions-api-revision/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/actions-api-revision.md)

Unless stated otherwise, the documentation on this site reflects the latest stable version of Flutter. Page last updated on 2024-04-04. [View source](https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/actions-api-revision.md) or [report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&&page-url=https://docs.flutter.dev/release/breaking-changes/actions-api-revision/&page-source=https://github.com/flutter/website/tree/main/src/content/release/breaking-changes/actions-api-revision.md "Report an issue with this page").

[![Flutter logo](/assets/images/branding/flutter/logo+text/horizontal/white.svg)](https://flutter.dev)

Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).

* [Terms](/tos "Terms of use")* [Brand](/brand "Brand usage guidelines")* [Privacy](https://policies.google.com/privacy "Privacy policy")* [Security](/security "Security philosophy and practices")

   