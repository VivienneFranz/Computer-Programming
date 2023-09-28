
salary =int(input("What is your salary? "))

years =int(input("What is your years of service? "))

if years >=5:
    print(f"Your bonus will be {salary * 0.05}")
else:
    print("You do not qualify for a bonus.")



d=int(input("enter the length of the figure"))

e=int(input("enter the breadth of the figure"))

if d==e:
    print("the figure is a square")
else:
    print("the firgure is not a sqaure")

a=int(input("Enter a value for a "))

b=int(input("Enter value for b "))
if a >= b:
    print(" a is greater than b")
else:
    print("b is greater than a")



person1=int(input("Enter age for person1 "))

person2=int(input("Enter age for person2 "))

person3=int(input("Enter age for person3 "))

if person1 > person2 and person1 > person3:
    print("Person one in the oldest. ")
elif person2 > person1 and person2 > person3:
    print:("Person two is the oldest. ")
else:
    print("Person 3 is the oldest. ")
if person1<person2 and person1<person3:
    print("Person one is the youngest. ")
elif person2<person1 and person2<person3:
    print("Person two is the youngest. ")
else:
    print("Person three is the youngest. ")



total_classes = int(input("How many classes are held? "))
attended_classes = int(input("How many classes are attened? "))
percentage_attendence = int((attended_classes/total_classes)*100)
if percentage_attendence < 75:
    print("You are free to be in the exam")
else:
    print("You can not be in the exam")


