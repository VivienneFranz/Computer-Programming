how_deep = int(input("How many Fibonacci numbers do you want to generate? "))
n1, n2 = 1, 0
count = 0

if how_deep == 1:
    print("Fibonacci sequence upto",how_deep,":")
    print(n1)
elif how_deep <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    while count < how_deep:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count += 1
