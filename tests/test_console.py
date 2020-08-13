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
    db = None

    def setup(self):
        """ Make connection to db """
        TestHBNBCommand.db = None
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            host_name = os.environ.get('HBNB_MYSQL_HOST')
            user_name = os.environ.get('HBNB_MYSQL_USER')
            pass_user = os.environ.get('HBNB_MYSQL_PWD')
            db_name = os.environ.get('HBNB_MYSQL_DB')
            TestHBNBCommand.db = MySQLdb.connect(host=host_name, port=3306,
                                                 user=user_name,
                                                 passwd=pass_user,
                                                 db=db_name)

    def tear_down(self):
        """ End connection to db"""
        if TestHBNBCommand.db:
            TestHBNBCommand.db.close()

    def test_bd_create_State(self):
        """ testing query execution"""
        if TestHBNBCommand.db:
            cur = self.db.cursor()
            query = "SELECT * FROM states;"
            res1 = cur.execute(query)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create State name=\"California\"")
                output = f.getvalue().strip()
            res2 = cur.execute(query)
            self.assertEqual(res2, res1 + 1)
            query = "SELECT * FROM cities;"
            city_qty1 = cur.execute(query)
            HBNBCommand().onecmd("create City name=\"SF\" state_id=\"{}\""
                                 .format(output))
            city_qty2 = cur.execute(query)
            self.assertEqual(citi_qty2, city_qty1 + 1)
            cur.close()

    @unittest.skipIf(os.environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "only for File storage")
    def test_do_create(self):
        """ """
#        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
#            with patch('sys.stdout', new=StringIO()) as f:
#                HBNBCommand().onecmd("create State name=\"Virginia\"")
#                output = f.getvalue().strip()
#                patter = '().+-().+-().+-().+-().+'
#                self.assertTrue(re.match(pattern, output))
#            return
        if TestHBNBCommand.db is None:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create State name=\"California\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))
                HBNBCommand().onecmd("create City name=\"SanFrancisco\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))
                HBNBCommand().onecmd("create User email=\"hbtn@shool.com\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))
                HBNBCommand().onecmd("create Place name=\"Iglu\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))
                HBNBCommand().onecmd("create Amenity name=\"Calefaction\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))
                HBNBCommand().onecmd("create Review text=\"Amazing\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))

if __name__ == '__main__':
    unittest.main()
