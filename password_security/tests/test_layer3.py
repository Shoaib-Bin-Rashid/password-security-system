import unittest
from layer1_users import users, register_user
from layer3_attack_simulator import simulate_bruteforce, detect_bruteforce

class TestLayer3(unittest.TestCase):
    def setUp(self):
        users.clear()
        register_user("attacker", "Strong123")

    def test_bruteforce_detection(self):
        result = simulate_bruteforce("attacker", "wrong", 4)
        self.assertTrue(result)
        self.assertTrue(detect_bruteforce("attacker"))

if __name__ == "__main__":
    unittest.main()