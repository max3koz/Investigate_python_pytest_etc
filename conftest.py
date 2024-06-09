import pytest


@pytest.fixture
def database():
    print('connection')
    data = 10
    yield data
    print('close')

def fixture_1():
    print('-> function')
    yield
    print('-. function <-')
