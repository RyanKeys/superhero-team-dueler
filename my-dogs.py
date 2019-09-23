

import dog


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


my_other_dog = Dog("Annie", "SuperDoggo")
my_dog = Dog("Rex", "superdoggo")
print(my_other_dog.name)
print(my_dog.breed)
my_dog.bark()
