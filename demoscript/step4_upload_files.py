#!/usr/bin/env python3
"""
Step 4: Upload Files to File Search Store

This script:
- Uploads files from the data directory to the file search store
- Extracts metadata using Gemini
- Handles duplicate file detection and replacement
"""
import sys
import os
import glob
import time

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demoscript.utils import (
    get_client, get_store, STORE_NAME, MODEL, UPLOAD_PATH,
    DocumentMetadata
)


def delete_doc(client, doc):
    """Delete a document from the file search store"""
    print(f"♻️  Deleting duplicate: '{doc.display_name}' (ID: {doc.name})")
    client.file_search_stores.documents.delete(name=doc.name, config={"force": True})
    time.sleep(2)  # Small throttle and allow propagation


def generate_metadata(client, file_name: str, temp_file) -> DocumentMetadata:
    """Generate metadata for a document using Gemini"""
    print(f"Extracting metadata from {file_name}...")
    
    response = client.models.generate_content(
        model=MODEL,
        contents=[
            """Please extract title, author, and short abstract from this document. 
            Each value should be under 200 characters.

            Abstracts should be succinct and NOT include preamble text like `This document describes...`

            Example bad abstract: 
            Now I want to cover a key consideration that can potentially 
            save you more in future IT spend than any other decision you can make: 
            embracing open source as a core element of your cloud strategy.

            Example good abstract:
            How you can significantly reduce IT spend by embracing open source
            as a core component of your cloud strategy.

            Example bad abstract:
            This article discusses how you can design your cloud landing zone.

            Example good abstract:
            How to design your cloud landing zone according to best practices.
            """,
            temp_file,
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": DocumentMetadata,
        },
    )

    metadata: DocumentMetadata = response.parsed
    print(f"  Title: {metadata.title}")
    print(f"  Author: {metadata.author}")
    print(f"  Abstract: {metadata.abstract}")

    return metadata


def upload_doc(client, file_path, file_search_store):
    """Upload a document to the file search store"""
    file_name = os.path.basename(file_path)

    print(f"Uploading {file_name} for metadata extraction...")
    temp_file = client.files.upload(file=file_path)

    # Verify file is active (ready for inference)
    while temp_file.state.name == "PROCESSING":
        print("  Still uploading...", end="\r")
        time.sleep(2)
        temp_file = client.files.get(name=temp_file.name)

    if temp_file.state.name != "ACTIVE":
        raise RuntimeError(f"File upload failed with state: {temp_file.state.name}")

    # Check if this is a replacement of an existing file
    for doc in client.file_search_stores.documents.list(parent=file_search_store.name):
        should_delete = False

        # Match by Display Name
        if doc.display_name == file_name:
            should_delete = True

        # Match by Custom Metadata
        elif doc.custom_metadata:
            for meta in doc.custom_metadata:
                if meta.key == "file_name" and meta.string_value == file_name:
                    should_delete = True
                    break

        if should_delete:
            delete_doc(client, doc)

    # Generate metadata
    metadata = generate_metadata(client, file_name, temp_file)

    # Import the file into the file search store with custom metadata
    operation = client.file_search_stores.upload_to_file_search_store(
        file_search_store_name=file_search_store.name,
        file=file_path,
        config={
            "display_name": metadata.title,
            "custom_metadata": [
                {"key": "title", "string_value": metadata.title},
                {"key": "file_name", "string_value": file_name},
                {"key": "author", "string_value": metadata.author},
                {"key": "abstract", "string_value": metadata.abstract},
            ],
        },
    )

    # Wait until import is complete
    while not operation.done:
        time.sleep(5)
        print("  Still importing...")
        operation = client.operations.get(operation)

    print(f"✓ {file_name} successfully uploaded and indexed")


def main():
    print("=" * 80)
    print("STEP 4: Upload Files to File Search Store")
    print("=" * 80)
    print()
    
    try:
        client = get_client()
        file_search_store = get_store(client, STORE_NAME)
        
        if file_search_store is None:
            print(f"❌ Store '{STORE_NAME}' not found.")
            print("   Please run 'python demoscript/step3_manage_store.py' first.")
            return 1
        
        print(f"Uploading files to store: {file_search_store.display_name}")
        print(f"Upload path: {UPLOAD_PATH}")
        print()
        
        # Find files to upload
        files_to_upload = glob.glob(f"{UPLOAD_PATH}/*")
        
        # Filter out directories
        files_to_upload = [f for f in files_to_upload if os.path.isfile(f)]
        
        if not files_to_upload:
            print(f"❌ No files found in {UPLOAD_PATH}")
            print(f"   Please ensure files exist in the '{UPLOAD_PATH}' directory")
            return 1
        
        print(f"Found {len(files_to_upload)} file(s) to upload:")
        for f in files_to_upload:
            print(f"  - {f}")
        print()
        
        # Upload each file
        for file_path in files_to_upload:
            print("-" * 80)
            print(f"Processing: {file_path}")
            print("-" * 80)
            try:
                upload_doc(client, file_path, file_search_store)
                print()
            except Exception as e:
                print(f"❌ Error uploading {file_path}: {e}")
                return 1
        
        print("=" * 80)
        print("✓ Upload complete!")
        print()
        print("Next step: Run 'python demoscript/step5_query_store.py'")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
