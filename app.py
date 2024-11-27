import math

history=[]

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
    result = 1/math.tan(math.radians(x))
    save_history(f"cot({x}) = {result}")
    return result
def sec(x):
    result = 1/math.cos(math.radians(x))
    save_history(f"sec({x}) = {result}")
    return result
def cosec(x):
    result = 1/math.sin(math.radians(x))
    save_history(f"cosec({x}) = {result}")
    return result

def save_history(entry):
    history.append(entry)

def show_history():
    if not history:
        print('No Calculations Present')
    else:
        print('Calculation History:')
        for i in history:
            print(i)

def repeat():
    opt = input('Do you want to continue (yes/no): ').strip().lower()
    if opt == 'yes':
        main()  # Restart from the beginning
    elif opt == 'no':
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Exiting...")
        exit()

def main():
    print('Welcome to Calculator')
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modular Division
    6. Floor Division
    7. Sine
    8. Cosine
    9. Tangent
    10. Cotangent
    11. Secant
    12. Cosecant
    13. Show History
    """)
    while True:
        try:
            option = int(input("Enter an option (1-13): "))
            if option in range(1, 7):  # Arithmetic operations
                x, y = map(int, input('Enter two numbers (separated by space): ').split())
                switch_case_example(option, x, y)
            elif option in range(7, 13):  # Trigonometric operations
                x = int(input("Enter an angle in degrees: "))
                switch_case_exam(option, x)
            elif option == 13:  # Show history
                show_history()
                repeat()
            else:
                print("Invalid option. Please choose a number between 1 and 13.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")


def switch_case_exam(option, x):
    match option:
        case 7:
            print(f"sin({x}) = {sin(x)}")
        case 8:
            print(f"cos({x}) = {cos(x)}")
        case 9:
            print(f"tan({x}) = {tan(x)}")
        case 10:
            print(f"cot({x}) = {cot(x)}")
        case 11:
            print(f"sec({x}) = {sec(x)}")
        case 12:
            print(f"cosec({x}) = {cosec(x)}")
    repeat()

def switch_case_example(option, x, y):
    match option:
        case 1:
            print(f'The addition of {x} and {y} is {add(x, y)}')
        case 2:
            print(f'The difference of {x} and {y} is {sub(x, y)}')
        case 3:
            print(f'The multiplication of {x} and {y} is {mul(x, y)}')
        case 4:
            print(f'The division of {x} and {y} is {div(x, y)}')
        case 5:
            print(f'The modular division of {x} and {y} is {mod(x, y)}')
        case 6:
            print(f'The floor division of {x} and {y} is {floor(x, y)}')
    
    repeat()  

# Run the program
main()
