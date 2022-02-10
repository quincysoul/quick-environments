class Person:
    name: str

    def __init__(self, name: str):
        self.name = name

    def say_name(self):
        return f"MY Name is: {self.name}"


if __name__ == "__main__":
    print("main method")
    person = Person("bob")
    res = person.say_name()
    print(res)
