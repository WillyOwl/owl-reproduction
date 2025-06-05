#!/usr/bin/env python3
"""
Playwright Installation Verification Script

This script tests the Playwright installation and browser automation functionality
by launching a browser, navigating to a website, and capturing a screenshot.
"""

import os
import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Define color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

async def test_playwright():
    """Test Playwright installation and browser automation functionality"""
    try:
        # Import Playwright - this will fail if not installed
        from playwright.async_api import async_playwright
        print(f"{GREEN}✓ Playwright module imported successfully{RESET}")
    except ImportError as e:
        print(f"{RED}✗ Failed to import Playwright: {str(e)}{RESET}")
        print(f"{YELLOW}Hint: Try installing Playwright with 'pip install playwright'{RESET}")
        return False

    # Create output directory for screenshots
    output_dir = Path("./playwright_test_output")
    output_dir.mkdir(exist_ok=True)
    
    screenshot_path = output_dir / f"test_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    
    try:
        async with async_playwright() as p:
            # Test browser launch
            print(f"{YELLOW}Launching Chromium browser...{RESET}")
            browser = await p.chromium.launch(headless=True)
            print(f"{GREEN}✓ Browser launched successfully{RESET}")
            
            # Create a new page
            print(f"{YELLOW}Creating new page...{RESET}")
            page = await browser.new_page()
            print(f"{GREEN}✓ Page created successfully{RESET}")
            
            # Navigate to a website
            print(f"{YELLOW}Navigating to https://example.com...{RESET}")
            await page.goto("https://example.com")
            print(f"{GREEN}✓ Navigation successful{RESET}")
            
            # Get page title
            title = await page.title()
            print(f"{BLUE}Page title: {title}{RESET}")
            
            # Take a screenshot
            print(f"{YELLOW}Taking screenshot...{RESET}")
            await page.screenshot(path=str(screenshot_path))
            print(f"{GREEN}✓ Screenshot saved to {screenshot_path}{RESET}")
            
            # Close the browser
            await browser.close()
            print(f"{GREEN}✓ Browser closed successfully{RESET}")
            
            return True
    except Exception as e:
        print(f"{RED}✗ Playwright test failed: {str(e)}{RESET}")
        
        # Check if this is a browser binary missing error
        if "Executable doesn't exist" in str(e):
            print(f"{YELLOW}Hint: You may need to install browser binaries with:{RESET}")
            print(f"{YELLOW}  python -m playwright install{RESET}")
        
        return False

async def test_browser_dependencies():
    """Test if browser dependencies are installed"""
    try:
        # Import Playwright
        from playwright.async_api import async_playwright
        
        print(f"{YELLOW}Checking browser dependencies...{RESET}")
        
        # Try to launch each browser type briefly to check dependencies
        async with async_playwright() as p:
            for browser_type_name, browser_type in [
                ("Chromium", p.chromium),
                ("Firefox", p.firefox),
                ("WebKit", p.webkit)
            ]:
                try:
                    browser = await browser_type.launch(headless=True)
                    await browser.close()
                    print(f"{GREEN}✓ {browser_type_name} browser dependencies installed{RESET}")
                except Exception as e:
                    print(f"{RED}✗ {browser_type_name} browser dependencies missing: {str(e)}{RESET}")
                    print(f"{YELLOW}Hint: Run 'playwright install-deps' to install system dependencies{RESET}")
                    print(f"{YELLOW}      Run 'playwright install {browser_type_name.lower()}' to install browser{RESET}")
        
        return True
    except Exception as e:
        print(f"{RED}✗ Failed to check browser dependencies: {str(e)}{RESET}")
        return False

async def main():
    """Main function to run all tests"""
    print(f"\n{YELLOW}Playwright Installation Verification{RESET}")
    print("=" * 50)
    
    # Test Playwright functionality
    success = await test_playwright()
    
    # Test browser dependencies
    await test_browser_dependencies()
    
    print("\n" + "=" * 50)
    if success:
        print(f"{GREEN}Playwright is correctly installed and working!{RESET}")
        print(f"{BLUE}You can use Playwright for browser automation in the OWL project.{RESET}")
    else:
        print(f"{RED}Playwright test failed. Please check the errors above.{RESET}")
        print(f"{YELLOW}You may need to:{RESET}")
        print(f"{YELLOW}1. Install Playwright: pip install playwright{RESET}")
        print(f"{YELLOW}2. Install browser binaries: python -m playwright install{RESET}")
        print(f"{YELLOW}3. Install system dependencies: playwright install-deps{RESET}")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main())) 