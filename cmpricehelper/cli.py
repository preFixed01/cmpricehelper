"""
Command-line interface for cmpricehelper

This module provides a command-line interface (CLI) for the cmpricehelper application.
It sets up argument parsing, configures logging with colored output, and provides
an entry point for running the CLI application.


Usage:
    Run this module as a script to use the command-line interface:

    ```bash
    python3 cmpricehelper [options]
    ```

    Options:
    - `--version`: Displays the version of the application.
    - `-v, --verbose`: Enables verbose mode, which increases the logging level to DEBUG.
"""

import argparse
import logging

from colorama import Fore, Style, init

from cmpricehelper.utils import read


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors based on log level."""

    LOG_COLORS = {
        logging.DEBUG: Fore.GREEN,
        logging.INFO: Fore.WHITE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        log_color = self.LOG_COLORS.get(record.levelno, Fore.WHITE)
        record.msg = f"{log_color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)


def main():
    """Entry point of cmpricehelper"""
    version = read("", "VERSION")

    # Initialize colorama
    init(autoreset=True)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simple CLI for cmpricehelper")

    # Add an option for version
    parser.add_argument("--version", action="version", version=version)

    # Add an option for verbose mode
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

    # Parse command line arguments
    args = parser.parse_args()

    # Configure logging
    handler = logging.StreamHandler()
    formatter = ColoredFormatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logging.getLogger().handlers = [handler]

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Main application code
    logging.info("Welcome to cmpricehelper %s", version)


if __name__ == "__main__":
    main()
