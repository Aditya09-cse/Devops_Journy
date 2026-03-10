# Day 37 – Docker Revision & Cheat Sheet

## Self-Assessment Checklist

- [**can do** ] Run a container from Docker Hub (interactive + detached)
- [ **can do**] List, stop, remove containers and images
- [**shaky** ] Explain image layers and how caching works
- [**can do** ] Write a Dockerfile from scratch with FROM, RUN, COPY, WORKDIR, CMD
- [ **shaky**] Explain CMD vs ENTRYPOINT
- [ **can do**] Build and tag a custom image
- [ **can do**] Create and use named volumes
- [**can do** ] Use bind mounts
- [**can do** ] Create custom networks and connect containers
- [**can do** ] Write a docker-compose.yml for a multi-container app
- [**can do** ] Use environment variables and .env files in Compose
- [ **can do**] Write a multi-stage Dockerfile
- [ **can do**] Push an image to Docker Hub
- [**can do** ] Use healthchecks and depends_on

---

## Quick-Fire Questions
Answer from memory, then verify:
1. What is the difference between an image and a container?
   - An Image is a read only blueprint while A container is running instance of this image.
     
2. What happens to data inside a container when you remove it?
   - Data is also deleted
   - data not deleted when we store in volume or bind mount
     
3. How do two containers on the same custom network communicate?
   - By container names they can communicate.
     
4. What does `docker compose down -v` do differently from `docker compose down`?
   - `docker compose down -v` -> Stop & remove conatiner with network along with their volume 
   - `docker compose down` -> Stop & remove conatiner with network
     
5. Why are multi-stage builds useful?
   - Multi-stage builds smaller images because they separate “build” from “runtime”, copying only what’s necessary into the final image.
     
6. What is the difference between `COPY` and `ADD`?
   - `CMD` -> copy the source code from local , required source and destination
   - `ADD` -> similar to `copy` give extra feature to download file from internet ,also we extract file
7. What does `-p 8080:80` mean?
   - ` -p 8080:80` -> means local port 80 is mapped with host port 8080
     
8. How do you check how much disk space Docker is using?
   - using commands `docker systen df`
  
---

## Build Your Docker Cheat Sheet
Create `docker-cheatsheet.md` organized by category:
- **Container commands** — run, ps, stop, rm, exec, logs
- **Image commands** — build, pull, push, tag, ls, rm
- **Volume commands** — create, ls, inspect, rm
- **Network commands** — create, ls, inspect, connect
- **Compose commands** — up, down, ps, logs, build
- **Cleanup commands** — prune, system df
- **Dockerfile instructions** — FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT

[cheetsheet](https://github.com/Aditya09-cse/DevOps-Commands-CheatSheet/blob/main/Docker.md)
