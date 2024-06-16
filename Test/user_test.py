import sys
import unittest
from flask import Flask
from tinydb import TinyDB, Query
sys.path.append('..')
from flaskr.app import app

class TestDataRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()

        cls.mock_db = TinyDB('mock_db.json')  # 使用一个mock的数据库文件
        cls.mock_users = cls.mock_db.table('Users')
        print(mock_db.all())        

    @classmethod
    def tearDownClass(cls):
        cls.mock_db.close()

    def setUp(self):
        self.mock_users.truncate()
    
    '''
    def test_get_ledger_datas(self):
        response = self.client.get('/data/get_ledger_datas?user_id=1&ledger_name=test_ledger')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['UID'], 1)
        self.assertEqual(data[0]['LName'], 'test_ledger')
        self.assertEqual(data[0]['DID'], 1)
        self.assertEqual(data[0]['Price'], 100)
        self.assertEqual(data[0]['DName'], 'Test Data')
        self.assertEqual(data[0]['DType'], 'Type A')
        self.assertEqual(data[0]['DDate'], '2024-06-16')  # 确保日期格式正确

    def test_insert_new_data(self):
        mock_request_data = {
            'user_id': '1',
            'ledger_name': 'test_ledger',
            'price': '150',
            'data_name': 'New Data',
            'data_type': 'Type B',
            'data_date': '2024-06-17'
        }
        response = self.client.post('/data/insert_new_data', json=mock_request_data)
        self.assertEqual(response.status_code, 200)

        new_data = self.mock_datas.get(Query().DName == 'New Data')
        self.assertIsNotNone(new_data)
        self.assertEqual(new_data['Price'], 150)
        self.assertEqual(new_data['DType'], 'Type B')
        self.assertEqual(new_data['DDate'], '2024-06-17')

    def test_update_data_name(self):
        response = self.client.put('/data/update_data_name', query_string={'data_id': '1', 'data_name': 'Updated Data Name'})
        self.assertEqual(response.status_code, 200)
        updated_data = self.mock_datas.get(Query().DID == 1)
        self.assertEqual(updated_data['DName'], 'Updated Data Name')

    def test_delete_data(self):
        response = self.client.delete('/data/delete_data', query_string={'data_id': '1'})
        self.assertEqual(response.status_code, 200)
        data_exists = self.mock_datas.search(Query().DID == 1)
        self.assertEqual(len(data_exists), 0)
    '''

if __name__ == '__main__':
    unittest.main()

