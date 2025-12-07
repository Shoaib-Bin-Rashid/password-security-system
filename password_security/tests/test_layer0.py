import unittest
from layer0_crypto import *

class TestLayer0(unittest.TestCase):
    def test_validate_password_strength(self):
        self.assertTrue(validate_password_strength("Strong123"))

    def test_invalid_password_type(self):
        with self.assertRaises(TypeError):
            validate_password_strength(None)

    def test_short_password(self):
        with self.assertRaises(ValueError):
            validate_password_strength("a1")

    def test_common_password(self):
        with self.assertRaises(ValueError):
            validate_password_strength("password")

    def test_hash_and_verify(self):
        salt = generate_salt()
        data = make_stored_password("Strong123", salt)
        self.assertTrue(verify_hash("Strong123", data["salt"], data["hash"]))
        self.assertFalse(verify_hash("Wrong123", data["salt"], data["hash"]))

if __name__ == "__main__":
    unittest.main()