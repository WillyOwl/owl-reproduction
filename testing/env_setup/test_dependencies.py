#!/usr/bin/env python3
"""
Dependency Test Script for OWL Project

This script attempts to import all key dependencies required by the OWL project
and reports success or failure for each import. It helps verify that the
environment is properly set up with all necessary packages.
"""

import sys
import importlib
from typing import Dict, List, Tuple

# Define color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Define the key dependencies to test
# Format: (package_name, [module_names_to_import])
DEPENDENCIES = [
    # Core dependencies
    ("camel-ai", ["camel"]),
    ("gradio", ["gradio"]),
    ("dotenv", ["dotenv"]),
    
    # Toolkit dependencies
    ("docx2markdown", ["docx2markdown"]),
    ("xmltodict", ["xmltodict"]),
    ("firecrawl", ["firecrawl"]),
    ("mcp-simple-arxiv", ["mcp_simple_arxiv"]),
    ("mcp-server-fetch", ["mcp_server_fetch"]),
    
    # Additional common dependencies
    ("numpy", ["numpy"]),
    ("pandas", ["pandas"]),
    ("playwright", ["playwright"]),
    ("requests", ["requests"]),
    ("pillow", ["PIL"]),
]

def test_import(module_name: str) -> Tuple[bool, str]:
    """
    Test importing a specific module
    
    Args:
        module_name: Name of the module to import
        
    Returns:
        Tuple of (success, error_message)
    """
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown version")
        return True, f"{module_name} ({version})"
    except ImportError as e:
        return False, str(e)

def main():
    """Main function to test all dependencies"""
    print(f"\n{YELLOW}OWL Project Dependency Test{RESET}")
    print("=" * 50)
    
    results: Dict[str, List[Tuple[str, bool, str]]] = {
        "success": [],
        "failure": []
    }
    
    # Test each dependency
    for package_name, modules in DEPENDENCIES:
        for module_name in modules:
            success, message = test_import(module_name)
            if success:
                results["success"].append((package_name, True, message))
            else:
                results["failure"].append((package_name, False, message))
    
    # Print results
    print(f"\n{YELLOW}Results:{RESET}")
    print("-" * 50)
    
    # Print successful imports
    if results["success"]:
        print(f"\n{GREEN}Successfully imported:{RESET}")
        for package_name, _, message in results["success"]:
            print(f"  ✓ {package_name}: {message}")
    
    # Print failed imports
    if results["failure"]:
        print(f"\n{RED}Failed imports:{RESET}")
        for package_name, _, message in results["failure"]:
            print(f"  ✗ {package_name}: {message}")
    
    # Print summary
    total = len(results["success"]) + len(results["failure"])
    success_rate = len(results["success"]) / total * 100 if total > 0 else 0
    
    print("\n" + "=" * 50)
    print(f"{YELLOW}Summary:{RESET}")
    print(f"  Total dependencies checked: {total}")
    print(f"  Successfully imported: {len(results['success'])}")
    print(f"  Failed imports: {len(results['failure'])}")
    print(f"  Success rate: {success_rate:.1f}%")
    
    # Check CAMEL version specifically
    try:
        import camel
        print(f"\n{YELLOW}CAMEL version:{RESET} {camel.__version__}")
        print(f"{YELLOW}Python version:{RESET} {sys.version}")
    except ImportError:
        print(f"\n{RED}CAMEL package not found{RESET}")
    
    # Return non-zero exit code if any imports failed
    return 1 if results["failure"] else 0

if __name__ == "__main__":
    sys.exit(main()) 