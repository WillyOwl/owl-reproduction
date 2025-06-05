#!/usr/bin/env python3
"""
OWL Functionality Test Script

This script tests the key functionality of the OWL framework by attempting to
import and instantiate core components. This helps verify that the OWL project
is properly installed and configured.
"""

import sys
import importlib
from typing import Dict, List, Tuple, Any, Optional

# Define color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_header(message: str) -> None:
    """Print a formatted header message"""
    print(f"\n{YELLOW}{message}{RESET}")
    print("-" * 50)

def test_import(module_path: str) -> Tuple[bool, Any, str]:
    """
    Test importing a specific module or component
    
    Args:
        module_path: Dot-separated path to the module or component
        
    Returns:
        Tuple of (success, module_object, error_message)
    """
    parts = module_path.split(".")
    
    # Try to import the base module first
    try:
        if len(parts) == 1:
            module = importlib.import_module(parts[0])
            return True, module, f"Successfully imported {module_path}"
        else:
            # Import the parent module
            parent_module = importlib.import_module(".".join(parts[:-1]))
            
            # Try to get the attribute from the parent module
            try:
                attr = getattr(parent_module, parts[-1])
                return True, attr, f"Successfully imported {module_path}"
            except AttributeError as e:
                return False, None, f"Failed to import {module_path}: {str(e)}"
    except ImportError as e:
        return False, None, f"Failed to import {module_path}: {str(e)}"

def test_owl_core() -> List[Tuple[str, bool, str]]:
    """Test core OWL components"""
    print_header("Testing OWL Core Components")
    
    results = []
    
    # Core components to test
    components = [
        "owl",
        "owl.utils",
        "owl.utils.run_society",
        "owl.utils.arun_society",
        "owl.utils.OwlRolePlaying",
        "owl.utils.DocumentProcessingToolkit",
    ]
    
    for component in components:
        success, obj, message = test_import(component)
        print(f"{'✓' if success else '✗'} {component}")
        results.append((component, success, message))
    
    return results

def test_camel_integration() -> List[Tuple[str, bool, str]]:
    """Test CAMEL framework integration"""
    print_header("Testing CAMEL Integration")
    
    results = []
    
    # CAMEL components to test
    components = [
        "camel",
        "camel.societies",
        "camel.societies.RolePlaying",
        "camel.agents",
        "camel.agents.ChatAgent",
        "camel.models",
        "camel.models.ModelFactory",
        "camel.toolkits",
    ]
    
    for component in components:
        success, obj, message = test_import(component)
        print(f"{'✓' if success else '✗'} {component}")
        results.append((component, success, message))
    
    return results

def test_toolkit_availability() -> List[Tuple[str, bool, str]]:
    """Test toolkit availability"""
    print_header("Testing Toolkit Availability")
    
    results = []
    
    # Toolkits to test
    toolkits = [
        "camel.toolkits.SearchToolkit",
        "camel.toolkits.BrowserToolkit",
        "camel.toolkits.CodeExecutionToolkit",
        "camel.toolkits.ImageAnalysisToolkit",
        "camel.toolkits.VideoAnalysisToolkit",
        "camel.toolkits.AudioAnalysisToolkit",
        "camel.toolkits.FileWriteToolkit",
        "camel.toolkits.ExcelToolkit",
        "owl.utils.DocumentProcessingToolkit",
    ]
    
    for toolkit in toolkits:
        success, obj, message = test_import(toolkit)
        print(f"{'✓' if success else '✗'} {toolkit}")
        results.append((toolkit, success, message))
    
    return results

def test_model_platforms() -> List[Tuple[str, bool, str]]:
    """Test model platform availability"""
    print_header("Testing Model Platform Availability")
    
    results = []
    
    try:
        from camel.types import ModelPlatformType
        
        # Get all available model platform types
        platform_types = [platform.name for platform in ModelPlatformType]
        print(f"{BLUE}Available model platforms:{RESET} {', '.join(platform_types)}")
        
        results.append(("ModelPlatformType", True, f"Found {len(platform_types)} platform types"))
    except ImportError as e:
        print(f"{RED}Failed to import ModelPlatformType: {str(e)}{RESET}")
        results.append(("ModelPlatformType", False, str(e)))
    
    return results

def main() -> int:
    """Main function to run all tests"""
    print(f"\n{YELLOW}OWL Framework Functionality Test{RESET}")
    print("=" * 50)
    
    all_results = []
    
    # Run all tests
    all_results.extend(test_owl_core())
    all_results.extend(test_camel_integration())
    all_results.extend(test_toolkit_availability())
    all_results.extend(test_model_platforms())
    
    # Print summary
    success_count = sum(1 for _, success, _ in all_results if success)
    total_count = len(all_results)
    
    print("\n" + "=" * 50)
    print(f"{YELLOW}Test Summary:{RESET}")
    print(f"  Total tests: {total_count}")
    print(f"  Successful tests: {success_count}")
    print(f"  Failed tests: {total_count - success_count}")
    print(f"  Success rate: {success_count / total_count * 100:.1f}%")
    
    # Print environment info
    print(f"\n{YELLOW}Environment Information:{RESET}")
    print(f"  Python version: {sys.version}")
    
    try:
        import camel
        print(f"  CAMEL version: {getattr(camel, '__version__', 'unknown')}")
    except ImportError:
        print(f"  {RED}CAMEL not installed{RESET}")
    
    # Print detailed failure information
    if total_count - success_count > 0:
        print(f"\n{YELLOW}Detailed Failure Information:{RESET}")
        for component, success, message in all_results:
            if not success:
                print(f"  {RED}✗ {component}: {message}{RESET}")
    
    # Return non-zero exit code if any tests failed
    return 0 if success_count == total_count else 1

if __name__ == "__main__":
    sys.exit(main()) 