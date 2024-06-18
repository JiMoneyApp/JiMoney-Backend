import requests

class TestCase:
    def __init__(self):
        self.base_url = 'http://localhost:5000'

    def test_get_all_wallets(self):
        suffix = '/home_page/get_all_wallets?user_id=1'
        response = requests.get(self.base_url + suffix)
        print(response.status_code)
        print(response.json())  # 打印回應的JSON內容

    def test_get_all_ledgers(self):
        suffix = '/home_page/get_all_ledgers?wallet_id=1'
        response = requests.get(self.base_url + suffix)
        print(response.status_code)
        print(response.json())

    def test_get_all_goals(self):
        suffix = '/home_page/get_all_goals?user_id=1'
        response = requests.get(self.base_url + suffix)
        print(response.status_code)
        print(response.json())

    def test_get_my_partner_goal(self):
        suffix = '/home_page/get_my_partner_goal?data_id=1'
        response = requests.get(self.base_url + suffix)
        print(response.status_code)
        print(response.json())
    def test_get_my_partner_ledger(self):
        suffix = '/home_page/get_my_partner_ledger?data_id=1'
        response = requests.get(self.base_url + suffix)
        print(response.status_code)
        print(response.json())

def main():
    test = TestCase()
    test.test_get_all_wallets()
    test.test_get_all_ledgers()
    test.test_get_all_goals()
    test.test_get_my_partner_goal()
    test.test_get_my_partner_ledger()


if __name__ == "__main__":
    main()

