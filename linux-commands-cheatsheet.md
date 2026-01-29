# 🐧 Cheetsheet for linux commands
# 📁 File System
  - ls => list files
  - ls -l => detailes list (owner of file , size of file)
  - ls -a => show hidden files
  - pwd => print current directory
  - cd dir => change directory
  - cd .. => go oee level up
  - mkdir dir => create directiry
  - rm file => to remove/delete file
  - cp src dst => copy file
  -  mv src dst => to move/rename file
  -  touch file => create empty file
  -  cat file => print file content
  -  chmod +x file => to change file permission
  -  df -h => disk usage by file system
  -  df -sh dir => folder size
  -  free => used to display used and free memory of your system

# ⚙️ Process Management
  - ps aux => list all process.
  - top => live process monitor
  - htop => interactive monitor ( better than top)
  - kill PID => stop process ( by signal SIGTERM)
  - kill -9 PID => force kill ( by signal SIGKILL)
  - pKill name => kill by processs name
  - nohup cmd & => run even after the logout

# 🌐 Networking / Troubleshooting
  - ip a => show ip address
  - ping host => test connectivity
  - curl url => fetch url / test HTTP
  - wget url => download file
  - ss -tulnp => show listening ports
  - netstat -ant => show tcp connections
  - ssh user@host => remote login
  - scp file user@host:/path
  - nslookup domain => DNS lookup
  - traceroute host => path to host

# Why This Matters for DevOps
Real production issues are solved at the command line.

The faster you can inspect logs and network issues, the faster you can:
  - Restore service
  - Reduce downtime
  - Gain trust as an operator
  
