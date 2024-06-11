import logging
import pytest

from Applications.string_update_function import StringUpdateFunction
from Applications.local_logger import console_logger, LogLevel

logger = console_logger(level=LogLevel.ERROR)


class TestStringUpdateFunction:
    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(
                StringUpdateFunction.between_markers("What is >apple<", ">", "<"), "apple",
                id="testcase_1"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "<head><title>My new site</title></head>",
                    "<title>", "</title>"), "My new site", id="testcase_2"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No[/b] hi", "[b]", "[/b]"), "No", id="testcase_3"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No [b]hi", "[b]", "[/b]"), "hi", id="testcase_4"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No hi", "[b]", "[/b]"), "No hi", id="testcase_5"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No <hi>", ">", "<"), "", id="testcase_6")
    ))
    def test_suite_find_text_between_expected_markers(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        try:
            assert actual_result == expected_result
        except Exception as e:
            logger.error(e.message), e.args
