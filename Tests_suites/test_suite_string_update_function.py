import pytest

from Applications.string_update_function import StringUpdateFunction
from Applications.local_logger import console_logger, LogLevel

logger = console_logger(level=LogLevel.ERROR)


class TestStringUpdateFunction:
    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(
                StringUpdateFunction.between_markers("What is >apple<", ">", "<"), "apple",
                id="testcase_1_find_text_between_expected_markers"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "<head><title>My new site</title></head>",
                    "<title>", "</title>"), "My new site", id="testcase_2_find_text_between_expected_markers"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No[/b] hi", "[b]", "[/b]"), "No", id="testcase_3_find_text_between_expected_markers"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No [b]hi", "[b]", "[/b]"), "hi", id="testcase_4_find_text_between_expected_markers"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No hi", "[b]", "[/b]"), "No hi", id="testcase_5_find_text_between_expected_markers"),
            pytest.param(
                StringUpdateFunction.between_markers(
                    "No <hi>", ">", "<"), "", id="testcase_6_find_text_between_expected_markers")
    ))
    def test_suite_find_text_between_expected_markers(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        try:
            assert actual_result == expected_result
        except Exception as e:
            logger.error(e.message), e.args

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.convert_date("25/12/2021"), "2021-12-25",
                         id="testcase_1_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("01/01/2000"), "2000-01-01",
                         id="testcase_2_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("15/06/1995"), "1995-06-15",
                         id="testcase_3_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("29/02/2020"), "2020-02-29",
                         id="testcase_4_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("10/10/2010"), "2010-10-10",
                         id="testcase_5_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("31/05/1985"), "1985-05-31",
                         id="testcase_6_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("07/08/1960"), "1960-08-07",
                         id="testcase_7_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("02/09/1999"), "1999-09-02",
                         id="testcase_8_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("30/04/1975"), "1975-04-30",
                         id="testcase_9_convert_data"),
            pytest.param(StringUpdateFunction.convert_date("29/02/2019"), "Error: Invalid date.",
                         id="testcase_10_convert_data_negative"),
            pytest.param(StringUpdateFunction.convert_date("30/04/1975/1"), "Error: Invalid date.",
                         id="testcase_11_convert_data_negative"),
    ))
    def test_suite_convert_data(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.first_word("Hello world"), "Hello",
                         id="testcase_1_find_first_word"),
            pytest.param(StringUpdateFunction.first_word(" a word "), "a",
                         id="testcase_2_find_first_word"),
            pytest.param(StringUpdateFunction.first_word("don't touch it"), "don't",
                         id="testcase_3_find_first_word"),
            pytest.param(StringUpdateFunction.first_word("greetings, friends"), "greetings",
                         id="testcase_4_find_first_word"),
    ))
    def test_suite_find_first_word(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result


    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.fuzzy_string_match("apple", "appel", 2), True,
                         id="testcase_1_find_fuzzy_string_match"),
            pytest.param(StringUpdateFunction.fuzzy_string_match("apple", "bpple", 1), True,
                         id="testcase_2_find_fuzzy_string_match"),
            pytest.param(StringUpdateFunction.fuzzy_string_match("apple", "bpple", 0), False,
                         id="testcase_3_find_fuzzy_string_match_negative"),
            pytest.param(StringUpdateFunction.fuzzy_string_match("apple", "apples", 1), True,
                         id="testcase_4_find_fuzzy_string_match"),
            pytest.param(StringUpdateFunction.fuzzy_string_match("apple", "apples", 0), False,
                         id="testcase_5_find_fuzzy_string_match_negative"),
            pytest.param(StringUpdateFunction.fuzzy_string_match('fuzzy', 'fuzy', 2), True,
                         id="testcase_6_find_fuzzy_string_match"),
    ))
    def test_suite_find_fuzzy_string_match(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.translation("hieeelalaooo"), "hello",
                         id="testcase_1_translation"),
            pytest.param(StringUpdateFunction.translation("hoooowe yyyooouuu duoooiiine"), "how you doin",
                         id="testcase_2_translation"),
            pytest.param(StringUpdateFunction.translation("aaa bo cy da eee fe"), "a b c d e f",
                         id="testcase_3_translation"),
            pytest.param(StringUpdateFunction.translation("sooooso aaaaaaaaa"), "sos aaa",
                         id="testcase_4_translation"),
    ))
    def test_suite_translation(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result


    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.sum_upto_n(1), 1, id="testcase_1_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(2), 3, id="testcase_2_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(3), 6, id="testcase_3_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(4), 10, id="testcase_4_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(5), 15, id="testcase_5_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(10), 55, id="testcase_6_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(20), 210, id="testcase_7_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(100), 5050, id="testcase_8_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(200), 20100, id="testcase_9_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(500), 125250, id="testcase_10_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_upto_n(1000), 500500, id="testcase_11_sum_upto_n"),
    ))
    def test_suite_sum_upto_n(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result


    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.goes_after("world", "w", "o"), True,
                         id="testcase_1_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("world", "w", "r"), False,
                         id="testcase_2_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("world", "l", "o"), False,
                         id="testcase_3_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("panorama", "a", "n"), True,
                         id="testcase_4_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("list", "l", "o"), False,
                         id="testcase_5_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("", "l", "o"), False,
                         id="testcase_6_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("list", "l", "l"), False,
                         id="testcase_7_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("world", "d", "w"), False,
                         id="testcase_8_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("Almaz", "a", "l"), False,
                         id="testcase_9_find_goes_after"),
            pytest.param(StringUpdateFunction.goes_after("Almaz", "A", "l"), True,
                         id="testcase_10_find_goes_after"),
    ))
    def test_suite_find_goes_after(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result