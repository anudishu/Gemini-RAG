# Gemini-RAG Makefile
# Standalone setup for Gemini File Search Store testing

.PHONY: help install setup run-all clean

help:
	@echo "Gemini-RAG - File Search Store Testing"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup     - Create virtual environment and install dependencies"
	@echo "  make install   - Install dependencies (requires venv to be activated)"
	@echo "  make run-all   - Run all demo steps"
	@echo "  make clean     - Remove virtual environment"
	@echo ""

setup:
	@echo "Setting up Gemini-RAG..."
	@python3 --version || (echo "Error: Python 3.12+ required" && exit 1)
	@if [ ! -d ".venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv .venv; \
	fi
	@echo "Activating virtual environment and installing dependencies..."
	@. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo ""
	@echo "✓ Setup complete!"
	@echo ""
	@echo "To activate the virtual environment, run:"
	@echo "  source .venv/bin/activate"
	@echo ""
	@echo "Then run the demo scripts:"
	@echo "  python demoscript/step1_setup.py"

install:
	@echo "Installing dependencies..."
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@echo "✓ Dependencies installed"

run-all:
	@echo "Running all demo steps..."
	@python demoscript/run_all.py

clean:
	@echo "Removing virtual environment..."
	@rm -rf .venv
	@echo "✓ Cleaned up"
