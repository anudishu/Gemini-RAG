#!/usr/bin/env python3
"""
Step 2: Initialize Gemini Client

This script:
- Initializes the Gemini API client
- Verifies the client is working correctly
"""
import sys
import os

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demoscript.utils import get_client, print_env_status


def main():
    print("=" * 80)
    print("STEP 2: Initialize Gemini Client")
    print("=" * 80)
    print()
    
    try:
        # Initialize client
        print("Initializing Gemini client...")
        client = get_client()
        print(f"✓ Client initialized: {type(client).__name__}")
        print()
        
        # Test client by listing stores (this will fail if credentials are wrong)
        print("Testing client connection...")
        stores = client.file_search_stores.list()
        store_count = len(list(stores))
        print(f"✓ Client connection successful (found {store_count} existing store(s))")
        print()
        
        print("Next step: Run 'python demoscript/step3_manage_store.py'")
        return 0
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print()
        print("Please run 'python demoscript/step1_setup.py' first to check your configuration.")
        return 1
    except Exception as e:
        print(f"❌ Error initializing client: {e}")
        print()
        print("Please check:")
        print("  1. Your GEMINI_API_KEY is valid")
        print("  2. You have internet connectivity")
        print("  3. The google-genai package is installed")
        return 1


if __name__ == "__main__":
    exit(main())
