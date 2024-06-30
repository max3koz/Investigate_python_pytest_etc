from collections.abc import Iterable


class ListUpdateFunction:
    @staticmethod
    def compress(items: list[int]) -> Iterable[int]:
        # your code here
        new_list = []
        if len(items) > 0:
            exist = items[0]
            new_list.append(exist)
            for item in items:
                if item != exist:
                    new_list.append(item)
                    exist = item
        return new_list

    @staticmethod
    def remove_all_after(items: list[int], border: int) -> Iterable[int]:
        """
        Not all of the elements are important.
        What you need to do here is to remove all of the elements after the given one from sequence.
        """
        if border in items:
            res = []
            for item in items:
                if item != border:
                    res.append(item)
                elif item == border:
                    res.append(item)
                    break
        else:
            res = items
        return res

    @staticmethod
    def is_ascending(items: list[int]) -> bool:
        """
        Determine whether a sequence of elements is ascending such that each of its elements is strictly larger
        than (and not merely equal to) the preceding element. Empty sequence is considered as ascending.
        """
        if len(items) <= 1:
            res = True
        else:
            for index, item in enumerate(items[:-1]):
                if item < items[index+1]:
                    res = True
                else:
                    res = False
                    break
        return res

    @staticmethod
    def abs_sorted_list(values: list) -> list:
        """
        The sequence has various numbers. You should sort it, but sort it by absolute value in ascending order.
        For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
        Your function should return the sorted list or tuple.
        """
        abs_list = {}
        res = []
        for num in values:
            abs_list[abs(num)] = num
        sorted_keys = sorted(abs_list.items())
        for values in sorted_keys:
            res.append(values[1])
        return res

    @staticmethod
    def words_order(text: str, words: list) -> bool:
        """
        You have a text and a sequence of words.
        You need to check if the words in sequence appear in the same order as in the given text.
        """
        if len(words) == 2 and len(set(words)) == 1:
            res = False
        else:
            res = False
            text_word_list = text.split(" ")
            counts = []
            for index_text, item_text in enumerate(text_word_list):
                for index_words, item_words in enumerate(words):
                    if item_text == item_words and item_text not in counts:
                        counts.append(item_text)
                        if counts == words:
                            res = True
        return res

    @staticmethod
    def remove_all_before(items: list, border: int) -> Iterable:
        if len(items) < 1:
            res = []
        elif border not in items:
            res = items
        else:
            for index, item in enumerate(items):
                if item != border:
                    items.pop(index)
                else:
                    res = items[index:]
                    break
        return res


print(ListUpdateFunction.remove_all_before([1, 1, 2, 2, 3, 3], 2))
