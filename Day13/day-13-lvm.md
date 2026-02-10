# Day 13 – Linux Volume Management (LVM)

## Overview
Today I practiced Linux Logical Volume Management (LVM) to understand how
storage can be created, managed, extended, and resized dynamically.
This is a critical skill for DevOps and Linux system administration.

---

## Initial Storage Check

Commands used:
```bash
lsblk
pvs
vgs
lvs
df -h
```
This helped me identify:
  - Existing root disk
  - Newly attached disk
  - No LVM configuration initially

## LVM Setup
### 1. Create Physical Volume
```
pvcreate /dev/nvme1n1
pvs
```
### 2. Create Volume Group
```
vgcreate devops-vg /dev/nvme1n1
vgs
```
### 3. Create Logical Volume
```
lvcreate -L 5G -n app-data devops-vg
lvs
```

## Format and Mount Logical Volume
```
mkfs.ext4 /dev/devops-vg/app-data
mkdir -p /mnt/app-data
mount /dev/devops-vg/app-data /mnt/app-data
df -h /mnt/app-data
```
The logical volume was successfully mounted and accessible.

## Extend Logical Volume (Live Resize)
```
lvextend -L +2G /dev/devops-vg/app-data
resize2fs /dev/devops-vg/app-data
df -h /mnt/app-data
```
- Logical volume extended from 5G to 7G
- Filesystem resized online (no unmount required)

## Unmount Verification
```
umount /dev/mapper/devops--vg-app--data
df -h
lsblk
```
- Mount point removed successfully
- Logical volume no longer mounted

## What I Learned
  - LVM allows flexible disk management without downtime.
  - Logical volumes can be resized safely while mounted.
  - Proper verification (lsblk, df -h) is essential after every change.

## Why LVM Matters in DevOps
  - Cloud storage expansion
  - Zero-downtime scaling
  - Better disk utilization
  - Production server maintenance
  - CI/CD and application data management
