#!/usr/bin/env python3
"""
Shared utility functions for the demo scripts
"""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel


# Load environment variables
load_dotenv()

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STORE_NAME = os.getenv("STORE_NAME", "demo-file-store")
MODEL = os.getenv("MODEL", "gemini-2.5-flash")
UPLOAD_PATH = os.getenv("UPLOAD_PATH", "data")


class DocumentMetadata(BaseModel):
    """Metadata for a document"""
    title: str
    author: str
    abstract: str


def get_client():
    """Initialize and return the Gemini client"""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please check your .env file.")
    return genai.Client()


def get_store(client: genai.Client, store_name: str = None):
    """Retrieve a store by its display name"""
    if store_name is None:
        store_name = STORE_NAME
    
    try:
        for a_store in client.file_search_stores.list():
            if a_store.display_name == store_name:
                return a_store
    except Exception as e:
        print(f"Error in get_store: {e}")
    return None


def list_all_stores(client: genai.Client):
    """List all file search stores"""
    try:
        stores = list(client.file_search_stores.list())
        return stores
    except Exception as e:
        print(f"Error listing stores: {e}")
        return []


def print_store_info(store):
    """Print information about a store"""
    if store:
        print(f"  Name: {store.name}")
        print(f"  Display Name: {store.display_name}")
    else:
        print("  Store not found")


def print_env_status():
    """Print the status of environment variables"""
    print("Environment Configuration:")
    print("=" * 80)
    if GEMINI_API_KEY:
        print(f"✓ GEMINI_API_KEY: {'*' * 20} (loaded)")
    else:
        print("✗ GEMINI_API_KEY: Not set")
    
    print(f"✓ STORE_NAME: {STORE_NAME}")
    print(f"✓ MODEL: {MODEL}")
    print(f"✓ UPLOAD_PATH: {UPLOAD_PATH}")
    print("=" * 80)
