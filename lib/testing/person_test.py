from lib.person import Person

def test_person_init_with_name():
    person = Person("Alice")
    assert person.name == "Alice"
