#!/usr/bin/python3
""" """
import unittest
import pep8
import json
from io import StringIO
import re
from console import HBNBCommand
from unittest.mock import patch
import MySQLdb
import os


class TestAmenity(unittest.TestCase):
    """Class for testing with unit test the HBNBCommand class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        console_path = 'console.py'
        result_console = pep8_val.check_files([console_path])
        self.assertEqual(result_console.total_errors, 0)

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_object(self):
        """ """
        pass
