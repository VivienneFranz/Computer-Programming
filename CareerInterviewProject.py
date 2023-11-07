
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
    print("Team Leader is a great choice! A softwear development team leader helps lead the team in developing software. A team leader also oversees teams of other programmers white completing development projects.         Please press Enter to continue.")
elif user_input1 == "Analyst":
    print("Analyst is a great choice! The Analyst's role is to define, develop, test, analyze, and maintain new software applications in support of the achievement of business requirements. This includes writing, coding, testing, and analyzing software programs and applications.      Please press Enter to continue.")
elif user_input1 == "Senior Developer":
    print("Senior Developer is a great choice! A senior programmer is responsible for the design, development, and implementation of software programs and applications that align with the business requirements.    Please press Enter to continue. ")
elif user_input1 == "Junior Developer":
    print("Junior Developer is a great choice! A Junior Developer is an entry-level programmer or software developer that assists a development team. Their duties include analyzing technical requirements, writing basic code, fixing bugs or error messages and collecting user feedback.        Please press Enter to continue. ")
elif user_input1 == "Product Manager":
    print("Product Manager is a great choice! Progect managers set the strateges and roadmap for the product, working with cross-functional teams to define and execute its success.        Please press Enter to continue. ")
else:
    print("The information you inputed is not correct please try again.")

user_input2 = input("Now that we have talked about what you are interested in lets start asking some more questions.   Please press Enter to continue.")

user_input3 = input("What are your years of experience? ")
print(f"Thats great that you have {user_input3} years of experience")

user_input4 = input("Do you have a desired salary?")

print("That's great.")

user_input5 = input("We will ask you a few TRUE or FALSE questions.")

user_input6 = input("True or False? It often takes a two-year associate or a four-year bachelor's degree to have some kind of computer programming career. ")
print(user_input6)

if user_input6 == "True":
    print("Correct!")
elif user_input6 == "False":
    print("Not correct")
else:
    print("The information you have typed is not matching up with TRUE or FALSE. ")


user_input7 = input("True or False? It is important to have technical skills include knowing several programming languages, understanding software and application design and functionality principles" )
print(user_input7)

if user_input7 == "True":
    print("Correct!")
elif user_input7 == "False":
    print("Not correct")
else:
    print("The information you have typed is not matching up with TRUE or FALSE. ")

user_input8 = input("True or False? The FOUR basics of programming are variables, data types, sequence, selection, and iteration.")
print(user_input8)

if user_input8 == "True":
    print("Correct!")
elif user_input8 == "False":
    print("Not correct. ")
else:
    print("The information you have typed is not matching up with TRUE or FALSE. ")

user_input9 = input(f"Thank you so much {user_input} for taking this interview! We are very pleased to here you are interested in {user_input1} We will reveiw this and let you know how you did. Have a great rest of your day!")
print(user_input9)