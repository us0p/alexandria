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