# Environment Setup

This document outlines the steps to set up the development environment for the OWL project.

## 1. Python Installation

**Cue Words:**
- Install Python 3.10, 3.11, or 3.12
- Verify Python installation
- Check Python version compatibility

**Testing Method:**
- Run `python --version` to verify the installed Python version
- Ensure the version is 3.10, 3.11, or 3.12

## 2. Virtual Environment Setup

**Cue Words:**
- Choose environment management tool (uv, venv, conda)
- Create virtual environment
- Activate virtual environment
- Verify environment isolation

**Testing Method:**
- Check that the virtual environment is active by running `which python`
- Verify that the path points to the virtual environment's Python interpreter

## 3. Repository Setup

**Cue Words:**
- Clone project repository
- Navigate to project directory
- Verify repository structure
- Set up version control

**Testing Method:**
- Verify the repository structure with `ls -la`
- Ensure all necessary directories and files are present
- Check git status with `git status`

## 4. Dependency Installation

**Cue Words:**
- Install core dependencies
- Install CAMEL framework
- Install additional required packages
- Configure dependency versions

**Testing Method:**
- Create a test script to import key dependencies
- Run the script to verify all imports work without errors
- Check installed package versions with `pip list`

## 5. API Key Configuration

**Cue Words:**
- Create .env file from template
- Configure API keys for services
- Set up environment variables
- Verify API key access

**Testing Method:**
- Create a test script that attempts to access API keys from environment
- Verify keys are properly loaded without exposing them
- Test connection to required services

## 6. Node.js Installation (for MCP)

**Cue Words:**
- Install Node.js
- Verify Node.js installation
- Install npm packages
- Configure npm environment

**Testing Method:**
- Run `node --version` and `npm --version` to verify installations
- Test npm package installation with a simple package

## 7. Playwright Installation

**Cue Words:**
- Install Playwright
- Configure browser automation
- Install browser dependencies
- Verify browser control

**Testing Method:**
- Run `playwright install-deps` to verify installation
- Create a simple Playwright test script to verify browser automation works

## 8. Docker Setup (Optional)

**Cue Words:**
- Install Docker
- Configure Docker environment
- Build Docker image
- Test Docker container

**Testing Method:**
- Verify Docker installation with `docker --version`
- Test Docker container functionality with a simple container run
- Verify access to mounted volumes

## 9. Environment Verification

**Cue Words:**
- Run environment verification script
- Check all components
- Verify system compatibility
- Test basic functionality

**Testing Method:**
- Use the comprehensive test scripts in the `testing` directory:
  - `test_environment.py`: Verifies all environment components
  - `test_dependencies.py`: Checks all required dependencies
  - `test_api_keys.py`: Verifies API key configuration
  - `test_playwright.py`: Tests Playwright installation and browser automation
- Run all tests with the `run_all_tests.sh` script
- Check for any errors or warnings in the test output
- Document any issues for troubleshooting 