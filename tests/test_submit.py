import difflib
import os
import hashlib
from pathlib import Path

# Paths to executables and directories required for testing
TESTING_DIR_PATH = r"./tests"
# Bin path is relative to the tests directory
BINARY_PATH_FROM_TEST_DIR = r"../../target/release/grade.exe"

# First function called
# Changes the directory into the tests dir
def test_initial_setup():
    os.chdir(TESTING_DIR_PATH)

def test_first_submit():
    return

def test_non_first_submit_wo_ignore():
    return

def test_non_first_submit_w_ignore():
    return