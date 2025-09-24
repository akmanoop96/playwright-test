import pytest


@pytest.fixture(scope="module")

def prework():
    print("I set Up Module Instance")
    return 'pass'

@pytest.fixture(scope="function")


def secondWork():
    print("I set Up secondWork Instance")
    yield
    print('Tear Down Validation')




@pytest.mark.smoke
def test_intialCheck(prework, secondWork):
    print('This is my first test')
    assert prework=='pass'

@pytest.mark.skip()

def test_secondcheck(presetupwork, secondWork):
    print("This is my second test")