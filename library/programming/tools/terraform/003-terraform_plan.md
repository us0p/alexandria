Takes the terraform config that we defined which is considered the desired state and compares it with the current terraform state.
All the differences between the current configuration and the current terraform state are going to be planned and moved to the terraform apply command to be applied to the current state.

Avoid making modifications outside terraform as those changes are not going to be monitored by the state file.