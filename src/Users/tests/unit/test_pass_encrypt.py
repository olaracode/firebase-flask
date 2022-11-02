from Users.encrypt import generate_password, check_password, generate_salt

test_salt = "jgkam1"
test_password = "test_password"

def test_password_encryption():
    """
    GIVEN a password encryption function
    WHEN encrypting a password
    THEN return a encrypted version of the password
    """

    encrypted_password = generate_password(test_password, test_salt)
    assert encrypted_password != test_password, "the generated password can not be the same as the password given"

def test_valid_password_decript():
    """
    GIVEN a encryptes password validator
    WHEN verifiying if the given password is equal to the decrypted
    THEN return True
    """
    
    encrypted_password = generate_password(test_password, test_salt)
    assert check_password(encrypted_password, test_password, test_salt) is True, "should return true when the passwords match"
