import pytest

class TestClass:

    def setup_method(self):
        print('connection to database')
        self.data = 10

    def  teardown_method(self):
        print('close database')
    @pytest.mark.smoke
    def test_1(self):
        print("test_1 running")
        assert self.data == 10

    def test_2(self):
        print("test_2 running")
        assert self.data > 9

def test_3(database):
    print("test_3 running")
    assert database > 8
