# Install and Run Examples in This Repo

## Initial Setup

First, install **PyCharm** on your machine.

Then set up a new Python project. It will ask for setup. Install **Python 3.11** and ask it to install **Poetry** via pip.

## Install SmoLAgents

```bash
poetry add smolagents --extras toolkit
```

### Handling the API Key Error

You might encounter this error:
```
You must provide an api_key to work with nebius API or log in with `hf auth login`.
```

**Solution:**

1. Create a **Hugging Face account**
2. Click on your **profile icon** (top right) and select **"Access Tokens"** from the menu
3. **Generate a new token** and copy it to a safe location locally
4. Run the following command in PyCharm terminal:
   ```bash
   hf auth login
   ```
5. Enter your access token when prompted

Now you can use Hugging Face services.

### Cost Considerations

This setup will allow you to run `smol_agent1.py` for a few times, but then it will start asking for payment.

**Options:**
- **Option 1:** Pay for credits in your Hugging Face account
- **Option 2:** Run the LLM locally on your laptop (recommended)

## Local LLM Setup with Ollama

### Install Ollama

```bash
poetry add ollama
```

### Start Ollama Server

**Method 1: Automatic (Recommended)**
- On Windows/Mac, Ollama typically starts automatically after installation and runs in the background

**Method 2: Manual Start**
- If it's not running, open terminal/command prompt and run:
  ```bash
  ollama serve
  ```
- This starts the Ollama server on `http://localhost:11434`

### Important Notes

- Make sure Ollama is running on the **latest version**
- If needed, uninstall and install the latest from their website
- Sometimes a **laptop restart** may be required

### Install a Local LLM Model

We want to run a small LLM locally. We'll use **Llama 3.2:3b** from Meta:

```bash
ollama pull llama3.2:3b
```

### Interactive Testing

You can test Ollama interactively by typing:
```bash
ollama
```

This runs Ollama in an interactive shell.

### Install Additional Dependencies

```bash
poetry add "smolagents[litellm,toolkit]"
```

### Verify Installation

Use this command to see all installed packages:
```bash
poetry show
```

## Example 4 Onwards

From **Example 4** onwards, we transition to a local chatbot that runs in a web browser. We used **Claude AI** to convert our Example 3 code into a **Streamlit server**, which provides a user-friendly web interface for interacting with our SmoLAgents setup.