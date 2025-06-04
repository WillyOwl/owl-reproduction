# OWL Project Test Scripts

This directory contains test scripts to verify the proper installation and configuration of the OWL project. These scripts help ensure that all dependencies are correctly installed and that the environment is properly set up.

## Available Test Scripts

### 1. Dependency Test (`test_dependencies.py`)

This script tests if all required dependencies for the OWL project are properly installed.

**Usage:**
```bash
python test_dependencies.py
```

**What it tests:**
- Core dependencies (camel-ai, gradio, dotenv, etc.)
- Toolkit dependencies (docx2markdown, xmltodict, etc.)
- Additional common dependencies (numpy, pandas, playwright, etc.)

**Output:**
- List of successfully imported dependencies
- List of failed imports
- Summary of test results
- Python and CAMEL versions

### 2. OWL Functionality Test (`test_owl_functionality.py`)

This script tests the key functionality of the OWL framework by attempting to import and instantiate core components.

**Usage:**
```bash
python test_owl_functionality.py
```

**What it tests:**
- Core OWL components
- CAMEL framework integration
- Toolkit availability
- Model platform availability

**Output:**
- Status of each component test
- Summary of test results
- Environment information
- Detailed failure information (if any)

### 3. API Key Configuration Test (`test_api_keys.py`)

This script tests if the required API keys are properly configured in the environment.

**Usage:**
```bash
python test_api_keys.py
```

**What it tests:**
- Required API keys (OpenAI API key)
- Optional API keys (Anthropic, Google, Azure, etc.)

**Output:**
- Status of each API key
- Summary of configured keys
- Recommendations for missing keys

## Running All Tests

To run all tests in sequence, you can use the following command:

```bash
for test in test_dependencies.py test_owl_functionality.py test_api_keys.py; do
    echo -e "\n\n===== Running $test =====\n"
    python $test
    echo -e "\n===== Finished $test =====\n"
done
```

## Interpreting Test Results

- **Green checkmarks (✓)** indicate successful tests
- **Red crosses (✗)** indicate failed tests
- Each script will provide a summary of test results at the end
- Non-zero exit codes are returned if critical tests fail

## Troubleshooting

If any tests fail, consider the following:

1. **Dependency failures**: Ensure all required packages are installed with the correct versions
   ```bash
   pip install -r requirements.txt --use-pep517
   ```

2. **API key issues**: Check that your `.env` file contains the necessary API keys
   ```bash
   cp .env_template .env
   # Edit .env with your API keys
   ```

3. **Import errors**: Ensure the OWL package is properly installed
   ```bash
   pip install -e .
   ```

4. **Path issues**: Make sure you're running the tests from the correct directory
   ```bash
   cd /path/to/owl
   python docs/test_dependencies.py
   ``` 