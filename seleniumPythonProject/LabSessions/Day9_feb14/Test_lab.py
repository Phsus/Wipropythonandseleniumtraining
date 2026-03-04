import pytest
import requests
import sys


# 1. Skip because feature is not implemented yet
@pytest.mark.skip(reason="Feature not implemented yet: waiting on backend PR #45")
def test_new_dashboard_feature():
    assert False


# 2. Run only on Linux, skip on Windows
@pytest.mark.skipif(sys.platform == "win32", reason="Linux-specific feature, does not run on Windows")
def test_linux_system_logs():
    # This will only execute if the OS is not Windows
    assert True


# 3. Dynamic skip based on API Health
def test_api_health_endpoint():
    url = "https://httpbin.org/status/404"  # Example URL that returns 404
    try:
        # Real-world check: If status is not 200, skip the rest of the test
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            pytest.skip(f"Endpoint returned {response.status_code}. Skipping test.")
    except requests.exceptions.RequestException:
        pytest.skip("API unreachable.")

    # Logic that only runs if API is healthy
    assert response.status_code == 200


# 4. Mark a failing test as xfail (Expected Failure)
@pytest.mark.xfail(reason="Bug #123: sorting algorithm intermittently fails")
def test_sorting_logic():
    items = [3, 1, 2]
    assert items == [1, 2, 3]


# 5. Parameterized cases with 2 specific xfails
@pytest.mark.parametrize("input_val, expected", [
    (1, 2),  # Case 1: Pass
    (2, 4),  # Case 2: Pass
    (3, 6),  # Case 3: Pass
    # Marking specific cases as xfail using pytest.param
    pytest.param(10, 20, marks=pytest.mark.xfail(reason="Bug #404: overflow error")),
    pytest.param(0, 0, marks=pytest.mark.xfail(reason="Bug #505: zero division")),
])
def test_multiplication_logic(input_val, expected):
    # Imagine a bug exists for inputs 10 and 0
    assert input_val * 2 == expected