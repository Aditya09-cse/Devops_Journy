# Linux Troubleshooting Runbook – Day 05


---

## Environment Basics

```bash
uname -a
```
Ubuntu 24.04 LTS running on AWS kernel (6.14.0-1018-aws)

```
cat /etc/os-release
```
Ubuntu 24.04.3 LTS (Noble)

## Filesystem Sanity
```
mkdir /tmp/runbook-demo
cp /etc/hosts /tmp/runbook-demo/hosts-copy && ls -l /tmp/runbook-demo
```
Filesystem read/write working correctly.

## Snapshot: CPU & Memory
```
pidof nginx
```
Multiple nginx worker processes running.

```
ps -o pid,pcpu,pmem,comm -p 600
```
nginx using ~0% CPU and memory — healthy.

```
free -h
```
~527MB memory available, no swap usage.

## Snapshot: Disk & IO
```
df -h
```
Root filesystem at 38% usage — safe.

```
sudo du -sh /var/log
```
Logs size ~66MB — no log explosion.

## Logs Reviewed
```
journalctl -u nginx -n 20
```
Service restarts logged, all restarts successful, no errors.
