class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


class Developer(Employee):

    def __init__(self, name, salary, language):

        super().__init__(name, salary)

        self.language = language

    def code(self):
        print(f"{self.name} writes {self.language}")


dev = Developer("Alice salary is ", 120000, "Python")

dev.display()
dev.code()
