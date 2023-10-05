user_1 = int(input("How many Fibonacci numbers do you want to generate? "))
n1, n2 = 0, 1
count = 0

if user_1 == 1:
    print("Fibonacci sequence upto",user_1,":")
    print(n1)
elif user_1 <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    while count < user_1:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count += 1
