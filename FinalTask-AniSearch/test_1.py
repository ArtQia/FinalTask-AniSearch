import unittest
import requests  
from urllib import response
from FinalTask_AniSearch import Search

class Test_test_1(unittest.TestCase):
    def test_Type(self):
        self.assertNotEqual(Search, str(Search), TypeError)

class Test_test_2(unittest.TestCase):
    def test_Status(self):
        StatusError = 'Status Error'
        self.assertNotEqual(response.status_code, 200, StatusError)
    def test_Len(self):
        URL = 'https://pokeapi.co/api/v2/pokemon/1'
        h = requests.head(URL)
        header = h.headers
        length = header.get('Content-Length')
        self.assertGreater(length, 0, 'Response have text')
        self.

if __name__ == '__main__':
    unittest.main()
