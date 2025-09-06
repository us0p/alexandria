# Contexts
GitHub Actions includes a collection of variables called **contexts** and a similar collection of variables called **default variables**.
- **Default Environment Variables**: Exist only on the runner that is executing the job.
- **Contexts**: Can be used at any point of your workflow, including when **default variables** would be unavailable. Once the job is running, you can also retrieve context variables from the runner that is executing the job, such as `runner.os`.

The following example demonstrates how these different types of variables can be used together:
```yaml
name: CI
on: push
jobs:
	prod-check:
		if: ${{ github.ref == 'refs/heads/main' }}
		runs-on: ubuntu-latest
		steps:
			- run: echo "Deploying to production server on branch $GITHUB_REF"
```

In the example, the `if` check is processed by GitHub Actions, and the job is only sent to the runner if the result is `true`. Once the job is sent to the runner, the step is executed and refers to the `$GITHUB_REF` variable from the runner.
## Context availability
Different contexts are available throughout a workflow run. In addition, some functions may only be used in certain places.

You can check the [Contexts reference - GitHub Docs](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability). It contains a table listing the restrictions on where each context and special function can be used within a workflow.

You can check the available contexts by visiting the [Contexts reference - GitHub Docs](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#available-contexts).