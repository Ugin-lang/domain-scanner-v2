# Recon Automation Tool

A lightweight recon pipeline automation tool for subdomain enumeration, live host detection, and vulnerability scanning.
Built for bug bounty workflow automation using popular security tools.

⚡️ Features

Subdomain enumeration using multiple sources

Automatic deduplication of results

Live host detection via HTTP probing

Vulnerability scanning with templates

Clean output into separate files

Simple interactive CLI interface

🔧 Tools used
This project integrates:

  Subdomain enumeration:
  
    subfinder
    amass
    assetfinder
  Live host checking:
  
    httpx
  Vulnerability scanning:
  
    nuclei

📦 Installation
1. Install dependencies
2.  Make sure you have these tools installed:
      Bash
      subfinder
      amass
      assetfinder
      httpx
      nuclei
4. Clone repository
6. Run script:
   
    python recon.py
  
🚀 Usage
When you start the tool, it will ask for input:

Step 1 — Enter domains

Input 1 domain for scan: example.com

Input 2 domain for scan: target.com

Input 3 domain for scan: end

Step 2 — Output files

You will be prompted for:

Name of file where will save subdomains:

Name of file where will save vulnerabilities:

Step 3 — Automation starts

The tool will:

Collect subdomains

Remove duplicates

Check live hosts

Run vulnerability scan

Save results

📁 Output example

Alive hosts file

https://example.com [200]

https://test.example.com [403]

Vulnerabilities file

high | https://example.com/admin | exposed-panel

critical | https://api.example.com | sql-injection

🧠 Workflow
Plain text

Domains

   ↓
   
Subdomain enumeration (subfinder / amass / assetfinder)

   ↓
   
Deduplication

   ↓
   
HTTP probing (httpx)

   ↓
   
Live hosts

   ↓
   
Vulnerability scanning (nuclei)

   ↓
   
Results saved

⚠️ Disclaimer

This tool is intended for:

Bug bounty programs

Authorized penetration testing

Educational purposes

Do not use it on systems without permission.

🔥 Future improvements

Async processing for speed optimization

Better CLI arguments (-d, -o)

JSON output support

Filtering by severity

Parallel scanning

💬 Author

Built as a learning project for recon automation and bug bounty workflow optimization.
