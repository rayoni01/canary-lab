# Canary Lab — Deception Detection with Thinkst Canarytokens
**Author:** Brian Pfeka | @rayoni_ir | SOC Analyst | Randburg, RSA
**Purpose:** Research for Solutions Engineer (Deception/Detection) — Thinkst Applied Research

### Overview
Lab to understand how attackers enumerate after initial access and where deception provides high-fidelity alerts vs noisy SIEM/EDR.

### Lab Setup
- Attacker: Kali Linux 2024.3 (VMware) - 192.168.56.101
- Victim: Windows 10 Pro (Finance user)
- File Share: Windows Server 2019 - `\\FILE-SRV\Finance$\`
- Monitoring: Canarytokens.org, Wireshark, Sysmon, Gmail alerts

### Linux Attacker Side (Kali 2024.3) — Commands Executed

```bash
# 1. Network discovery — finding file server
nmap -sV 192.168.56.0/24
smbclient -L //192.168.56.102 -U guest

# 2. Initial foothold — simulated phishing (macro) already gave low-priv shell
whoami
id
pwd
ls -la /home/finance/Documents/

# 3. Credential hunting — T1552.001
cat /home/finance/Documents/config.env
grep -r "AKIA" /home/finance/ 2>/dev/null
grep -r "aws_access" / --include="*.env" 2>/dev/null

# 4. Triggering the canaries
cat "Passwords_2024.docx"
ls -la /mnt/finance-share/Admin-Backups/
aws sts get-caller-identity --profile canary

# 5. Post-trigger check
tail -f /var/log/syslog | grep canary
