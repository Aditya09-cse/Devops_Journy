# Day 19 – Shell Scripting Project  
## Log Rotation, Backup & Scheduled Maintenance

---

## Task 1: Log Rotation Script

### log_rotate.sh

- Compress `.log` files older than 7 days
- Delete `.gz` files older than 30 days
- Print count of affected files
- Exit if directory doesn't exist

### Sample Output

Compressed 0 log files.
Deleted 0 old archives.

---

## Task 2: Server Backup Script

### backup.sh

- Takes source and destination as arguments
- Creates timestamped archive
- Verifies creation
- Prints size
- Deletes backups older than 14 days

### Sample Output

Backup created: ./backups/backup-2026-02-16.tar.gz (4.0K)

---

## Task 3: Cron Entries

# Run log rotation daily at 2 AM
0 2 * * * /home/ubuntu/shell-script/log_rotate.sh /myapp

# Run backup every Sunday at 3 AM
0 3 * * 0 /home/ubuntu/shell-script/backup.sh /data /backups

# Health check every 5 minutes
*/5 * * * * /home/ubuntu/shell-script/server_check.sh

# Maintenance script daily at 1 AM
0 1 * * * /home/ubuntu/shell-script/maintenance.sh

---

## Task 4: Maintenance Script

- Calls log rotation
- Calls backup
- Logs output with timestamps

---

## What I Learned

1. How to automate system maintenance tasks
2. How to handle errors properly in shell scripts
3. How cron scheduling works in real-world DevOps
