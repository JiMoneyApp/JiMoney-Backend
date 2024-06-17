import json
import requests
import unittest
from main import db
from tinydb import TinyDB, Query


user_table = db.table('Users')


class ApiUsersTestCase(unittest.TestCase):

    base_url = "http://localhost:5000"

    @classmethod
    def setUpClass(cls):
        user_table.truncate()
        data = [
            {
                "UID": 0,
                "BUDGET": 100,
                "UName": "root",
                "UPassword": "root1234",
                "UAccount": "root",
                "UNickname": "root",
                "isrightHander": True,
                "isDarkMode": False,
                "NoticeTime": "21:00:00"
            }
        ]        
        user_table.insert_multiple(data)
    
    def test_get_user_id(self):
        suffix = '/user/get_user_id?user_acc=root&user_pass=root1234'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, 0)
        self.assertEqual(response.status_code, 200)

    def test_get_user_name(self):
        suffix = '/user/get_name?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, "root")
        self.assertEqual(response.status_code, 200)

    def test_get_is_right(self):
        suffix = '/user/get_isright?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, True)
        self.assertEqual(response.status_code, 200)

    def test_get_is_dark(self):
        suffix = '/user/get_isdark?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, False)
        self.assertEqual(response.status_code, 200)

    def test_get_notice_time(self):
        suffix = '/user/get_ntime?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, "21:00:00")
        self.assertEqual(response.status_code, 200)

    def test_get_user_acc(self):
        suffix = '/user/get_acc?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, "root")
        self.assertEqual(response.status_code, 200)

    def test_get_user_password(self):
        suffix = '/user/get_password?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, "root1234")
        self.assertEqual(response.status_code, 200)

    def test_get_budget(self):
        suffix = '/user/get_budget?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(data, 100)
        self.assertEqual(response.status_code, 200)

    def test_get_user_nickname(self):
        suffix = '/user/get_nname?user_id=0'
        response = requests.get(self.base_url + suffix)
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_update_user_name(self):
        suffix = '/user/update_name?user_id=0&new_name=root_new'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_user_password(self):
        suffix = '/user/update_password?user_id=0&new_password=1234'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_user_acc(self):
        suffix = '/user/update_acc?user_id=0&new_acc=1234'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_user_nickname(self):
        suffix = '/user/update_nname?user_id=0&new_nname=newadmin'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_notice_time(self):
        suffix = '/user/update_ntime?user_id=0&new_ntime=090000'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_is_right(self):
        suffix = '/user/update_isright?user_id=0&new_isright=False'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_is_dark(self):
        suffix = '/user/update_isdark?user_id=0&new_isdark=True'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)

    def test_update_budget(self):
        suffix = '/user/update_budget?user_id=0&new_budget=2000'
        response = requests.get(self.base_url + suffix)
        data = response.text
        self.assertEqual(data, 'success!')
        self.assertEqual(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()
        
