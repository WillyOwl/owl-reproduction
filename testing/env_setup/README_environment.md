# OWL Environment Verification

This document provides instructions for using the environment verification script to ensure your system is properly set up for the OWL project.

## Overview

The `test_environment.py` script performs comprehensive testing of your environment setup for the OWL project, verifying all components except Docker setup. It checks:

1. Python version compatibility
2. Virtual environment setup
3. Repository structure
4. Dependency installation
5. API key configuration
6. Node.js installation
7. Playwright installation
8. System compatibility

## Prerequisites

Before running the verification script, ensure you have:

1. Installed Python 3.10, 3.11, or 3.12
2. Set up a virtual environment (using uv, venv, or conda)
3. Installed the required dependencies
4. Configured API keys in a `.env` file

## Running the Verification

To run the environment verification:

```bash
python test_environment.py
```

The script will run all tests and provide a detailed report of the results.

## Understanding the Results

The verification script uses color-coded output to indicate the status of each test:

- **Green (PASSED)**: The component is properly configured
- **Red (FAILED)**: The component has issues that need to be addressed
- **Yellow (SKIPPED)**: The test was skipped due to dependencies not being met

At the end of the verification, a summary is displayed showing the total number of tests, along with how many passed, failed, or were skipped.

## Fixing Common Issues

### Python Version Issues

If the Python version test fails, install a compatible version (3.10, 3.11, or 3.12):

```bash
# For Ubuntu/Debian
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip

# For macOS with Homebrew
brew install python@3.10
```

### Virtual Environment Issues

If the virtual environment test fails, set up a virtual environment:

```bash
# Using venv
python3.10 -m venv .venv
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows

# Using uv
pip install uv
uv venv .venv --python=3.10
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows

# Using conda
conda create -n owl python=3.10
conda activate owl
```

### Dependency Issues

If dependency tests fail, install the missing dependencies:

```bash
# Install from requirements.txt
pip install -r requirements.txt --use-pep517

# Or install as a package
pip install -e .
```

### API Key Issues

If API key tests fail, create or update your `.env` file:

```bash
cp .env_template .env
# Edit .env with your API keys
```

### Node.js Issues

If Node.js tests fail, install Node.js and npm:

```bash
# For Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm -y

# For macOS with Homebrew
brew install node

# For Windows
# Download from https://nodejs.org/
```

### Playwright Issues

If Playwright tests fail, install Playwright and its dependencies:

```bash
# Install Playwright
pip install playwright

# Install browser binaries
python -m playwright install

# Install system dependencies (Linux only)
playwright install-deps
```

## Additional Notes

- The script checks for both required and optional API keys
- Memory and disk space checks ensure your system has enough resources
- Repository structure checks verify that all essential files and directories are present

If all tests pass, your environment is properly set up and ready to use the OWL framework. 