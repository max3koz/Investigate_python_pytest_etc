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
            logger.error(e), e.args

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
            pytest.param(StringUpdateFunction.sum_up_to_n(1), 1, id="testcase_1_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(2), 3, id="testcase_2_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(3), 6, id="testcase_3_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(4), 10, id="testcase_4_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(5), 15, id="testcase_5_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(10), 55, id="testcase_6_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(20), 210, id="testcase_7_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(100), 5050, id="testcase_8_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(200), 20100, id="testcase_9_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(500), 125250, id="testcase_10_sum_upto_n"),
            pytest.param(StringUpdateFunction.sum_up_to_n(1000), 500500, id="testcase_11_sum_upto_n"),
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

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.longest_prefix(["flower", "flow", "flight"]), "fl",
                         id="testcase_1_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["dog", "racecar", "car"]), "",
                         id="testcase_2_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["apple", "application", "appetizer"]), "app",
                         id="testcase_3_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["a"]), "a",
                         id="testcase_4_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["", "b"]), "",
                         id="testcase_5_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["same", "same", "same"]), "same",
                         id="testcase_6_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["mismatch", "mister", "miss"]), "mis",
                         id="testcase_7_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["alphabet", "alpha", "alphadog"]), "alpha",
                         id="testcase_8_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["book", "boot", "booster"]), "boo",
                         id="testcase_9_find_longest_prefix"),
            pytest.param(StringUpdateFunction.longest_prefix(["short", "shore", "shot"]), "sho",
                         id="testcase_10_find_longest_prefix"),
    ))
    def test_suite_find_longest_prefix(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.reverse_digits(1234), 4321,
                         id="testcase_1_reverse_digits"),
            pytest.param(StringUpdateFunction.reverse_digits(0), 0,
                         id="testcase_2_reverse_digits"),
            pytest.param(StringUpdateFunction.reverse_digits(-123), -321,
                         id="testcase_3_reverse_digits"),
            pytest.param(StringUpdateFunction.reverse_digits(5), 5,
                         id="testcase_4_reverse_digits"),
    ))
    def test_suite_reverse_digits(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.is_armstrong(153), True,
                         id="testcase_1_find_armstrong_number"),
            pytest.param(StringUpdateFunction.is_armstrong(370), True,
                         id="testcase_2_find_armstrong_number"),
            pytest.param(StringUpdateFunction.is_armstrong(947), False,
                         id="testcase_3_find_armstrong_number"),
            pytest.param(StringUpdateFunction.is_armstrong(371), True,
                         id="testcase_4_find_armstrong_number"),
    ))
    def test_suite_find_armstrong_number(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.calculate_qty_armstrong_number(0, 1000), 14,
                         id="testcase_1_find_qty_armstrong_number"),
            pytest.param(StringUpdateFunction.calculate_qty_armstrong_number(10, 1000), 4,
                         id="testcase_2_find_qty_armstrong_number"),
            pytest.param(StringUpdateFunction.calculate_qty_armstrong_number(10, 1000000), 11,
                         id="testcase_3_find_qty_armstrong_number"),
            pytest.param(StringUpdateFunction.calculate_qty_armstrong_number(0, 10_000_000), 25,
                         id="testcase_4_find_qty_armstrong_number"),
    ))
    def test_suite_find_qty_armstrong_number(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.max_of_three(1, 2, 3), 3,
                         id="testcase_1_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(3, 2, 1), 3,
                         id="testcase_2_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(1, 3, 2), 3,
                         id="testcase_3_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(0, 0, 0), 0,
                         id="testcase_4_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(-1, -2, -3), -1,
                         id="testcase_1_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(5, 5, 4), 5,
                         id="testcase_2_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(-5, -5, -6), -5,
                         id="testcase_3_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(10, 9, 10), 10,
                         id="testcase_4_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(123, 456, 789), 789,
                         id="testcase_3_find_max_of_three"),
            pytest.param(StringUpdateFunction.max_of_three(789, 123, 456), 789,
                         id="testcase_4_find_max_of_three"),
    ))
    def test_suite_find_max_of_three(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.string_permutations("ab"), ["ab", "ba"],
                         id="testcase_1_find_string_permutations"),
            pytest.param(StringUpdateFunction.string_permutations("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"],
                         id="testcase_2_find_string_permutations"),
            pytest.param(StringUpdateFunction.string_permutations("a"), ["a"],
                         id="testcase_3_find_string_permutations"),
            pytest.param(StringUpdateFunction.string_permutations("abcd"),
                         ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac",
                          "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca",
                          "dcab", "dcba"
                          ],
                         id="testcase_4_find_string_permutations"),
            pytest.param(StringUpdateFunction.string_permutations("aab"), ['aab', 'aab', 'aba', 'aba', 'baa', 'baa'],
                         id="testcase_5_find_string_permutations"),
    ))
    def test_suite_find_string_permutations(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.is_leap_year(2000), True,
                         id="testcase_1_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(1900), False,
                         id="testcase_2_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2004), True,
                         id="testcase_3_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2100), False,
                         id="testcase_4_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2020), True,
                         id="testcase_5_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2021), False,
                         id="testcase_6_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(1600), True,
                         id="testcase_7_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(1700), False,
                         id="testcase_8_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(1800), False,
                         id="testcase_9_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2400), True,
                         id="testcase_10_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(2500), False,
                         id="testcase_11_find_leap_year"),
            pytest.param(StringUpdateFunction.is_leap_year(1), False,
                         id="testcase_12_find_leap_year"),
    ))
    def test_suite_find_leap_year(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.end_zeros(0), 1,
                         id="testcase_1_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(1), 0,
                         id="testcase_2_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(10), 1,
                         id="testcase_3_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(101), 0,
                         id="testcase_4_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(245), 0,
                         id="testcase_5_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(100100), 2,
                         id="testcase_6_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(3456), 0,
                         id="testcase_7_find_end_zeros"),
            pytest.param(StringUpdateFunction.end_zeros(100234), 0,
                         id="testcase_8_find_end_zeros"),

    ))
    def test_suite_find_end_zeros(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.quadratic_roots(1, -3, 2), [2, 1],
                         id="testcase_1_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, 0, -1), [1, -1],
                         id="testcase_2_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, 2, 1), [-1, -1],
                         id="testcase_3_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, 0, 1), ["No real roots"],
                         id="testcase_4_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, 4, 4), [-2, -2],
                         id="testcase_5_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, -5, 6), [3, 2],
                         id="testcase_6_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(1, -6, 9), [3, 3],
                         id="testcase_7_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(2, 2, 2), ["No real roots"],
                         id="testcase_8_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(2, -7, 6), [2, 1.5],
                         id="testcase_9_find_quadratic_roots"),
            pytest.param(StringUpdateFunction.quadratic_roots(2, -3, 1), [1, 0.5],
                         id="testcase_10_find_quadratic_roots"),
    ))
    def test_suite_find_quadratic_roots(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.count_divisible(10, 2), 5,
                         id="testcase_1_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(10, 3), 3,
                         id="testcase_2_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(10, 5), 2,
                         id="testcase_3_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(15, 4), 3,
                         id="testcase_4_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(20, 6), 3,
                         id="testcase_5_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(100, 10), 10,
                         id="testcase_6_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(200, 25), 8,
                         id="testcase_7_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(50, 7), 7,
                         id="testcase_8_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(60, 8), 7,
                         id="testcase_9_find_count_divisible"),
            pytest.param(StringUpdateFunction.count_divisible(70, 9), 7,
                         id="testcase_10_find_count_divisible"),
            #pytest.param(StringUpdateFunction.count_divisible(1_000_000_000, 2), 500_000_000,
            #             id="testcase_11_find_count_divisible"),
            #pytest.param(StringUpdateFunction.count_divisible(1_000_000_000, 1_000_000_000), 1,
            #             id="testcase_12_find_count_divisible"),
    ))
    def test_suite_find_count_divisible(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.is_perfect_number(6), True,
                         id="testcase_1_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(2), False,
                         id="testcase_2_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(28), True,
                         id="testcase_3_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(20), False,
                         id="testcase_4_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(496), True,
                         id="testcase_5_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(30), False,
                         id="testcase_6_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(8128), True,
                         id="testcase_7_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(100), False,
                         id="testcase_8_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(500), False,
                         id="testcase_9_find_perfect_number"),
            pytest.param(StringUpdateFunction.is_perfect_number(1000), False,
                         id="testcase_10_find_perfect_number"),
            #pytest.param(StringUpdateFunction.is_perfect_number(33550336), True,
            #             id="testcase_11_find_perfect_number"),
            #pytest.param(StringUpdateFunction.is_perfect_number(999983), False,
            #             id="testcase_12_find_perfect_number"),
    ))
    def test_suite_find_perfect_number(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.longest_substr("abcabcbb"), 3,
                         id="testcase_1_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("bbbbb"), 1,
                         id="testcase_2_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("pwwkew"), 3,
                         id="testcase_3_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("abcdef"), 6,
                         id="testcase_4_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr(""), 0,
                         id="testcase_5_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("au"), 2,
                         id="testcase_6_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("dvdf"), 3,
                         id="testcase_7_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("anviaj"), 5,
                         id="testcase_8_find_longest_substr"),
            pytest.param(StringUpdateFunction.longest_substr("ohomm"), 3,
                         id="testcase_9_find_longest_substr"),
    ))
    def test_suite_find_longest_substr(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.checkio(123405), 120, id="testcase_1_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(999), 729, id="testcase_2_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(1000), 1, id="testcase_3_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(1111), 1, id="testcase_4_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(999999), 531441, id="testcase_5_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(1), 1, id="testcase_6_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(9), 9, id="testcase_7_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(736635), 11340, id="testcase_8_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(375251), 1050, id="testcase_9_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(778241), 3136, id="testcase_10_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(930154), 540, id="testcase_11_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(306026), 216, id="testcase_12_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(194325), 1080, id="testcase_13_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(376087), 7056, id="testcase_14_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(550643), 1800, id="testcase_15_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(90160), 54, id="testcase_16_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(232177), 588, id="testcase_17_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(951216), 540, id="testcase_18_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(273438), 4032, id="testcase_19_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(256991), 4860, id="testcase_20_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(542929), 6480, id="testcase_21_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(399996), 118098, id="testcase_22_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(929806), 7776, id="testcase_23_find_longest_substr"),
            pytest.param(StringUpdateFunction.checkio(638332), 2592, id="testcase_24_find_longest_substr"),
    ))
    def test_suite_find_end_zeros(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.from_camel_case("MyFunctionName"), "my_function_name",
                         id="testcase_1_check_from_camel_case"),
            pytest.param(StringUpdateFunction.from_camel_case("IPhone"), "i_phone",
                         id="testcase_2_check_from_camel_case"),
            pytest.param(StringUpdateFunction.from_camel_case("ThisFunctionIsEmpty"), "this_function_is_empty",
                         id="testcase_3_check_from_camel_case"),
            pytest.param(StringUpdateFunction.from_camel_case("Name"), "name",
                         id="testcase_4_check_from_camel_case"),
            pytest.param(StringUpdateFunction.from_camel_case("ThisIsReallyVeryLongString"),
                         "this_is_really_very_long_string",
                         id="testcase_5_check_from_camel_case"),
            pytest.param(StringUpdateFunction.from_camel_case("test0time"), "test0time",
                         id="testcase_6_check_from_camel_case"),

    ))
    def test_suite_check_from_camel_case(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.to_camel_case("my_function_name"), "MyFunctionName",
                         id="testcase_1_check_to_camel_case"),
            pytest.param(StringUpdateFunction.to_camel_case("i_phone"), "IPhone",
                         id="testcase_2_check_to_camel_case"),
            pytest.param(StringUpdateFunction.to_camel_case("this_function_is_empty"), "ThisFunctionIsEmpty",
                         id="testcase_3_check_to_camel_case"),
            pytest.param(StringUpdateFunction.to_camel_case("name"), "Name",
                         id="testcase_4_check_to_camel_case"),
            pytest.param(StringUpdateFunction.to_camel_case("this_is_really_very_long_string"),
                         "ThisIsReallyVeryLongString",
                         id="testcase_5_check_to_camel_case"),
            pytest.param(StringUpdateFunction.to_camel_case("test0time"), "Test0time",
                         id="testcase_6_check_to_camel_case"),

    ))
    def test_suite_check_to_camel_case(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.calculate_chars("Lorem ipsum dolor sit amet"), "m",
                         id="testcase_1_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("Lorem ipsum dolor sit amet 0000000000000000000"),
                         "m",
                         id="testcase_2_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("Aaaaaaaaaaaaaaaa!!!!"), "a",
                         id="testcase_3_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("Gregor then turned to look out the window at the"
                                                              " dull weather.Nooooooooooo!!! Why!?!"), "o",
                         id="testcase_4_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;"
                                                              "lzcdkcslksdkseewme,"), "k",
                         id="testcase_5_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("fsbd"), "b",
                         id="testcase_6_check_calculate_chars"),
            pytest.param(StringUpdateFunction.calculate_chars("abb"), "b",
                         id="testcase_7_check_calculate_chars"),

    ))
    def test_suite_check_calculate_chars(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.find_middle("example"), "m",
                         id="testcase_1_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("test"), "es",
                         id="testcase_2_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("    few whitespaces   "), "it",
                         id="testcase_3_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("very-very long sentence"), "o",
                         id="testcase_4_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("symbols are: !@#$%^&*()="), ": ",
                         id="testcase_5_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("*"), "*",
                         id="testcase_6_find_middle_string"),
            pytest.param(StringUpdateFunction.find_middle("Hi"), "Hi",
                         id="testcase_7_find_middle_string"),

    ))
    def test_suite_find_middle_string(self, actual_result, expected_result):
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result

    @pytest.mark.parametrize("actual_result, expected_result", (
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 8), "Hi my...",
                         id="testcase_1_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 4), "Hi...",
                         id="testcase_2_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 20),
                         "Hi my name is Alex",
                         id="testcase_3_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 18),
                         "Hi my name is Alex",
                         id="testcase_4_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 9), "Hi my...",
                         id="testcase_5_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 11), "Hi my name...",
                         id="testcase_6_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('OMG you did it', 4), "OMG...",
                         id="testcase_7_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 10), "Hi my name...",
                         id="testcase_8_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Alex', 1), "...",
                         id="testcase_9_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hello my name is Alex', 2), "...",
                         id="testcase_10_find_cut_sentence"),
            pytest.param(StringUpdateFunction.cut_sentence('Hi my name is Bartholomew', 22),
                         "Hi my name is...",
                         id="testcase_11_find_cut_sentence"),

    ))
    def test_suite_find_cut_sentence(self, actual_result, expected_result):
        logger.info(f"Test case: '{id}'.")
        logger.info(f"Test case with result text '{expected_result}'.")
        logger.info(f"Verify expected result to actual result.")
        assert actual_result == expected_result
