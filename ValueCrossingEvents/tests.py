from django.test import TestCase

# Create your tests here.

import requests, json
import unittest

# Create your tests here.


class TestValueCrossingEvent(unittest.TestCase):

    def get_user_authentication_token(self):
        #token = 1150114b773b7ba6721f439167f416396bfa2caf
        resp = requests.post('http://localhost:8000/api-token-auth/',{'username':'apiuser', 'password':'wdictevf'})
        print (json.loads(resp.text))
        return (json.loads(resp.text)["token"])

    def test_get_value_crossing_events(self):
        token=self.get_user_authentication_token()
        resp = requests.get('http://localhost:8000/api/',headers={ 'Authorization': 'Token {}'.format(token)} )
        print (resp.status_code, resp.text)
        self.assertEqual(resp.status_code, 200)

    def test_post_value_crossing_events(self):
        token = self.get_user_authentication_token()
        headers = { 'Authorization': 'Token {}'.format(token),
                    'Content-Type': 'application/json; charset=utf-8'
                  }
        data = {"signal":[1,2,3,3,3,7,8,5,7,3,7,3], "value":3}
        resp = requests.post('http://localhost:8000/api/',data=json.dumps(data), headers=headers)
        print(resp.status_code, resp.text)









if __name__ == '__main__':
    unittest.main()