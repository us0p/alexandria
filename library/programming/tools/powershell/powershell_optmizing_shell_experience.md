# Tab-Completion
PowerShell automatically expands the name to the first match that it finds.

Pressing `Tab` again cycles through all the available choices with each key press.

`PSReadLine` also provides a `MenuComplete` function that's bound to `Ctrl` + `Space`. The `MenuComplete` function displays a list of matching completions below the command line.
## Predictors in `PSReadLine`
When enabled, the `Predictive IntelliSense` provides suggestions for full commands based on items from your `PSReadLine` history.

There are two modes of `Predictive IntelliSense`:
- `InlineView`: It's the default and displays information in the same line as the cursor.
- `ListView`: Display information as a list of suggestions under the cursor.

You can switch between the two modes by pressing `F2`.

You can change the prediction source using the `Set-PSReadLineOption` with the `PredictionSource` parameter.
### Changing Key bindings
`PSReadLine` contains functions to navigate and accept predictions. For example:
- `AcceptSuggestion`: Accept the current inline suggestion
- `AcceptNextSuggestionWord`: Accept the next word of the inline suggestion
- `AcceptSuggestion`: is built within `ForwardChar`, which is bound to `RightArrow` by default
- `AcceptNextSuggestionWord`: is built within the function `ForwardWord`, which can be bound to `Ctrl+F`
You can use the `Set-PSReadLineKeyHandler` cmdlet to change key bindings.

```PowerShell
Set-PSReadLineKeyHandler -Chord "Ctrl+f" -Function ForwardWord
```

With this binding, pressing `Ctrl+F` accepts the next word of an inline suggestion when the cursor is at the end of current editing line.

The names of the keys in the chord are defined by the `[System.ConsoleKey]` enumeration.
## Commonly used key handlers
- `MenyComplete`: `Ctrl+Spacebar`
- `ClearScreen`: `Ctrl+l`
- `SelectCommandArgument`: `Alt+a`
- `GotoBrace`: `Ctrl+]`
- `DigitArgument`: `Alt+[0-9]`
## Dynamic Help
Provides a view of full cmdlet help shown in an alternative screen buffer. `PSReadLine` maps the function `ShowCommandHelp` to the `F1` key.
- When the cursor is at the end of a fully expanded cmdlet name, pressing `F1` displays the help for that cmdlet.
- When the cursor is at the end of a fully expanded parameter name, pressing `F1` displays the help for the cmdlet beginning at the parameter.
## Selecting arguments on the command line
You can use `alt + a` to hop into the argument (it only work for argument values, it doesn't hop into command names or options) in your command line without having to move the cursor manually.
## Managing Command Aliases
The commands in PowerShell that are used to manage aliases are:
- `Export-Alias`
- `Get-Alias`
- `Import-Alias`
- `New-Alias`
- `Remove-Alias`
- `Set-Alias`

PowerShell also provides ways to create shorthand names for parameters. Parameter aliases are defined using the `Alias` attribute when you declare the parameter.

PowerShell lets you specify the parameter name using the fewest characters needed to uniquely identify the parameter. For example, the `Get-ChildItem` has the `Recurse` and `ReadOnly` parameters. To uniquely identify the `Recurse` parameter you only need to provide `-Rec`.
## Customizing your shell environment
The `$PROFILE` automatic variable stores the paths to the PowerShell profiles that are available in the current session.

There are four possible profiles available to support different user scopes and different PowerShell hosts. The fully qualified paths for each profile script are stored in the following member properties of `$PROFILE`.

- `AllUsersAllHosts`
- `AllUsersCurrentHost`
- `CurrentUserAllHosts`
- `CurrentUserCurrentHost`

You can create profile scripts that run for all users or just one user, the `CurrentUser`. `CurrentUser` profiles are stored under the user's home directory path. The location varies depending on the operating system and the version of PowerShell you use.

By default, referencing the `$PROFILE` variable returns the path to the `Current User, Current Host` profile. The other profiles path can be accessed through the properties of the `$PROFILE` variable.

There are also profiles that run for all PowerShell hosts or specific hosts. The profile script for each PowerShell host has a name unique for that host. For example, the filename for the standard Console Host on Windows or the default terminal application on other platforms is `Microsoft.PowerShell_profile.ps1`. For Visual Studio Code (VS Code), the filename is `Microsoft.VSCode_profile.ps1`.