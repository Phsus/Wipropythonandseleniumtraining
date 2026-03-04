import pytest

# --- FUNCTION SCOPE FIXTURES (Runs for every test) ---

@pytest.fixture(scope='function')
def openbrowser():
    print("\n[FUNC SETUP] Opening browser for this specific test")
    yield
    print("[FUNC TEARDOWN] Closing browser after this specific test")

@pytest.fixture(scope='function')
def closebrowser():
    # Note: Usually, setup and teardown are in ONE fixture using yield,
    # but since you used two separate ones earlier, here they are:
    print("[FUNC ACTION] Executing specific close browser logic")


# --- CLASS SCOPE FIXTURES (Runs once per class) ---

@pytest.fixture(scope='class')
def class_setup():
    print("\n[CLASS SETUP] Initializing Server/Environment for the Class")
    yield
    print("\n[CLASS TEARDOWN] Cleaning up Environment after the Class")


# --- DATA FIXTURES (Default function scope) ---

@pytest.fixture
def simple_data():
    return 45

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print(f"Current browser param: {request.param}")
    return request.param


@pytest.fixture(scope = "module")
def setupapi():
    print("authorizze apis with username and password")
    yield
    print("Unauthorize apis with username and password")  # tear do


@pytest.fixture(scope = "session")
def sessionsetup():
    print("Tests in qaenvironment")
    yield
    print("teardown")

@pytest.fixture
def fixture_a():
    return "Data from A"


@pytest.fixture
def fixture_b(fixture_a):
    return f"{fixture_a} + Data from B"