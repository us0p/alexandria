# Workflow
Configurable automated process made up of one or more jobs. You must create a YAML file to define your workflows configuration.
## Most used properties
### `name`
The name of the workflow. If you omit `name`, GitHub displays the workflow file path relative to the root of the repository.
### `on`
Automatically trigger a workflow when defined events happen.

For a list of available events, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).
#### Using filters
Some events have filters. For example, the `push` event has a `branches` filter that causes your workflow to run only when a push to a branch that matches the `branches` filter occurs.
```yaml
on:
	push:
		branches:
			- main
			- 'releases/**'
	pull_request:
		branches: [ "main", "releases/**" ] # Using JSON sequence style
```
### `jobs`
Components of a `workflow`.

Run parallel by default.

Each job runs in a runner environment specified by `runs-on`.
#### `jobs.<job_id>`
Used to give your job a unique identifier.

`<job_id>` is a string and its value is a map of the job's configuration data. It must start with a letter or `_` and contain only alphanumeric characters, `-`, or `_`.
#### `jobs.<job_id>.runs-on`
Used to define the type of machine to run the job on.

The destination machine can be either a GitHub-hosted runner, larger runner or a self-hosted runner.

You can target runners based on the labels assigned to them, their group membership, or a combination of these.
```yaml
jobs:
	build: # job_id
		runs-on: ubuntu-latest # Will run on a GitHub hosted machine.
```
#### `jobs.<job_id>.steps`
Sequence of tasks assigned to a job.

Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry.

Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps.
#### `jobs.<job_id>.steps[*].name`
A name for your step to display on GitHub.
```yaml
steps:
	- name: Awesome name
```

If you define a `run` step, the name will default to the text specified in the `run` command.
#### `jobs.<job_id>.steps[*].uses`
Selects an action to run as part of a step in your job. An action is a reusable unit of code.

It's strongly recommended to include the version of the action you are using by specifying a Git ref, SHA, or Docker tag.

Actions are either JavaScript files or Docker containers. If the action you're using is a Docker container you must run the job in a Linux environment.
```yaml
steps:
	# Reference the major version or a release
	- uses: actions/checkout@v4
```
#### `job.<job_id>.steps[*].run`
Runs command-line programs that do not exceed 21000 characters using the operating system's shell.

Commands run using non-login shells by default. You can choose a different shell and customize the shell used to run commands.

Each `run` keyword represents a new process and shell in the runner environment. When you provide multi-line commands, each line runs in the same shell.
```yaml
# Single-line command
- name: Install Dependencies
  run: npm install

# Multi-line command
- name: Clen install dependencies and build
  run: |
	  npm ci
	  npm run build
```
#### `job.<job_id>.steps[*].with`
A `map` of the input parameters defined by the action.

Input parameters are set as environments variables.

The variable is prefixed with `INPUT_` and converted to upper case.

Input parameters defined for a Docker container must use `args`.
```yaml
jobs:
	my_first_job:
		steps:
			- name: My First Step
			  uses: actions/hello_world@main
			  # Parameters defined by the action.
			  with:
				  first_name: Mona
				  middle_name: The
				  last_name: Octocat
```
#### `job.<job_id>.strategy`
Sets a matrix strategy for your jobs.

A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables. For example, you can use a matrix strategy to test your code in multiple versions of a language.
##### `job.<job_id>.strategy.matrix`
Used to define a matrix of different job configurations.

A matrix will generate a maximum of 256 jobs per workflow run.

The variables you define become properties in the `matrix` context, and you can reference the property in other areas of your workflow file.

The order of the variables in the matrix determines the order in which the jobs are created.
```yaml
# Using single-dimension matrix
# The workflow will run three jobs
jobs:
	example_matrix:
		strategy:
			matrix:
				version: [10, 12, 14]
		steps:
			- uses: actions/setup-node@v4
			  with:
				  node-version: ${{ matrix.version }}

# Using multi-dimensional matrix
# Job will run for each possible combination of the variables
# The workflow will run six jobs, one for each combination of the `os` and `version` variables.
jobs:
	example_matrix:
		strategy:
			matrix:
				os: [ubuntu-22.04, ubuntu-20.04]
				version: [10, 12, 14]
		runs-on: ${{ matrix.os }}
		steps:
			- uses: actions/setup-node@v4
			  with:
				  node-version: ${{ matrix.version }}

# A variable configuration in a matrix can be an array of objects.
# Each job in the matrix will have its own combination of os and node values.
matrix:
	os:
		- ubuntu-latest
		- macos-latest
	node:
		- version: 14
		- version: 20
		  env: NODE_OPTIONS=--openssl-legacy-provider
```