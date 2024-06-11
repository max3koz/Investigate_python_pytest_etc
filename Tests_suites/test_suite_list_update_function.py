import pytest
import logging

from Applications.list_update_function import ListUpdateFunction


class TestSuiteListUpdateFunction:
    @pytest.mark.parametrize("data, result", (
            pytest.param(list(ListUpdateFunction.compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])),
                         [5, 4, 5, 6, 5, 7, 8, 0, 1], id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([7, 7])), [7],
                         id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])), [1, 2, 1],
                         id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([])), [],
                         id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([1, 2, 3, 4])), [1, 2, 3, 4],
                         id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9])), [9],
                         id="testcase_with_suite_data_1"),
            pytest.param(list(ListUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])), [9, 0, 9],
                         id="testcase_with_suite_data_1"),
    ))
    def test_list_update_func(self, data, result):
        logging.info(f"Test case with testing list {data} and result list {result}.")
        logging.info((f"Step 1. Verify expected result to actual result."))
        assert data == result
