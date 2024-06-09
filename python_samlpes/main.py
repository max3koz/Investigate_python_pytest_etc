"""
var_1 = 10
print(var_1)
print(type(var_1))
var_1 = "Text"
print(var_1)
print(type(var_1))

print()
prace = float(input("How mach does it cost? "))
discount = float(input("Which discount do you have in %?: "))
print("Your cost is ", float(prace * (1 - discount/100)))

side_a = float(input("Enter the sida a: "))
side_b = float(input("Enter the sida b: "))

p_value = 2 * (side_a + side_b)
s_value = side_a * side_b

print("The perimetr is ", p_value)
print("The sque is ", s_value)

var = 10
new_var = bool(var)
print(type(new_var), new_var)

empty_string = ''
string = input("Enter string:")
print()
print(f"The string is '{string}'. Is it empty? ", empty_string == string)


first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))
third_value = float(input("Enter third value: "))

assert first_value + second_value + third_value == 100, "You have the problam with the calculation )))"


first_password = input("Enter password: ")
second_password = input("Repeat password: ")
assert first_password == second_password, "The password string in not equal"
print("The password is agree!!!")

list_of_marks = input('Enter list with values: ')
marks_list = list_of_marks.split(' ')
print(marks_list)
sum_marks = 0
for mark in marks_list:
    sum_marks += int(mark)
middle_mark = sum_marks/len(marks_list)
print('The middle of marks is ', middle_mark)

list_of_marks = input('Enter 4 words via gap: ')
words_list = list_of_marks.split(' ')
for i in range(2):
    words_list.pop()
words_list.append('Maks')
print(words_list)


number_list = [-2, -3, 0, 1, 2]
new_number_list = []
print(number_list)
for mark in number_list:
    mark = mark * mark
    new_number_list.append(mark)
print(new_number_list)

counter = 0
sum = 0
while counter <= 100:
    sum += counter
    counter += 1
    print(sum)


counter = 10
while counter > 0:
    print(counter)
    counter = counter - 1
"""

#our_string = "Hello world"

#print(our_string.upper()) #HELLO WORLD
#print(our_string.lower()) #hello world
#print(our_string.count("l")) #3
#print(our_string.count("ll")) #1
#print(our_string.count("l", 3)) #2
#print(our_string.count("l", 3, 7)) #1
#print(our_string.find("wor")) #6
#print(our_string.find("o")) #4
#print(our_string.rfind("apple")) ValueError: substring not found
#print(our_string.index("apple")) ValueError: substring not found
#print(our_string.replace("Hello", "Hej")) #Hej world
#print(our_string.replace(" ", "")) #Helloworld
#print(our_string.isalpha()) #False
#print("asdfag".isalpha()) #True
#print(our_string.isdigit()) #False
#print("text".rjust(10)) #      text
#print("text".rjust(10, "!")) # !!!!!!text
#print("text".ljust(10, "1")) # text111111
#new_string = "     hi     "
#print(new_string.strip()) # hi
#print(new_string.lstrip()) # hi
#print(new_string.rstrip()) #      hi

'''
mark_list = [2, 4, 5, 3, 2, 4, 2, 5]
new_mark_list = []
for elem in mark_list:
    if elem > 3:
        new_mark_list.append(elem)
new_mark_list.sort()
print(new_mark_list)
'''

word_1 = ["apple", "banana"]
word_2 = ["limon", "jui"]
word_1.extend(word_2)
print(word_1)
word_1.sort(key=len)
print(word_1)
for elem in word_1:
    print(f"{elem} ({len(elem)})")
