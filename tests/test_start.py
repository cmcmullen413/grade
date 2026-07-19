import os
import shutil
import subprocess

# Paths to executables and directories required for testing
TESTING_DIR_PATH = r"./tests"
# Bin path is relative to the tests directory
BINARY_PATH_FROM_TESTS = r"../target/release/grade.exe"
BINARY_PATH_FROM_TEST_DIR = r"../../target/release/grade.exe"

# Paths for the various files and directories that start should create or verify
# Paths are relative to the tests directory
TEST_DIR_NAME = "TEST_DIR"
TEST_DIR_PATH = r"./TEST_DIR"
GRADE_DIR_PATH = r"./TEST_DIR/.grade"
IGNORE_FILE_PATH = r"./TEST_DIR/.gradeignore"


# First function called
# Changes the directory into the tests dir
def test_initial_setup():
    os.chdir(TESTING_DIR_PATH)

# Tests the start command with a passed in directory that does not exist
def test_directory_creation():
    # Pre clean
    cleanup_tests()

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME], capture_output=True)

    # Check that the right output was sent; Expecting:
    #   stdout -> empty
    #   stderr -> empty
    assert len(output.stdout) == 0
    assert len(output.stderr) == 0

    # Check that the required directories and files were created
    assert os.path.isdir(TEST_DIR_PATH)
    assert os.path.isdir(GRADE_DIR_PATH)
    assert os.path.isfile(IGNORE_FILE_PATH)

    # Clean up
    cleanup_tests()

# Tests the start command with no provided directory with the working directory being empty
def test_no_path_provided_empty():
    # Pre clean
    cleanup_tests()

    # Change the directory to an empty TEST_DIR
    os.mkdir(TEST_DIR_NAME)
    os.chdir(TEST_DIR_PATH)

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TEST_DIR, "start"], capture_output=True)

    # Move out of the TEST_DIR
    os.chdir(r"../")

    # Check that the right output was sent; Expecting:
    #   stdout -> empty
    #   stderr -> empty
    assert len(output.stdout) == 0
    assert len(output.stderr) == 0

    # Check that the required directories and files were created
    assert os.path.isdir(GRADE_DIR_PATH)
    assert os.path.isfile(IGNORE_FILE_PATH)

    # Clean up
    cleanup_tests()

# Test the start command with no provided directory and the working directory contains a .grade subdirectory
def test_no_path_provided_non_empty():
    # Pre clean
    cleanup_tests()

    # Make a new grade dir and change directory into it
    subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME])
    os.chdir(TEST_DIR_PATH)

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TEST_DIR, "start"], capture_output=True)

    # Move out of the TEST_DIR
    os.chdir(r"../")

    # Check that the right output was sent; Expecting:
    #   stdout -> "Grade book already exists"
    #   stderr -> empty
    assert output.stdout == b"Grade book already exists\n"
    assert len(output.stderr) == 0

    # No directories or files will be created

    # Clean up
    cleanup_tests()

# Tests the start command with a passed in directory that exists, but is empty
def test_directory_exists_empty():
    # Pre clean
    cleanup_tests()

    # Make an empty TEST_DIR
    os.mkdir(TEST_DIR_NAME)

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME], capture_output=True)

    # Check that the right output was sent; Expecting:
    #   stdout -> empty
    #   stderr -> empty
    assert len(output.stdout) == 0
    assert len(output.stderr) == 0

    # Check that the required directories and files were created
    assert os.path.isdir(GRADE_DIR_PATH)
    assert os.path.isfile(IGNORE_FILE_PATH)

    # Clean up
    cleanup_tests()

# Tests the start command with a passed in directory that exists and contains a .grade subdirectory
def test_directory_exists_non_empty():
    # Pre clean
    cleanup_tests()

    # Make a new grade dir
    subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME])

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME], capture_output=True)

    # Check that the right output was sent; Expecting:
    #   stdout -> "Grade book already exists"
    #   stderr -> empty
    assert output.stdout == b"Grade book already exists\n"
    assert len(output.stderr) == 0

    # No directories or files will be created

    # Clean up
    cleanup_tests()

# Tests the start command with a passed in path that is not a directory
def test_path_not_directory():
    # Pre clean
    cleanup_tests()

    # Create a file with the TEST_DIR name
    open(TEST_DIR_NAME, "w")

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME], capture_output=True)

    # Check that the right output was sent; Expecting:
    #   stdout -> empty
    #   stderr -> "Could not start grade book at provided path. Path is not a directory"
    assert len(output.stdout) == 0
    assert output.stderr == b"Could not start grade book at provided path. Path is not a directory\n"

    # No directories or files will be created

    # Clean up
    cleanup_tests()

# Tests the start command with a passed in path where the .grade subpath is not a directory
def test_grade_path_not_directory():
    # Pre clean
    cleanup_tests()

    # Make a TEST_DIR with a file inside named ".grade"
    os.mkdir(TEST_DIR_NAME)
    open(GRADE_DIR_PATH, "w")

    # Call the command to be tested
    output = subprocess.run([BINARY_PATH_FROM_TESTS, "start", TEST_DIR_NAME], capture_output=True)

    # Check that the right output was sent; Expecting:
    #   stdout -> empty
    #   stderr -> "Failed to start grade book. Path to .grade is not a directory"
    assert len(output.stdout) == 0
    assert output.stderr == b"Failed to start grade book. Path to .grade is not a directory\n"

    # No directories or files will be created

    # Clean up
    cleanup_tests()

# Make sure the cleanup function is called at the end in case of failures
def test_final_cleanup():
    cleanup_tests()

# Cleans up the test environment by removing the TEST_DIR and its contents
# Should be called before and after each test to ensure the correct environment in case of failures
def cleanup_tests():
    # Remove the directory and everything in it
    try:
        shutil.rmtree(TEST_DIR_PATH)
    # If the path was a file not a dir, remove it in the correct way
    except NotADirectoryError:
        os.remove(TEST_DIR_PATH)
    except FileNotFoundError:
        return