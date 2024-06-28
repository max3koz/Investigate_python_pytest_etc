import datetime

from collections.abc import Iterable
from typing import Union
from math import sqrt


class StringUpdateFunction:
    @staticmethod
    def between_markers(text: str, begin: str, end: str) -> str:
        """
        returns substring between two given markers
        """
        # your code here
        begin_position,  end_position = 0, len(text)
        if text.count(begin) <= 1 and text.count(end) <= 1:
            if text.count(begin) == 1:
                begin_position = text.find(begin) + len(begin)
            if text.count(end) == 1:
                end_position = text.find(end)
        return text[begin_position:end_position]

    @staticmethod
    def convert_date(date: str) -> str:
        """
        This function should take a date string in the format dd/mm/yyyy and convert it to the format yyyy-mm-dd.
        If the input is not in the correct format, the function should return an error message "Error: Invalid date.".
        """
        try:
            d, m, y = date.split("/")
            res_data = datetime.date(int(y), int(m), int(d)).isoformat()
            return res_data
        except ValueError:
            return "Error: Invalid date."

    @staticmethod
    def first_word(text: str) -> str:
        """
        You are given a string where you have to find its first word.
        When solving a task pay attention to the following points:
        There can be dots and commas in a string.
        - a string can start with a letter or, for example, one/multiple dot(s) or space(s);
        - a word can contain an apostrophe, and it's a part of a word;
        - the whole text can be represented with one word and that's it.
        """
        word = text.replace(".", " ").replace(",", " ").split()
        return word[0]

    @staticmethod
    def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
        """
        Given two strings and a permissible number of character differences,
        determine if the strings can be considered approximately equal.
        """
        count_item = abs(len(str1) - len(str2))
        for index in range(0, min(len(str1), len(str2))):
            if str1[index] != str2[index]:
                count_item += 1
        if count_item <= threshold:
            return True
        return False

    @staticmethod
    def translation(text: str) -> str:
        """
        Make a translation module.
        The bird converts words by two rules:
        - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
        - after each vowel letter the bird appends two of the same letter (a ⇒ aaa).
        """
        letters = "aeiouy"
        res_list = ''
        index = 0
        while index < len(text):
            if text[index] == " ":
                res_list += text[index]
            elif text[index] not in letters and text[index + 1] in letters:
                res_list += text[index]
                index += 1
            elif text[index] in letters:
                if text[index:index+3] == text[index] * 3:
                    res_list += text[index]
                    index += 2
            index += 1
        return res_list

    @staticmethod
    def sum_up_to_n(n: int) -> int:
        """Calculate sum of integers from 1 to given N (including)."""
        res = 0
        for num in range(1, n+1):
            res += num
        return res

    @staticmethod
    def goes_after(word: str, first: str, second: str) -> bool:
        """
        In a given word you need to check if one symbol goes only right after another.
        Cases you should expect while solving this challenge:
        - one of the symbols is not in the given word - your function should return False;
        - any symbol appears in a word more than once - use only the first one;
        - two symbols are the same - your function should return False;
        - the condition is case-sensitive, which means 'a' and 'A' are two different symbols.
        """
        res = False
        first_letter_num = word.find(first)
        second_letter_num = word.find(second)
        if first_letter_num != -1 and second_letter_num != -1:
            if first_letter_num + 1 == second_letter_num:
                res = True
        return res

    @staticmethod
    def longest_prefix(arr: list[str]) -> str:
        """
        This function should take a list of strings and determine
        the longest common prefix among all the strings.
        If there is no common prefix, it should return an empty string.
        """
        res = arr.pop()
        word_length = len(res)
        while arr:
            second_word = arr.pop()
            index = 0
            while index < min(word_length, len(second_word)) and res[index] == second_word[index]:
                index += 1
            if not (word_length := index):
                return ""
        return res[:word_length]

    @staticmethod
    def reverse_digits(num: int) -> int:
        """
        Reverse the digits of a given integer.
        For instance, 1234 should become 4321.
        For negative integers, the sign should remain in the front; e.g., -123 becomes -321.
        """
        num_string = str(num)
        if num_string[0] == '-':
            reversed_num_string = num_string[0] + "".join(reversed(num_string[1:]))
        else:
            reversed_num_string = "".join(reversed(num_string))
        return int(reversed_num_string)

    @staticmethod
    def is_armstrong(num: int) -> bool:
        """
        In number theory, an Armstrong number (after Michael F. Armstrong) or narcissistic number
        in a given number base (10 for this mission) is a number that is the sum of its own digits
        each raised to the power of the number of digits.
        For example, 153 is an Armstrong number because 13 + 53 + 33 == 153.
        """
        res = False
        armstrong = 0
        num_length = len(str(num))
        for num_elem in str(num):
            armstrong += int(num_elem) ** num_length
        if armstrong == num:
            res = True
        return res

    @staticmethod
    def calculate_qty_armstrong_number(num_first: int, num_end: int) -> int:
        """
        Calculate how many armstrong number in given range
        """
        count = 0
        for number in range(num_first, num_end):
            if StringUpdateFunction.is_armstrong(number) is True:
                count += 1
        return count

    @staticmethod
    def max_of_three(a: int, b: int, c: int) -> int:
        """
        Given three integers, determine which one is the largest.
        """
        res = max(a, b, c)
        return res

    @staticmethod
    def string_permutations(s: str) -> Iterable[str]:
        """
        Given a string, return all possible permutations of its characters, sorted alphabetically.
        """
        all_permutations = []
        if len(s) < 2:
            return [s]
        for index, char in enumerate(s):
            remaining_chars = s[:index] + s[index+1:]
            for perm in StringUpdateFunction.string_permutations(remaining_chars):
                all_permutations.append(char + perm)
        res = all_permutations
        return res

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Check if the given year is leap year.
        A year is a leap year if it is divisible by 4, except for end-of-century years which must be divisible by 400.
        This means that the year 2000 was a leap year, although 1900 was not.
        """
        status_leap_year = True
        if year % 4 != 0 or (year % 400 != 0 and year % 100 == 0):
            status_leap_year = False
        return status_leap_year

    @staticmethod
    def end_zeros(a: int) -> int:
        """
        Try to find out how many zeros a given number has at the end.
        """
        count = 0
        for number in reversed(str(a)):
            if number == "0":
                count += 1
            else:
                break
        return count

    @staticmethod
    def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
        """
        The code must return Iterable containing two values: the roots x1, x2, sorted descending.
        If there's only one real root, both values will be the same.
        If there are no real roots, the Iterable should contain the string "No real roots".
        """
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            return [x1, x2]
        elif discriminant == 0:
            x = -b / 2 * a
            return [x, x]
        else:
            return ["No real roots"]

    @staticmethod
    def count_divisible(n: int, k: int) -> int:
        """
        Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive)
        are divisible by k.
        """
        count = 0
        for item in range(1, n+1):
            if item % k == 0:
                count += 1
        return count

    @staticmethod
    def is_perfect_number(n: int) -> bool:
        """
        A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
        For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
        """
        total = 0
        for item in range(1, n):
            if n % item == 0:
                total += item
        if total == n:
            return True
        else:
            return False

    @staticmethod
    def longest_substr(s: str) -> int:
        data = {}
        start = res = 0
        for index, char in enumerate(s):
            if char in data:
                start = max(start, data[char]+1)
            data[char] = index
            res = max(res, index - start + 1)
        return res

    @staticmethod
    def checkio(number: int) -> int:
        """
        You are given a positive number.
        Your function should calculate the product of the digits excluding any zeroes.
        """
        res = 1
        for item in str(number):
            if int(item) != 0:
                res = res * int(item)
        return res

    @staticmethod
    def from_camel_case(name: str) -> str:
        """
        Convert the name of a function from CamelCase ("MyFunctionName") into the Python format ("my_function_name")
        where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
        """
        new_name = []
        for index, item in enumerate(name):
            if item.isupper() is True and index != 0:
                new_name.append("_" + item.lower())
            elif item.isupper() is True and index == 0:
                new_name.append(item.lower())
            else:
                new_name.append(item)
        res = "".join(new_name)
        return res

    @staticmethod
    def to_camel_case(name: str) -> str:
        """
        Convert the name of a function from the Python format (for example "my_function_name")
        into CamelCase ("MyFunctionName") where the first char of every word is in uppercase
        and all words are concatenated without any intervening characters.
        """
        res = ""
        new_name = name.split("_")
        for index, item in enumerate(new_name):
            res += item.capitalize()
        return res

    @staticmethod
    def calculate_chars(text: str) -> str:
        """
        You are given a text, which contains different English letters and punctuation symbols.
        You should find the most frequent letter in the text. The letter returned must be in lower case.
        """
        data = {}
        for char in text.lower():
            if char in data:
                data[char] += 1
            else:
                data[char] = 1
        count_value = 0
        chat_list = dict(sorted(data.items(), reverse=True))
        print(chat_list)
        for char in chat_list:
            if data[char] >= count_value and char.isalpha() is True:
                count_value = data[char]
                res = char
        return res

    @staticmethod
    def find_middle(text: str) -> str:
        """
        You are given some string where you need to find its middle character(s).
        The string may contain one word, a few symbols or a whole sentence.
        If the length of the string is even, then you should return two middle characters,
        but if the length is odd, return just one.
        """
        string_middle = len(text) // 2
        if len(text) % 2 != 0:
            return text[string_middle]
        else:
            return text[string_middle - 1] + text[string_middle]


print(StringUpdateFunction.find_middle("test"))
