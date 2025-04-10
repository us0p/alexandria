# PowerShell - Discovering Objects, Properties, and Methods.
PowerShell is an object-oriented scription language. It represents data and system states using structured objects derived from .NET classes in the .NET framework. PowerShell also has access to the .NET framework class library, which contains a vast collection of classes.

In PowerShell, each item or state is an instance of an object that can be explored and manipulated. 
## Get-Member
Provides insight into the object, properties, and methods associated with PowerShell commands. You can pipe any PowerShell command that produces object-based output to `Get-Member` to reveal the structure of the object returned by the command, detailing its properties and methods.

```powershell
Get-Service -Name W32Time | Get-Member
```

Sometimes, you find `Get-*` commands without a corresponding `Set-*` command. Often, you can find a method to perform a `Set-*` action with `Get-Member -MemberType Method`.

You can't pipe a command to `Get-Member` that doesn't generate object-based output.
## String
In PowerShell, it's a best practice to use single quotes for static strings, reserving double quotes for situations where the string contains variables that require expansion.

Single quotes tell PowerShell to treat the content literally without parsing for variables.

This approach enhances performance, as PowerShell expends less processing effort on string within single quotes.
```powershell
'w32time' # Static String
$str = "w32time" | "$str" # Variable expansion
```
## Variables
Variables are prefixed with a $ sign in PowerShell
```
$myString = 'Hello, World!'
```
## `PowerShellGet`
It's a module included with PowerShell 5.0 or higher. It provides commands to discover, install, update, and publish PowerShell modules and other items in a NuGet repository.

The [PowerShell Gallery](https://www.powershellgallery.com/) It's an online repository hosted by Microsoft, designed as a central hub for sharing PowerShell modules, scripts, and other resources. Modules and scripts are mostly contributions of the community.
## See Also
- `Get-Service`
- `Get-Member`
- `Select-Object`
- `Find-Module`