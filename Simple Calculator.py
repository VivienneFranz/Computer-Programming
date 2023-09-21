
First_user_input = input("Choose a number")
print(f'{First_user_input}')

Second_user_input = input("Choose another number")
print(f'{Second_user_input}')

Third_user_input = input("add, subrtact, multiply, divide")
print(f'{Third_user_input}')

def add():
    print(First_user_input + Second_user_input)
def subtract():
    print(First_user_input - Second_user_input)
def multiply():
    print(First_user_input * Second_user_input)
def divide():
    print(First_user_input / Second_user_input)



def simple_calculator(First, second, third):
    print(f"We start by calculating {First}")
    print(f"by {second}")
    print(f"This then equals {third}")

simple_calculator('First_user_input', 'Second_user_input', 'Third_user_input')
