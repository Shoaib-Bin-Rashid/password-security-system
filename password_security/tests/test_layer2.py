import unittest
import time
from layer1_users import users, register_user
from layer2_sessions import generate_token, validate_token

class TestLayer2(unittest.TestCase):
    def setUp(self):
        users.clear()
        register_user("user3", "Strong123")

    def test_token_generation(self):
        token = generate_token("user3", 1)
        self.assertTrue(validate_token(token))
        time.sleep(1.1)
        self.assertFalse(validate_token(token))

if __name__ == "__main__":
    unittest.main()