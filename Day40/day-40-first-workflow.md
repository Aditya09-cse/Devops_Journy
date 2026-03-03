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
Look at your workflow file and write in your notes what each key does:
- `on:`
  ---
  
- `jobs:`

  A job is a unit of work inside a stage.

  A job:
  - Runs on a runner
  - Contains multiple steps
  - Executes a specific task (e.g., build app, run tests)

Each job runs independently unless configured otherwise.

---

- `runs-on:`
- `steps:`
    A step is a single command or action inside a job.

  Examples:
    - Install dependencies
    - Run tests
    - Build Docker image
    - Upload artifact

  Steps are the smallest executable unit in a pipeline.
---

- `uses:`
  
  ---
- `run:`

  ---
- `name:` (on a step)

---
