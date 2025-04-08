# Help System
## Discoverability
Compiled commands in PowerShell are known as **cmdlets**, pronounced as **command-let**. The naming convention for **cmdlets** follows a singular **Verb-Noun** format to make them easily discoverable.

For instance:
- `Get-Process`: List of processes that are running.
- `Get-Service`: List of services.

Functions, also known as **script cmdlet**, and aliases are other types of PowerShell commands.

**PowerShell command** describes any command in PowerShell, regardless of whether it's a cmdlet, function, or alias.

You can also run operating system native commands from PowerShell, such as traditional command-line programs like `ping.exe` and `ipconfig.exe`.
## Get-Help
Multipurpose command that helps you learn how to use commands once you find them.
## Parameter sets
The **SYNTAX** section for `Get-Help` might appear repeated some times. Each block of syntax is an individual parameter set and each parameter set contains at least one unique parameter, making it different from the others.

Parameter sets are mutually exclusive. Once you specify a unique parameter that only exists in one parameter set, PowerShell limits you to using the parameters contained within that parameter set.
## Syntax
### Positional Parameters
Allow you to provide a value without specifying the name of the parameter. You must specify its value in the correct position on the command line. When you explicitly specify parameter names, you can use the parameter in any order.
```plaintext
CommandName [-PositionalParameter] <System.String>
CommandName [[-OptionalPositionalParameter] <System.String>]
```
### Possible values
Some parameters expect a set of defined values, they're defined between curly brackets.
```plaintext
CommanName [-PositionalParameter {Value1 | Value2 | ... | ValueX}]
```
### Switch Parameters
A parameter that doesn't require a value. Can be easily identified because there's no datatype following the parameter name. When you specify a switch parameter, its value is `true`, else `false`.
```plaintext
CommandName [-SwitchParameter]
```
# Get-Command
Multipurpose command that helps you find commands.

For more information, see:
- `Get-Help`
- `Get-Command`