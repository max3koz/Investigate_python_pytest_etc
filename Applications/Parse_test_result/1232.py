l = [[4, 5, [3]], 3, [2, 5]]

def sum(list_data):
    if type(list_data) == int:
        return list_data
    else:
        result = 0
        for item in list_data:
            result += sum(item)
        return result

print(sum(l))

text = "lkasakhjg"

def count_letter(text_sample: str) -> dict:
    counter_dict = {}
    for letter in text_sample:
        if letter in counter_dict.keys():
            counter_dict[letter] += 1
        else:
            counter_dict[letter] = 1
    return counter_dict

print(count_letter(text))

# from subprocess import Popen, PIPE
#
#
# pwd_command = "cat 12*"
#
# output = Popen(pwd_command, shell=True, text=True, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
#
# for line in output.stdout:
#     print(line)
# print(output)


# l = [8, 2, 5, 3]
# d = l[::-1]
# # l.sort()
# print(l)
# print(d)
#
# s = "asd"
# s1 = s[::-1]
# print(s)
# print(s1)


