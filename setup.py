"""Python setup.py for cmpricehelper package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("cmpricehelper", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    """
    Reads a requirements file and returns a list of cleaned lines.

    This function reads the file at `path` and returns a list of lines,
    stripping whitespace and excluding lines that start with quotes, '#',
    '-', or 'git+'.

    Args:
        path (str): The path to the file.

    Returns:
        list: A list of cleaned lines from the file.
    """
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="cmpricehelper",
    version=read("cmpricehelper", "VERSION"),
    description="Tools for CardMarket",
    url="https://github.com/preFixed01/cmpricehelper.git",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ASSE Romain",
    packages=find_packages(exclude=["tests"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["cmpricehelper = cmpricehelper.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
