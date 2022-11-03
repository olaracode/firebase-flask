from Users.encrypt import generate_password, check_password, generate_salt

test_salt = "jgkam1"
test_password = "test_password"
encrypted_password = generate_password(test_password, test_salt)

class TestEncryption:
    def test_password_encryption(self):
        """
        GIVEN a password encryption function
        WHEN encrypting a password
        THEN return a encrypted version of the password
        """

        assert encrypted_password != test_password, "the generated password can not be the same as the password given"


    def test_valid_password_decript(self):
        """
        GIVEN an encrypted password validator
        WHEN verifying if the correct password is valid
        THEN return True
        """

        assert check_password(encrypted_password, test_password, test_salt) is True, "should return true when the passwords match"

    def test_invalid_password_decript(self):
        """
        GIVEN an encrypted password validator
        WHEN verifying if the invalid password is correct
        THEN return false
        """
        password_check = check_password(encrypted_password, "this_is_an_incorrect_password", test_salt)
        assert password_check is False, "should return False when the password is incorrect"
    
    def test_salt_generator(self):
        """
        GIVEN a function that generates a random salt
        WHEN calling the function
        THEN return a random string
        """

        first_salt = generate_salt()
        assert isinstance(first_salt, str) is True, "should return a string"
    
    def test_random_salt(self):
        """
        GIVEN a function that generates a random salt
        WHEN calling the function several times
        THEN return a different string each time
        """
        first_salt = generate_salt()
        second_salt = generate_salt()

        assert first_salt != second_salt, "each time the function is called it should return a different random string"