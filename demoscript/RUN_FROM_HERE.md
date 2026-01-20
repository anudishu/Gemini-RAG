# ⚠️ IMPORTANT: How to Run the Demo Scripts

## The Problem

If you see this error:
```
ModuleNotFoundError: No module named 'dotenv'
```

**You're running the script from the wrong directory!**

## The Solution

### ✅ Correct Way (From Project Root):

```bash
# 1. Navigate to the project root
cd "/Users/Sumit_Kumar/Library/CloudStorage/GoogleDrive-sumit.kumar@66degrees.com/My Drive/2025 projects/cet-training/Gemini-FileSearch/gemini-file-search-demo"

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Run the script (from project root, not from demoscript/)
python demoscript/step1_setup.py
```

### ❌ Wrong Way (From Inside demoscript/):

```bash
cd demoscript/
python step1_setup.py  # ❌ This will fail!
```

## Quick Fix

If you're currently in the `demoscript` directory:

```bash
# Go back to project root
cd ..

# Activate virtual environment
source .venv/bin/activate

# Now run the script
python demoscript/step1_setup.py
```

## All Scripts Must Be Run From Project Root

All scripts should be run like this:

```bash
# From project root directory
python demoscript/step1_setup.py
python demoscript/step2_init_client.py
python demoscript/step3_manage_store.py
python demoscript/step4_upload_files.py
python demoscript/step5_query_store.py
```

## Using the Helper Scripts

You can also use the `run_all.py` or `run_all.sh` scripts:

```bash
# From project root
python demoscript/run_all.py

# Or using shell script
./demoscript/run_all.sh
```

These scripts automatically handle the correct paths.
