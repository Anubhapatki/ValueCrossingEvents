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

    def test_api_accessible(self):
        token=self.get_user_authentication_token()
        resp = requests.get('http://localhost:8000/api/',headers={ 'Authorization': 'Token {}'.format(token)} )
        self.assertEqual(resp.status_code, 200)

    def test_incorrect_api_url(self):
        token=self.get_user_authentication_token()
        resp = requests.get('http://localhost:8000/aipi/',headers={ 'Authorization': 'Token {}'.format(token)} )
        print(resp.status_code, resp.text)
        self.assertEqual(resp.status_code, 404)

    def test_authenticate(self):
        resp = requests.get('http://localhost:8000/api/')
        print(resp.status_code, resp.text)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(json.loads(resp.text)["detail"], "Authentication credentials were not provided.")

    def test_post_value_crossing_events(self):
        token = self.get_user_authentication_token()
        headers = { 'Authorization': 'Token {}'.format(token),
                    'Content-Type': 'application/json; charset=utf-8'
                  }
        data = {"signal":[1,2,3,3,3,7,8,5,4,3,7,2], "value":3}
        resp = requests.post('http://localhost:8000/api/',data=json.dumps(data), headers=headers)
        print(resp.status_code, resp.text)

    def test_get_tornado_app(self):
        credentials = {'apiuser1': 'password'}
        resp = requests.get('http://localhost:8888/?value=3&signal=1,2,3,3,3,7,8,5,4,3,7,2')
        print(resp.status_code, resp.text)
        #self.assertEqual(resp.status_code, 200)








if __name__ == '__main__':
    unittest.main()