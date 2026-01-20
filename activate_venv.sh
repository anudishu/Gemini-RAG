#!/bin/bash
# Helper script to activate virtual environment in Gemini-RAG folder

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/.venv/bin/activate"

if [ -f "$VENV_PATH" ]; then
    echo "Activating virtual environment..."
    source "$VENV_PATH"
    echo "✓ Virtual environment activated!"
    echo "  You are now in: $(pwd)"
    echo ""
    echo "You can now run the demo scripts:"
    echo "  python demoscript/step1_setup.py"
    echo "  python demoscript/step2_init_client.py"
    echo "  python demoscript/step3_manage_store.py"
    echo "  python demoscript/step4_upload_files.py"
    echo "  python demoscript/step5_query_store.py"
    echo ""
    echo "Or run all at once:"
    echo "  python demoscript/run_all.py"
else
    echo "❌ Error: Virtual environment not found!"
    echo "   Please run setup first:"
    echo "     ./setup.sh"
    echo "   or"
    echo "     make setup"
    exit 1
fi
