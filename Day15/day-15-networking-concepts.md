# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

---

## Task 1: DNS – How Names Become IPs

### What happens when we type google.com?

1. Browser checks local cache.
2. If not found, it queries DNS server.
3. DNS resolves the domain name to an IP address.
4. Browser sends HTTP/HTTPS request to that IP.

---

### DNS Record Types

- A – Maps domain to IPv4
- AAAA – Maps domain to IPv6
- CNAME – Alias of another domain
- MX – Mail exchange server
- NS – Name server

---

### dig google.com Output
```
google.com. 233 IN A 142.251.34.206
```


- A Record IP: 142.251.34.206
- TTL: 233 seconds

TTL (Time To Live) defines how long this DNS record stays cached.

---

## Task 2: IP Addressing

IPv4 is a 32-bit address divided into 4 octets.

Example:
192.168.1.10

Private IP Ranges:
- 10.0.0.0/8
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0/16

Public IP Example:
8.8.8.8

---

## Task 3: CIDR & Subnetting

| CIDR | Subnet Mask       | Total IPs | Usable Hosts |
|------|------------------|-----------|--------------|
| /24  | 255.255.255.0    | 256       | 254          |
| /16  | 255.255.0.0      | 65536     | 65534        |
| /28  | 255.255.255.240  | 16        | 14           |

Why Subnet?
- Reduce broadcast domain
- Better IP management
- Improve security
- Network segmentation

---

## Task 4: Ports

### Common Ports

| Port | Service  |
|------|----------|
| 22   | SSH      |
| 80   | HTTP     |
| 443  | HTTPS    |
| 53   | DNS      |
| 3306 | MySQL    |
| 6379 | Redis    |
| 27017| MongoDB  |

---

### ss Command Output

SSH:
```
0.0.0.0:22
users:(("sshd",pid=796))
```


NGINX:
```
0.0.0.0:80
users:(("nginx",pid=605))
```


This confirms:
- SSH is running on port 22
- NGINX is running on port 80

---

## Task 5: Scenario

### curl http://myapp.com:8080

Involves:
- DNS resolution
- IP address
- Port 8080
- TCP connection
- HTTP protocol

---

### App can't reach 10.0.1.50:3306

Check:
- Is MySQL running?
- Is port 3306 open?
- Firewall / Security groups?
- Network connectivity?
- Routing issues?

---

## What I Learned

1. DNS converts names into IP addresses.
2. CIDR defines network vs host bits.
3. Ports allow multiple services on a single machine.
4. `ss` helps verify listening services.
5. TTL controls DNS caching behavior.

