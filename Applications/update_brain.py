###################################
# is number even or odd?

def decision_even_or_odd(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

def decision_even_or_odd_binary(number: int) -> bool:
    if bin(number)[len((bin(number)))-1] == "0":
        return True
    else:
        return False

print(decision_even_or_odd(5))
print(decision_even_or_odd(6))

print(decision_even_or_odd_binary(7))
print(decision_even_or_odd_binary(8))

##################################
# Count how often each character appears in a string
string = 'qweraaaqqq'
d = {
    'q': 4,
}


def qty_letter_in_word(word):
    letters_dict = {}
    for letter in string:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

print(qty_letter_in_word(string))

###################################
# Array (list) rotation
input_list = [1, 2, 3, 4, 5, 6]
rotate = 3
direction = "left"
result = [3, 4, 5, 6, 1, 2]

def array_rotation(executed_list, exp_rotate, exp_direction) -> list:
    for _ in range(exp_rotate):
        if exp_direction == "left":
            element = executed_list.pop(0)
            executed_list.append(element)
        elif exp_direction == "right":
            element = executed_list.pop(len(executed_list)-1)
            executed_list.insert(0, element)
    return executed_list

print(array_rotation(input_list, rotate, direction))

###################################
# Sum all ints in list of lists

l = [[4, 5, [3], 4, [2, 3]], 7, [3, 4]]

def sum(list_data: [int, list]) -> int:
    if type(list_data) == int:
        return list_data
    else:
        result = 0
        for item in list_data:
            result += sum(item)
        return result
print(sum(l))

def factorial_recursive(n):
    print(f"{n=}")
    if n == 1:
        return n
    else:
        f = n * factorial_recursive(n - 1)
        return f

print("res = ", factorial_recursive(1))
print("res = ", factorial_recursive(2))
print("res = ", factorial_recursive(3))
print("res = ", factorial_recursive(4))

###################################
# Write function to print pyramid, when levels given:
    #
   ###
  #####
 #######
#########
def tree_print(levels):
    reverse_tree = []
    for qty_star in range(1, levels*2, 2):
        print(" " * (levels*2//2 - qty_star//2 - 1) + "#" * qty_star)
        reverse_tree.append(" " * (levels*2//2 - qty_star//2 - 1) + "#" * qty_star)

    print("\n".join(reverse_tree[::-1]))

    print("\n".join(" " * (levels * 2 // 2 - qty_star // 2 - 1) + "#" * qty_star for qty_star in range(1, levels * 2, 2)))
    print("\n".join(" " * (levels * 2 // 2 - qty_star // 2 - 1) + "#" * qty_star for qty_star in range(1, levels * 2, 2)[::-1]))

tree_print(6)
