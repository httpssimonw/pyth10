class Person:
    def greeting(self):
        return "Hello! Я человек."

    def __str__(self):
        return "Person"

class Student(Person):
    def greeting(self):
        return "Hello! Я студент."

    def __str__(self):
        return "Student"

class Teacher(Student):
    def greeting(self):
        return "Hello! Я учитель."

    def __str__(self):
        return "Teacher"

person = Person()
student = Student()
teacher = Teacher()

print(person.greeting())
print(str(person))

print(student.greeting())
print(str(student))

print(teacher.greeting())
print(str(teacher))



class Dog:
    def greeting(self):
        return "Woof! I am a dog."
    def __str__(self):
        return "Dog"

class Cat:
    def greeting(self):
        return "Meow! I am a cat."
    def __str__(self):
        return "Cat"

class Bird:
    def greeting(self):
        return "Chirp! I am a bird."
    def __str__(self):
        return "Bird"


dog = Dog()
cat = Cat()
bird = Bird()

print(dog.greeting())
print(cat.greeting())
print(bird.greeting())
