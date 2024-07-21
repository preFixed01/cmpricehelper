"""Test module for base module"""

from cmpricehelper.base import NAME


def test_base():
    """Ensures project name is correct"""
    assert NAME == "cmpricehelper"
