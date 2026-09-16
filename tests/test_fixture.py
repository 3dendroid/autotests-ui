import pytest


@pytest.fixture(autouse=True)
def send_analytics():
    print("[AUTOUSE] Sending data to analytic server")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initialization session settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Creating class one time for classes")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Open browser everytime")


class TestUserFlow:
    def test_user_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
