import logging
import pytest

from Applications.list_update_function import ListUpdateFunction
from Applications.local_logger import console_logger, LogLevel

logger = console_logger(level=LogLevel.ERROR)


class TestSuiteListUpdateFunction:
    @pytest.mark.parametrize("data, result", (
            pytest.param(list(ListUpdateFunction.compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])),
                         [5, 4, 5, 6, 5, 7, 8, 0], id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([7, 7])), [7],
                         id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])), [1, 2, 1],
                         id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([])), [],
                         id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([1, 2, 3, 4])), [1, 2, 3, 4],
                         id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9])), [],
                         id="testcase_with_suite_data_"),
            pytest.param(list(ListUpdateFunction.compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])), [9, 0, 9],
                         id="testcase_with_suite_data_"),
    ))
    def test_list_update_func(self, data, result):
        logger.info(f"Test case with testing list {data} and result list {result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        try:
            assert data == result
        except Exception as e:
            logger.error(e.message)
