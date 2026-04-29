"""
python_inheritance_demo.py

This file demonstrates:
- Single Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Method Overriding
- Use of super()
"""

# -----------------------------
# Base Class
# -----------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# -----------------------------
# Single Inheritance
# -----------------------------
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# -----------------------------
# Multilevel Inheritance
# -----------------------------
class Puppy(Dog):
    def weep(self):
        print(f"{self.name} weeps softly.")

# -----------------------------
# Another Base Class
# -----------------------------
class Walker:
    def walk(self):
        print("This animal can walk.")

# -----------------------------
# Multiple Inheritance
# -----------------------------
class Cat(Animal, Walker):
    def speak(self):
        print(f"{self.name} meows.")

# -----------------------------
# Using super()
# -----------------------------
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)  # calling parent constructor
        self.wingspan = wingspan

    def speak(self):
        print(f"{self.name} chirps.")

    def show_details(self):
        print(f"Name: {self.name}, Wingspan: {self.wingspan} cm")


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    print("=== Single Inheritance ===")
    dog = Dog("Buddy")
    dog.speak()

    print("\n=== Multilevel Inheritance ===")
    puppy = Puppy("Max")
    puppy.speak()
    puppy.weep()

    print("\n=== Multiple Inheritance ===")
    cat = Cat("Whiskers")
    cat.speak()
    cat.walk()

    print("\n=== Using super() ===")
    bird = Bird("Tweety", 25)
    bird.speak()
    bird.show_details()