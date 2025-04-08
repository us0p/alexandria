# PowerShell Execution Policy
Controls the conditions under which you can run PowerShell scripts.
It's not a security boundary because it can't stop determined users from deliberately running scripts.

You can set an execution policy for the local computer, current user, or a PowerShell session. You can also set execution policies for user and computers with Group Policy.

Regardless of the execution policy setting, you can run any PowerShell command interactively. The execution policy only affects commands running in a script.

All Windows client operating systems have the default execution policy setting of `Restricted`.

You must run PowerShell elevated as an administrator to change the execution policy for the **Local Machine**.

For more information, see:
- `Get-ExecutionPolicy`
- `Set-ExecutionPolicy`