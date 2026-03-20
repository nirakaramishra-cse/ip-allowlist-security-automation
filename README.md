
# IP Allowlist Security Automation Tool (Python)

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Focus-SOC_Automation-critical?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-success?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Security-IP_Allowlisting-important?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---


## 📌 Overview

This project is a Python-based security automation tool that manages IP allowlists by removing unauthorized addresses. It simulates real-world SOC workflows where automation is used to enforce access control and reduce manual errors.


## ✨ Key Features

- Automates IP allowlist updates  
- Removes unauthorized IP addresses safely  
- Enforces least-privilege access control  
- Reduces manual errors in configuration  
- Simple and reusable security automation script


## 🔐 Security Concepts

- Access Control  
- Least Privilege Principle  
- Security Automation  
- Configuration Management  
- Operational Security (SecOps)


## Project Overview

IP allowlisting is a common access control mechanism used to restrict access to
systems and services. Manually maintaining allowlists can be error-prone and
inefficient, especially in dynamic environments.

This project automates the process of:
- Reading an existing IP allowlist
- Identifying IP addresses that should no longer have access
- Removing unauthorized IPs safely and consistently
- Writing the updated allowlist back to a file

The automation helps ensure that access policies remain accurate and aligned
with the principle of least privilege.

---

## 🎯 Use Case

This project demonstrates how SOC analysts automate repetitive security tasks such as updating access control lists. It reflects real-world scenarios where quick and accurate removal of unauthorized access is critical for maintaining system security.



## Tools and Technologies Used

- Python 3
- File handling (`open`, read, write)
- Lists and string manipulation
- Conditional logic and loops
- Basic error prevention techniques



## Project Structure

```

ip-allowlist-security-automation/
│
├── README.md
│
├── data/
│   ├── allow_list.txt
│   └── remove_list.txt
│
├── src/
│   └── update_allowlist.py
│
└── references.md

```

## ▶️ How to Run

1. Clone the repository  
2. Navigate to the project folder  
3. Run the script:

python src/update_allowlist.py


---

## 📈 Impact

- Improves accuracy of access control management  
- Reduces time required for manual updates  
- Minimizes risk of unauthorized access  
- Demonstrates practical security automation skills


## 📄 Example

Allowlist:
192.168.1.1  
192.168.1.2  

Remove list:
192.168.1.2  

Updated allowlist:
192.168.1.1  




