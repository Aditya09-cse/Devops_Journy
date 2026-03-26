# Day 45 – Docker Build & Push in GitHub Actions

### Task 1: Prepare
1. Use the app you Dockerized on Day 36
   
   [app](https://github.com/Aditya09-cse/My-DevOps-Journy/tree/main/Day36/flask-task-manager)
   
2. Add the Dockerfile to your `github-actions-practice` repo

   [Dockerfile](https://github.com/Aditya09-cse/github-actions-practice/blob/main/flask-task-manager/Dockerfile)
   
3. Make sure `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets are set from Day 44

---

### Task 2: Build the Docker Image in CI
Create `.github/workflows/docker-publish.yml` that:
1. Triggers on push to `main`
2. Checks out the code
3. Builds the Docker image and tags it

**Verify:** Check the build step logs — does the image build successfully?'

- **yes image build successfully**

<img width="1176" height="494" alt="image" src="https://github.com/user-attachments/assets/b8e4cdb3-0c2a-48eb-ad45-a8fa6683e19c" />

---

### Task 3: Push to Docker Hub
Add steps to:
1. Log in to Docker Hub using your secrets
2. Tag the image as `username/repo:latest` and also `username/repo:sha-<short-commit-hash>`
3. Push both tags

**Verify:** Go to Docker Hub — is your image there with both tags?

<img width="1134" height="501" alt="image" src="https://github.com/user-attachments/assets/052c8d05-a0dc-471d-85ee-c4dbacbc293a" />

---

### Task 4: Only Push on Main
Add a condition so the push step only runs on the `main` branch — not on feature branches or PRs.

Test it: push to a feature branch and verify the image is built but NOT pushed.

<img width="1324" height="571" alt="image" src="https://github.com/user-attachments/assets/6d96b8c5-6398-4236-ba4e-de93c8a627ba" />


---

### Task 5: Add a Status Badge
1. Get the badge URL for your `docker-publish` workflow from the Actions tab
2. Add it to your `README.md`
3. Push — the badge should show green

  <img width="856" height="221" alt="image" src="https://github.com/user-attachments/assets/b47891af-b9c1-4e2f-b6e2-b245bca7a209" />

---

### Task 6: Pull and Run It
1. On your local machine (or a cloud server), pull the image you just pushed
2. Run it
3. Confirm it works
   - *`yes it working fine`*

[Docker-Hub](https://hub.docker.com/repository/docker/aditya0910/flask-task-manager/tags?ordering=last_updated&page=1)

<img width="1345" height="643" alt="image" src="https://github.com/user-attachments/assets/694fe6f8-8369-4dc8-b068-f0337ef633a7" />

<img width="1080" height="578" alt="image" src="https://github.com/user-attachments/assets/486523e0-b8ac-4ef4-8222-70f7810ab033" />



Write in your notes: What is the full journey from `git push` to a running container?

1. git push – Code is pushed to GitHub.

2. GitHub Actions triggers – The CI/CD workflow starts.

3. Checkout code: `uses: actions/checkout@v4`

4. Login to Docker Hub: `uses: docker/login-action@v3`

5. Build Docker image using the Dockerfile.
    - If code is pushed to main: Docker image is built, tagged, and pushed to Docker Hub.
    - If pushed to other branches or PRs:Docker image is only built for testing.It is not pushed to Docker Hub.

6. Run the container: `docker run -d --name my-app -p 5000:5000 aditya0910/flask-task-manager`

---


