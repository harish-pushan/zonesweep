# 🔍 Zonesweep — Passive Reconnaissance Tool

Zonesweep is a **passive reconnaissance and OSINT automation tool** designed for security researchers, penetration testers, and bug bounty hunters. It gathers intelligence about a target domain using multiple external data sources and APIs through a simple command-line interface.

🚧 **Project Status:**  
Zonesweep is in **active development** and is currently **in the process of completion**. Features, arguments, and module behavior may change as development continues.

---

## 🚀 Features

Zonesweep supports modular, passive reconnaissance using individual or combined switches.

### 🌐 Subdomain Enumeration
- Aggregates subdomains from multiple sources

### 📜 Certificate Transparency
- Extracts certificates and related domains using **crt.sh**

### 🧭 DNS Intelligence
- Fetches DNS and infrastructure data using **SecurityTrails**

### 🌍 IP Intelligence
- Retrieves IP and service metadata using **Censys**

### 🕰️ Historical Recon
- Collects archived URLs and assets using the **Wayback Machine**
- Supports timestamp-based queries

### 🔎 URL Scanning
- Retrieves scan results using **UrlScan.io UUIDs**

### 📦 Unified Output
- Collects and outputs recon data in structured JSON format
- Supports running all modules together

---

## 📁 Project Structure
.
├── modules
│ ├── apikeys
│ ├── certificates
│ │ └── crtsh
│ ├── dns_info
│ │ └── securitytrails
│ ├── ip_info
│ │ └── censys
│ ├── sub_domains
│ ├── urlscan
│ ├── wayback
│ └── output
│ └── json_output
├── main.py
└── README.md


---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/zonesweep.git
cd zonesweep
pip install -r requirements.txt

--- 

🔑 API Keys Configuration

Zonesweep relies on multiple third-party APIs.
API keys must be configured inside the modules/apikeys directory.

Supported services include:

    SecurityTrails

    Censys

    UrlScan.io

---

▶️ Usage
python main.py example.com [options]

Available Options
Argument	Description
--subsonly	Run subdomain enumeration only
--dnsinfo	Fetch DNS intelligence
--certs	Fetch certificate transparency data
--ipinfo	Fetch IP intelligence
--urlscan	Fetch UrlScan results
--timestamp <int>	Fetch Wayback data for a specific timestamp
--all	Run all available reconnaissance modules
--config	Display configured API keys
--output	Output format (planned feature)

If no arguments are provided, Zonesweep will automatically display the help menu.

---

📤 Output

Recon data is returned in structured JSON format

Designed for easy integration with:

OSINT workflows

Automation pipelines

Further analysis tools

---

🔮 Roadmap

Zonesweep is under active development. Planned enhancements include:

Additional OSINT and threat intelligence sources

Improved output formatting (CSV / JSON support)

Asynchronous execution for faster scans

GitHub leak detection

Better error handling and logging

Plugin-based module system

Expect frequent updates and possible breaking changes.

---

⚠️ Disclaimer

Zonesweep is intended for educational purposes and authorized security testing only.
The author is not responsible for misuse or illegal activity.

---

🤝 Contributing

Contributions are welcome:

Bug reports

Feature requests

New modules

Documentation improvements

Feel free to open an issue or submit a pull request.

---

⭐ Support

If you find Zonesweep useful:

Star the repository ⭐

Share feedback

Suggest new features


---

