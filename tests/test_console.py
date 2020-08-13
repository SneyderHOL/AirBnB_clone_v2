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


class TestHBNBCommand(unittest.TestCase):
    """Class for testing with unit test the HBNBCommand class"""

    def setup(self):
        """ Make connection to db """
        self.db = None
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            host_name = os.environ.get('HBNB_MYSQL_HOST')
            user_name = os.environ.get('HBNB_MYSQL_USER')
            pass_user = os.environ.get('HBNB_MYSQL_PWD')
            db_name = os.environ.get('HBNB_MYSQL_DB')
            self.db = MySQLdb.connect(host=host_name, port=3306,
                                      user=user_name, passwd=pass_user,
                                      db=db_name)

    def tear_down(self):
        """ End connection to db"""
        if self.db:
            self.db.close()

    def test_bd(self):
        """ testing query execution"""
        if self.db:
            cur = self.db.cursor()
            query = "SELECT * FROM states;"
            res1 = cur.execute(query)
            HBNBCommand().onecmd("create State name=\"California\"")
            res2 = cur.execute(query)
            cur.close()
            self.assertEqual(res2, res1 + 1)

    def test_do_create(self):
        """ """
#        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
#            with patch('sys.stdout', new=StringIO()) as f:
#                HBNBCommand().onecmd("create State name=\"Virginia\"")
#                output = f.getvalue().strip()
#                patter = '().+-().+-().+-().+-().+'
#                self.assertTrue(re.match(pattern, output))
#            return
        if self.db is None:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create State name=\"California\"")
                output = f.getvalue().strip()
                self.assertTrue(re.match('().+-().+-().+-().+-().+', output))

if __name__ == '__main__':
    unittest.main()
