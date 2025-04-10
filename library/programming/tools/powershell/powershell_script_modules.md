## Dot-sourcing functions
When you run a script that defines a function, the function is loaded into the **Script** scope. Once the script finishes executing, PowerShell discards that scope along with the function.

To keep the function available after the script runs, it need to be loaded into the **Global** scope. You can accomplish this by dot-sourcing the script file.
```powershell
.\my_script.ps1 # Script scope
. .\my_script_.ps1 # Global scope
```
## Script modules
A script modules is a `.psm1` file that contains one or more functions.

To make the functions in your script module available, use `Import-Module`.

Autoloading was introduced in version 3. To take advantage of this feature, the script module must be saved in a folder with the same base name as the `.pms1` file. That folder must be located in one of the directories specified in the `$env:PSModulePath` environment variable.

For Dynamic modules that exist only in memory, see `New-Module`
## Module manifest
Every module should include a module manifest, which is a `.psd1` file containing metadata about the module.

Note that, not all `.psd1` files are module manifests. You can also use them for other purposes, such as defining environment data in a DSC configuration.

You can create a module manifest using the `New-ModuleManifest` cmdlet. The only required parameter is `Path`, but for the module to work correctly, you must also specify the `RootModule` parameter.

If you omit any values when initially creating the manifest, you can updated it later using the `Update-ModuleManifest` cmdlet.
## Defining public and private functions
If you're not following best practices and only have a `.psm1` file without a proper module structure, your only option is to control visibility using the `Export-ModuleMember` cmdlet.
```powershell
function Get-PSVersion {
	$PSVersionTable
}

function Get-PSComputerName {
	$env:COMPUTERNAME
}

# Only Get-PSVersion is exported, everything else is keep private.
Export-ModuleMember -Function Get-PSVersion
```

If you add a manifest to your module, it's a best practice to explicity