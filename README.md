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

### Step 1: Initial Setup (First Time Only)

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

---

## 🎯 Step-by-Step Demo Flow

Follow these steps in order to see the difference between a basic agent (no RAG) and a RAG-enabled agent.

### Part 1: The Basic Agent (Baseline)

First, let's establish a baseline. We're going to use the raw `google-genai` SDK to run a simple agent.

#### The Code

Take a look at `app/sdk_agent.py`. It's a minimal implementation that:
- Instantiates a `genai.Client()`
- Enables the `google_search` tool
- That's it. **No RAG.**

#### Running the Basic Agent

**Using Make:**
```bash
make test-agent
```

**Or directly:**
```bash
python app/sdk_agent.py
```

#### Test 1: General Question (Should Work)

Let's ask it a general question that Google Search can answer:

```
> What is the stock price of Google?
```

It should answer correctly using Google Search to find the current price.

#### Test 2: Story-Specific Question (Should Fail)

Now, let's ask a question it doesn't know how to answer. It requires the agent to have read our Republic Day story:

```
> When did India become a republic?
```

Or:

```
> Who was the first President of India?
```

**Expected Result:** The model will either:
- Fail to answer correctly
- Hallucinate (make up an answer)
- Say it doesn't know

This demonstrates that **without RAG, the agent has no knowledge of our custom content**.

Type `quit` or `exit` to exit the agent.

---

### Part 2: Setting Up File Search Store (RAG)

Now let's set up RAG so the agent can answer questions about our story.

#### Step 1: Check Environment Setup

```bash
python demoscript/step1_setup.py
```

**What it does:**
- Loads environment variables from `.env` file
- Verifies that all required configuration is present
- Displays the configuration status

**Expected output:**
```
✓ GEMINI_API_KEY: ******************** (loaded)
✓ STORE_NAME: demo-file-store
✓ MODEL: gemini-2.5-flash
✓ UPLOAD_PATH: data
```

#### Step 2: Initialize Gemini Client

```bash
python demoscript/step2_init_client.py
```

**What it does:**
- Initializes the Gemini API client
- Tests the connection by listing existing stores
- Verifies credentials are working

**Expected output:**
```
✓ Client initialized successfully
  Found X existing store(s)
```

#### Step 3: Create File Search Store

```bash
python demoscript/step3_manage_store.py
```

**What it does:**
- Lists all existing file search stores
- Creates a new store if it doesn't exist
- Displays store information

**Expected output:**
```
✓ Successfully created store:
  Name: fileSearchStores/...
  Display Name: demo-file-store
```

#### Step 4: Upload Files to Store

```bash
python demoscript/step4_upload_files.py
```

**What it does:**
- Finds files in the `data/` directory
- Uploads each file to the file search store
- Extracts metadata (title, author, abstract) using Gemini
- Handles duplicate detection and replacement

**Expected output:**
```
Uploading story.md for metadata extraction...
Title: Republic Day: A Celebration of Democracy
Author: ...
Abstract: ...
✓ story.md successfully uploaded and indexed
```

#### Step 5: Query the Store (Verify RAG Works)

```bash
python demoscript/step5_query_store.py
```

**What it does:**
- Queries the file search store with example questions
- Demonstrates RAG functionality
- Shows how the File Search Tool retrieves relevant information

**Expected output:**
```
Question: When did India become a republic?

Response:
India became a republic on January 26, 1950...
```

**Or run all steps at once:**

```bash
python demoscript/run_all.py
```

**Or using Make:**

```bash
make run-all
```

---

### Part 3: The RAG Agent (With File Search Store)

Now let's test the RAG-enabled agent that uses the File Search Store.

#### The Code

Take a look at `app/sdk_rag_agent.py`. It:
- Instantiates a `genai.Client()`
- Retrieves the File Search Store we created
- Attaches the File Search Tool to the agent
- **Now has RAG capabilities!**

#### Running the RAG Agent

**Using Make:**
```bash
make test-rag-agent
```

**Or directly:**
```bash
python app/sdk_rag_agent.py
```

#### Test: Story-Specific Questions (Should Work!)

Now ask the same questions that failed before:

```
> When did India become a republic?
```

**Expected Result:** The agent should answer correctly using information from your uploaded story!

```
> Who was the first President of India?
```

**Expected Result:** Correct answer from the story!

```
> What are the key features of the Republic Day parade?
```

**Expected Result:** Detailed answer based on the uploaded content!

**Notice the difference:**
- ✅ The RAG agent can answer questions about your custom content
- ✅ It shows grounding information (chunks found from File Search)
- ✅ Answers are accurate and based on your uploaded story

Type `quit` or `exit` to exit the agent.

---

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
make help          # Show available commands
make setup         # Create venv and install dependencies
make install       # Install dependencies (venv must be activated)
make run-all       # Run all demo steps
make test-agent    # Run basic agent (Google Search only)
make test-rag-agent # Run RAG agent (File Search Store)
make clean         # Remove virtual environment
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

1. ✓ Basic agent works for general questions but fails on story questions
2. ✓ Environment configured
3. ✓ Client initialized
4. ✓ Store created
5. ✓ File uploaded and indexed
6. ✓ Queries returning answers based on the Republic Day story
7. ✓ RAG agent successfully answers story-specific questions!

The File Search Store enables RAG to retrieve relevant information from your uploaded story and answer questions accurately!

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
