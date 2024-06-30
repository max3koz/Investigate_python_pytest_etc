import logging
import pytest

from Applications.list_update_function import ListUpdateFunction
from Applications.local_logger import console_logger, LogLevel

logger = console_logger(level=LogLevel.ERROR)


class TestSuiteListUpdateFunction:
    @pytest.mark.parametrize("data, expected_result", (
            pytest.param([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0], [5, 4, 5, 6, 5, 7, 8, 0],
                         id="verify_update_func_"),
            pytest.param([7, 7], [7], id="testcase_verify_update_func_"),
            pytest.param([1, 1, 1, 1, 2, 2, 2, 1, 1, 1], [1, 2, 1], id="testcase_verify_update_func_"),
            pytest.param([], [], id="testcase_verify_update_func_"),
            pytest.param([1, 2, 3, 4], [1, 2, 3, 4], id="testcase_verify_update_func_"),
            pytest.param([9, 9, 9, 9, 9, 9, 9], [9], id="testcase_verify_update_func_"),
            pytest.param([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9], [9, 0, 9], id="testcase_verify_update_func_"),
    ))
    def test_suite_list_verify_update_func(self, data, expected_result):
        logger.info(f"Test case with testing data {data} and result list {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert list(ListUpdateFunction.compress(data)) == expected_result

    @pytest.mark.parametrize("items, border, expected_result", (
            pytest.param([1, 2, 3, 4, 5], 3, [1, 2, 3], id="testcase_verify_remove_all_after_"),
            pytest.param([1, 1, 2, 2, 3, 3], 2, [1, 1, 2], id="testcase_verify_remove_all_after_"),
            pytest.param([1, 1, 2, 4, 2, 3, 4], 2, [1, 1, 2], id="testcase_verify_remove_all_after_"),
            pytest.param([1, 1, 5, 6, 7], 2, [1, 1, 5, 6, 7], id="testcase_verify_remove_all_after_"),
            pytest.param([10, 1, 5, 6, 7, 10], 5, [10, 1, 5], id="testcase_verify_remove_all_after_"),
            pytest.param([1, 2, 6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3], 6, [1, 2, 6],
                         id="testcase_verify_remove_all_after_"),
    ))
    def test_suite_list_verify_remove_all_after(self, items, border, expected_result):
        logger.info(f"Test case with testing list: {items}, border: {border} and result list: {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert list(ListUpdateFunction.remove_all_after(items, border)) == expected_result

    @pytest.mark.parametrize("items, expected_result", (
            pytest.param([-5, 10, 99, 123456], True, id="testcase_verify_is_ascending_"),
            pytest.param([99], True, id="testcase_with_suite_data_"),
            pytest.param([4, 5, 6, 7, 3, 7, 9], False, id="testcase_verify_is_ascending_"),
            pytest.param([], True, id="testcase_verify_is_ascending_"),
            pytest.param([1, 1, 1, 1], False, id="testcase_verify_is_ascending_"),
            pytest.param([1, 3, 3, 5], False, id="testcase_verify_is_ascending_"),
            pytest.param([-5, -6], False, id="testcase_verify_is_ascending_"),
            pytest.param([1, 2, 3], True, id="testcase_verify_is_ascending_"),
            pytest.param([1, 1], False, id="testcase_verify_is_ascending_"),
            pytest.param([-1, 0, 1], True, id="testcase_verify_is_ascending_"),
            pytest.param([1, 0, 1], False, id="testcase_verify_is_ascending_"),
            pytest.param([1, 2, 4, 3, 5], False, id="testcase_verify_is_ascending_"),
    ))
    def test_suite_list_verify_is_ascending(self, items, expected_result):
        logger.info(f"Test case with testing list: {items} and result list: {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert ListUpdateFunction.is_ascending(items) == expected_result

    @pytest.mark.parametrize("values, expected_result", (
            pytest.param([-20, -5, 10, 15], [-5, 10, 15, -20], id="testcase_verify_abs_sorted_list_"),
            pytest.param([1, 2, 3, 0], [0, 1, 2, 3], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-1, -2, -3, 0], [0, -1, -2, -3], id="testcase_verify_abs_sorted_list_"),
            pytest.param([0], [0], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83,
                          -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65,
                          -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47,
                          -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29,
                          -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11,
                          -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],
                         [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20,
                          -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39,
                          -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58,
                          -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77,
                          -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96,
                          -97, -98, -99], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-2, 1], [1, -2], id="testcase_verify_abs_sorted_list_"),
            pytest.param([0, 1], [0, 1], id="testcase_verify_abs_sorted_list_"),
            pytest.param([3, -76], [3, -76], id="testcase_verify_abs_sorted_list_"),
            pytest.param([40, 11, 28, 99, 72, -23, 88, 15, 47, 68, 56, 93, 60, -59, -18, -37, 27, -46, 53, 30],
                         [11, 15, -18, -23, 27, 28, 30, -37, 40, -46, 47, 53, 56, -59, 60, 68, 72, 88, 93, 99],
                         id="testcase_verify_abs_sorted_list_"),
            pytest.param([7], [7], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-68, 57, -58, 55, -99, 10, 14],
                         [10, 14, 55, 57, -58, -68, -99], id="testcase_verify_abs_sorted_list_"),
            pytest.param([69, -40, 22, 79, 2, -26, -58, -96, 73, -46, -15, -59, 47],
                         [2, -15, 22, -26, -40, -46, 47, -58, -59, 69, 73, 79, -96],
                         id="testcase_verify_abs_sorted_list_"),
            pytest.param([35, -24, 83], [-24, 35, 83], id="testcase_verify_abs_sorted_list_"),
            pytest.param([32, -54, 50, -78, 9, -31, -11, -89, 16, -85, -79, -13, -68, -30, -53, 22, -25, 59, 24],
                         [9, -11, -13, 16, 22, 24, -25, -30, -31, 32, 50, -53, -54, 59, -68, -78, -79, -85, -89],
                         id="testcase_verify_abs_sorted_list_"),
            pytest.param([25, -69], [25, -69], id="testcase_verify_abs_sorted_list_"),
            pytest.param([66], [66], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-97, 57, 52, 96], [52, 57, 96, -97], id="testcase_verify_abs_sorted_list_"),
            pytest.param([-41, 71, -99, 20, 2, 43, 64, 33, 23, 45, 16],
                         [2, 16, 20, 23, 33, -41, 43, 45, 64, 71, -99], id="testcase_verify_abs_sorted_list_"),
            pytest.param([96, 7, -66, -25, 16, -8, -68, -41, 98, -99, 58, 88, 67, -45, 89, 31],
                         [7, -8, 16, -25, 31, -41, -45, 58, -66, 67, -68, 88, 89, 96, 98, -99],
                         id="testcase_verify_abs_sorted_list_"),
            pytest.param([62, 49, 13, 99, -75, 15, -74, -40, -72, -88, -66, 26, -71, 48],
                         [13, 15, 26, -40, 48, 49, 62, -66, -71, -72, -74, -75, -88, 99],
                         id="testcase_verify_abs_sorted_list_"),
            pytest.param([2, -36, 42, -45, -67, 7, 86],
                         [2, 7, -36, 42, -45, -67, 86], id="testcase_verify_abs_sorted_list_"),
    ))
    def test_suite_list_verify_abs_sorted_list(self, values, expected_result):
        logger.info(f"Test case with testing list: {values} and result list: {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert ListUpdateFunction.abs_sorted_list(values) == expected_result

    @pytest.mark.parametrize("text, words, expected_result", (
            pytest.param('hi world im here', ['world', 'here'], True, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['here', 'world'], False, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['world'], True, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['world', 'here', 'hi'], False, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['world', 'im', 'here'], True, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['world', 'hi', 'here'], False, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['world', 'world'], False, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['country', 'world'], False, id="testcase_verify_words_order"),
            pytest.param('hi world im here', ['wo', 'rld'], False, id="testcase_verify_words_order"),
            pytest.param('', ['world', 'here'], False, id="testcase_verify_words_order"),
            pytest.param('hi world world im here', ['world', 'world'], False,id="testcase_verify_words_order"),
            pytest.param('hi world world im here hi world world im here', ['world', 'here'], True,
                         id="testcase_verify_words_order"),
            pytest.param('london in the capital of great britain', ['London'], False, id="testcase_verify_words_order"),
            pytest.param('london in the capital of great britain', ['london'], True, id="testcase_verify_words_order"),
            pytest.param('london in the capital of great britain', ['london', 'great'], True, id="testcase_verify_words_order"),
            pytest.param('london in the capital of great britain', ['london', 'of', 'great'], True,
                         id="testcase_verify_words_order"),
            pytest.param('london in the capital of great britain', ['britain', 'great'], False,
                         id="testcase_verify_words_order"),
    ))
    def test_suite_list_verify_words_order(self, text, words, expected_result):
        logger.info(f"Description:\n    Test case with \n     - testing list: {text}, \n     - border: {words} \n     - result list: {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert ListUpdateFunction.words_order(text, words) == expected_result

    @pytest.mark.parametrize("items, border, expected_result", (
            pytest.param([1, 2, 3, 4, 5], 3, [3, 4, 5], id="testcase_verify_remove_all_before_"),
            pytest.param([1, 1, 2, 2, 3, 3], 2, [2, 2, 3, 3], id="testcase_verify_remove_all_before_"),
            pytest.param([1, 1, 2, 4, 2, 3, 4], 2, [2, 4, 2, 3, 4], id="testcase_verify_remove_all_before_"),
            pytest.param([1, 1, 5, 6, 7], 2, [1, 1, 5, 6, 7], id="testcase_verify_remove_all_before_"),
            pytest.param([], 0, [], id="testcase_verify_remove_all_before_"),
            pytest.param([7, 7, 7, 7, 7, 7, 7, 7, 7], 7, [7, 7, 7, 7, 7, 7, 7, 7, 7],
                         id="testcase_verify_remove_all_before_"),

            pytest.param([10, 1, 5, 6, 7, 10], 5, [5, 6, 7, 10], id="testcase_verify_remove_all_before_"),
            pytest.param([1, 2, 6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3], 6, [6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3],
                         id="testcase_verify_remove_all_before_"),
    ))
    def test_suite_list_verify_remove_all_after(self, items, border, expected_result):
        logger.info(f"Test case with testing list: {items}, border: {border} and result list: {expected_result}.")
        logger.info(f"Step 1. Verify expected result to actual result.")
        assert list(ListUpdateFunction.remove_all_before(items, border)) == expected_result
