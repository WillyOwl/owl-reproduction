#!/usr/bin/env python3
"""
Simple script to check environment variables and .env file loading
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    print("Checking environment variables and .env files...")
    
    # Print current working directory
    cwd = Path.cwd()
    print(f"Current working directory: {cwd}")
    
    # Check for .env file in current directory
    env_file = cwd / ".env"
    if env_file.exists():
        print(f".env file found in current directory: {env_file}")
        load_dotenv(dotenv_path=env_file)
        print("Loaded .env from current directory")
    else:
        print(f"No .env file found in current directory")
    
    # Check for .env file in owl/owl directory
    owl_owl_env = Path("/home/willyowl/owl/owl/.env")
    if owl_owl_env.exists():
        print(f".env file found in owl/owl directory: {owl_owl_env}")
        load_dotenv(dotenv_path=owl_owl_env)
        print("Loaded .env from owl/owl directory")
    else:
        print(f"No .env file found in owl/owl directory")
    
    # Check for .env file in owl directory
    owl_env = Path("/home/willyowl/owl/.env")
    if owl_env.exists():
        print(f".env file found in owl directory: {owl_env}")
        load_dotenv(dotenv_path=owl_env)
        print("Loaded .env from owl directory")
    else:
        print(f"No .env file found in owl directory")
    
    # Check if OPENAI_API_KEY is set
    openai_key = os.environ.get("OPENAI_API_KEY")
    if openai_key:
        print("OPENAI_API_KEY is set in environment variables")
        # Print first few characters of the key for verification (safely)
        masked_key = openai_key[:4] + "*" * (len(openai_key) - 4)
        print(f"Key starts with: {masked_key}")
    else:
        print("OPENAI_API_KEY is NOT set in environment variables")
    
    # Print all environment variables (for debugging)
    print("\nAll environment variables:")
    for key, value in os.environ.items():
        if "API_KEY" in key:
            # Mask API keys for security
            masked_value = value[:4] + "*" * (len(value) - 4) if value else "(empty)"
            print(f"{key}={masked_value}")

if __name__ == "__main__":
    main() 