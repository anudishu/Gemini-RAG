#!/bin/bash
# Setup script for Gemini-RAG
# Creates virtual environment and installs dependencies

set -e

echo "=========================================="
echo "Gemini-RAG Setup"
echo "=========================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "   Please install Python 3.12 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo ""
echo "Virtual environment is now activated."
echo ""
echo "Next steps:"
echo "  1. Create a .env file with your API key:"
echo "     export GEMINI_API_KEY='your-api-key'"
echo "     export STORE_NAME='demo-file-store'"
echo "     export MODEL='gemini-2.5-flash'"
echo ""
echo "  2. Run the demo scripts:"
echo "     python demoscript/step1_setup.py"
echo "     python demoscript/step2_init_client.py"
echo "     python demoscript/step3_manage_store.py"
echo "     python demoscript/step4_upload_files.py"
echo "     python demoscript/step5_query_store.py"
echo ""
echo "  Or run all at once:"
echo "     python demoscript/run_all.py"
echo ""
