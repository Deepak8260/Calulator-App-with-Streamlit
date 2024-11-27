import math

history = []

# Arithmetic operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero is not allowed"

def mod(x, y):
    return x % y

def floor(x, y):
    return x // y

# Trigonometric functions
def sin(x):
    result = math.sin(math.radians(x))
    save_history(f"sin({x}) = {result}")
    return result

def cos(x):
    result = math.cos(math.radians(x))
    save_history(f"cos({x}) = {result}")
    return result

def tan(x):
    result = math.tan(math.radians(x))
    save_history(f"tan({x}) = {result}")
    return result

def cot(x):
    result = 1 / math.tan(math.radians(x))
    save_history(f"cot({x}) = {result}")
    return result

def sec(x):
    result = 1 / math.cos(math.radians(x))
    save_history(f"sec({x}) = {result}")
    return result

def cosec(x):
    result = 1 / math.sin(math.radians(x))
    save_history(f"cosec({x}) = {result}")
    return result

# Save calculation to history
def save_history(entry):
    history.append(entry)

# Retrieve calculation history
def get_history():
    return history
