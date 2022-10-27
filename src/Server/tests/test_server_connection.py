
def test_server_connection(client):
    """
    GIVEN a flask application
    WHEN requesting a connection
    THEN return a message
    """
    with client as test:
        response = test.get('/')
        assert response.status_code == 200