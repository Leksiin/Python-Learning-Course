from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

    def defend(self):
        print("Dog is defending")

    def speak(self):
        print("Woof!")

    def move(self):
        print("Dog is running")


dog = Dog("Dog", 20, "Husky")

print(dog)

dog.speak()
dog.move()
dog.defend()
