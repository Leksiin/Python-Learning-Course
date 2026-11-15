from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cat")

    def speak(self):
        print("Miau")

    def move(self):
        print("Cat is walking")

cat1 = Cat("Marusya", 10)
cat2 = Cat("John", 11)

print(cat1)
print(cat2)

cat1.speak()
cat2.speak()

cat1.move()
cat2.move()
