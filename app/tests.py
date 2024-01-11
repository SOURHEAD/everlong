import unittest
from main import request_get

class load_website(unittest.TestCase):
    def test_website(self):
        self.assertEqual(request_get("http://127.0.0.1:5000/"), 200)
        
if __name__ == "__main__":
    unittest.main()
