#!/usr/bin/env python3
"""
Run all demo steps sequentially
"""
import sys
import os
import subprocess

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Steps to run in order
steps = [
    "step1_setup.py",
    "step2_init_client.py",
    "step3_manage_store.py",
    "step4_upload_files.py",
    "step5_query_store.py",
]


def run_step(step_name):
    """Run a single step and return success status"""
    step_path = os.path.join(script_dir, step_name)
    print(f"\n{'='*80}")
    print(f"Running: {step_name}")
    print('='*80)
    print()
    
    result = subprocess.run(
        [sys.executable, step_path],
        cwd=project_root,
        capture_output=False
    )
    
    return result.returncode == 0


def main():
    print("=" * 80)
    print("Running All Demo Steps")
    print("=" * 80)
    print()
    
    for step in steps:
        if not run_step(step):
            print(f"\n❌ Failed at step: {step}")
            print("Please check the error messages above.")
            return 1
    
    print("\n" + "=" * 80)
    print("✓ All steps completed successfully!")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    exit(main())
