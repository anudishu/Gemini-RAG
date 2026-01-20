#!/usr/bin/env python3
"""
Step 5: Query File Search Store

This script:
- Queries the file search store using the File Search Tool
- Demonstrates RAG functionality by asking questions about uploaded content
"""
import sys
import os

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demoscript.utils import get_client, get_store, STORE_NAME, MODEL
from google.genai import types


def query_store(client, store, question: str):
    """Query the file search store with a question"""
    print(f"Question: {question}")
    print("-" * 80)
    
    try:
        # Use the File Search Tool
        response = client.models.generate_content(
            model=MODEL,
            contents=question,
            config=types.GenerateContentConfig(
                tools=[types.Tool(file_search=types.FileSearch(file_search_store_names=[store.name]))]
            ),
        )
        
        print("\nResponse:")
        print(response.text)
        print()
        
        # Show which chunks were used (if available)
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'grounding_metadata'):
                grounding = candidate.grounding_metadata
                if hasattr(grounding, 'grounding_chunks'):
                    chunks = grounding.grounding_chunks
                    if chunks:
                        print(f"Found {len(chunks)} relevant chunk(s) in the store")
                        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Query failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 80)
    print("STEP 5: Query File Search Store")
    print("=" * 80)
    print()
    
    try:
        client = get_client()
        store = get_store(client, STORE_NAME)
        
        if store is None:
            print(f"❌ Store '{STORE_NAME}' not found.")
            print("   Please run 'python demoscript/step3_manage_store.py' first.")
            return 1
        
        print(f"Querying store: {store.display_name}")
        print(f"Store ID: {store.name}")
        print()
        
        # Example queries about Republic Day
        questions = [
            "When did India become a republic?",
            "Who was the first President of India?",
            "What are the key features of the Republic Day parade?",
            "What values does Republic Day celebrate?",
        ]
        
        for i, question in enumerate(questions, 1):
            print(f"\n{'='*80}")
            print(f"Query {i}/{len(questions)}")
            print('='*80)
            print()
            
            if not query_store(client, store, question):
                return 1
        
        print("=" * 80)
        print("✓ All queries completed successfully!")
        print()
        print("Demo complete! The File Search Store is working correctly.")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
