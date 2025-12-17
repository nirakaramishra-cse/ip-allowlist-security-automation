
# IP Allowlist Security Automation (Python)

This project demonstrates a Python-based security automation workflow used to
manage IP allowlists by removing unauthorized addresses. It reflects a
SOC / Blue Team use case where automation is applied to enforce access control
and reduce human error in security configurations.

The project focuses on practical security automation rather than complex
algorithms, highlighting how simple scripting can significantly improve
security operations.

---

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

## Security Use Case (SOC Perspective)

From a Security Operations Center (SOC) perspective, this automation supports:

- Enforcement of access control policies
- Reduction of configuration drift
- Faster response to access revocation requests
- Minimization of manual errors in security files
- Consistent and repeatable security operations

This type of scripting is commonly used by SOC analysts and security engineers
to support day-to-day operational security tasks.

---

## Tools and Technologies Used

- Python 3
- File handling (`open`, read, write)
- Lists and string manipulation
- Conditional logic and loops
- Basic error prevention techniques

---

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

---

## How the Automation Works

1. The script reads the list of currently allowed IP addresses.
2. It reads a second list containing IPs that must be removed.
3. Each IP in the removal list is checked against the allowlist.
4. Matching IPs are removed safely without causing errors.
5. The updated allowlist is written back to the file.

This ensures that only authorized IP addresses retain access.

---

## Why This Project Matters

Many entry-level security projects focus on scanning or analysis only. This
project demonstrates **security automation**, which is a critical skill for
modern SOC and Blue Team roles.

It shows the ability to:
- Translate security requirements into code
- Automate repetitive security tasks
- Apply least-privilege principles programmatically
- Think operationally about security controls

---

## Intended Audience

- SOC Analysts
- Blue Team Practitioners
- Cybersecurity students
- Anyone learning security automation with Python

---

## Author

**Nirakar Mishra**  
Cybersecurity Student | SOC & Blue Team Focused

#### **Connect with me:**

- 🌐 [Portfolio](https://nirakaramishra-cse.github.io/Portfolio)

---


