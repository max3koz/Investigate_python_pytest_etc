import pytest

from Applications.string_update_function import StringUpdateFunction

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename="report.log",
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class TestSuiteStringUpdateFunction:

    def test_string_update_func_1(self):
        assert (list(StringUpdateFunction.compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) ==
                [5, 4, 5, 6, 5, 7, 8, 0,]), logging.error(f"Error!!")

    def test_string_update_func_2(self):
        assert (list(StringUpdateFunction.compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1])

    @pytest.mark.parametrize("data, result", (
            pytest.param(list(StringUpdateFunction.compress([7, 7])), [7],
                         id="test_param_1"),
            pytest.param(list(StringUpdateFunction.compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])), [1, 2, 1],
                         id="test_param_2")
    ))
    def test_string_update_func_3(self, data, result):
        assert data == result

    def test_string_update_func_4(self):
        assert list(StringUpdateFunction.compress([])) == []

    def test_string_update_func_5(self):
        assert list(StringUpdateFunction.compress([1, 2, 3, 4])) == [1, 2, 3, 4]

    def test_string_update_func_6(self):
        assert list(StringUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9])) == [9]

    def test_string_update_func_7(self):
        assert list(StringUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]
