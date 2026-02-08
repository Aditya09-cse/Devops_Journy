# Day 11 – File Ownership in Linux (chown & chgrp)

## Overview
Today I practiced Linux file ownership concepts using `chown` and `chgrp`.
The focus was on understanding how users and groups control access to files
and directories — a core concept in DevOps and Linux system administration.

---

## Files & Directories Created

### Files
- notes.txt
- team-notes.txt
- project-config.yaml
- heist-project/vault/gold.txt
- heist-project/plans/strategy.conf
- bank-heist/access-codes.txt
- bank-heist/blueprints.pdf
- bank-heist/escape-plan.txt

### Directories
- app-logs/
- heist-project/
- heist-project/vault/
- heist-project/plans/
- bank-heist/

---

## Ownership Changes Performed

### File Ownership (`chown`)
- `project-config.yaml` → `professor:heist-team`
- `access-codes.txt` → `tokyo:vault-team`
- `blueprints.pdf` → `berlin:tech-team`
- `escape-plan.txt` → `nairobi:vault-team`

### Directory Ownership
- `app-logs/` → `berlin:heist-team`
- `heist-project/` (recursive) → `professor:planners`

---

## Commands Used

```bash
ls -l
sudo chown user filename
sudo chgrp group filename
sudo chown user:group filename
sudo chown -R user:group directory/
ls -lR directory/
