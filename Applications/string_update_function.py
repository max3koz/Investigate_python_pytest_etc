import datetime


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
            res = text[begin_position:end_position]
        return res

    @staticmethod
    def convert_date(date: str) -> str:
        try:
            d, m, y = date.split("/")
            res_data = datetime.date(int(y), int(m), int(d)).isoformat()
            return res_data
        except ValueError:
            return "Error: Invalid date."

    @staticmethod
    def first_word(text: str) -> str:
        word = text.replace(".", " ").replace(",", " ").split()
        return word[0]

    @staticmethod
    def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
        count_item = abs(len(str1) - len(str2))
        for index in range(0, min(len(str1), len(str2))):
            if str1[index] != str2[index]:
                count_item += 1
        if count_item <= threshold:
            return True
        return False

    @staticmethod
    def translation(text: str) -> str:
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
    def sum_upto_n(N: int) -> int:
        res = 0
        for num in range(1, N+1):
            res += num
        return res

    @staticmethod
    def goes_after(word: str, first: str, second: str) -> bool:
        res = False
        first_letter_num = word.find(first)
        second_letter_num = word.find(second)
        if first_letter_num != -1 and second_letter_num != -1:
            if first_letter_num + 1 == second_letter_num:
                res = True
        return res

#print(StringUpdateFunction.between_markers("No <hi>", ">", "<"))

#print(StringUpdateFunction.convert_date("25/12/2021"))

#print(StringUpdateFunction.first_word(" a word "))

#print(StringUpdateFunction.fuzzy_string_match('fuzzy', 'fuzy', 2))

#print(StringUpdateFunction.translation("hoooowe yyyooouuu duoooiiine"))

#print(StringUpdateFunction.sum_upto_n(3))

print(StringUpdateFunction.goes_after('almaz', 'r', 'a'))
