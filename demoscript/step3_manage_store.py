#!/usr/bin/env python3
"""
Step 3: Manage File Search Store

This script:
- Lists all existing file search stores
- Creates a new store if it doesn't exist
- Displays store information
"""
import sys
import os

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demoscript.utils import get_client, get_store, list_all_stores, print_store_info, STORE_NAME


def main():
    print("=" * 80)
    print("STEP 3: Manage File Search Store")
    print("=" * 80)
    print()
    
    try:
        client = get_client()
        
        # List all stores
        print("Listing all file search stores:")
        print("-" * 80)
        stores = list_all_stores(client)
        
        if stores:
            for i, store in enumerate(stores, 1):
                print(f"\nStore {i}:")
                print_store_info(store)
        else:
            print("No stores found.")
        print()
        
        # Check if our target store exists
        print(f"Checking for store: '{STORE_NAME}'")
        print("-" * 80)
        existing_store = get_store(client, STORE_NAME)
        
        if existing_store:
            print(f"✓ Store '{STORE_NAME}' already exists")
            print_store_info(existing_store)
        else:
            print(f"Store '{STORE_NAME}' does not exist. Creating it...")
            try:
                new_store = client.file_search_stores.create(config={"display_name": STORE_NAME})
                print(f"✓ Successfully created store:")
                print_store_info(new_store)
            except Exception as e:
                print(f"❌ Error creating store: {e}")
                return 1
        
        print()
        print("Next step: Run 'python demoscript/step4_upload_files.py'")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
