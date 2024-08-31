def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

# Add_numbers function definition
def add_numbers(a, b):
    return a + b

# Decorator and call the function application
print(apply_decorator(add_numbers)(1, 2))