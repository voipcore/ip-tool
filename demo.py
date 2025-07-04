#!/usr/bin/env python3
"""
NWO Lookup Tool Demo
Demonstrates the capabilities of the IP lookup tool
"""

from nwo_lookup_cli import NWOLookupCLI
import time

def main():
    """Run demo with sample IPs"""
    cli = NWOLookupCLI()

    # Demo IPs
    demo_ips = [
        "8.8.8.8",      # Google DNS
        "1.1.1.1",      # Cloudflare DNS
        "208.67.222.222"  # OpenDNS
    ]

    cli.print_banner()
    cli.print_colored("🎬 NWO Lookup Tool - DEMO MODE", "yellow")
    cli.print_colored("This demo will analyze several well-known IP addresses", "cyan")
    print()

    for i, ip in enumerate(demo_ips, 1):
        cli.print_colored(f"🎯 Demo {i}/{len(demo_ips)}: Analyzing {ip}", "yellow")
        print()

        data = cli.get_ip_info(ip)
        cli.display_results(ip, data)

        if i < len(demo_ips):
            print()
            cli.print_colored("Press Enter to continue to next demo...", "cyan")
            input()

    print()
    cli.print_colored("🎉 Demo completed! You can now use the tool with your own IP addresses.", "green")
    cli.print_colored("Run 'python nwo_lookup_cli.py' for interactive mode", "cyan")
    cli.print_colored("Or 'python nwo_lookup_cli.py <IP>' for single lookup", "cyan")

if __name__ == "__main__":
    main()
