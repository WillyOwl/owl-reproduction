#!/usr/bin/env python3
"""
OWL Environment Verification Script

This script performs comprehensive testing of the OWL project environment setup,
verifying all components except Docker setup.
"""

import os
import sys
import subprocess
import platform
import importlib
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
import json

# Define color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Test result counters
TOTAL_TESTS = 0
PASSED_TESTS = 0
FAILED_TESTS = 0
SKIPPED_TESTS = 0

def print_header(message: str) -> None:
    """Print a formatted header message"""
    print(f"\n{YELLOW}{BOLD}{message}{RESET}")
    print("=" * 60)

def print_subheader(message: str) -> None:
    """Print a formatted subheader message"""
    print(f"\n{CYAN}{message}{RESET}")
    print("-" * 60)

def print_result(test_name: str, success: bool, message: str = "", skip: bool = False) -> None:
    """Print a formatted test result"""
    global TOTAL_TESTS, PASSED_TESTS, FAILED_TESTS, SKIPPED_TESTS
    
    TOTAL_TESTS += 1
    
    if skip:
        status = f"{YELLOW}SKIPPED{RESET}"
        SKIPPED_TESTS += 1
    elif success:
        status = f"{GREEN}PASSED{RESET}"
        PASSED_TESTS += 1
    else:
        status = f"{RED}FAILED{RESET}"
        FAILED_TESTS += 1
    
    print(f"{status} - {test_name}")
    if message:
        print(f"       {message}")

def run_command(command, capture_output=True, shell=False) -> Tuple[bool, str, str]:
    """Run a shell command and return the result"""
    try:
        if shell:
            if isinstance(command, list):
                command = " ".join(command)
        
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE if capture_output else None,
            stderr=subprocess.PIPE if capture_output else None,
            text=True,
            check=False,
            shell=shell
        )
        
        success = result.returncode == 0
        stdout = result.stdout if capture_output else ""
        stderr = result.stderr if capture_output else ""
        
        return success, stdout, stderr
    except Exception as e:
        return False, "", str(e)

def check_python_version() -> None:
    """Test Python version compatibility"""
    print_subheader("Python Version Check")
    
    python_version = platform.python_version()
    major, minor, _ = map(int, python_version.split("."))
    
    success = (major == 3 and minor >= 10 and minor <= 12)
    message = f"Python {python_version} detected"
    
    if not success:
        message += f" - {RED}Python 3.10, 3.11, or 3.12 is required{RESET}"
    
    print_result("Python version compatibility", success, message)

def check_virtual_environment() -> None:
    """Test virtual environment setup"""
    print_subheader("Virtual Environment Check")
    
    # Check if running in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if in_venv:
        venv_path = sys.prefix
        message = f"Virtual environment active at: {venv_path}"
        success = True
    else:
        message = "Not running in a virtual environment"
        success = False
    
    print_result("Virtual environment active", success, message)

def check_repository_structure() -> None:
    """Test repository structure"""
    print_subheader("Repository Structure Check")
    
    # Get the repository root directory
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    
    # Essential directories and files to check
    essential_items = [
        ("owl", "directory"),
        ("examples", "directory"),
        ("docs", "directory"),
        ("pyproject.toml", "file"),
        ("requirements.txt", "file"),
        ("README.md", "file")
    ]
    
    for item_name, item_type in essential_items:
        item_path = repo_root / item_name
        
        if item_type == "directory":
            exists = item_path.is_dir()
        else:
            exists = item_path.is_file()
        
        print_result(
            f"Repository {item_type} '{item_name}'",
            exists,
            f"Path: {item_path}" if exists else f"Missing: {item_path}"
        )

