[CI/CD](cicd.md) platform that allows you to automate your build, test, and deployment pipeline.

You can also create workflows for events outside the DevOps bubble.

GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, you can also host your own runner.
## Billing
You can check the billing details for GitHub actions runners [here](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
## Components of GitHub Actions
You can configure a [workflow](github_actions_workflow.md) to be triggered when an **event** occurs in your repository, such as a pull request. Your workflow contains one or more **jobs** which can run in sequential order or in parallel. Each job will run inside its own virtual machine **runner**, or inside a container, and has one or more **steps** that either run a script that you define or run an **action**, which is a reusable extension that can simplify your workflow.
## Workflow
Configurable automated process that will run one or more jobs.

Workflows are defined by a YAML file **checked** in to your repository and will run when triggered by an event in your repository.

Workflows are defined in the `.github/workflows` directory in a repository.

A repository can have multiple workflows.

You can reference a workflow within another workflow.
## Events
Specific activity in a repository that triggers a workflow run. 

E.g.: Pull request.

You can also trigger a workflow to run on a schedule, by posting to a REST API, or manually.
## Jobs
Set of **steps** in a workflow that is executed on the same **runner**. Each step is either a shell script that will be executed, or an **action** that will be run.

Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

By default, jobs have no dependencies and run in parallel. When a job takes a dependency on another job, it waits for the dependent job to complete before running.

You can also use a **matrix** to run the same job multiple times, each with a different combination of variables.
## Actions
Pre-defined, reusable set of jobs or code that performs specific tasks within a workflow.

You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.
## Runners
Server that runs your workflows when they're triggered. Each runner can run a single job at a time.

Each workflow run executes in a fresh, newly-provisioned virtual machine.

If you need a different operating system or require a specific hardware configuration, you can host your own runners.
## Using open-source GitHub Actions
- Review the action's `action.yml` file for inputs, outputs, and to make sure the code does what it says it does.
- Include the version of the action you're using by specifying a Git ref, SHA ,or tag.
## Types of GitHub Actions
There are three types of GitHub Actions:
- Container actions: Environment is part of the action's code. Can only be run in a Linux environment that GitHub hosts. Support many different languages.
- JavaScript actions: Don't include the environment in the code. You have to specify the environment to execute these actions. Can be run in VM, cloud or on-prem. Supports Linux, macOS and Windows environments.
- Composite actions: Allow you to combine multiple workflow steps within one action.