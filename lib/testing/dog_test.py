from lib.dog import Dog

def test_dog_init_with_name_and_breed_default_to_mutt():
    dog = Dog("Buddy")
    assert dog.name == "Buddy"
    assert dog.breed == "Mutt"

def test_dog_init_with_name_and_custom_breed():
    dog = Dog("Max", "Labrador")
    assert dog.name == "Max"
    assert dog.breed == "Labrador"
