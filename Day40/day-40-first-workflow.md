# Day 40 – Your First GitHub Actions Workflow


### Task 2: Hello Workflow
Create `.github/workflows/hello.yml` with a workflow that:
1. Triggers on every `push`
2. Has one job called `greet`
3. Runs on `ubuntu-latest`
4. Has two steps:
   - Step 1: Check out the code using `actions/checkout`
   - Step 2: Print `Hello from GitHub Actions!`

Push it. Go to the **Actions** tab on GitHub and watch it run.

**Verify:** Is it green? Click into the job and read every step.

  <img width="1356" height="544" alt="image" src="https://github.com/user-attachments/assets/00710406-f68c-44d0-a991-f3f54094cba6" />


---

### Task 3: Understand the Anatomy
# GitHub Actions Workflow Key Components

## `on:`
Defines the trigger events that cause the workflow to run.

**Examples:**
- `push` — runs on every push to the repository  
- `pull_request` — runs when a PR is opened or updated  
- `schedule` — runs on a schedule (cron jobs)  
- `workflow_dispatch` — allows manual triggering  

---

## `jobs:`
Defines one or more jobs that run as part of the workflow.

- Each job runs in its own runner instance.  
- Jobs can run in parallel or sequentially depending on your configuration.

---

## `runs-on:`
Specifies the type of machine (runner) where the job executes.

**Common options:**
- `ubuntu-latest` — Linux runner  
- `windows-latest` — Windows runner  
- `macos-latest` — macOS runner  

Self-hosted runners are also supported.

---

## `steps:`
An ordered list of tasks that execute within a job.

- Each step runs sequentially in the same runner.  
- Steps can use actions, run shell commands, or execute scripts.

---

## `uses:`
Specifies a reusable action (pre-built workflow code) to run.

**Format:**
owner/repo@version


**Example:**
```yaml
uses: actions/checkout@v4
```
 - Checks out your repository code
 - Actions can be from GitHub, the Marketplace, or a custom repository

## `run:`
Executes a shell command directly on the runner

**Example:**
```
run: echo "Hello from GitHub Actions!"
```

- Runs in bash on Linux/macOS
- Runs in PowerShell on Windows

## `name: (on a step`
Provides a human-readable label for a step.

- Appears in the Actions tab logs
- kes workflows easier to understand

**Example:**
  ```
  name: Print greeting message
  ```
---
