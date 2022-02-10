import unittest

from src.__main__ import Person

person = Person("bob")


class TestPerson(unittest.TestCase):
    def test_person_name(self):
        "person has a name"
        self.assertEqual(person.say_name(), "MY Name is: bob")
