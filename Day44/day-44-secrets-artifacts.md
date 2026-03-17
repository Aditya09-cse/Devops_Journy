# Day 44 – Secrets, Artifacts & Running Real Tests in CI

### Task 1: GitHub Secrets
1. Go to your repo → Settings → Secrets and Variables → Actions
2. Create a secret called `MY_SECRET_MESSAGE`
3. Create a workflow that reads it and prints: `The secret is set: true` (never print the actual value)
4. Try to print `${{ secrets.MY_SECRET_MESSAGE }}` directly — what does GitHub show?

   <img width="738" height="163" alt="image" src="https://github.com/user-attachments/assets/112ea0f5-699f-4424-9493-e53991feb5f6" />


  <img width="785" height="357" alt="image" src="https://github.com/user-attachments/assets/caf06548-6013-41fd-a180-5c2e26eab666" />

[GitHub-Secret](secrets.yml)

Write in your notes: Why should you never print secrets in CI logs?
  - Permanent Exposure: Logs are often saved and shared, making secrets visible to anyone with access to the system.
  - Irreversible Leak: Once a secret is printed, it’s nearly impossible to delete from all backups, caches, and monitoring tools.
    
---

### Task 2: Use Secrets as Environment Variables
1. Pass a secret to a step as an environment variable
2. Use it in a shell command without ever hardcoding it
3. Add `DOCKER_USERNAME` and `DOCKER_TOKEN` as secrets 

  <img width="994" height="478" alt="image" src="https://github.com/user-attachments/assets/7cb286aa-ce4e-49ac-84fc-707aede11198" />


[Secrets Message](docker-secret-env.ym)

---

### Task 3: Upload Artifacts
1. Create a step that generates a file — e.g., a test report or a log file
2. Use `actions/upload-artifact` to save it
3. After the workflow runs, download the artifact from the Actions tab

   <img width="1170" height="539" alt="image" src="https://github.com/user-attachments/assets/fe76651e-e240-4cd2-94c9-99169b122bf5" />


[upload-artifacts](upload-artifacts.yml)


**Verify:** Can you see and download it from GitHub?
  - *`yes`* -> i seen and download it from github
    
---

### Task 4: Download Artifacts Between Jobs
1. Job 1: generate a file and upload it as an artifact
2. Job 2: download the artifact from Job 1 and use it (print its contents)

  <img width="1039" height="356" alt="image" src="https://github.com/user-attachments/assets/52fc0763-4761-4a1a-b1bc-2526a833c75c" />

  <img width="1091" height="489" alt="image" src="https://github.com/user-attachments/assets/a1f8d3d6-6b67-465c-95d9-3c82299e79b5" />


  <img width="1058" height="556" alt="image" src="https://github.com/user-attachments/assets/4848666c-1eb3-499f-9cec-effe24384934" />

  

[articats-bw-jobs.yml](articats-bw-jobs.yml)


Write in your notes: When would you use artifacts in a real pipeline?
  - Artifacts are used to store and transfer files generated during pipelines.
  - Test reports,

---

### Task 5: Run Real Tests in CI
Take any script from your earlier days (Python or Shell) and run it in CI:
1. Add your script to the `github-actions-practice` repo
2. Write a workflow that:
   - Checks out the code
   - Installs any dependencies needed
   - Runs the script
   - Fails the pipeline if the script exits with a non-zero code
3. Intentionally break the script — verify the pipeline goes red


   <img width="1127" height="469" alt="image" src="https://github.com/user-attachments/assets/94b3d216-55fa-4c33-a72e-ad6755ae0150" />

    <img width="1315" height="432" alt="image" src="https://github.com/user-attachments/assets/db078e48-69d8-4ef0-bb5b-66e0c23c244e" />

[test-ci](test-ci.yml)   

4. Fix it — verify it goes green again
  - *`yes`* -> it goes green again
    
---

### Task 6: Caching
1. Add `actions/cache` to a workflow that installs dependencies
2. Run it twice — observe the time difference

   <img width="1294" height="486" alt="image" src="https://github.com/user-attachments/assets/a742151e-ae21-4424-bf6f-979d7c4ab99d" />

   <img width="1287" height="378" alt="image" src="https://github.com/user-attachments/assets/bde5e532-22eb-43bf-b975-09cc1cdad087" />

  [caching](cache.yml)


3. Write in your notes: What is being cached and where is it stored?
  - What is cached: Python packages downloaded by pip from requirements.txt.
  - Where it’s stored: On GitHub Actions servers,restored to the runner at ~/.cache/pip.

---


 **What I lerned from Secret Management**

- Store sensitive data (like API keys, tokens, passwords) in GitHub Actions Secrets, not in code.
- They are encrypted, injected at runtime, and never exposed in logs.
