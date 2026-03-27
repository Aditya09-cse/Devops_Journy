# Day 50 – Kubernetes Architecture and Cluster Setup

### Task 1: Recall the Kubernetes Story
Before touching a terminal, write down from memory:

1. Why was Kubernetes created? What problem does it solve that Docker alone cannot?
   - kubernetes was created to manage the problem of container crashing and auto-heal problem
   - google internal system faced problem of auto-scale & auto-heal when traffic increase or container crashes, docker is not able to solve this issue
   - to solve this issue google created borg, which can auto-heal & auto-scale when needed
     
3. Who created Kubernetes and what was it inspired by?
   - kubernetes is created by google in 2014,
   - This project was inspired by borg,an interal system used by google to manage containers at massiv scale
   - Borg automatically autoheal when get crashed & auto-scale when traffic spike sudden
   - later on, google made this project open source, now it was managed by CNCF(Cloud Native Computing Foundation) which is part of Linux foundation
    
3. What does the name "Kubernetes" mean?
   - The name Kubernetes comes from a Greek word meaning “helmsman” or “ship pilot.” It refers to someone who steers a ship.
   - This name reflects the role of Kubernetes, which guides and manages containers, similar to how a helmsman controls a ship.
   - Kubernetes is often shortened to K8s, where the number 8 represents the eight letters between K and S.


---

### Task 2: Draw the Kubernetes Architecture
From memory, draw or describe the Kubernetes architecture. Your diagram should include:

**Control Plane (Master Node):**
- API Server — the front door to the cluster, every command goes through it
- etcd — the database that stores all cluster state
- Scheduler — decides which node a new pod should run on
- Controller Manager — watches the cluster and makes sure the desired state matches reality

**Worker Node:**
- kubelet — the agent on each node that talks to the API server and manages pods
- kube-proxy — handles networking rules so pods can communicate
- Container Runtime — the engine that actually runs containers (containerd, CRI-O)



  <img width="925" height="431" alt="image" src="https://github.com/user-attachments/assets/142b0dd0-53b8-4cec-87fe-6f55be9173df" />


After drawing, verify your understanding:
- What happens when you run `kubectl apply -f pod.yaml`? Trace the request through each component.
- What happens if the API server goes down?
- What happens if a worker node goes down?

---
