#!/usr/bin/env python3
"""
Step 1: Setup and Environment Check

This script:
- Loads environment variables from .env file
- Verifies that all required configuration is present
- Displays the configuration status

IMPORTANT: Run this script from the project root directory, not from inside demoscript/
Example: python demoscript/step1_setup.py
"""
import sys
import os

# Add parent directory to path to import utils
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Check if we're being run from the correct location
if os.path.basename(os.getcwd()) == 'demoscript':
    print("❌ ERROR: Please run this script from the project root directory!")
    print(f"   Current directory: {os.getcwd()}")
    print(f"   Expected: {project_root}")
    print(f"\n   Run: cd {project_root}")
    print(f"   Then: python demoscript/step1_setup.py")
    sys.exit(1)

try:
    from demoscript.utils import print_env_status, GEMINI_API_KEY, STORE_NAME, MODEL, UPLOAD_PATH
except ImportError as e:
    print(f"❌ ERROR: Failed to import required modules: {e}")
    print("\nPlease make sure:")
    print("  1. You're running from the project root directory")
    print("  2. The virtual environment is activated: source .venv/bin/activate")
    print("  3. Dependencies are installed: make install")
    sys.exit(1)


def main():
    print("=" * 80)
    print("STEP 1: Setup and Environment Check")
    print("=" * 80)
    print()
    
    # Print environment status
    print_env_status()
    print()
    
    # Verify critical settings
    if not GEMINI_API_KEY:
        print("❌ ERROR: GEMINI_API_KEY is not set!")
        print("   Please create a .env file with your Gemini API key.")
        print("   Example: export GEMINI_API_KEY='your-api-key-here'")
        return 1
    
    print("✓ All required environment variables are set")
    print()
    print("Next step: Run 'python demoscript/step2_init_client.py'")
    return 0


if __name__ == "__main__":
    exit(main())
