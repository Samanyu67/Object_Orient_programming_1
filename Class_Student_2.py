class student:
    grade = 7
    name = "Samanyu"

    def introduction(self):
        print("Hello, I am a student")

    def details(self):
        print("My name is:", self.name)
        print("I am in:", self.grade)

ob = student()
ob.introduction()
ob.details()