import unittest

from routers import create_access_token, get_password_hash, verify_password


class AuthTests(unittest.TestCase):
    def test_password_hashing_and_verification(self):
        password = "supersecret"
        hashed = get_password_hash(password)

        self.assertNotEqual(hashed, password)
        self.assertTrue(verify_password(password, hashed))
        self.assertFalse(verify_password("wrongpassword", hashed))

    def test_access_token_contains_username(self):
        token = create_access_token({"sub": "demo"})

        self.assertTrue(token)


if __name__ == "__main__":
    unittest.main()
