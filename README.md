# llm-proofreader
Microservice to send emails to authors with suggestions.

## Getting started - For WSL/ Linux/ MacOS

Python version: 3.12.7 (Easily install using pyenv)

Navigate to this directory in the terminal.

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```

Afterwards, install all the requirements.

```bash
pip install -r requirements.txt
```

Make a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Fill the `.env` with valid values.


Run the `main.py` file:

```bash
python main.py
```