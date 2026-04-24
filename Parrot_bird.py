class parrot:

    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

james = parrot("James", 12)
john = parrot("John", 14)

print("James is a {}".format(james.species))
print("John is a {}".format(john.species))

print("{} is {} years old".format(james.name, james.age))
print("{} is {} years old".format(john.name, john.age))