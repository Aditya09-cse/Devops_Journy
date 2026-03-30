# Day 46 – Reusable Workflows & Composite Actions


### Task 1: Understand `workflow_call`
Before writing any code, research and answer in your notes:
1. What is a **reusable workflow**?
   - Reusable workflows are predefined workflows stored in a single location and invoked by other workflows across repositories.
   - This approach centralizes logic, reduces duplication, and ensures consistent implementation of processes like testing, deployment, and linting.
2. What is the `workflow_call` trigger?
   - workflow_call is a special trigger in GitHub Actions that makes a workflow reusable.
   - This workflow will not run by itself (like on push/pull).
   - It will run only when another workflow calls it using uses:.
     ```
     on:
       workflow_call:
     ```

     ```
     jobs:
      call-workflow:
        uses: username/repo/.github/workflows/reusable.yml@main
     ```
3. How is calling a reusable workflow different from using a regular action (`uses:`)?
   - regular action - A single action (like a plugin/tool), Runs inside a job as one step
     ```
     - name: Checkout code
      uses: actions/checkout@v4
     ```
    - Calling a Reusable Workflow - A full workflow, Contains multiple jobs + steps, Called at the job level, not step level
    ```
    jobs:
      deploy:
        uses: username/repo/.github/workflows/deploy.yml@main
    ```
   
4. Where must a reusable workflow file live?
   - A resuable workflow file must be inside ` .github/workflows ` folder
   ```
   .github/workflows/reusable.yml
   ```
---

### Task 2: Create Your First Reusable Workflow
Create `.github/workflows/reusable-build.yml`:
1. Set the trigger to `workflow_call`
2. Add an `inputs:` section with:
   - `app_name` (string, required)
   - `environment` (string, required, default: `staging`)
3. Add a `secrets:` section with:
   - `docker_token` (required)
4. Create a job that:
   - Checks out the code
   - Prints `Building <app_name> for <environment>`
   - Prints `Docker token is set: true` (never print the actual secret)

**Verify:** This file alone won't run — it needs a caller. That's next.

---
