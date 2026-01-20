# Gemini-RAG - File Search Store Testing

**Standalone folder for testing Gemini File Search Store with RAG (Retrieval Augmented Generation).**

This is a completely self-contained setup - no dependencies on other folders!

## 📁 Structure

```
Gemini-RAG/
├── app/              # Agent implementations (SDK and ADK versions)
├── data/             # Files to upload to the store
│   └── story.md      # Republic Day story (26 January)
├── demoscript/       # Step-by-step test scripts
│   ├── step1_setup.py
│   ├── step2_init_client.py
│   ├── step3_manage_store.py
│   ├── step4_upload_files.py
│   ├── step5_query_store.py
│   └── utils.py
├── .venv/            # Virtual environment (created during setup)
├── .env              # Environment variables (API keys, etc.)
├── requirements.txt  # Python dependencies
├── Makefile          # Make commands for setup
├── setup.sh          # Setup script
└── activate_venv.sh  # Helper to activate virtual environment
```

## 🚀 Quick Start

### Step 1: Setup (First Time Only)

**Option A: Using the setup script (Recommended)**

```bash
cd Gemini-RAG
./setup.sh
```

**Option B: Using Make**

```bash
cd Gemini-RAG
make setup
```

**Option C: Manual setup**

```bash
cd Gemini-RAG
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

This will:
- Create a virtual environment (`.venv`)
- Install all required dependencies
- Activate the virtual environment

### Step 2: Configure Environment Variables

Create a `.env` file in the Gemini-RAG directory:

```bash
export GEMINI_API_KEY="your-api-key"
export STORE_NAME="demo-file-store"
export MODEL="gemini-2.5-flash"
```

**To get your Gemini API Key:**
- Go to [Google AI Studio](https://aistudio.google.com/)
- Sign in and create an API key
- Copy it to your `.env` file

### Step 3: Activate Virtual Environment

**Option 1: Use helper script**

```bash
source activate_venv.sh
```

**Option 2: Manual activation**

```bash
source .venv/bin/activate
```

### Step 4: Run the Demo Scripts

From the **Gemini-RAG** directory:

```bash
# Step 1: Check environment setup
python demoscript/step1_setup.py

# Step 2: Initialize Gemini client
python demoscript/step2_init_client.py

# Step 3: Create the file search store
python demoscript/step3_manage_store.py

# Step 4: Upload files from data/ folder
python demoscript/step4_upload_files.py

# Step 5: Query the store (tests RAG functionality)
python demoscript/step5_query_store.py
```

**Or run all steps at once:**

```bash
python demoscript/run_all.py
```

**Or using Make:**

```bash
make run-all
```

## 📝 What Each Script Does

1. **step1_setup.py** - Checks environment configuration and verifies `.env` file
2. **step2_init_client.py** - Initializes Gemini API client and tests connection
3. **step3_manage_store.py** - Lists stores and creates a new file search store
4. **step4_upload_files.py** - Uploads files from `data/` folder to the store (with metadata extraction)
5. **step5_query_store.py** - Queries the store with questions about Republic Day to test RAG

## 📚 Content

The demo uses a **Republic Day story** (26 January) as the test content:

- **File:** `data/story.md`
- **Topic:** India's Republic Day celebration
- **Content:** History, Constitution, traditions, and significance

The queries in step5 will ask questions like:
- "When did India become a republic?"
- "Who was the first President of India?"
- "What are the key features of the Republic Day parade?"
- "What values does Republic Day celebrate?"

## 🔧 Requirements

- **Python 3.12+** (check with `python3 --version`)
- **Internet connection** (to download packages and access Gemini API)
- **Gemini API key** (get from [Google AI Studio](https://aistudio.google.com/))

## 📦 Dependencies

The project uses minimal dependencies:
- `google-genai>=1.49.0` - Gemini API client
- `python-dotenv>=1.0.0` - Environment variable management
- `pydantic>=2.0.0` - Data validation

All dependencies are listed in `requirements.txt`.

## 🛠️ Available Commands

Using Make:

```bash
make help      # Show available commands
make setup     # Create venv and install dependencies
make install   # Install dependencies (venv must be activated)
make run-all   # Run all demo steps
make clean     # Remove virtual environment
```

## ⚠️ Important Notes

- **Always run scripts from the Gemini-RAG directory**, not from inside `demoscript/`
- The virtual environment (`.venv`) is created inside this folder
- All scripts use the `.env` file in the Gemini-RAG directory
- The file search store will be created with the name specified in `STORE_NAME` (default: `demo-file-store`)
- **This folder is completely standalone** - no dependencies on other folders!

## 🐛 Troubleshooting

### Error: "Module not found"
- Make sure virtual environment is activated: `source .venv/bin/activate` or `source activate_venv.sh`
- Run setup: `./setup.sh` or `make setup`
- Check you're running from Gemini-RAG directory, not from demoscript/

### Error: "GEMINI_API_KEY not set"
- Verify `.env` file exists in Gemini-RAG directory
- Check that it contains `export GEMINI_API_KEY="your-key"`
- Make sure you've sourced the `.env` file or it's loaded by the script

### Error: "Store not found"
- Run `step3_manage_store.py` first to create the store

### Error: "No files found"
- Make sure `data/story.md` exists
- Check the file path in step4 script

### Error: "Python 3.12+ required"
- Install Python 3.12 or higher
- Check version: `python3 --version`

## 🎯 Expected Results

After running all steps successfully, you should see:

1. ✓ Environment configured
2. ✓ Client initialized
3. ✓ Store created
4. ✓ File uploaded and indexed
5. ✓ Queries returning answers based on the Republic Day story

The File Search Store will use RAG to retrieve relevant information from your uploaded story and answer questions accurately!

## 🔄 Clean Setup

To start fresh:

```bash
make clean      # Remove virtual environment
./setup.sh      # Recreate and setup
```

## 📖 Learn More

- [Gemini File Search Documentation](https://ai.google.dev/gemini-api/docs/file-search)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

## 📄 License

This is a demo project for testing Gemini File Search Store functionality.
