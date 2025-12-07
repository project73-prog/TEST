from flask import Flask, render_template
import app as tested_app
import unittest
class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_add_success(self):
        r = self.app.get('/add?a=10&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'176.0')

if __name__ == '__main__':
    unittest.main()