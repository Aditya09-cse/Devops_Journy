# Day 41 – Triggers & Matrix Builds

### Task 1: Trigger on Pull Request
1. Create `.github/workflows/pr-check.yml`
2. Trigger it only when a pull request is **opened or updated** against `main`
3. Add a step that prints: `PR check running for branch: <branch name>`
4. Create a new branch, push a commit, and open a PR
5. Watch the workflow run automatically

**Verify:** Does it show up on the PR page? 
 - **`yes`**


<img width="1353" height="581" alt="image" src="https://github.com/user-attachments/assets/2bb92f5b-059c-48d5-80de-c1dab2fba040" />

---

### Task 2: Scheduled Trigger
1. Add a `schedule:` trigger to any workflow using cron syntax
2. Set it to run every day at midnight UTC

 <img width="1340" height="584" alt="image" src="https://github.com/user-attachments/assets/03275d94-a732-4dfb-9287-f80b4079f02c" />

3. Write in your notes: What is the cron expression for every Monday at 9 AM?
   - *`0 9 * * 1`*

---

### Task 3: Manual Trigger
1. Create `.github/workflows/manual.yml` with a `workflow_dispatch:` trigger
2. Add an **input** that asks for an `environment` name (staging/production)
3. Print the input value in a step
4. Go to the **Actions** tab → find the workflow → click **Run workflow**

**Verify:** Can you trigger it manually and see your input printed?
 - *yes* i am able to trigger it manually and see my output (output -> production)


 <img width="991" height="441" alt="image" src="https://github.com/user-attachments/assets/9fa1bae7-e574-4d80-9cad-cbb37ed0b430" />

---

### Task 4: Matrix Builds
Create `.github/workflows/matrix.yml` that:
1. Uses a matrix strategy to run the same job across:
   - Python versions: `3.10`, `3.11`, `3.12`
2. Each job installs Python and prints the version
3. Watch all 5 run in parallel

 <img width="1114" height="453" alt="image" src="https://github.com/user-attachments/assets/a0eb3224-217c-421e-b6ae-ca57c07541be" />


Then extend the matrix to also include 2 operating systems — how many total jobs run now?

 <img width="1072" height="592" alt="image" src="https://github.com/user-attachments/assets/e8fa39ab-e950-45e1-b7ae-d59f52c25385" />


---

### Task 5: Exclude & Fail-Fast
1. In your matrix, **exclude** one specific combination (e.g., Python 3.10 on Windows)
2. Set `fail-fast: false` — trigger a failure in one job and observe what happens to the rest

   <img width="1117" height="491" alt="image" src="https://github.com/user-attachments/assets/1f4d077e-8d9d-45ff-8299-a3bdd40f8738" />

3. Write in your notes: What does `fail-fast: true` (the default) do vs `false`?
   - `fail-fast: true` -> If any job in the matrix fails, GitHub immediately cancels the remaining running matrix jobs
   - `fail-fast: false` -> If a job fails, GitHub still runs the remaining jobs.

---

