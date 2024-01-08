import pytest

@pytest.mark.xfail(condition=True, reason='123', strict=True) # condition - пометка теста, причина необходима для кондишена. strict - представление ожидаемого результата, задаем что выйдет на выходе по этому тесту.
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False