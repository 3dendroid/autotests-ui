import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.skip(reason="feature in progress")
def test_feature_in_development_1():
    pass


@pytest.mark.skip(reason="feature in progress")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        pass

    def test_feature_in_development_2(self):
        pass
