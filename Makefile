# Gemini-RAG Makefile
# Standalone setup for Gemini File Search Store testing

.PHONY: help install setup run-all clean test-agent test-rag-agent

help:
	@echo "Gemini-RAG - File Search Store Testing"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup          - Create virtual environment and install dependencies"
	@echo "  make install        - Install dependencies (requires venv to be activated)"
	@echo "  make run-all        - Run all demo steps"
	@echo "  make test-agent     - Run SDK agent (Google Search only)"
	@echo "  make test-rag-agent - Run SDK RAG agent (File Search Store)"
	@echo "  make clean          - Remove virtual environment"
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

test-agent:
	@echo "==============================================================================="
	@echo "| 🤖 Running SDK Agent (Google Search only)                                    |"
	@echo "==============================================================================="
	@echo ""
	@echo "This agent uses Google Search but has NO RAG capabilities."
	@echo "It will NOT know about your Republic Day story."
	@echo ""
	@echo "Try asking:"
	@echo "  - 'What is the current weather in New York?'"
	@echo "  - 'What is the stock price of Google?'"
	@echo "  - 'Who won the latest cricket match?'"
	@echo ""
	@echo "Type 'exit' or 'quit' to stop."
	@echo "==============================================================================="
	@echo ""
	@python app/sdk_agent.py

test-rag-agent:
	@echo "==============================================================================="
	@echo "| 🤖 Running SDK RAG Agent (File Search Store)                               |"
	@echo "==============================================================================="
	@echo ""
	@echo "This agent uses the File Search Store for RAG."
	@echo "Make sure you've completed steps 1-4 first!"
	@echo ""
	@echo "Try asking about Republic Day:"
	@echo "  - 'When did India become a republic?'"
	@echo "  - 'Who was the first President of India?'"
	@echo "  - 'What are the key features of the Republic Day parade?'"
	@echo ""
	@echo "Type 'exit' or 'quit' to stop."
	@echo "==============================================================================="
	@echo ""
	@python app/sdk_rag_agent.py

clean:
	@echo "Removing virtual environment..."
	@rm -rf .venv
	@echo "✓ Cleaned up"
