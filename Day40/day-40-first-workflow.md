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
### Task 4: Add More Steps
Update `hello.yml` to also:
1. Print the current date and time
2. Print the name of the branch that triggered the run (hint: GitHub provides this as a variable)
3. List the files in the repo
4. Print the runner's operating system

Push again — watch the new run.

   <img width="1350" height="742" alt="image" src="https://github.com/user-attachments/assets/ecd11d2d-f2f8-41c5-b828-12169694242a" />

---

### Task 5: Break It On Purpose
1. Add a step that runs a command that will **fail** (e.g., `exit 1` or a misspelled command)
2. Push and observe what happens in the Actions tab
3. Fix it and push again

   <img width="1316" height="587" alt="image" src="https://github.com/user-attachments/assets/f1ad9b0c-a17b-4bcb-91bb-271fc4ddaf69" />

### Write in your notes: What does a failed pipeline look like? How do you read the error?

## Visual Indicators

- Red ✗ (X mark) in the **Actions** tab instead of a green checkmark  
- The workflow run shows a **FAILED** status (red badge)  
- The job name is highlighted in red  
- The specific step that failed is marked with a red ✗  

---

## How to Read the Error

1. Go to the **Actions** tab → Click on the failed workflow run  
2. Identify the failing job (shown in red)  
3. Click the failed job to expand it  
4. Scroll through the step logs to find the red ✗ step  
5. Read the error message — it will show:
   - The command that failed  
   - The exit code (typically non-zero, like `exit 1`)  
   - Any `stderr` / `stdout` messages explaining what went wrong  

---

## Common Error Patterns

- `exit 1` → Command explicitly failed  
- `command not found` → Typo in command or missing tool  
- `Timeout` → Step took too long to execute  
- `Permission denied` → Insufficient permissions for the operation  
- `Syntax error` → Invalid YAML in your workflow file  



---
