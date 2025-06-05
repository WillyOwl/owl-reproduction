# Playwright Installation Verification

This document provides instructions for verifying the Playwright installation and browser automation functionality for the OWL project.

## Overview

The `test_playwright.py` script tests whether Playwright is correctly installed and functioning by:

1. Importing the Playwright module
2. Launching a browser (Chromium)
3. Navigating to a website
4. Capturing a screenshot
5. Checking browser dependencies

## Prerequisites

Before running the test script, ensure you have:

1. Installed Playwright:
   ```bash
   pip install playwright
   ```

2. Installed browser binaries:
   ```bash
   python -m playwright install
   ```

3. Installed system dependencies (for Linux users):
   ```bash
   playwright install-deps
   ```

## Running the Test

To run the Playwright verification test:

```bash
python test_playwright.py
```

## What the Test Verifies

The test script verifies:

- **Playwright Module**: Checks if the Playwright module can be imported
- **Browser Launch**: Tests if a browser can be launched
- **Navigation**: Verifies that the browser can navigate to a website
- **Screenshot Capability**: Tests if screenshots can be captured
- **Browser Dependencies**: Checks if dependencies for Chromium, Firefox, and WebKit are installed

## Test Output

The test will create a directory called `playwright_test_output` containing a screenshot from the test website. This confirms that Playwright can interact with web pages and capture visual output.

## Troubleshooting

If the test fails, you may see one of the following issues:

### Module Import Error

```
✗ Failed to import Playwright: No module named 'playwright'
```

**Solution**: Install Playwright with `pip install playwright`

### Browser Binary Missing

```
✗ Playwright test failed: Executable doesn't exist at [path]
```

**Solution**: Install browser binaries with `python -m playwright install`

### System Dependencies Missing

```
✗ Chromium browser dependencies missing: [error message]
```

**Solution**: Install system dependencies with `playwright install-deps`

## Integration with OWL

Once Playwright is verified to be working correctly, the OWL project can use it for browser automation tasks such as:

- Web scraping
- Automated testing
- Website interaction
- Data extraction from web pages

This verification ensures that the BrowserToolkit in OWL will function properly when used for automation tasks.
