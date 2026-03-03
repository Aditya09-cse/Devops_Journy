# Day 39 – What is CI/CD?

### Task 1: The Problem
Think about a team of 5 developers all pushing code to the same repo manually deploying to production.

Write in your notes:
1. What can go wrong?
2. What does "it works on my machine" mean and why is it a real problem?

   - this is classic tech problem where developer writes code and push to github but in clien side thier are some dependienies are missing due to this he is not able to run this program
   - so he says to developer to check the program again
   - developer check the program and run on their machine and it runs succesfully
   - so developer says it work on machine
   - it is real problem because due to this conflicts happend between dev and client
     
3. How many times a day can a team safely deploy manually?

---

### Task 2: CI vs CD
Research and write short definitions (2-3 lines each):
1. **Continuous Integration** — what happens, how often, what it catches
   - continoues integration means developer push code to vcs(github) coninouesly
     
2. **Continuous Delivery** — how it's different from CI, what "delivery" means
   - contionues deleivery means our application/program are continoues deliver with option of reviewing
     
3. **Continuous Deployment** — how it differs from Delivery, when teams use it
    - Continuous Deployment-> Automatic deploy of application without manual internvantion

Write one real-world example for each.

---

### Task 3: Pipeline Anatomy
A pipeline has these parts — write what each one does:
- **Trigger** — what starts the pipeline
- **Stage** — a logical phase (build, test, deploy)
- **Job** — job has a particular task to run like code, build , test , deploy
- **Step** — a single command or action inside a job
- **Runner** — the machine that executes the job
- **Artifact** — output produced by a job

---

### Task 4: Draw a Pipeline
Draw a CI/CD pipeline for this scenario:
> A developer pushes code to GitHub. The app is tested, built into a Docker image, and deployed to a staging server.

Include at least 3 stages. Hand-drawn and photographed is perfectly fine.

  <img width="976" height="419" alt="image" src="https://github.com/user-attachments/assets/ce80d8d9-cee7-49c3-9e9b-385f5138d322" />

--

### Task 5: Explore in the Wild
1. Open any popular open-source repo on GitHub 
2. Find their `.github/workflows/` folder
3. Open one workflow YAML file

    [workflow](https://github.com/OpenHub-Store/GitHub-Store/blob/main/.github/workflows/build-desktop-platforms.yml)
   
4. Write in your notes:
   - What triggers it?

```
on:
  push:
    branches:
      - generate-installers
```
   - How many jobs does it have?

      This workflow file has **3 jobs**:

   1. **build-windows** - Builds Windows installers (EXE & MSI)
   2. **build-macos** - Builds macOS installers (DMG & PKG) with a matrix strategy for both Intel (x64) and Apple Silicon (arm64)
   3. **build-linux** - Builds Linux installers (DEB, RPM, AppImage) with a matrix strategy for modern Ubuntu and Debian 12 compatibility

 - What does it do? (best guess)

     

##  What does it do

| Aspect | Details |
|--------|---------|
| **Workflow Name** | Build Desktop Platform Installers |
| **Trigger** | Push to `generate-installers` branch |
| **Purpose** | Build and package desktop installers for GitHub-Store app |
| **Windows Build** | Creates EXE & MSI installers on Windows latest |
| **macOS Build** | Creates DMG & PKG installers for Intel (x64) & Apple Silicon (arm64) |
| **Linux Build** | Creates DEB, RPM, & AppImage on Ubuntu latest; DEB & RPM on Ubuntu 22.04 |
| **Build Tool** | Gradle with Java 21 |
| **Retry Logic** | Up to 3 attempts with exponential backoff |
| **Artifact Retention** | 30 days |
| **Execution** | Parallel builds across all platforms |


---
