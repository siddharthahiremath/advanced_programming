import unittest
from people.py import Person
class TestPeople(unittest.TestCase):
    def test_person_creation(self):
        person = Person("John", 30)
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 30)

    def test_person_birthday(self):
        person = Person("John", 30)
        person.birthday()
        self.assertEqual(person.age, 31)

    def test_person_name_change(self):
        person = Person("John", 30)
        person.change_name("Jane")
        self.assertEqual(person.name, "Jane")

if __name__ == '__main__':
    unittest.main()