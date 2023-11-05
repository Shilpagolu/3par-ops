import subprocess
import pytest
import logging
from remote_operations.remote_operations import run_remote_commands
import os
print("Current Working Directory:", os.getcwd())

# Set up logging
logging.basicConfig(filename=r'C:\Users\sprasad\PycharmProjects\3par-ops\test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define the storage array details for testing
ARRAY_HOST = "10.157.208.240"
ARRAY_USER = "root"
ARRAY_PASSWORD = "ssmssm"

def test_check_array_version():
    commands = ["showversion -b"]
    output = run_remote_commands(ARRAY_HOST, ARRAY_USER, ARRAY_PASSWORD, commands)

    expected_first_line = "Release version 9.5.18.14"
    first_line = output.strip().splitlines()[0]

    if first_line == expected_first_line:
        logging.info("Array version check passed.")
    else:
        logging.error(f"Array version check failed. Expected: '{expected_first_line}', Actual: '{first_line}'")
        pytest.fail(f"Array version check failed. Expected: '{expected_first_line}', Actual: '{first_line}'")

