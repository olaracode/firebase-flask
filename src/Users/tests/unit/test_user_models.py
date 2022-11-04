from Users.models import User
fake_name = "Fake user"
fake_email = "fake_user@gmail.com"
fake_password = "some_password"

class TestUserModels:
    def test_user_models(self):
        """
        GIVEN a database model User
        WHEN all the fields are given
        THEN it should create an instance of said model
        """
        fake_user = User(name=fake_name, email=fake_email, password="some_password", salt="some_salt")
        assert fake_name == fake_user.name, "It should store the name"
        