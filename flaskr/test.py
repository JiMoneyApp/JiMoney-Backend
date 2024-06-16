import requests

class TestCase:
    def __init__(self):
        self.base_url = 'http://localhost:5000'

    def test_insert_user(self):
        suffix = '/user/insert_acc_password?user_name=root&user_acc=root&user_password=root1234'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test insert user : passed")
            return True
        else:
            print("Test insert user : failed")
            return False
    
    
    def test_get_user_id(self):
        suffix = '/user/get_user_id?user_acc=root&user_password=root1234'
        response = requests.get(self.base_url + suffix)
        print(response.json())
        if response.status_code == 200 and response.json() == [1]:
            print("Test get user id : passed")
            return True
        else:
            print("Test get user id : failed")
            return False
     
        
     def get_ledger_datas(self):
        suffix = '/data/get_ledger_datas/user_id=1&ledger_name=test_ledger'
        response = requests.get(self.base_url + suffix)
        test_json = {
                "user_id":1,
                "ledger_name":"test_ledger",
                "price":100,
                "data_name":"test_name",
                "data_type":"test_type",
                "data_date":"20021027"
        }
        if response.status_code == 200 and response.json() == test_json:
            print("Test get ledger datas : passed")
        else:
            print("Test get ledger datas : failed")

    def test_insert_data(self):
        suffix = '/data/insert_new_data/user_id=1&ledger_name=test_ledger&price=100&data_name=test_name&data_type=test_type&data_date=20021027'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test insert data : passed")
        else:
            print("Test insert data : failed")
            return False
    
    def test_update_data_name(self):
        suffix = '/data/update_data_name/data_id=1&data_name=test_name'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test update data name : passed")
            return True
        else:
            print(f"Test update data name failed with status code {response.status_code}")
            return False 

    def test_update_data_price(self):
        suffix = '/data/update_data_price/user_id=1&ledger_name=test_ledger&data_id=1&price=200'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test update data price : passed")
            return True
        else:
            print(f"Test update data price failed with status code {response.status_code}")
            return False
    
    def test_update_data_type(self):
        suffix = '/data/update_data_price/data_id=1&data_type=test_type'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test update data type : passed")
            return True
        else:
            print(f"Test update data type failed with status code {response.status_code}")
            return False
        
    def test_delete_data(self):
        suffix = '/data/update_data_price/data_id=1'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.text == 'success!':
            print("Test delete data : passed")
            return True
        else:
            print(f"Test delete data type failed with status code {response.status_code}")
            return False

