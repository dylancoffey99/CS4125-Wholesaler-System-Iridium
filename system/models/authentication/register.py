from system.models.database.db_handler import UserDB
import hashlib
import os

class Register:
    def input_info(self):
        user_name = input ("Username")
        password = input ("Password")
        self.check_username(user_name, password)
        country = input ("What country do you live in?")
        country_id = self.set_country_id(country)
        is_admin = "false"

    def check_username(self, user_name, password, user: UserDB):
        if user_name == user.get_user(user_name):
            print("Change username")
        else:
            print("Username available")
            user.add_user(user_name)
            user.add_user(password)

    def set_country_id(self, country) -> int:
        countries = ["Austria", "Belgium", "Bulgaria," "Croatia", "Cyprus", "Czech Republic",
                     "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
                     "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
                     "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
                     "Spain", "Sweden", "United Kingdom"]
        country_id = countries.index(country)
        return country_id

    def get_hashed_password(self, password: str) -> str:
    # https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
    # https://stackoverflow.com/questions/48448830/hashing-password-in-py-file
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            password.encode('utf-8'),  # Convert the password to bytes
            salt,  # Provide the salt
            100000  # It is recommended to use at least 100,000 iterations of SHA-256
        )
        # Store them as:
        storage = salt + key

        # Getting the values back out
        salt_from_storage = storage[:32]  # 32 is the length of the salt
        key_from_storage = storage[32:]

        salt_and_key = [salt_from_storage, key_from_storage]

        return salt_and_key