def check_dependencies() -> None:
    """Test dependency installation"""
    print_subheader("Dependency Check")
    
    # Core dependencies to check
    dependencies = [
        ("camel", "camel-ai"),
        ("gradio", "gradio"),
        ("dotenv", "python-dotenv"),
        ("docx2markdown", "docx2markdown"),
        ("xmltodict", "xmltodict"),
        ("firecrawl", "firecrawl"),
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("playwright", "playwright"),
        ("requests", "requests"),
        ("PIL", "pillow")
    ]
    
    for module_name, package_name in dependencies:
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, "__version__", "unknown version")
            print_result(
                f"Dependency '{package_name}'",
                True,
                f"Version: {version}"
            )
        except ImportError as e:
            print_result(
                f"Dependency '{package_name}'",
                False,
                f"Error: {str(e)}"
            )

def check_api_keys() -> None:
    """Test API key configuration"""
    print_subheader("API Key Configuration Check")
    
    # Required API keys
    required_keys = [
        "OPENAI_API_KEY"
    ]
    
    # Optional but common API keys
    optional_keys = [
        "GOOGLE_API_KEY",
        "GEMINI_API_KEY",
        "AZURE_OPENAI_API_KEY",
    ]
    
    # Load environment variables from .env file if it exists
    env_files_loaded = []
    
    # Try to load from the repository root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    
    env_file = repo_root / ".env"
    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=str(env_file))
            env_files_loaded.append(str(env_file))
        except ImportError:
            pass
    
    # Try to load from the owl directory
    owl_env_file = repo_root / "owl" / ".env"
    if owl_env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=str(owl_env_file))
            env_files_loaded.append(str(owl_env_file))
        except ImportError:
            pass
    
    if env_files_loaded:
        print(f"{BLUE}Loaded environment variables from: {', '.join(env_files_loaded)}{RESET}")
    
    # Check required API keys
    for key in required_keys:
        value = os.environ.get(key, "")
        has_key = bool(value)
        
        # Mask the API key value for security
        masked_value = "********" if has_key else "Not set"
        
        print_result(
            f"Required API key '{key}'",
            has_key,
            f"Value: {masked_value}"
        )
    
    # Check optional API keys
    for key in optional_keys:
        value = os.environ.get(key, "")
        has_key = bool(value)
        
        # Mask the API key value for security
        masked_value = "********" if has_key else "Not set"
        
        print_result(
            f"Optional API key '{key}'",
            True,  # Always pass for optional keys
            f"Value: {masked_value}"
        )

def check_nodejs() -> None:
    """Test Node.js installation"""
    print_subheader("Node.js Installation Check")
    
    # Check if Node.js is installed
    success, stdout, stderr = run_command(["node", "--version"], shell=False)
    
    if success:
        node_version = stdout.strip()
        print_result("Node.js installation", True, f"Version: {node_version}")
    else:
        print_result("Node.js installation", False, "Node.js is not installed or not in PATH")
    
    # Check if npm is installed
    success, stdout, stderr = run_command(["npm", "--version"], shell=False)
    
    if success:
        npm_version = stdout.strip()
        print_result("npm installation", True, f"Version: {npm_version}")
    else:
        print_result("npm installation", False, "npm is not installed or not in PATH")
    
    # Check for MCP server
    success, stdout, stderr = run_command(["npm", "list", "-g", "@executeautomation/playwright-mcp-server"], shell=False)
    
    if "playwright-mcp-server" in stdout:
        print_result("MCP server installation", True, "Playwright MCP server is installed globally")
    else:
        print_result(
            "MCP server installation",
            False,
            "Playwright MCP server is not installed. Install with: npm install -g @executeautomation/playwright-mcp-server"
        )

