import pytest
import requests



# 1. FIXTURE: SESSION SCOPE AUTH TOKEN

@pytest.fixture(scope="session")
def auth_token():
    # In a real scenario, this would be an API call to /login
    print("\n[SESSION] Generating Auth Token...")
    token = "bearer-qa-senior-token-123"
    return token



# 2. FIXTURE: SETUP & TEARDOWN WITH YIELD

@pytest.fixture(scope="function")
def test_user(auth_token):
    # Setup: Create user
    print("\n[SETUP] Creating test user via API...")
    user_id = 101
    user_data = {"id": user_id, "username": "pytest_user"}

    yield user_data  # This provides the data to the test

    # Teardown: Delete user
    print(f"\n[TEARDOWN] Deleting test user {user_id}...")



# 5. FIXTURE CHAINING

@pytest.fixture(scope="session")
def base_url():
    print("\n[CHAIN 1] Providing Base URL")
    return "https://api.example.com"


@pytest.fixture(scope="session")
def chained_token(base_url):
    print(f"\n[CHAIN 2] Generating Token for {base_url}")
    return "token-xyz"


@pytest.fixture(scope="function")
def chained_user(chained_token):
    print(f"\n[CHAIN 3] Creating User with {chained_token}")
    return "User_001"




def test_user_profile_access(auth_token, test_user):
    print(f"Test running for {test_user['username']} using {auth_token}")
    assert test_user['id'] == 101


# 3. TEST: JSON SCHEMA VALIDATION
def test_json_schema():
    response_json = {
        "id": 1,
        "name": "Product A",
        "price": 25.50,
        "tags": ["electronics", "sale"]
    }

    print("\n[TEST] Validating JSON Keys and Types")
    assert isinstance(response_json["id"], int)
    assert isinstance(response_json["name"], str)
    assert isinstance(response_json["tags"], list)
    assert "price" in response_json


# 4. PARAMETRIZED STATUS CODE TEST
@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_http_status_codes(status_code):
    print(f"\n[TEST] Validating status code: {status_code}")
    assert status_code in [200, 400, 401, 500]


# 5. TEST: FIXTURE CHAIN EXECUTION
def test_fixture_chain(chained_user):
    print(f"\n[TEST] Test case executing for {chained_user}")
    assert chained_user == "User_001"