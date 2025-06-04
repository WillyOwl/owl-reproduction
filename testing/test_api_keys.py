#!/usr/bin/env python3
"""
Simplified API Key Configuration Test Script

This script tests the API key configuration for the OWL project by checking
if the required API keys are set in the environment variables. It only checks
the .env file in the /home/willyowl/owl/ directory.
"""

import os
import sys
from typing import Dict, List, Tuple
from pathlib import Path
from dotenv import load_dotenv

# Define color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Define the required API keys
REQUIRED_KEYS = [
    "OPENAI_API_KEY",  # OpenAI API key (required for most examples)
]

# Define the optional API keys
OPTIONAL_KEYS = [
    "ANTHROPIC_API_KEY",      # Anthropic API key (for Claude models)
    "GOOGLE_API_KEY",         # Google API key (for search, etc.)
    "GOOGLE_CSE_ID",          # Google Custom Search Engine ID
    "BING_SEARCH_V7_KEY",     # Bing Search API key
    "BING_SEARCH_V7_ENDPOINT", # Bing Search API endpoint
    "SERPAPI_API_KEY",        # SerpAPI key (for search)
    "GEMINI_API_KEY",         # Google Gemini API key
    "AZURE_OPENAI_API_KEY",   # Azure OpenAI API key
    "AZURE_OPENAI_ENDPOINT",  # Azure OpenAI endpoint
    "MISTRAL_API_KEY",        # Mistral AI API key
    "NOVITA_API_KEY",         # Novita AI API key
    "TOGETHER_API_KEY",       # Together AI API key
    "GROQ_API_KEY",           # Groq API key
    "QWEN_API_KEY",           # Qwen API key
    "PPIO_API_KEY",           # PPIO API key
    "DEEPSEEK_API_KEY",       # Deepseek API key
    "OPENROUTER_API_KEY",     # OpenRouter API key
    "VOLCENGINE_ACCESS_KEY",  # Volcengine access key
    "VOLCENGINE_SECRET_KEY",  # Volcengine secret key
]

def load_env_files() -> List[str]:
    """
    Load environment variables from .env files
    
    Returns:
        List of paths to loaded .env files
    """
    loaded_files = []
    
    # Only check the project root .env file
    owl_root_env = Path("/home/willyowl/owl/owl/.env")
    if owl_root_env.exists():
        load_dotenv(dotenv_path=owl_root_env)
        loaded_files.append(str(owl_root_env))
    
    return loaded_files

def check_api_keys() -> Tuple[Dict[str, bool], Dict[str, bool]]:
    """
    Check if the required and optional API keys are set
    
    Returns:
        Tuple of (required_keys_status, optional_keys_status)
    """
    required_keys_status = {}
    optional_keys_status = {}
    
    # Check required keys
    for key in REQUIRED_KEYS:
        required_keys_status[key] = key in os.environ and bool(os.environ[key])
    
    # Check optional keys
    for key in OPTIONAL_KEYS:
        optional_keys_status[key] = key in os.environ and bool(os.environ[key])
    
    return required_keys_status, optional_keys_status

def print_key_status(key: str, is_set: bool, is_required: bool) -> None:
    """Print the status of an API key"""
    status = f"{GREEN}✓ Set{RESET}" if is_set else f"{RED}✗ Not set{RESET}"
    required = f"{RED}(Required){RESET}" if is_required and not is_set else ""
    print(f"  {key}: {status} {required}")

def main() -> int:
    """Main function to check API key configuration"""
    print(f"\n{YELLOW}OWL Project API Key Configuration Test{RESET}")
    print("=" * 50)
    
    # Load environment variables
    loaded_files = load_env_files()
    if loaded_files:
        print(f"\n{BLUE}Loaded environment variables from:{RESET}")
        for file in loaded_files:
            print(f"  - {file}")
    else:
        print(f"\n{YELLOW}Warning: No .env files found{RESET}")
        print("  Environment variables should be set directly in the system environment")
    
    # Check API keys
    required_keys_status, optional_keys_status = check_api_keys()
    
    # Print required keys status
    print(f"\n{YELLOW}Required API Keys:{RESET}")
    for key, is_set in required_keys_status.items():
        print_key_status(key, is_set, True)
    
    # Print optional keys status
    print(f"\n{YELLOW}Optional API Keys:{RESET}")
    for key, is_set in optional_keys_status.items():
        print_key_status(key, is_set, False)
    
    # Print summary
    required_set = sum(1 for is_set in required_keys_status.values() if is_set)
    optional_set = sum(1 for is_set in optional_keys_status.values() if is_set)
    
    print("\n" + "=" * 50)
    print(f"{YELLOW}Summary:{RESET}")
    print(f"  Required API keys: {required_set}/{len(required_keys_status)} configured")
    print(f"  Optional API keys: {optional_set}/{len(optional_keys_status)} configured")
    
    # Print recommendations
    if required_set < len(required_keys_status):
        print(f"\n{RED}Some required API keys are missing!{RESET}")
        print("  Please set the required API keys to use the OWL framework")
        print("  You can set them in a .env file or directly in the environment")
    
    if optional_set < len(optional_keys_status):
        print(f"\n{YELLOW}Note:{RESET} Some optional API keys are not set")
        print("  These keys are only needed for specific features")
        print("  Set them if you plan to use the corresponding features")
    
    # Return non-zero exit code if any required keys are missing
    return 0 if required_set == len(required_keys_status) else 1

if __name__ == "__main__":
    sys.exit(main()) 