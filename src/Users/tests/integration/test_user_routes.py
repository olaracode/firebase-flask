import json
import random

# Helping data
def generate_test_email():
    random_number = random.randint(0, 99) * 123456
    return f"Test{random_number}@test.com"

test_name = "test"
test_password = "testpassword"

class TestUserRoutes():
    def test_get_user(self, client):
        """
        GIVEN a User model
        WHEN a list of users is requested
        THEN return a serialized list of users
        """
        with client as test:
            response = test.get("/user")
            data = json.loads(response.data)

            assert response.status_code == 200, "should return 200 if successful"
            assert type(data) == list, "Should return a list"

    # def test_create_user(self, client):
    #     """
    #     GIVEN a create user request
    #     WHEN all required data is given
    #     THEN create the user and return success
    #     """
    #     with client as test:
    #         current_test_mail = generate_test_email()
    #         request = test.post("/user/register", json={
    #             "email": current_test_mail, "name": test_name, "password": test_password
    #         })
    #         data = json.loads(request.data)
    #         data = data["user"]
            
    #         assert request.status_code == 201, "should return 201 created"
    #         assert data["email"] == current_test_mail, "User should be created with the given email"
    #         assert data["name"] == test_name, "User should be created with the given name"

    #         assert data["active_order"] == "No active order", "user should be created with no active orders"

    #         assert type(data["orders"]) == list, "user orders should be of type list"
    #         assert len(data["orders"]) == 0, "user orders should be an empty list"

    def test_create_error_empty(self, client):
        """
        GIVEN a create user
        WHEN all fields are blank
        THEN return a 400 error
        """
        with client as test:
            request = test.post("/user/register", json={
                "email": "", "name": "", "password": ""
            })
            data = json.loads(request.data)
            assert request.status_code == 400, "should return 400 when no fie"
            assert data["error"] == "All fields are required", "should return an error dict with All fields are required value"

    def test_create_error_none(self, client):
        """
        GIVEN a create user request
        WHEN no fields are given
        THEN return a 400 error
        """
        with client as test:
            request = test.post("/user/register") 
            assert request.status_code == 400, "should return a 400 error when no fields are given"
