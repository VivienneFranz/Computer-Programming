
computer = input("Greetings! We are willing to conduct an interveiw on types of programing careers you may be interested in. If you wish to continue please press Enter")
print(computer)

user_input = input("what is your name? ")
print(f'Nice to meet you, {user_input}! ')

user_input1 = input("We know you are thinking about some possible job careers. Here is a list of careers you may possibly be thinking about. Please press Enter to veiw")

list = 'Team Leader', 'Analyst', 'Senior Developer', 'Junior Developer', 'Product Manager'
for item in list:
    print(item)

user_input1 = input("What type of programming are you interested in? ")
print(f'Thats great that you are interested in {user_input1}. ')

if user_input1 == "Team Leader":
    print("Team Leader is a great choice! A softwear development team leader helps lead the team in developing software. A team leader also oversees teams of other programmers white completing development projects. ")
elif user_input1 == "Analyst":
    print("Analyst is a great choice! A analyst does")
