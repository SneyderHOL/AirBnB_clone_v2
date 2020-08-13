#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
import pep8
import json
from io import StringIO
import re
from console import HBNBCommand
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Class for testing with unit test the HBNBCommand class"""

    def test_do_create(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
            self.assertTrue(re.match('().+-().+-().+-().+-().+', output))

if __name__ == '__main__':
    unittest.main()
