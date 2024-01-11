import unittest
from flask import Flask, render_template

def create_page():                #here form the main.py file because imports just won't work with python container
    app = Flask(__name__)

    @app.route("/")
    def hello():
        message = "Hello, World"
        return render_template('index.html', message=message)

    return app

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.app = create_page()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_hello_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
