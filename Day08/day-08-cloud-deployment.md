# Day 08 – Cloud Server Deployment with Nginx (AWS EC2)

## Objective
Deploy a live Nginx web server on a cloud instance and make it accessible from the internet using a public IP.

This task helped me understand real-world cloud server setup, service management, and log handling.

---

## Cloud Setup Details
- Cloud Provider: AWS EC2
- OS: Ubuntu
- Instance Type: t3.micro
- Web Server: Nginx
- Protocol: HTTP (Port 80)

---

## Steps Performed

### 1. Launch EC2 Instance
- Created an EC2 instance on AWS
- Selected Ubuntu AMI
- Chose instance type: `t3.micro`
- Configured Security Group:
  - Allowed inbound traffic on **port 80 (HTTP)** for Nginx

---

### 2. Connect to Instance via SSH
Connected to the instance using SSH from the terminal:

```bash
ssh -i your-private-key.pem ubuntu@<public-dns>
```
### 3. Install Nginx
Installed Nginx web server on the instance:

```
sudo apt update
sudo apt install nginx -y
```
### 4. Verify Nginx Service
Checked whether the Nginx service was running:

```
systemctl status nginx
```
### 5. Access Web Server from Browser

- Copied the public IP of the EC2 instance
- Opened it in a web browser
- Successfully viewed the “Welcome to Nginx” page
- Modified the default HTML page for a better UI

### 6. View Nginx Access Logs
Navigated to the Nginx log directory and viewed access logs:

```
sudo cat /var/log/nginx/access.log
```

### 7. Extract and Save Logs to File
Copied the access logs to a file in the home directory:

```
sudo cp /var/log/nginx/acces.log ~/nginx-logs.txt
```

### 8. Verify Log File Creation
Checked the home directory to confirm the log file was created:
```
ls
```
File created:
 - nginx-logs.txt
   
#### Challenges Faced
- Faced permission denied error while accessing Nginx logs
- Resolved the issue using sudo
  
#### What I Learned
 - How to launch and configure a cloud server
 - How to deploy and verify a web service
 - How security groups control network access
 - How to view and extract server logs
 -  Importance of logs in real-world troubleshooting

#### Conclusion
This task gave me hands-on experience with deploying a real web server on the cloud and understanding how services and logs are managed in a production-like environment.
