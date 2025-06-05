# OWL Project Testing Scripts

This directory contains testing scripts to verify the proper installation, configuration, and functionality of the OWL project environment.

## Available Test Scripts

### 1. Environment Verification (`test_environment.py`)

A comprehensive script that verifies all components of the OWL environment setup (except Docker).

**Usage:**
```bash
python test_environment.py
```

**What it tests:**
- Python version compatibility
- Virtual environment setup
- Repository structure
- Dependency installation
- API key configuration
- Node.js installation
- Playwright installation
- System compatibility

**Documentation:**
- See [README_environment.md](README_environment.md) for detailed information

### 2. Playwright Verification (`test_playwright.py`)

A specialized script that focuses on testing Playwright installation and browser automation functionality.

**Usage:**
```bash
python test_playwright.py
```

**What it tests:**
- Playwright module import
- Browser launch capabilities
- Web navigation
- Screenshot capture
- Browser dependencies

**Documentation:**
- See [README_playwright.md](README_playwright.md) for detailed information

### 3. Dependency Test (`test_dependencies.py`)

A script that tests if all required dependencies for the OWL project are properly installed.

**Usage:**
```bash
python test_dependencies.py
```

**What it tests:**
- Core dependencies (camel-ai, gradio, dotenv, etc.)
- Toolkit dependencies (docx2markdown, xmltodict, etc.)
- Additional common dependencies (numpy, pandas, playwright, etc.)

### 4. API Key Configuration Test (`test_api_keys.py`)

A script that tests if the required API keys are properly configured in the environment.

**Usage:**
```bash
python test_api_keys.py
```

**What it tests:**
- Required API keys (OpenAI API key)
- Optional API keys (Anthropic, Google, Azure, etc.)

## Running All Tests

To run all tests in sequence and get a comprehensive verification of your environment, you can use:

```bash
for test in test_dependencies.py test_api_keys.py test_playwright.py test_environment.py; do
    echo -e "\n\n===== Running $test =====\n"
    python $test
    echo -e "\n===== Finished $test =====\n"
done
```

## Test Script Organization

The test scripts are designed to be modular and focused on specific aspects of the environment:

- `test_dependencies.py` - Focuses solely on package dependencies
- `test_api_keys.py` - Focuses solely on API key configuration
- `test_playwright.py` - Focuses solely on Playwright and browser automation
- `test_environment.py` - Comprehensive test that covers all aspects

You can run individual tests based on what you need to verify, or run all tests for a complete verification.

## Troubleshooting

If any tests fail, refer to the specific README file for that test for troubleshooting information. Each test script provides detailed error messages and suggestions for fixing common issues.

For general troubleshooting:

1. Make sure you're running the tests from within your activated virtual environment
2. Check that all dependencies are installed with the correct versions
3. Verify that API keys are properly set in your `.env` file
4. For Playwright issues, ensure browser binaries and system dependencies are installed 