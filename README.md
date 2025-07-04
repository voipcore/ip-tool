# NWO Lookup - IP Intelligence Tool

A modern, terminal-style IP lookup tool with both GUI and CLI interfaces that provides comprehensive IP geolocation and security analysis. Features a putty-like terminal appearance with colorama styling.

## Features

- 🎯 **Comprehensive IP Analysis** - Get detailed information about any IP address
- 🌍 **Geolocation Data** - Country, region, city, coordinates, timezone
- 🏢 **ISP Information** - Internet Service Provider, organization, AS number
- 🔒 **Security Analysis** - Proxy detection, hosting detection, threat assessment
- 💰 **Additional Data** - Currency, languages, calling codes
- 🎨 **Dual Interface** - Both GUI (tkinter) and CLI versions available
- 🖥️ **Terminal Styling** - Putty-like appearance with colorama color coding
- 📊 **Multiple APIs** - Combines data from multiple sources for accuracy
- ⚡ **Real-time Results** - Fast lookups with colored status indicators
- 🔄 **Interactive Mode** - Continuous lookup capability in CLI version
- 📱 **Cross-Platform** - Works on Windows, Linux, and macOS

## Installation

1. **Clone or download this repository**
2. **Run the setup script:**
   ```bash
   python3 setup.py
   ```
   This will create a virtual environment and install all dependencies.

## Usage

The tool offers both GUI and CLI interfaces:

### Quick Start
```bash
# Run setup first
python3 setup.py

# Start the application (auto-detects best interface)
python3 run.py

# Or use the convenience scripts
./start.sh          # Linux/Mac
start.bat           # Windows
```

### CLI Usage (Recommended)

**Interactive Mode:**
```bash
venv/bin/python nwo_lookup_cli.py
# Enter IPs interactively, type 'quit' to exit
```

**Single Lookup:**
```bash
venv/bin/python nwo_lookup_cli.py 8.8.8.8
```

**Demo Mode:**
```bash
venv/bin/python demo.py
```

### GUI Usage (if tkinter available)
```bash
venv/bin/python nwo_lookup.py
```

1. **Enter an IP address** in the input field
2. **Click "🔍 LOOKUP"** or press Enter
3. **View results** in the terminal-style output
4. **Use "🗑️ CLEAR"** to clear the output

## API Sources

The tool combines data from multiple free APIs:
- **ip-api.com** - Comprehensive geolocation and ISP data
- **ipinfo.io** - Additional location and organization data
- **IPGeolocation** - Extended geographic information

## Requirements

- Python 3.6+
- tkinter (for GUI version - usually included with Python)
- requests (auto-installed by setup.py)
- colorama (auto-installed by setup.py)
- Internet connection for API access

**Note:** The setup.py script will automatically create a virtual environment and install all Python dependencies.

## Sample Output

```
[14:30:25] 🎯 Starting lookup for IP: 8.8.8.8
[14:30:25] ═══════════════════════════════════════════════════════════════════════════════
[14:30:26] 📡 Querying IPStack API...
[14:30:26] ✅ IPStack - Success
[14:30:27] 📡 Querying IPInfo API...
[14:30:27] ✅ IPInfo - Success

🎯 COMPREHENSIVE IP ANALYSIS REPORT
═══════════════════════════════════════════════════════════════════════════════
📍 BASIC INFORMATION
Target IP: 8.8.8.8

🌍 GEOGRAPHIC LOCATION
Country: United States
Region: California
City: Mountain View
Latitude: 37.4056
Longitude: -122.0775
Timezone: America/Los_Angeles

🏢 ISP & NETWORK INFORMATION
ISP: Google LLC
Organization: Google Public DNS
AS Number: AS15169
AS Name: GOOGLE

🔒 SECURITY ANALYSIS
Is Proxy: False
Is Hosting: True
Is Mobile: False

✅ ANALYSIS COMPLETE
```

## Features Explained

### Terminal-Style Interface
- Dark theme with green terminal text
- Putty-like appearance and feel
- Colored output for different information types
- Scrollable output with timestamps

### Comprehensive Data Collection
- Geographic location with coordinates
- ISP and network organization details
- Autonomous System (AS) information
- Security flags (proxy, hosting, mobile)
- Currency and language information

### Modern GUI Elements
- Progress bar for lookup status
- Status indicators
- Easy-to-use input controls
- Professional appearance

## License

This tool is provided for educational and legitimate security research purposes only.

## Disclaimer

This tool is intended for legitimate purposes such as network administration, security research, and educational use. Users are responsible for complying with applicable laws and regulations.
