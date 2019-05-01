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
        resp = requests.get('http://localhost:8000/',headers={ 'Authorization': 'Token {}'.format(token)} )
        print (resp.status_code, resp.text)
        self.assertEqual(resp.status_code, 200)

    def test_post_value_crossing_events(self):
        token = self.get_user_authentication_token()
        headers = { 'Authorization': 'Token {}'.format(token),
                    'Content-Type': 'application/json; charset=utf-8'
                  }
        data = {"signal":[1,2,3,3,7,8,5,6,3,2,1], "value":7}
        resp = requests.post('http://localhost:8000/',data=json.dumps(data), headers=headers)
        print(resp.status_code, resp.text)



    """
    def test_near_by_postcodes(self):
        postcode = 'RG20GY'
        distance = 10
        nearest_stores = ['RG30 1PR', "RG41 5HH", 'RG2 0HB', 'RG40 2NU' ]

        resp = requests.get('http://127.0.0.1:8000/nearest_locations/{}/{}'.format(postcode,distance))
        nearest_stores_returned = [location["postcode"] for location in resp.json()]
        self.assertEqual(nearest_stores,nearest_stores_returned)

    def test_valid_request(self):
        resp = requests.get('http://127.0.0.1:8000/nearest_locations/')
        self.assertEqual(resp.status_code, 404)
        pass
    """





if __name__ == '__main__':
    unittest.main()