class StringUpdateFunction:
    @staticmethod
    def between_markers(text: str, begin: str, end: str) -> str:
        """
        returns substring between two given markers
        """
        # your code here
        begin_position,  end_position= 0, len(text)
        if text.count(begin) <= 1 and text.count(end) <= 1:
            if text.count(begin) == 1:
                begin_position = text.find(begin) + len(begin)
            if text.count(end) == 1:
                end_position = text.find(end)
            print(begin_position)
            print(end_position)
            res = text[begin_position:end_position]
        return res

print("Example:")
print(StringUpdateFunction.between_markers("No <hi>", ">", "<"))

