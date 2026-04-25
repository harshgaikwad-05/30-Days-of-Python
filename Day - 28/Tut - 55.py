# decorators_example.py

# ------------------------------------------
# WHAT IS A DECORATOR?
# A decorator is a function that adds extra
# behavior to another function.
# ------------------------------------------


# STEP 1: Create a simple decorator
def my_decorator(func):
    def wrapper():
        print("⭐ Something is happening BEFORE the function runs")
        func()
        print("⭐ Something is happening AFTER the function runs")
    return wrapper


# STEP 2: Create a normal function
def say_hello():
    print("Hello, students!")


# STEP 3: Apply decorator manually
decorated_function = my_decorator(say_hello)

print("Running decorated function (manual way):")
decorated_function()

print("\n-----------------------------\n")


# STEP 4: Use @ syntax (easy way)
@my_decorator
def say_goodbye():
    print("Goodbye, students!")


print("Running decorated function (using @):")
say_goodbye()

print("\n-----------------------------\n")


# ------------------------------------------
# DECORATOR WITH ARGUMENTS
# ------------------------------------------

def smart_decorator(func):
    def wrapper(name):
        print("🔹 Preparing to greet...")
        func(name)
        print("🔹 Greeting done!")
    return wrapper


@smart_decorator
def greet(name):
    print(f"Hello, {name}!")


print("Decorator with arguments:")
greet("Rahul")

print("\n-----------------------------\n")


# ------------------------------------------
# REAL LIFE EXAMPLE: LOGIN CHECK
# ------------------------------------------

def login_required(func):
    def wrapper():
        is_logged_in = True   # change to False to test

        if is_logged_in:
            func()
        else:
            print("❌ You must log in first!")
    return wrapper


@login_required
def view_dashboard():
    print("📊 Welcome to your dashboard!")


print("Login example:")
view_dashboard()

print("\n-----------------------------\n")


# ------------------------------------------
# SUMMARY
# ------------------------------------------

print("Summary:")
print("1. Decorators add extra features to functions")
print("2. Use @decorator_name for easy syntax")
print("3. They help avoid repeating code")