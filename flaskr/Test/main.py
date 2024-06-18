import unittest
from tinydb import TinyDB, Query

db = TinyDB('mock_db.json')

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='*Test.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
