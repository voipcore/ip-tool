#!/usr/bin/env python3
"""
NWO Lookup Tool Setup Script
Creates virtual environment and installs dependencies
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("🚀 NWO Lookup Tool Setup")
    print("=" * 50)

    # Check if virtual environment exists
    venv_path = "venv"
    if not os.path.exists(venv_path):
        # Create virtual environment
        if not run_command(f"{sys.executable} -m venv {venv_path}", "Creating virtual environment"):
            return False

    # Determine activation script based on OS
    if os.name == 'nt':  # Windows
        pip_path = os.path.join(venv_path, "Scripts", "pip")
        python_path = os.path.join(venv_path, "Scripts", "python")
    else:  # Linux/Mac
        pip_path = os.path.join(venv_path, "bin", "pip")
        python_path = os.path.join(venv_path, "bin", "python")

    # Install requirements
    if not run_command(f"{pip_path} install -r requirements.txt", "Installing dependencies"):
        return False

    print("\n🎉 Setup completed successfully!")
    print(f"💡 To run the application:")
    if os.name == 'nt':
        print(f"   {python_path} run.py")
    else:
        print(f"   {python_path} run.py")

    return True

if __name__ == "__main__":
    main()
