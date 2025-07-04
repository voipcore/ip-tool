#!/usr/bin/env python3
"""
NWO IP Lookup Tool - Command Line Version
A modern IP lookup tool with terminal-style interface using colorama
"""

import requests
import json
import ipaddress
import time
from datetime import datetime
import sys
import os

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    # Fallback color class
    class Fore:
        GREEN = RED = YELLOW = CYAN = WHITE = BLUE = MAGENTA = RESET = ""
    class Style:
        BRIGHT = DIM = RESET_ALL = ""

class NWOLookupCLI:
    def __init__(self):
        self.colors = {
            'green': Fore.GREEN + Style.BRIGHT,
            'red': Fore.RED + Style.BRIGHT,
            'yellow': Fore.YELLOW + Style.BRIGHT,
            'cyan': Fore.CYAN + Style.BRIGHT,
            'white': Fore.WHITE,
            'blue': Fore.BLUE + Style.BRIGHT,
            'magenta': Fore.MAGENTA + Style.BRIGHT,
            'reset': Style.RESET_ALL
        }

    def print_colored(self, message, color="white"):
        """Print colored message to terminal"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        color_code = self.colors.get(color, self.colors['white'])
        print(f"{color_code}[{timestamp}] {message}{self.colors['reset']}")

    def print_banner(self):
        """Print application banner"""
        banner = f"""
{self.colors['cyan']}╔══════════════════════════════════════════════════════════════════════════════╗
║                          ⚡ NWO LOOKUP - IP Intelligence Tool ⚡             ║
║                         Advanced IP Geolocation & Security Analysis          ║
╚══════════════════════════════════════════════════════════════════════════════╝{self.colors['reset']}
"""
        print(banner)

    def print_separator(self, char="═", length=80):
        """Print separator line"""
        print(f"{self.colors['white']}{char * length}{self.colors['reset']}")

    def validate_ip(self, ip_string):
        """Validate IP address format"""
        try:
            ipaddress.ip_address(ip_string)
            return True
        except ValueError:
            return False

    def get_ip_info(self, ip):
        """Get IP information from multiple APIs"""
        self.print_colored(f"🎯 Starting lookup for IP: {ip}", "cyan")
        self.print_separator()

        # Multiple API sources for comprehensive data
        apis = [
            {
                'name': 'IP-API',
                'url': f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query',
                'free': True
            },
            {
                'name': 'IPInfo',
                'url': f'https://ipinfo.io/{ip}/json',
                'free': True
            }
        ]

        all_data = {}

        for api in apis:
            try:
                self.print_colored(f"📡 Querying {api['name']} API...", "yellow")
                response = requests.get(api['url'], timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    all_data[api['name']] = data
                    self.print_colored(f"✅ {api['name']} - Success", "green")
                else:
                    self.print_colored(f"❌ {api['name']} - Error: {response.status_code}", "red")

            except Exception as e:
                self.print_colored(f"❌ {api['name']} - Exception: {str(e)}", "red")

        return all_data

    def display_results(self, ip, data):
        """Display comprehensive IP lookup results"""
        print()
        self.print_separator()
        self.print_colored("🎯 COMPREHENSIVE IP ANALYSIS REPORT", "cyan")
        self.print_separator()

        # Basic Info
        self.print_colored("📍 BASIC INFORMATION", "yellow")
        self.print_colored(f"Target IP: {ip}", "white")

        # Compile data from all sources
        compiled_data = self._compile_data(data)

        if compiled_data:
            # Geographic Information
            print()
            self.print_colored("🌍 GEOGRAPHIC LOCATION", "yellow")
            geo_fields = [
                ('country', 'Country'),
                ('region', 'Region'),
                ('city', 'City'),
                ('latitude', 'Latitude'),
                ('longitude', 'Longitude'),
                ('timezone', 'Timezone'),
                ('postal_code', 'Postal Code'),
                ('continent', 'Continent')
            ]

            for field, display_name in geo_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_colored(f"{display_name}: {compiled_data[field]}", "white")

            # ISP Information
            print()
            self.print_colored("🏢 ISP & NETWORK INFORMATION", "yellow")
            isp_fields = [
                ('isp', 'ISP'),
                ('organization', 'Organization'),
                ('as_number', 'AS Number'),
                ('as_name', 'AS Name')
            ]

            for field, display_name in isp_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_colored(f"{display_name}: {compiled_data[field]}", "white")

            # Security Analysis
            print()
            self.print_colored("🔒 SECURITY ANALYSIS", "yellow")
            security_fields = [
                ('is_proxy', 'Is Proxy'),
                ('is_hosting', 'Is Hosting'),
                ('is_mobile', 'Is Mobile')
            ]

            for field, display_name in security_fields:
                if field in compiled_data:
                    value = compiled_data[field]
                    color = "red" if value and isinstance(value, bool) else "green"
                    self.print_colored(f"{display_name}: {value}", color)

            # Additional Information
            print()
            self.print_colored("💰 ADDITIONAL INFORMATION", "yellow")
            additional_fields = [
                ('currency', 'Currency'),
                ('country_code', 'Country Code'),
                ('continent_code', 'Continent Code')
            ]

            for field, display_name in additional_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_colored(f"{display_name}: {compiled_data[field]}", "white")
        else:
            self.print_colored("❌ No data retrieved from APIs", "red")

        # Raw data section (compact)
        if data:
            print()
            self.print_colored("📊 RAW API RESPONSES (Summary)", "yellow")
            for api_name, api_data in data.items():
                self.print_colored(f"\n--- {api_name} ---", "cyan")
                # Show only key fields to avoid clutter
                if api_name == 'IP-API' and api_data.get('status') == 'success':
                    key_fields = ['query', 'country', 'regionName', 'city', 'isp', 'org', 'as']
                    for field in key_fields:
                        if field in api_data:
                            self.print_colored(f"  {field}: {api_data[field]}", "white")
                elif api_name == 'IPInfo':
                    key_fields = ['ip', 'city', 'region', 'country', 'org', 'postal']
                    for field in key_fields:
                        if field in api_data:
                            self.print_colored(f"  {field}: {api_data[field]}", "white")

        print()
        self.print_separator()
        self.print_colored("✅ ANALYSIS COMPLETE", "green")
        self.print_separator()

    def _compile_data(self, data):
        """Compile data from multiple API sources"""
        compiled = {}

        # Process ip-api.com data
        if 'IP-API' in data and data['IP-API'].get('status') == 'success':
            d = data['IP-API']
            compiled.update({
                'country': d.get('country'),
                'country_code': d.get('countryCode'),
                'region': d.get('regionName'),
                'city': d.get('city'),
                'latitude': d.get('lat'),
                'longitude': d.get('lon'),
                'timezone': d.get('timezone'),
                'postal_code': d.get('zip'),
                'continent': d.get('continent'),
                'continent_code': d.get('continentCode'),
                'isp': d.get('isp'),
                'organization': d.get('org'),
                'as_number': d.get('as', '').split(' ')[0] if d.get('as') else None,
                'as_name': d.get('asname'),
                'is_proxy': d.get('proxy', False),
                'is_hosting': d.get('hosting', False),
                'is_mobile': d.get('mobile', False),
                'currency': d.get('currency')
            })

        # Process ipinfo.io data (fill gaps)
        if 'IPInfo' in data:
            d = data['IPInfo']
            if not compiled.get('country'):
                compiled['country'] = d.get('country')
            if not compiled.get('region'):
                compiled['region'] = d.get('region')
            if not compiled.get('city'):
                compiled['city'] = d.get('city')
            if not compiled.get('postal_code'):
                compiled['postal_code'] = d.get('postal')
            if not compiled.get('organization'):
                compiled['organization'] = d.get('org')

        return compiled

    def interactive_mode(self):
        """Run in interactive mode"""
        self.print_banner()
        self.print_colored("Welcome to NWO Lookup - IP Intelligence Tool", "green")
        self.print_colored("Enter 'quit' or 'exit' to terminate the application", "cyan")
        print()

        while True:
            try:
                # Get IP input
                ip_input = input(f"{self.colors['yellow']}Enter IP address to lookup: {self.colors['reset']}").strip()

                if ip_input.lower() in ['quit', 'exit', 'q']:
                    self.print_colored("Goodbye! 👋", "cyan")
                    break

                if not ip_input:
                    self.print_colored("Please enter a valid IP address", "red")
                    continue

                if not self.validate_ip(ip_input):
                    self.print_colored("Invalid IP address format", "red")
                    continue

                # Perform lookup
                print()
                data = self.get_ip_info(ip_input)
                self.display_results(ip_input, data)

                print()
                self.print_colored("Lookup completed. Enter another IP or 'quit' to exit.", "green")
                print()

            except KeyboardInterrupt:
                print()
                self.print_colored("Application terminated by user", "yellow")
                break
            except Exception as e:
                self.print_colored(f"An error occurred: {str(e)}", "red")

    def single_lookup(self, ip):
        """Perform a single IP lookup"""
        self.print_banner()

        if not self.validate_ip(ip):
            self.print_colored("Invalid IP address format", "red")
            return False

        data = self.get_ip_info(ip)
        self.display_results(ip, data)
        return True

def main():
    """Main function"""
    cli = NWOLookupCLI()

    if len(sys.argv) > 1:
        # Command line argument provided
        ip = sys.argv[1]
        cli.single_lookup(ip)
    else:
        # Interactive mode
        cli.interactive_mode()

if __name__ == "__main__":
    main()
