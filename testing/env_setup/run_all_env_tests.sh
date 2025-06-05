#!/bin/bash
# Run all OWL environment verification tests in sequence

# Define color codes
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
BOLD="\033[1m"
RESET="\033[0m"

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Print header
echo -e "\n${BOLD}${BLUE}OWL Environment Verification Suite${RESET}"
echo -e "${BLUE}=====================================${RESET}\n"
echo -e "Running all verification tests for the OWL project environment...\n"

# Define the test scripts to run in order
TEST_SCRIPTS=(
    "test_dependencies.py"
    "test_api_keys.py"
    "test_playwright.py"
    "test_environment.py"
)

# Track overall success
ALL_TESTS_PASSED=true

# Run each test script
for test in "${TEST_SCRIPTS[@]}"; do
    # Check if the test script exists
    if [ ! -f "$SCRIPT_DIR/$test" ]; then
        echo -e "${YELLOW}Warning: Test script $test not found, skipping...${RESET}"
        continue
    fi
    
    # Print test header
    echo -e "\n\n${BOLD}${BLUE}===== Running $test =====${RESET}\n"
    
    # Run the test script
    python "$SCRIPT_DIR/$test"
    
    # Check the exit code
    if [ $? -eq 0 ]; then
        echo -e "\n${GREEN}✓ $test completed successfully${RESET}"
    else
        echo -e "\n${YELLOW}⚠ $test reported issues${RESET}"
        ALL_TESTS_PASSED=false
    fi
    
    echo -e "\n${BLUE}===== Finished $test =====${RESET}\n"
    
    # Add a separator between tests
    echo -e "---------------------------------------\n"
done

# Print summary
echo -e "\n${BOLD}${BLUE}Test Suite Summary${RESET}"
echo -e "${BLUE}=====================================${RESET}\n"

if $ALL_TESTS_PASSED; then
    echo -e "${GREEN}${BOLD}All tests completed successfully!${RESET}"
    echo -e "Your environment is properly set up for the OWL project."
else
    echo -e "${YELLOW}${BOLD}Some tests reported issues.${RESET}"
    echo -e "Please review the test output above and fix any reported issues."
    echo -e "Refer to the README files for troubleshooting information."
fi

echo -e "\n${BLUE}=====================================${RESET}\n" 