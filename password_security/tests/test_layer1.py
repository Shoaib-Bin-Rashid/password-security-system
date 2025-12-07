import unittest
from layer1_users import users, register_user, login_user, UserError

class TestLayer1(unittest.TestCase):
    def setUp(self):
        users.clear()

    def test_register_and_login(self):
        register_user("user1", "Strong123")
        self.assertTrue(login_user("user1", "Strong123"))

    def test_duplicate_user(self):
        register_user("user1", "Strong123")
        with self.assertRaises(UserError):
            register_user("user1", "Strong456")

    def test_wrong_login(self):
        register_user("user2", "Strong123")
        with self.assertRaises(UserError):
            login_user("user2", "WrongPass")
        self.assertEqual(users["user2"]["login_attempts"], 1)

if __name__ == "__main__":
    unittest.main()