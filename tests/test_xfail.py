import pytest


@pytest.mark.xfail(reason="Bug shut down the test run")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Bug already fixed, but test still shut down")
def test_without_bug():
    pass
