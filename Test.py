import os
import unittest
import json
from datetime import date, datetime
from devbops_user_microservice import app

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestLoader.sortTestMethodsUsing = None
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_0_delete_(self):

        req = {
            "Username":"DevBops_Admin"
        }
        rv = self.app.post('/delete', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == False

    def test_1_signup(self):
        req = {
            "Action":"register",
            "Username":"QA_Tester_Dec",
            "Password":"password12345678",
            "Email":"QA@gmail.com",
            "FirstName":"Quality",
            "LastName":"Assurance",
            "Country":"USA",
            "City":"New York City"
        }

        rv = self.app.post('/register', json=req)
        data = json.loads(rv.data)
        print(data)
        assert data['Result'] == True

    def test_2_Signup_Second(self):
        req = {
            "Action":"register",
            "Username":"QA_Tester_Dec",
            "Password":"password12345678",
            "Email":"QA1@gmail.com",
            "FirstName":"Quality",
            "LastName":"Assurance",
            "Country":"USA",
            "City":"New York City"
        }

        rv = self.app.post('/register', json=req)
        data = json.loads(rv.data)
        print(data)
        assert data['Result'] == False


    def test_3_login(self):

        req = {
            "Username":"QA_Tester_Dec",
            "Password":"password12345678"
        }
        rv = self.app.post('/login', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == True


    def test_4_update_info(self):

        req = {
            "Username":"QA_Tester_Dec",
            "FirstName":"New_first_name",
            "LastName":"New_last_name",
            "City":"New_city",
            "Country":"New_city",
            "Password":"New_password",
            "Email":"New_email"
        }

        rv = self.app.post('/update-user-info', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == True


    def test_5_delete(self):
        req = {
            "Username":"QA_Tester_Dec"
        }

        rv = self.app.post('/delete', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == True

    # def test_5_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertEqual(response.status_code, 302)

      
if __name__ == '__main__':
    unittest.main()
