# 🛒 Product Price Checker with LangChain & Streamlit

A simple LLM-powered app that checks product prices and provides insights via a Streamlit frontend.

## 🔐 Prerequisites

Before getting started, make sure you have the following:

* **LangSmith API Key**
  Get it from [LangSmith](https://smith.langchain.com)

* **OpenAI API Key**
  Sign up at [OpenAI](https://platform.openai.com/signup) and generate your key

## ⚙️ Project Setup Using `uv`

We'll use [`uv`](https://github.com/astral-sh/uv) — a fast Python package manager — for managing dependencies and virtual environments.

### 1. Install `uv`

```bash
pip install uv
```

### 2. Initialize the Project

Navigate to your project folder and run:

```bash
uv init
```

This will automatically:

* Create a `.venv` virtual environment
* Generate a `pyproject.toml`
* Manage dependencies cleanly (no need for `requirements.txt`)

### 3. Install Dependencies

Install packages using `uv add`:

```bash
uv add langchain
uv add streamlit
uv add python-dotenv
```

### 4. Install Ruff for Linting & Formatting

```bash
uv tool install ruff
uv tool update-shell
# Restart your shell afterwards
```

To automatically fix formatting and lint issues:

```bash
ruff check --fix .
```

### 5. Set Environment Variables

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

## 🧠 Build the App

Create a simple **Product Price Checker** using LangChain for LLM calls. Use Streamlit for the frontend.

Your main app entry point should be `main.py`.

## ▶️ Run the App

Activate your virtual environment:

```bash
source .venv/bin/activate
```

Then launch the Streamlit UI:

```bash
streamlit run main.py
```

Certainly! Here's the properly formatted and polished version of that section:

---

## 📊 Monitor Your Usage

Gain deeper insights into your application's performance, LLM traces, and usage analytics by visiting the [**LangSmith UI**](https://smith.langchain.com).

---


