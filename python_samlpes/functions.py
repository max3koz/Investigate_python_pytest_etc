def sun_number(num_1, num_2):
    res = num_1 - num_2
    return res


def check_odd_even(number):
    check_value = number % 2
    if check_value == 0:
        result_string = 'Even'
    else:
        result_string = 'Odd'
    return result_string


def find_max(num_1, num_2, num_3):
    result = max(num_1, num_2, num_3)
    return result
