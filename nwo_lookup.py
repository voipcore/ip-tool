#!/usr/bin/env python3
"""
NWO IP Lookup Tool
A modern IP lookup tool with terminal-style GUI
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import json
import threading
import ipaddress
import time
from datetime import datetime
import sys
import os

class NWOLookupTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NWO Lookup - IP Intelligence Tool")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1e1e1e')

        # Configure style for modern look
        self.setup_styles()

        # Create main interface
        self.create_interface()

        # Terminal colors for output
        self.colors = {
            'green': '#00ff00',
            'red': '#ff0000',
            'yellow': '#ffff00',
            'cyan': '#00ffff',
            'white': '#ffffff',
            'gray': '#808080',
            'blue': '#0080ff'
        }

    def setup_styles(self):
        """Setup modern dark theme styles"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure dark theme
        style.configure('TFrame', background='#1e1e1e')
        style.configure('TLabel', background='#1e1e1e', foreground='#ffffff', font=('Consolas', 10))
        style.configure('TButton',
                       background='#2d2d2d',
                       foreground='#ffffff',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Consolas', 10, 'bold'))
        style.map('TButton',
                 background=[('active', '#404040'),
                           ('pressed', '#1a1a1a')])

        style.configure('TEntry',
                       fieldbackground='#2d2d2d',
                       background='#2d2d2d',
                       foreground='#ffffff',
                       borderwidth=1,
                       insertcolor='#ffffff',
                       font=('Consolas', 11))

    def create_interface(self):
        """Create the main GUI interface"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))

        title_label = ttk.Label(header_frame,
                               text="⚡ NWO LOOKUP - IP Intelligence Tool ⚡",
                               font=('Consolas', 16, 'bold'))
        title_label.pack()

        subtitle_label = ttk.Label(header_frame,
                                  text="Advanced IP Geolocation & Security Analysis",
                                  font=('Consolas', 10))
        subtitle_label.pack()

        # Input section
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        ip_label = ttk.Label(input_frame, text="Target IP Address:", font=('Consolas', 11, 'bold'))
        ip_label.pack(anchor=tk.W)

        entry_frame = ttk.Frame(input_frame)
        entry_frame.pack(fill=tk.X, pady=(5, 0))

        self.ip_entry = ttk.Entry(entry_frame, font=('Consolas', 12))
        self.ip_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.ip_entry.bind('<Return>', lambda e: self.lookup_ip())

        self.lookup_btn = ttk.Button(entry_frame, text="🔍 LOOKUP", command=self.lookup_ip)
        self.lookup_btn.pack(side=tk.RIGHT)

        self.clear_btn = ttk.Button(entry_frame, text="🗑️ CLEAR", command=self.clear_output)
        self.clear_btn.pack(side=tk.RIGHT, padx=(0, 5))

        # Progress bar
        self.progress = ttk.Progressbar(input_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(10, 0))

        # Output terminal
        terminal_frame = ttk.Frame(main_frame)
        terminal_frame.pack(fill=tk.BOTH, expand=True)

        terminal_label = ttk.Label(terminal_frame, text="Terminal Output:", font=('Consolas', 11, 'bold'))
        terminal_label.pack(anchor=tk.W)

        # Create text widget with scrollbar
        self.output_text = tk.Text(terminal_frame,
                                  bg='#0c0c0c',
                                  fg='#00ff00',
                                  font=('Consolas', 10),
                                  insertbackground='#00ff00',
                                  selectbackground='#2d2d2d',
                                  selectforeground='#ffffff',
                                  wrap=tk.WORD,
                                  state=tk.DISABLED)

        scrollbar = ttk.Scrollbar(terminal_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)

        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=(5, 0))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(5, 0))

        # Configure text tags for colors
        for color_name, color_value in self.colors.items():
            self.output_text.tag_configure(color_name, foreground=color_value)

        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))

        self.status_label = ttk.Label(status_frame, text="Ready", font=('Consolas', 9))
        self.status_label.pack(side=tk.LEFT)

        time_label = ttk.Label(status_frame, text=f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                              font=('Consolas', 9))
        time_label.pack(side=tk.RIGHT)

        # Initialize terminal
        self.print_to_terminal("NWO Lookup Tool initialized successfully", "green")
        self.print_to_terminal("Enter an IP address to begin analysis...", "cyan")
        self.print_to_terminal("═" * 80, "gray")

    def print_to_terminal(self, message, color="white"):
        """Print colored message to terminal output"""
        self.output_text.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"[{timestamp}] {message}\n"

        self.output_text.insert(tk.END, formatted_message, color)
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)

    def clear_output(self):
        """Clear the terminal output"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.print_to_terminal("Terminal cleared", "yellow")
        self.print_to_terminal("═" * 80, "gray")

    def validate_ip(self, ip_string):
        """Validate IP address format"""
        try:
            ipaddress.ip_address(ip_string)
            return True
        except ValueError:
            return False

    def lookup_ip(self):
        """Perform IP lookup in separate thread"""
        ip = self.ip_entry.get().strip()

        if not ip:
            messagebox.showerror("Error", "Please enter an IP address")
            return

        if not self.validate_ip(ip):
            messagebox.showerror("Error", "Invalid IP address format")
            return

        # Start lookup in separate thread
        self.lookup_btn.config(state='disabled')
        self.progress.start()
        self.status_label.config(text="Performing lookup...")

        thread = threading.Thread(target=self._perform_lookup, args=(ip,))
        thread.daemon = True
        thread.start()

    def _perform_lookup(self, ip):
        """Perform the actual IP lookup"""
        try:
            self.print_to_terminal(f"🎯 Starting lookup for IP: {ip}", "cyan")
            self.print_to_terminal("═" * 80, "gray")

            # Multiple API sources for comprehensive data
            apis = [
                {
                    'name': 'IPStack',
                    'url': f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query',
                    'free': True
                },
                {
                    'name': 'IPInfo',
                    'url': f'https://ipinfo.io/{ip}/json',
                    'free': True
                },
                {
                    'name': 'IPGeolocation',
                    'url': f'https://api.ipgeolocation.io/ipgeo?apiKey=&ip={ip}',
                    'free': True
                }
            ]

            all_data = {}

            for api in apis:
                try:
                    self.print_to_terminal(f"📡 Querying {api['name']} API...", "yellow")
                    response = requests.get(api['url'], timeout=10)

                    if response.status_code == 200:
                        data = response.json()
                        all_data[api['name']] = data
                        self.print_to_terminal(f"✅ {api['name']} - Success", "green")
                    else:
                        self.print_to_terminal(f"❌ {api['name']} - Error: {response.status_code}", "red")

                except Exception as e:
                    self.print_to_terminal(f"❌ {api['name']} - Exception: {str(e)}", "red")

            # Process and display results
            self._display_results(ip, all_data)

        except Exception as e:
            self.print_to_terminal(f"❌ Lookup failed: {str(e)}", "red")
        finally:
            # Re-enable UI
            self.root.after(0, self._finish_lookup)

    def _finish_lookup(self):
        """Finish lookup and re-enable UI"""
        self.progress.stop()
        self.lookup_btn.config(state='normal')
        self.status_label.config(text="Ready")

    def _display_results(self, ip, data):
        """Display comprehensive IP lookup results"""
        self.print_to_terminal("═" * 80, "gray")
        self.print_to_terminal("🎯 COMPREHENSIVE IP ANALYSIS REPORT", "cyan")
        self.print_to_terminal("═" * 80, "gray")

        # Basic Info
        self.print_to_terminal("📍 BASIC INFORMATION", "yellow")
        self.print_to_terminal(f"Target IP: {ip}", "white")

        # Compile data from all sources
        compiled_data = self._compile_data(data)

        if compiled_data:
            # Geographic Information
            self.print_to_terminal("\n🌍 GEOGRAPHIC LOCATION", "yellow")
            geo_fields = ['country', 'region', 'city', 'latitude', 'longitude', 'timezone', 'postal_code']
            for field in geo_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_to_terminal(f"{field.replace('_', ' ').title()}: {compiled_data[field]}", "white")

            # ISP Information
            self.print_to_terminal("\n🏢 ISP & NETWORK INFORMATION", "yellow")
            isp_fields = ['isp', 'organization', 'as_number', 'as_name']
            for field in isp_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_to_terminal(f"{field.replace('_', ' ').title()}: {compiled_data[field]}", "white")

            # Security Analysis
            self.print_to_terminal("\n🔒 SECURITY ANALYSIS", "yellow")
            security_fields = ['is_proxy', 'is_hosting', 'is_mobile', 'threat_level']
            for field in security_fields:
                if field in compiled_data:
                    color = "red" if compiled_data[field] and field.startswith('is_') else "green"
                    self.print_to_terminal(f"{field.replace('_', ' ').title()}: {compiled_data[field]}", color)

            # Additional Information
            self.print_to_terminal("\n💰 ADDITIONAL INFORMATION", "yellow")
            additional_fields = ['currency', 'languages', 'calling_code']
            for field in additional_fields:
                if field in compiled_data and compiled_data[field]:
                    self.print_to_terminal(f"{field.replace('_', ' ').title()}: {compiled_data[field]}", "white")
        else:
            self.print_to_terminal("❌ No data retrieved from APIs", "red")

        # Raw data section
        if data:
            self.print_to_terminal("\n📊 RAW API RESPONSES", "yellow")
            for api_name, api_data in data.items():
                self.print_to_terminal(f"\n--- {api_name} ---", "cyan")
                formatted_json = json.dumps(api_data, indent=2)
                for line in formatted_json.split('\n'):
                    self.print_to_terminal(line, "gray")

        self.print_to_terminal("\n" + "═" * 80, "gray")
        self.print_to_terminal("✅ ANALYSIS COMPLETE", "green")
        self.print_to_terminal("═" * 80, "gray")

    def _compile_data(self, data):
        """Compile data from multiple API sources"""
        compiled = {}

        # Process ip-api.com data
        if 'IPStack' in data and data['IPStack'].get('status') == 'success':
            d = data['IPStack']
            compiled.update({
                'country': d.get('country'),
                'region': d.get('regionName'),
                'city': d.get('city'),
                'latitude': d.get('lat'),
                'longitude': d.get('lon'),
                'timezone': d.get('timezone'),
                'postal_code': d.get('zip'),
                'isp': d.get('isp'),
                'organization': d.get('org'),
                'as_number': d.get('as', '').split(' ')[0] if d.get('as') else None,
                'as_name': d.get('asname'),
                'is_proxy': d.get('proxy', False),
                'is_hosting': d.get('hosting', False),
                'is_mobile': d.get('mobile', False),
                'currency': d.get('currency')
            })

        # Process ipinfo.io data
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

    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main function to run the NWO Lookup Tool"""
    try:
        app = NWOLookupTool()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user")
    except Exception as e:
        print(f"Application error: {e}")

if __name__ == "__main__":
    main()
