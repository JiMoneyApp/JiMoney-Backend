import requests

class TestCase:
    def __init__(self):
        self.base_url = 'http://localhost:5000'

    def test_insert_user(self):
        suffix = '/user/insert_acc_password?user_name=root&user_acc=root&user_password=root1234'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.data.decode() == 'success!':
            print("Test insert user : passed")
            return True
        else:
            print("Test insert user : failed")
            return False
    
    """"
    def test_get_user_id(self):
        suffix = '/user/get_user_id?user_acc=root&user_password=root1234'
        response = requests.get(self.base_url + suffix)
        if response.status_code == 200 and response.data.decode() == '1':
            print("Test get user id : passed")
            return True
        else:
            print("Test get user id : failed")
            return False
    """ 
        

def main():
    test = TestCase()
    test.test_insert_user()
