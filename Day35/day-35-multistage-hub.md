# Day 35 – Multi-Stage Builds & Docker Hub

### Task 1: The Problem with Large Images
1. Write Node.js app (even a "Hello World" is fine)
2. Create a Dockerfile that builds and runs it in a **single stage**
3. Build the image and check its **size**

Note down the size — you'll compare it later.
  - `**135MB**`

<img width="691" height="78" alt="image" src="https://github.com/user-attachments/assets/ea3d61cc-d465-4903-89e1-fe3aec1023d2" />

---
### Task 2: Multi-Stage Build
1. Rewrite the Dockerfile using **multi-stage build**:
   - Stage 1: Build the app (install dependencies, compile)
   - Stage 2: Copy only the built artifact into a minimal base image (`alpine`, `distroless`, or `scratch`)
2. Build the image and check its size again
3. Compare the two sizes

   - `*125MB*` -> size only reduce 10MB because i use aline as base image that already are small in size
        
  <img width="721" height="99" alt="image" src="https://github.com/user-attachments/assets/e6c81a56-f659-4d64-a683-97e8c676f836" />

Write in your notes: Why is the multi-stage image so much smaller?
- Multi-stage builds smaller images because they separate “build” from “runtime”, copying only what’s necessary into the final image.

---
### Task 3: Push to Docker Hub
1. Create a free account on [Docker Hub](https://hub.docker.com) (if you don't have one)
2. Log in from your terminal
3. Tag your image properly: `yourusername/image-name:tag`
4. Push it to Docker Hub
5. Pull it on a different machine (or after removing locally) to verify


   --- 
  <img width="880" height="499" alt="image" src="https://github.com/user-attachments/assets/df6b1651-4f4f-4e7f-aa72-3be6659983e6" />


  ---
  <img width="1029" height="526" alt="image" src="https://github.com/user-attachments/assets/12cd6050-11da-4059-9d33-b576e5d1b984" />
  

---
  <img width="997" height="523" alt="image" src="https://github.com/user-attachments/assets/1ad98f04-f3d9-4ba8-9b54-072f180de59d" />
  

---
  <img width="812" height="557" alt="image" src="https://github.com/user-attachments/assets/7b7d1586-1ab5-4c79-a132-721f2f6bb6bf" />


---

### Task 4: Docker Hub Repository
1. Go to Docker Hub and check your pushed image
2. Add a **description** to the repository
3. Explore the **tags** tab — understand how versioning works
4. Pull a specific tag vs `latest` — what happens?

<img width="1006" height="478" alt="image" src="https://github.com/user-attachments/assets/d6b9f02c-8daf-45cb-9304-67172cf7bbc6" />


---





















# pending
### Task 5: Image Best Practices
Apply these to one of your images and rebuild:
1. Use a **minimal base image** (alpine vs ubuntu — compare sizes)
2. **Don't run as root** — add a non-root USER in your Dockerfile
3. Combine `RUN` commands to **reduce layers**
4. Use **specific tags** for base images (not `latest`)

Check the size before and after.

---











