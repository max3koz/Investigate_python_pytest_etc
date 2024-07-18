# is number even or odd?
n = 42
n2 = 15


def is_even(num):
    s = False
    if num % 2 == 0:
        s = True
    return print(s)


is_even(n)
is_even(n2)

##################################
# Count how often each character appears in a string
string = 'qweraaaqqq'
d = {
    'q': 4,
}


def counter(string):
    d = {}
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(counter(string))




###################################
# Array (list) rotation
input = [1, 2, 3, 4, 5, 6]
rotate = 2
direction = "left"
#  result = [3, 4, 5, 6, 1, 2]


def rotate_list(input, rotate, direction):
    for i in range(rotate):
        if direction == "left":
            num = input.pop(0)
            input.append(num)
        else:
            num = input.pop(len(input)-1)
            input.insert(0, num)
    return input

print(rotate_list(input, rotate, direction))

###################################
# Sum all ints in list of lists

l = [[4, 5, [3]], 7, [3, 4]]


def list_sum(item):
    if type(item) == int:
        return item
    else:
        res = 0
        for i in item:
            res += list_sum(i)
        return res

# [4, 5, 3]
# res += list_sum(4) = 4
# res += list_sum(5) = 5
# res += list_sum(3) = 3
# 12
#
# [7, [3, 4]]
# res += list_sum(7) = 7
# res += list_sum([3, 4]) != int
# [3, 4]
# res += list_sum(3) = 3
# res += list_sum(4) = 4
# 7
# res += 7
# 14


print(list_sum(l))


# def factorial_recursive(n):
#     print(f"{n=}")
#     if n == 1:
#         return n
#     else:
#         f = n * factorial_recursive(n - 1)
#         print(f"{n=}", f)
#         return f
#
# factorial_recursive(4)



##################################

# Write function to print pyramid, when levels given:

    #
   ###
  #####
 #######
#########
pyramid_height = 6


def pyramid(levels):
    for i in range(1, levels*2, 2):
        print(" " * (levels*2//2-i//2-1) + "#" * i)

pyramid(pyramid_height)


# def is_year_leap(year):
#     #
#     # Ваш код з попередньої лабораторної роботи.
#     #
#     if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#         return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     #
#     # Ваш код з попередньої лабораторної роботи.
#     #
#     if month == 2 and is_year_leap(year) == True:
#         return 29
#     elif month == 2 and is_year_leap(year) == False:
#         return 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     else:
#         return 31
#
# def day_of_year(year, month, day):
#     #
#     # Напишіть тут свій новий код.
#     #
#     total = 0
#     for month_num in range(1, month):
#         print(month_num)
#
#         if day > 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10
#                          or month == 12):
#             return None
#             break
#         elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
#             return None
#             break
#         elif is_year_leap(year) is True and day > 29 and month == 2:
#             return None
#             break
#         elif is_year_leap(year) is False and day > 28 and month == 2:
#             return None
#             break
#
#         if month == 2:
#             if is_year_leap(year) == True and day < 30:
#                 total += days_in_month(year, month_num)
#             elif is_year_leap(year) == True and day < 29:
#                 total += days_in_month(year, month_num)
#             else:
#                 return None
#                 break
#         else:
#             total += days_in_month(year, month_num)
#         print(days_in_month(year, month_num), total)
#     return total + day
#
#
# print(day_of_year(2000, 11, 31))


def is_prime(num):
    #
    # Напишіть тут свій код.
    #
    count = 0
    for number in range(2, num):
        if num % number == 0:
            count += 1
    if count == 0:
        return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()