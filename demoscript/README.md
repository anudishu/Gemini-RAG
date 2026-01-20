# Demo Scripts - Step-by-Step File Search Store Testing

This directory contains step-by-step scripts to test the Gemini File Search Store functionality without using a Jupyter notebook.

## Scripts Overview

1. **step1_setup.py** - Setup and environment check
2. **step2_init_client.py** - Initialize Gemini client
3. **step3_manage_store.py** - View and create file search stores
4. **step4_upload_files.py** - Upload files to the store
5. **step5_query_store.py** - Query the store to verify RAG functionality

## Prerequisites

1. Make sure you have a `.env` file in the project root with:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   export STORE_NAME="demo-file-store"
   export MODEL="gemini-2.5-flash"
   ```

2. Ensure dependencies are installed:
   ```bash
   make install
   # or
   uv sync --extra jupyter
   ```

## Running the Scripts

**⚠️ IMPORTANT: Always run scripts from the project root directory, not from inside the `demoscript` folder!**

### Prerequisites

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   # or on Windows:
   # .venv\Scripts\activate
   ```

2. **Make sure dependencies are installed:**
   ```bash
   make install
   # or
   uv sync --extra jupyter
   ```

### Option 1: Run All Steps Sequentially

```bash
# From the project root directory (NOT from demoscript/)
cd "/path/to/gemini-file-search-demo"
source .venv/bin/activate  # Activate virtual environment first!

python demoscript/step1_setup.py
python demoscript/step2_init_client.py
python demoscript/step3_manage_store.py
python demoscript/step4_upload_files.py
python demoscript/step5_query_store.py
```

### Option 2: Run Individual Steps

You can run any step independently (as long as previous steps have been completed):

```bash
# Check setup
python demoscript/step1_setup.py

# Initialize client
python demoscript/step2_init_client.py

# Manage stores
python demoscript/step3_manage_store.py

# Upload files
python demoscript/step4_upload_files.py

# Query the store
python demoscript/step5_query_store.py
```

### Option 3: Run All at Once

You can also create a simple runner script:

```bash
#!/bin/bash
python demoscript/step1_setup.py && \
python demoscript/step2_init_client.py && \
python demoscript/step3_manage_store.py && \
python demoscript/step4_upload_files.py && \
python demoscript/step5_query_store.py
```

## What Each Script Does

### Step 1: Setup
- Loads environment variables from `.env` file
- Verifies all required configuration is present
- Displays configuration status

### Step 2: Initialize Client
- Initializes the Gemini API client
- Tests the connection by listing existing stores
- Verifies credentials are working

### Step 3: Manage Store
- Lists all existing file search stores
- Creates a new store if the target store doesn't exist
- Displays store information

### Step 4: Upload Files
- Finds files in the `data/` directory
- Uploads each file to the file search store
- Extracts metadata (title, author, abstract) using Gemini
- Handles duplicate detection and replacement

### Step 5: Query Store
- Queries the file search store with example questions
- Demonstrates RAG functionality
- Shows how the File Search Tool retrieves relevant information

## Troubleshooting

### Error: GEMINI_API_KEY not set
- Make sure you have a `.env` file in the project root
- Check that the file contains `export GEMINI_API_KEY="your-key"`

### Error: Store not found
- Run `step3_manage_store.py` first to create the store

### Error: No files found
- Make sure you have files in the `data/` directory
- Check the `UPLOAD_PATH` in `utils.py` or your `.env` file

### Error: Client initialization failed
- Verify your API key is valid
- Check your internet connection
- Ensure the `google-genai` package is installed and up-to-date

## Customization

You can customize the scripts by modifying:

- **utils.py**: Change default values for `STORE_NAME`, `MODEL`, `UPLOAD_PATH`
- **step5_query_store.py**: Add your own questions to test
- **step4_upload_files.py**: Modify metadata extraction prompts

## Notes

- The scripts use the same logic as the Jupyter notebook
- Each script is independent and can be run separately
- Scripts will fail gracefully with helpful error messages
- All scripts use the shared `utils.py` module for common functions
