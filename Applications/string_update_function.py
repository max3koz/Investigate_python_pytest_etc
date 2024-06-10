from collections.abc import Iterable


class StringUpdateFunction:

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
