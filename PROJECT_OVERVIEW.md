# NWO Lookup - IP Intelligence Tool
## 🎯 Project Overview

A **professional-grade IP lookup tool** featuring both GUI and CLI interfaces with putty-style terminal appearance and comprehensive IP intelligence capabilities.

## ✨ Key Features Implemented

### 🎨 **Modern Interface Design**
- **Dual Interface**: GUI (tkinter) + CLI versions for maximum compatibility
- **Putty-style Terminal**: Dark theme with colorama color coding
- **Professional Banner**: ASCII art header with tool branding
- **Real-time Status**: Colored status indicators and progress feedback

### 🌍 **Comprehensive IP Analysis**
- **Geographic Location**: Country, region, city, coordinates, timezone
- **ISP Information**: Internet Service Provider, organization, AS number
- **Security Analysis**: Proxy detection, hosting detection, mobile detection
- **Network Details**: Autonomous System (AS) information
- **Additional Data**: Currency, country codes, postal codes

### 📊 **Multi-API Integration**
- **IP-API.com**: Primary geolocation and ISP data
- **IPInfo.io**: Additional location and organization data
- **Data Fusion**: Combines multiple sources for accuracy
- **Error Handling**: Graceful fallback when APIs are unavailable

### 🔧 **Technical Excellence**
- **Virtual Environment**: Automatic setup with `setup.py`
- **Cross-Platform**: Works on Windows, Linux, macOS
- **Input Validation**: IP address format validation
- **Thread Safety**: Non-blocking API calls in GUI version
- **Error Recovery**: Comprehensive error handling and reporting

## 📁 Project Structure

```
nwo-ip-lookup/
├── 🖥️  nwo_lookup.py       # GUI version (tkinter)
├── 💻  nwo_lookup_cli.py   # CLI version (recommended)
├── 🚀  run.py             # Smart launcher (tries GUI, falls back to CLI)
├── ⚙️  setup.py           # Virtual environment setup
├── 🎬  demo.py            # Demo with multiple IP examples
├── 📋  requirements.txt   # Python dependencies
├── 🪟  start.bat          # Windows launcher
├── 🐧  start.sh           # Linux/Mac launcher
├── 📖  README.md          # Comprehensive documentation
└── 📁  venv/              # Virtual environment (auto-created)
```

## 🎮 Usage Examples

### 🔍 **Single IP Lookup**
```bash
venv/bin/python nwo_lookup_cli.py 8.8.8.8
```

### 🔄 **Interactive Mode**
```bash
venv/bin/python nwo_lookup_cli.py
# Enter IPs interactively, type 'quit' to exit
```

### 🎬 **Demo Mode**
```bash
venv/bin/python demo.py
# Analyzes Google DNS, Cloudflare DNS, OpenDNS
```

### 🖥️ **GUI Mode** (if tkinter available)
```bash
venv/bin/python nwo_lookup.py
```

## 🎨 Visual Design

### 🎨 **Color Scheme**
- **Green**: Success messages, positive status
- **Red**: Errors, security warnings
- **Yellow**: Processing, warnings
- **Cyan**: Headers, section titles
- **White**: Regular data
- **Gray**: Separators, raw data

### 📱 **Terminal Style**
- **Dark Background**: `#0c0c0c` (putty-like)
- **Green Text**: `#00ff00` (classic terminal)
- **Professional Borders**: ASCII box drawing characters
- **Timestamped Output**: `[HH:MM:SS]` format

## 📊 Sample Output

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                  ⚡ NWO LOOKUP - IP Intelligence Tool ⚡                     ║
║                 Advanced IP Geolocation & Security Analysis                ║
╚══════════════════════════════════════════════════════════════════════════════╝

[19:11:24] 🎯 Starting lookup for IP: 8.8.8.8
════════════════════════════════════════════════════════════════════════════════
[19:11:24] 📡 Querying IP-API API...
[19:11:24] ✅ IP-API - Success
[19:11:24] 📡 Querying IPInfo API...
[19:11:24] ✅ IPInfo - Success

🎯 COMPREHENSIVE IP ANALYSIS REPORT
════════════════════════════════════════════════════════════════════════════════
📍 BASIC INFORMATION
Target IP: 8.8.8.8

🌍 GEOGRAPHIC LOCATION
Country: United States
Region: Virginia
City: Ashburn
Latitude: 39.03
Longitude: -77.5
Timezone: America/New_York

🏢 ISP & NETWORK INFORMATION
ISP: Google LLC
Organization: Google Public DNS
AS Number: AS15169
AS Name: GOOGLE

🔒 SECURITY ANALYSIS
Is Proxy: False
Is Hosting: True
Is Mobile: False

💰 ADDITIONAL INFORMATION
Currency: USD
Country Code: US
Continent Code: NA

✅ ANALYSIS COMPLETE
════════════════════════════════════════════════════════════════════════════════
```

## 🛠️ Technical Implementation

### 🏗️ **Architecture**
- **Modular Design**: Separate GUI and CLI implementations
- **API Abstraction**: Clean separation of data sources
- **Error Handling**: Comprehensive exception management
- **Threading**: Non-blocking operations in GUI

### 🔌 **API Integration**
- **HTTP Requests**: Using `requests` library
- **JSON Parsing**: Structured data extraction
- **Rate Limiting**: Respectful API usage
- **Timeout Handling**: Network error recovery

### 🎨 **UI/UX Features**
- **Progress Indicators**: Visual feedback during lookups
- **Input Validation**: Real-time IP format checking
- **Status Messages**: Clear operation feedback
- **Keyboard Shortcuts**: Enter key for quick lookup

## 🚀 Quick Start

1. **Setup**: `python3 setup.py`
2. **Run**: `venv/bin/python nwo_lookup_cli.py`
3. **Test**: Enter `8.8.8.8` to see Google DNS analysis
4. **Demo**: `venv/bin/python demo.py` for full showcase

## 🎯 Achievement Summary

✅ **Professional Terminal UI** with putty-style appearance
✅ **Dual Interface Support** (GUI + CLI)
✅ **Comprehensive IP Intelligence** from multiple APIs
✅ **Modern Python Architecture** with virtual environments
✅ **Cross-Platform Compatibility** (Windows/Linux/Mac)
✅ **Beautiful Color-Coded Output** using colorama
✅ **Production-Ready Code** with error handling
✅ **Interactive Demo Mode** with real examples
✅ **Professional Documentation** and setup scripts
✅ **Security Analysis Features** (proxy/hosting detection)

## 🔒 Security & Ethics

This tool is designed for **legitimate purposes only**:
- Network administration
- Security research
- Educational use
- Troubleshooting connectivity issues

Users are responsible for complying with applicable laws and regulations.

---

**Built with ❤️ using Python, colorama, requests, and tkinter**
