"""Test module for utils module"""

import os

import pytest
from cmpricehelper.utils import read


def test_read(tmpdir):
    """Test the read function with temporary files."""

    # Create a temporary READ_TEST2 file with some content
    read_test_1 = tmpdir.join("READ_TEST1")
    read_test_1.write("read test")

    # Create a temporary READ_TEST2 file with some content
    read_test_2 = tmpdir.join("READ_TEST2")
    read_test_2.write("")

    # Create a temporary DIFFERENT file with some content
    different_file = tmpdir.join("DIFFERENT")
    different_file.write("Different content")

    # Test reading the READ_TEST1 file
    version_content = read(os.path.dirname(str(read_test_1)), "READ_TEST1")
    assert version_content == "read test"

    # Test reading the READ_TEST2 file
    version_content = read(os.path.dirname(str(read_test_1)), "READ_TEST2")
    assert version_content == ""

    # Read the file and check for non-equality
    different_content = read(os.path.dirname(str(different_file)), "DIFFERENT")
    assert different_content != "Expected content"

    # Test the case where the requested file does not exist
    with pytest.raises(FileNotFoundError):
        read(os.path.dirname(str(tmpdir)), "NON_EXISTENT_FILE")
