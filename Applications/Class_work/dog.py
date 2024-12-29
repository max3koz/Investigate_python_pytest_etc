class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting now!")

    def roll_over(self):
        print(f"{self.name} is rolled over now!")

first_dog = Dog("Boy", 6)

print(f"First dog name is {first_dog.name} and it is {first_dog.age} years old!")
first_dog.sit()
print(f"Now {first_dog.name} is sitting!")
first_dog.roll_over()
print(f"Now {first_dog.name} is rolling over!")