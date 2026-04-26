"""
GETTERS AND SETTERS IN PYTHON
============================

In Python, getters and setters are used to control access to class attributes.
They allow you to add logic when getting or setting a value, instead of directly
accessing the variable.

Unlike some languages (like Java), Python encourages a more elegant approach
using properties instead of explicit getX() / setX() methods.

--------------------------------------------------
1. WHY USE GETTERS AND SETTERS?
--------------------------------------------------

- Encapsulation: Protect internal data
- Validation: Ensure only valid values are assigned
- Flexibility: Change implementation without changing interface

--------------------------------------------------
2. BASIC APPROACH (NOT PYTHONIC)
--------------------------------------------------

This is the traditional style (less preferred in Python):

class Person:
    def __init__(self, name):
        self._name = name   # underscore = "internal use"

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value


Usage:
p = Person("Alice")
print(p.get_name())   # getter
p.set_name("Bob")     # setter

--------------------------------------------------
3. PYTHONIC WAY: USING @property
--------------------------------------------------

Python provides a cleaner way using decorators.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        '''Getter'''
        return self._name

    @name.setter
    def name(self, value):
        '''Setter'''
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value


Usage:
p = Person("Alice")

print(p.name)     # calls getter
p.name = "Bob"    # calls setter

NOTE:
It looks like direct access, but actually runs your logic.

--------------------------------------------------
4. ADDING A DELETER (OPTIONAL)
--------------------------------------------------

You can also define a deleter:

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


Usage:
p = Person("Alice")
del p.name

--------------------------------------------------
5. VALIDATION EXAMPLE
--------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


Usage:
acc = BankAccount(100)
acc.balance = 200     # OK
acc.balance = -50     # ERROR

--------------------------------------------------
6. READ-ONLY PROPERTY
--------------------------------------------------

If you only define @property and NOT a setter, it becomes read-only.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


Usage:
c = Circle(5)
print(c.area)   # works
# c.area = 100  # ERROR (no setter)

--------------------------------------------------
7. KEY CONCEPTS
--------------------------------------------------

- _variable: convention for "internal use"
- @property: defines getter
- @x.setter: defines setter
- @x.deleter: defines delete behavior

--------------------------------------------------
8. WHEN TO USE?
--------------------------------------------------

Use properties when:
- You need validation
- You may change implementation later
- You want computed attributes (like area, speed, etc.)

Avoid overusing them for simple direct attributes unless needed.

--------------------------------------------------
9. SUMMARY
--------------------------------------------------

- Python doesn't require explicit getters/setters
- Use @property for clean and readable code
- It gives control WITHOUT changing how the object is used

--------------------------------------------------
END OF FILE
--------------------------------------------------
"""