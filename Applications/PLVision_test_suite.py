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
