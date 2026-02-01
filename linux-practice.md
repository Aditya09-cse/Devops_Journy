# Day 04 – Linux Practice: Processes and Services

Date: [02-02-2026]

OS: Ubuntu Linux

Service Inspected: Nginx

## 🔹 Process Checks

### List running processes
```bash
ps aux | head -n 10
```
Observation :
 - Dispaly all active/running process
 - pid 1 belong to systemd/init

### Monitor processes in real time
```bash
top
```
Observation:
 - Show CPU and Memory usage
 - Helps identify high resource usage process

## 🔹 Service Checks

### Check nginx service status 
```bash
systemctl status nginx
```
Observation :
  - Loaded enabled(start automativally boot)
  - active - running
  - Shows Main PID and worker processes

### List active services
```bash
systemctl list-units --type-service | grep nginx
```
Observation :
  - nginx.service is active and loaded

## 🔹 Log Checks
  
###  View recent service logs
```bash
journalctl -u nginx -n 10
```
Observation :
  - Shows recent start/stop events
  - Useful for debugging failures
    
### Monitor logs live
```bash
journalctl -u nginx -f
```
Observation :
  - Dispaly logs in real time

## 🔹 Mini Troubleshooting Steps

###  Scenario: Website not loading
```bash
pgrep nginx
systemctl status nginx
journalctl -u nginx -xe
sudo systemctl restart nginx
curl localhost
```
Result :
  - Serive restarted successfully
  - website responded locally

## 🔹 Summary
 - Today I practiced Linux process monitoring, service management, and log analysis.
I inspected the Nginx service and followed a troubleshooting flow:
process → service → logs → restart.

```
Done ✅  
```


