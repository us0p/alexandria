# Looping
### `ForEach-Object`
Is a cmdlet for iterating through items in a pipeline, such as with PowerShell one-liners.
```powershell
# The Module parameter of Get-Command accepts multiple string values.
# But it only accepts them via pipeline input by property name.
# To pipe two string values we use the ForEach-Object.
'ActiveDirectory', 'SQLServer' |
ForEach-Object {Get-Command -Module $_} |
Group-Object -Property ModuleName -NoElement |
Sort-Object -Property Count -Descending

# Count Name
# ----- ----
#   147 ActiveDirectory
#    82 SqlServer
```

In the example, `$_` is the current object.
### foreach
When using `foreach` keyword, you must store the items in memory before iterating through them.
```powershell
$ComputerName = 'DC01', 'WEB01'
foreach ($Computer in $ComputerName) {
	Get-ADComputer -Identity $Computer
}

```
Sometimes, you can get the same results while eliminating the loop. Consult the cmdlet help to understand your options.
```powershell
# It raises an error
Get-ADComputer -Identity 'DC01', 'WEB01'

# Work the same as expected
'DC01', 'WEB01' | Get-ADComputer
```
### for
Iterates while a specified condition is true.
```powershell
for ($i = 1; $i -lt 5; $i++) {
	Write-Output "Sleeping for $i seconds"
	Start-Sleep -Seconds $i
}
```
### do
`do` loops always run at least once because the condition is evaluated at the end of the loop.
- `do until`: Runs until the specified condition is `false`.
- `do while`: Runs until the specified condition is `true`.
```powershell
# do until
$number = Get-Random -Minimum 1 -Maximum 10
do {
	$guess = Read-Host -Prompt "What's your guess?"
	if ($guess -lt $number) {
		Write-Output 'Too low!'
	} elseif ($guess -gt $number) {
		Write-Output 'Too high!'
	}
}
until ($guess -eq $number)

# do while
$number = Get-Random -Minimum 1 -Maximum 10
do {
	$guess = Read-Host -Prompt "What's your guess?"
	if ($guess -lt $number) {
		Write-Output 'Too low!'
	} elseif ($guess -gt $number) {
		Write-Output 'Too high!'
	}
}
while ($guess -ne $number)
```
### while
Runs as long as the specified condition is `true`. It evaluates the condition at the top of the loop before any code is run.
```powershell
$date = Get-Date -Date 'November 22'
while ($date.DayOfWeek -ne 'Thursday') {
	$date = $date.AddDays(1)
}
Write-Output $date
```
### break
Is designed to exit a loop and is often used with the `switch` statement.
```powershell
for ($i = 1; $i -lt 5; $i++) {
	Write-Output "Sleeping for $i seconds"
	Start-Sleep -Seconds $i
	break
}
```
### continue
Is designed to skip the next iteration of a loop.
```powershell
while ($i -lt 5) {
	$i += 1
	if ($i -eq 3) {
		continue
	}
	Write-Output $i
}
```
### return
Is designed to exit out of the existing scope.
```powershell
$number = 1..10
foreach ($n in $number) {
	if ($n -ge 4) {
		return $n
	}
}
```
## Errors
**Terminating Errors** are severe errors that stop the script from continuing. When a terminating error occurs, the script execution halts unless handled by a `try-catch` block.

**Non-terminating Errors** allow the script to continue running. These errors are often related to issues like missing files or operations that return errors but do not stop the script. These errors get logged into the `$Error` variable, which keeps a collection of error records for review.

When an error occurs, an `ErrorRecord` object is created. It contains information including the **Exception** message and the **Category** of the error.

In PowerShell, the throw keyword is used to create a terminating error.

```PowerShell
function Fail {
	throw "I'm a failure"
}

# You can also throw specific exceptions:
function SpecificFailure {
	throw [System.Exception]::new("I'm a failure")
}
```
## Try, Catch and Finally blocks
```PowerShell
try {
	# Code that may throw an exception
}
catch [System.FormatException] {
	# Code to handle ONLY FormatExceptions
}
catch {
	# Code to handle any other exceptions
}
finally {
	# Code that runs regardless of an error ocurring or not
}
```
## Ternary Operator
```PowerShell
$isSunday = $false
if ($isSunday) {Write-Output "It's Sunday"} else {Write-Output "It's not Sunday"}
```
## CLI Arguments
```PowerShell
$Name = $args[0]
$Age = $args[1]

Write-Output "I'm $Name and i'm $Age years old."
```
## Type accelerator
Are shortcuts or aliases for full `.NET` type names. It lets you reference complex `.NET` classes more easily and cleanly in your PowerShell code.

```PowerShell
[System.Collections.Generic.List[string]]
[List[string]] # [List] is a shortcut to the full System.Collections.Generic.List
```

## Common Type Accelerators

| Type Accelerator | `.NET` Type                             |
| ---------------- | --------------------------------------- |
| `[int]`          | `System.Int32`                          |
| `[string]`       | `System.String`                         |
| `[bool]`         | `System.Boolean`                        |
| `[datetime]`     | `System.DateTime`                       |
| `[regex]`        | `System.Text.RegularExpressions.Regex`  |
| `[byte[]]`       | `System.Byte[]`                         |
| `[hashtable]`    | `System.Collections.Hashtable`          |
| `[psobject]`     | `System.Management.Automation.PSObject` |
## `.NET` classes

| Class                    | Description                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `[System.Text.Encoding]` | Convert strings to byte arrays and back, supports different character encodings (UTF8, ASCII, Unicode, etc)                                 |
| `[System.Convert]`       | Provides methods to convert almost any type to another, strings to numbers, booleans to integers, byte arrays to base64 strings, and so on. |
## Special built-in values
Predefined variables that represent fundamental concepts or states in the language. You don't create them.

They're constants that help scripts handle logic, state, or represent system-wide values.
## Common Special Built-In Values
- `$null`
- `$true`
- `$false`
- `$?`: Check if the last command was successful
- `$_`: The current object in the pipeline (like a loop variable).
- `$HOME`
- `$Error`: An array of error objects from the session.