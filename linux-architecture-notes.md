# Day 02 – Linux Architecture, Processes, and systemd

# The core components of Linux (kernel, user space, init/systemd) ?
- The core components of linux kernal , user space , init/systemd work to together to create powerful operating system.
- It makes linux more secure, scalable and widely used operating system.

# How processes are created and managed ?
- process are created using systemctl (commands like fork() )
- first process that created by kernal is boot process with pid 1.
- process are created using mechanishm like fork().
- process can be in various state like running , sleeping and zombie that are orginized in hierchal structure (parent child relationship)

# What systemd does and why it matters
- syetemd stands for system deamon that uses to running the process in background
- it start the first process with pid 1
- To see all the "background processes" systemd is currently managing, you can run:
   - systemctl list-units --type=service
- systemctl status [name] | 	Shows if the process is running, its PID, and recent logs.
  
# List 5 commands you would use daily
  - mkdir => to create a file or directory.
  - cp/mv/rm => to copy/move/rename/remove file or directory.
  - ip addr => to find ip address
  - ping => to ping a website
  - free / df -h => to see memory/storage used or how much left.