def check_playwright() -> None:
    """Test Playwright installation"""
    print_subheader("Playwright Installation Check")
    
    # Check if Playwright module is installed
    try:
        import playwright
        playwright_version = getattr(playwright, "__version__", "unknown version")
        print_result("Playwright Python package", True, f"Version: {playwright_version}")
    except ImportError:
        print_result(
            "Playwright Python package",
            False,
            "Playwright is not installed. Install with: pip install playwright"
        )
        # Skip other Playwright tests if the module is not installed
        print_result("Playwright browser binaries", False, "Skipped due to missing Playwright package", skip=True)
        print_result("Playwright browser launch", False, "Skipped due to missing Playwright package", skip=True)
        return
    
    # Check if browser binaries are installed
    success, stdout, stderr = run_command(["playwright", "install", "--help"], shell=False)
    
    if not success:
        print_result(
            "Playwright CLI",
            False,
            "Playwright CLI is not available. Try reinstalling Playwright."
        )
        print_result("Playwright browser binaries", False, "Skipped due to missing Playwright CLI", skip=True)
        print_result("Playwright browser launch", False, "Skipped due to missing Playwright CLI", skip=True)
        return
    
    # Try to launch a browser to check if binaries are installed
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=True)
                browser.close()
                print_result("Playwright browser launch", True, "Successfully launched Chromium browser")
            except Exception as e:
                print_result(
                    "Playwright browser launch",
                    False,
                    f"Failed to launch browser: {str(e)}. Try running: python -m playwright install"
                )
    except Exception as e:
        print_result(
            "Playwright browser launch",
            False,
            f"Error: {str(e)}"
        )

def check_system_compatibility() -> None:
    """Test system compatibility"""
    print_subheader("System Compatibility Check")
    
    # Check operating system
    os_name = platform.system()
    os_version = platform.version()
    
    print_result("Operating System", True, f"{os_name} {os_version}")
    
    # Check Python implementation
    py_implementation = platform.python_implementation()
    
    print_result("Python Implementation", True, py_implementation)
    
    # Check available memory
    try:
        import psutil
        memory = psutil.virtual_memory()
        available_gb = memory.available / (1024 ** 3)
        total_gb = memory.total / (1024 ** 3)
        
        sufficient_memory = available_gb >= 2.0  # Require at least 2GB available
        
        print_result(
            "Available Memory",
            sufficient_memory,
            f"{available_gb:.1f}GB available out of {total_gb:.1f}GB total"
        )
    except ImportError:
        print_result("Available Memory", True, "psutil not installed, skipping memory check", skip=True)
    
    # Check disk space
    try:
        disk_usage = shutil.disk_usage(Path.home())
        free_gb = disk_usage.free / (1024 ** 3)
        total_gb = disk_usage.total / (1024 ** 3)
        
        sufficient_disk = free_gb >= 5.0  # Require at least 5GB free
        
        print_result(
            "Available Disk Space",
            sufficient_disk,
            f"{free_gb:.1f}GB free out of {total_gb:.1f}GB total"
        )
    except Exception as e:
        print_result("Available Disk Space", True, f"Error checking disk space: {str(e)}", skip=True)

def print_summary() -> None:
    """Print a summary of the test results"""
    print_header("Environment Verification Summary")
    
    print(f"Total tests:    {TOTAL_TESTS}")
    print(f"Passed tests:   {GREEN}{PASSED_TESTS}{RESET}")
    print(f"Failed tests:   {RED}{FAILED_TESTS}{RESET}")
    print(f"Skipped tests:  {YELLOW}{SKIPPED_TESTS}{RESET}")
    
    if FAILED_TESTS == 0:
        print(f"\n{GREEN}{BOLD}All tests passed! Your environment is properly set up for OWL.{RESET}")
    else:
        print(f"\n{YELLOW}{BOLD}Some tests failed. Please fix the issues before using OWL.{RESET}")

def main() -> int:
    """Main function to run all environment verification tests"""
    print_header("OWL Environment Verification")
    print(f"Running comprehensive environment verification for OWL project...")
    
    # Run all verification tests
    check_python_version()
    check_virtual_environment()
    check_repository_structure()
    check_dependencies()
    check_api_keys()
    check_nodejs()
    check_playwright()
    check_system_compatibility()
    
    # Print summary
    print_summary()
    
    # Return non-zero exit code if any tests failed
    return 1 if FAILED_TESTS > 0 else 0

if __name__ == "__main__":
    sys.exit(main()) 