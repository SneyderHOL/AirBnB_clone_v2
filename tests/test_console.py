#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
import pep8
import json
from io import StringIO
import re
from console import HBNBCommand
from unittest.mock import patch
import MySQLdb
import os


class TestHBNBCommand(unittest.TestCase):
    """Class for testing with unit test the HBNBCommand class"""

    def connection(self):
        """ Make connection to db """
        db = None
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            host_name = os.environ.get('HBNB_MYSQL_HOST')
            user_name = os.environ.get('HBNB_MYSQL_USER')
            pass_user = os.environ.get('HBNB_MYSQL_PWD')
            db_name = os.environ.get('HBNB_MYSQL_DB')
            db = MySQLdb.connect(host=host_name, port=3306,
                                 user=user_name,
                                 passwd=pass_user,
                                 db=db_name)
        return db

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') != 'db',
                     "only for File storage")
    def test_bd_create_State(self):
        """ testing query execution"""
        output = None
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
        db = self.connection()
        cur = db.cursor()
        query = "SELECT * FROM states;"
        res = cur.execute(query)
        results = cur.fetchall()
        save = False
        for result in results:
            if result[0] == output:
                save = True
                break
        self.assertTrue(save)
        cur.close()
        db.close()

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_state(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_city(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City name=\"SanFrancisco\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_user(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=\"hbtn@shool.com\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_place(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place name=\"Iglu\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_amenity(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity name=\"Calefaction\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create_review(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review text=\"Amazing\"")
            output = f.getvalue().strip()
            self.assertIsNotNone(re.match('(.+)-(.+)-(.+)-(.+)-(.+)', output))

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        console_path = 'console.py'
        result_console = pep8_val.check_files([console_path])
        self.assertEqual(result_console.total_errors, 0)

    def test_all(self):
        """Testing outputs formats"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            print(output)
            self.assertIsNotNone(re.search('[[\w]*]', output))

    def test_missin_parameters(self):
        """Missing parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual('** class name missing **', output)

    def test_wrong_parameters(self):
        """wrong parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create state")
            output = f.getvalue().strip()
            self.assertEqual('** class doesn\'t exist **', output)

    def test_wrong_parameters_all(self):
        """wrong parameters to all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all state")
            output = f.getvalue().strip()
            self.assertEqual('** class doesn\'t exist **', output)

if __name__ == '__main__':
    unittest.main()
