#!/usr/bin/env python3
"""
NWO Lookup Tool Launcher
Simple launcher for the IP lookup application
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Try GUI version first
    from nwo_lookup import main as gui_main
    print("Starting GUI version...")
    gui_main()
except ImportError as e:
    print(f"GUI version not available: {e}")
    print("Starting CLI version...")
    try:
        from nwo_lookup_cli import main as cli_main
        cli_main()
    except ImportError as e2:
        print(f"CLI Import error: {e2}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")
    except Exception as e2:
        print(f"Error running CLI application: {e2}")
except Exception as e:
    print(f"Error running GUI application: {e}")
    print("Falling back to CLI version...")
    try:
        from nwo_lookup_cli import main as cli_main
        cli_main()
    except Exception as e2:
        print(f"Error running CLI application: {e2}")
