# Day 42 – Runners: GitHub-Hosted & Self-Hosted

# Introduction

In GitHub Actions, every workflow job runs on a **runner**.

A **runner** is a machine that executes the steps in a workflow job.

GitHub provides two types of runners:

- **GitHub-Hosted Runners** – Managed by GitHub  
- **Self-Hosted Runners** – Managed by us on our own machine/server

In this task, we explored both types and configured a self-hosted runner on a cloud VM.

---

### Task 1: GitHub-Hosted Runners
1. Create a workflow with 3 jobs, each on a different OS:
   - `ubuntu-latest`
   - `windows-latest`
   - `macos-latest`


      
2. In each job, print:
   - The OS name
   - The runner's hostname
   - The current user running the job
3. Watch all 3 run in parallel

Write in your notes: What is a GitHub-hosted runner? Who manages it?

---
