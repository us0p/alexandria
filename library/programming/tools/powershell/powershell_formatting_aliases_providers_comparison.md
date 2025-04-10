## Format Right
Filter should be to the left as possible. Formatting should be as far to the right as possible.

Most common format commands are:
- `Format-Table`
- `Format-List`

A command that returns mor than four properties defaults to a list unless custom formatting is used.
```powershell
# Display information as a list
Get-Service w32time |
Select-Object -Property Status, DisplayName, Can*

# Display information as a table
Get-Service w32time |
Select-Object -Property Status, DisplayName, Can* |
Format-Table
```
The number one thing to be aware of with the format cmdlets is they produce format objects that are different than normal objects in PowerShell.
```powershell
# Pay attention to the types of the following command
Get-Service -Name w32time |
Format-List |
Get-Member
```

What this means is format commands can't be piped to most other commands. They can be piped to some of the `Out-*` commands, but that's about it. This is why you want to perform any formatting at the very end of the line (format right).
## Aliases
An alias in PowerShell is a shorter name for a command.

To get more information about an alias, see `Get-Alias`.

Aliases shouldn't be used in scripts or any code that you're saving or sharing with others.
## Providers
A provider is an interface that allows file system-like access to a data store.

To get a list of available providers, see `Get-PSProvider`.

The actual drives that these providers use to expose their data store can be determined with the `Get-PSDrive` cmdlet. It not only display drives exposed by providers but also displays Windows logical drives, including drives mapped to network shares.

`PSDrives` can be accessed just like a traditional file system.
## Comparison Operators
All the operators listed in the table are case-insensitive. To make them case-sensitive, place a `c` in front of the operator. For example, `-ceq` is the case sensitive version of the `-eq` operator.

Comparison operators are often used with the `Where-Object` cmdlet.

| Operator       | Definition                                                  |
| -------------- | ----------------------------------------------------------- |
| `-eq`          | Equal to                                                    |
| `-ne`          | Not equal to                                                |
| `-gt`          | Greater than                                                |
| `-ge`          | Greater than or equal to                                    |
| `-lt`          | Less than                                                   |
| `-le`          | Less than or equal to                                       |
| `-like`        | Match using the `*` wildcard character                      |
| `-notlike`     | Doesn't match using the `*` wildcard character              |
| `-match`       | Matches the specified regular expression                    |
| `-notmatch`    | Doesn't match the specified regular expression              |
| `-contains`    | Determines if a collection contains a specified value       |
| `-notcontains` | Determines if a collection doesn't contain a specific value |
| `-in`          | Determines if a specified value is in a collection          |
| `-notin`       | Determines if a specified value isn't in a collection       |
| `-replace`     | Replaces the specified value                                |
Notes:
- `gt, ge, lt, le`: Work with string or numeric values.
- Use the range operator to store the number 1 through 10 in a variable `$Numbers = 1..10`.
- Specifying one value with `-replace` replaces that value with nothing.
- `Hello, World` -replace `world`, `You`: Replaces "World" with "You".