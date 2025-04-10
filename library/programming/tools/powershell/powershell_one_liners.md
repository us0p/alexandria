An one-lines is one continuous pipeline. A command might extend over many physical lines, and still be an one-linter, it must form one continuous pipeline.

```powershell
Get-Service |
Where-Object CanPauseAndContinue -EQ $true |
Selct-Object -Property *

# Not an one-liner as there's two commands
$Service = 'w32time'; Get-Service -Name $Service
```

Natural line breaks can occur at commonly used characters, including:
- Pipe Symbol
- Comma
- Opening Brackets, Braces and Parenthesis
- Semicolon
- Equal sign
- Opening Single and Double Quotes
## Pipeline
When handling pipeline input, a parameter that accepts pipeline input both by property name and by type prioritizes by type binding first.

For instance, if you pipe the output of a command that generates a `ServiceController` object to `Stop-Service`, this output is bound to the `InputObject` parameter. If the piped command produces a String object, it associates the output with the Name parameter. If you pipe output from a command that doesn't produce a `ServiceController` or String object, but does include a property named Name, `Stop-Service` binds the value of the Name property to its Name parameter.
## Parentheses
You can use parentheses to pass the output of one command as input for a parameter to another command.

```powershell
Stop-Service -DisplayyName (Get-Content -Path $env:TEMP\services.txt)
```

Just as mathematical operations within parentheses are computed first.