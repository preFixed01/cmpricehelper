"""Configure test environment.

This module provides a pytest fixture to configure the test environment by
ensuring that each test runs in its own temporary directory. This helps to
isolate tests and prevent them from interfering with each other.

It dynamically adjusts the current working directory and the sys.path to
include the temporary directory, allowing local test-created packages to be
imported.
"""

import sys
import pytest


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    """A pytest fixture to change the current working directory to a temporary directory.

    This fixture runs automatically for each test and ensures that each test
    runs in its own temporary directory. It dynamically adjusts the sys.path
    to include the temporary directory, allowing local test-created packages
    to be imported.

    Args:
        request (pytest.FixtureRequest): The pytest request object that provides
            access to the requesting test context.

    Yields:
        None: This fixture does not return a value. It changes the directory
            context for the duration of the test.
    """
    # Get the fixture dynamically by its name.
    tmpdir = request.getfixturevalue("tmpdir")
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    with tmpdir.as_cwd():
        yield
