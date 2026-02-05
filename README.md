# Zonesweep --- Passive Reconnaissance Tool
Version: v1.0.0

Status: Stable Release
Zonesweep is a passive reconnaissance and OSINT automation tool designed
for security researchers, penetration testers, and bug bounty hunters.
It collects intelligence about a target domain using multiple external
data sources and APIs through a simple command-line interface.

## Features
Zonesweep supports modular, passive reconnaissance using individual or
combined switches.

### Subdomain Enumeration
·	Aggregates subdomains from multiple passive sources
### Certificate Transparency
·	Extracts certificate data and related domains using crt.sh
### DNS Intelligence
·	Retrieves DNS and infrastructure information using SecurityTrails
### IP Intelligence
·	Collects IP and service metadata using Censys and other sources
### Historical Recon
·	Collects archived URLs and assets from the Wayback Machine
·	Supports timestamp-based queries
### URL Scanning
·	Retrieves scan data using UrlScan.io
### GitHub Leak Detection
·	Searches for potential credential or configuration leaks
### Technology Stack Detection
·	Identifies technologies used by the target
### Unified Output
·	Consolidates reconnaissance data into structured JSON output
·	Supports combined execution of all modules

## Project Structure
```
.
├── modules
│   ├── apikeys
│   ├── certificates
│   │   └── crtsh
│   ├── dns_info
│   │   └── securitytrails
│   ├── ip_info
│   │   └── censys
│   ├── sub_domains
│   ├── urlscan
│   ├── wayback
│   ├── github_leaks
│   ├── tech_stack
│   └── output
│       └── json_output
├── main.py
|──.env
└── README.md
```

## Installation
```
git clone https://github.com/yourusername/zonesweep.git
cd zonesweep
pip install -r requirements.txt
```

## API Keys Configuration
Zonesweep relies on multiple third-party APIs.
API keys must be configured inside the modules/apikeys directory.

### Example configuration:
```
security_trails={YOUR_API_KEY}
virustotal={YOUR_API_KEY}
shodan={YOUR_API_KEY}
builtwith={YOUR_API_KEY}
way_back_access={YOUR_API_KEY}
way_back_secret={YOUR_API_KEY}
urlscan={YOUR_API_KEY}
alienvault={YOUR_API_KEY}
censys={YOUR_API_KEY}
```

## Usage
### Basic syntax:
```
python main.py example.com [options]
```

### Full command help:
```
usage: main.py [-h] [--subsonly] [--dnsinfo] [--certs] [--ipinfo] [--githubleaks] [--techstack] [--urlscan] [--all] [--output] [--config] [--timestamp TIMESTAMP] Url
Zonesweep a simple passive recon tool
positional arguments:

Url                   Target to recon (google.com)
options:
-h, --help            show this help message and exit
--subsonly            Subdomain enumeration switch
--dnsinfo             DNS enumeration switch
--certs               Certificate switch
--ipinfo              IP information switch
--githubleaks         GitHub leaks enumeration switch
--techstack           Technology stack enumeration switch
--urlscan             UrlScan enumeration switch
--all                 Enable all modules
--output              Output option
--config              Show configured API ke
--timestamp TIMESTAMP Timestamp for Wayback queries
If no arguments are provided, Zonesweep displays the help menu.
```

## Output
Reconnaissance data is returned in structured JSON format.
### The output is designed for easy integration with:
·	OSINT workflows
·	Automation pipelines
·	Further analysis tools

## Roadmap
### Planned enhancements include:
·	Additional OSINT and threat intelligence sources
·	Improved output formats (CSV and enhanced JSON)
·	Asynchronous execution for faster scans
·	Expanded GitHub leak detection
·	Improved error handling and logging
·	Plugin-based module system

## License
This project is released under the MIT License.
See the LICENSE file for more details.

## Disclaimer
Zonesweep is intended for educational purposes and authorized security
testing only.

The author is not responsible for misuse or illegal activity.

## Contributing
Contributions are welcome, including:
·	Bug reports
·	Feature requests
·	New modules
·	Documentation improvements
Please open an issue or submit a pull request on the repository.
