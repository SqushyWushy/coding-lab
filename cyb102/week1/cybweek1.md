# **Week 1: Blue Team Cybersecurity Fundamentals**

---

# CYB102 – Week 1 Notes: Blue Team Defense Concepts

## 🔵 What is a Blue Team?

- Defends an organization's information systems.
- Maintains security posture against real and simulated attacks.
- Goal: detect, respond, and prevent breaches.

---

## 🛠️ Blue Team Activities

- Analyze security posture of the organization.
- Digital footprint analysis.
- DNS audits and firewall configuration.
- Monitor network activity.
- Set up endpoint security software.
- Enforce least-privilege access.

---

## 🧠 Key Skills for Blue Team Members

- **Risk Assessment**: Identify valuable assets and vulnerabilities.
- **Threat Intelligence**: Stay updated on known attack methods (TTPs).
- **Hardening Techniques**: Secure systems by fixing weak points.
- **Monitoring & Detection**: Use tools like:
  - Packet sniffers (e.g., Wireshark)
  - SIEM (e.g., Splunk, Wazuh)
  - IDS/IPS (e.g., Snort)

---

## 🏢 What is a SOC (Security Operations Center)?

- A team/location where Blue Team operations are coordinated.
- Roles: SOC analysts, malware analysts, network engineers.
- Responsibilities:
  - Monitor systems for threats
  - Analyze anomalies
  - Isolate and remediate incidents

### ⚙️ SOC Functional Areas

- **Monitor**: Constantly observe logs and alerts.
- **Hunt**: Proactively search for threats.
- **Triage**: Prioritize alerts by severity.
- **Respond**: Take action against confirmed threats.
- **Remediate**: Fix the root cause.

---

## 🧰 Real-World SOC Tools

- **Wazuh**: SIEM for detecting and alerting on security events.
- **TheHive**: SIRP tool for tracking security incidents.
- **Cortex**: Analyzes event data and observables to guide response.

---

## 🧠 What is a Cyber Fusion Center?

- Next-gen SOC that adds collaboration and coordination.
- Combines:
  - Security Operations
  - Crisis Response
  - Physical Security
  - IT Operations
- Purpose:
  - Break down silos
  - Reduce response time
  - Improve threat detection and mitigation

---

## 🛡️ NIST Cybersecurity Framework (CSF)

- Published by the National Institute of Standards and Technology.
- **Voluntary**, flexible standard used by many organizations.
- Helps orgs:
  - Understand and manage cyber risk
  - Set priorities
  - Improve long-term resilience

### 🧪 NIST System Monitoring

- **External** monitoring: Look at events at system boundaries.
- **Internal** monitoring: Look at what’s happening _inside_ the system.

#### 🔍 Monitoring Tools

- Intrusion Detection/Prevention Systems (IDPS)
- Malware protection software
- Vulnerability scanners
- Audit log monitors
- Network monitoring systems

---

## ✅ Week 1 Lab: “It Wasn’t Me”

### Goal: Identify who sent a sensitive email.

Steps:

1. Use Wireshark to analyze a `.pcap` network capture file.
2. Find the source IP from the SMTP traffic.
3. Cross-reference the IP in a `dhcp.txt` log to get the host device name.
4. Look into `security_log.rtf` to find which user was logged into that host at the time.

Conclusion: Identify the rogue user and report your findings.

---

> 🔁 "Blue Teamers don’t just block threats — they investigate digital evidence to build the full story."
