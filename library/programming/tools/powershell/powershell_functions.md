## Naming
Use a Pascal case name with an approved verb and a singular noun.
Modules that contain functions with unapproved verbs generate a warning message when they're imported.

For a list of approved verbs, run `Get-Verb`.

```powershell
function Get-Version {
	$PSVersionTable.PSVersion
}
```

When you use a generic name for your functions, such as the example above, it could cause naming conflicts. Prefix the noun portion of your function names to help prevent naming conflicts. `<ApprovedVerb>-<Prefix><SingularNoun>`

```powershell
# This function produces the same output as the previous example
function Get-PSVersion {
	$PSVersionTable.PSVersion
}
```
## Parameters
When naming your parameters, use the same name and case as the default cmdlets for your parameter names whenever possible.

```powershell
function Test-PSParameter {
	param (
		$ComputerName
	)
	Write-Output $ComputerName
}

# Queries all commands on your system and returns the number with specific parameter names.
function Get-PSParameterCount {
	param (
		[string[]]$ParameterName
	)

	foreach ($Parameter in $ParameterName) {
		$Results = Get-Command -ParameterName $Parameter -ErrorAction SilentlyContinue

		[pscustomobject]@{
			ParameterName   = $Parameter
			NumberOfCmdlets = $Results.Count
		}
	}
}
```
# Advanced Functions
One of the differences between function and advanced function is that advanced functions have common parameters that are automatically added. Common parameters include parameters such as **Verbose** and **Debug**

```powershell
function Test-PSParameter {
	[CmdletBinding()] # Turns a regular function indo an advanced function.
	param (
		$ComputerName
	)

	Write-Output $ComputerName
}
```

When you specify `CmdletBinding`, the common parameters are added automatically. `CmdletBinding` requires a `param` block, but the `param` block can be empty.
## `SupportsShouldProcess`
This attribute adds the `Whatif` and `Confirm` risk mitigation parameters. Only needed for commands that make changes.
```powershell
function Test-PSSuuportShouldProcess {
	[CmdletBinding(SupportShouldProcess)]
	param (
		$ComputerName
	)

	Write-Output $ComputerName
}
```
## Parameter Validation
Always specify a datatype for the variable used for parameters.
```powershell
function Test-PSPersonInfo {
	[CmdletBinding()]
	param (
		# Optional parameter
		[number]$PersonAge

		# Required parameter
		# [Parameter(Mandatory=$true)] Compatibility >= 2.0
		[Parameter(Mandatory)] # Compatibility >= 3.0
		[string]$PersonName # Now it's required

		# Default value
		# Default values can't be use with "Mandatory"
		[ValidateNotNullOrEmpty()]
		[string]$PersonCountry = 'Brazil'
	)

	Write-Output $ComputerName
}

function Test-PSRequiredParameter {
	[CmdletBinding()]
	param (
	)

	Write-Output $ComputerName
}
```
## Pipeline input
Extra code is necessary when you want your function to accept pipeline input. Commands can accept pipeline input **by value** (by type) or **by property name**. You can write your functions like the native commands so they accept either one or both of these input types.

You can only accept pipeline input by value from one parameter of each datatype.

Pipeline input is received one item at a time, similar to how items are handled in a `foreach` loop. A `process` block is required.
```powershell
# Accepting pipeline input by type
function Test-PSPipelineInput {
	[CmdletBinding()]
	param (
		[Parameter(Mandatory,
				   ValueFromPipeline)]
		[string[]]$ComputerName
	)
	
	process {
		Write-Output $ComputerName
	}
}

# Accepting pipeline input by property name
function Test-PSPipelineInput {
	[CmdletBinding()]
	param (
		[Parameter(Mandatory,
				   ValueFromPipelineByPropertyName)]
		[string[]]$ComputerName
	)

	# Optional perform initial work BEFORE items are received from the pipeline.
	# Doesn't have access to piped values.
	# begin { } 
	
	process {
		Write-Output $ComputerName
	}

	# Optional, perform cleanup AFTER all items piped in are processed.
	# end { }
}
```
## Error handling
In PowerShell, `Try/Catch` is the more modern way to handle errors.

Note about `Try/Catch`. Only  terminating errors are caught.
```powershell
function Test-PSErrorHandling {

	[CmdletBinding()]
	param (
		[Parameter(Mandatory,
				   ValueFromPipeline,
				   ValueFromPipelineByPropertyName)]
		[string[]]$ComputerName
	)

	process {
		foreach ($Computer in $ComputerName) {
			# Applies try/catch but still generates unhandled exception.
			# The command doesn't generate a terminating error.
			try {
				Test-WSMan -ComputerName $Computer
			}
			catch {
				Write-Warning -Message "Unable to connect to Computer: $Computer"
			}
		}
	}
}

function Test-PSErrorHandling {
	# Same as above ...
	process {
		foreach ($Computer in $ComputerName) {
			# Specify ErrorAction with Stop
			# It turns a nonterminating error into a terminating one.
			try {
				Test-WSMan -ComputerName $Computer -ErrorAction Stop
			}
			catch {
				Write-Warning -Message "Unable to connect to Computer: $Computer"
			}
		}
	}
}
```
## Comment-based help
```powershell
function Get-PSAutoStoppedService {
	<#
		.HEADER
			Description...

		.HEADER 2
			Description...
	#>

	[CmdletBinding()]
	param ()
}
```