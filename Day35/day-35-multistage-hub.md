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

