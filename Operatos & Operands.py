Modulo = 2 % 1

multiply = 1 * 5

integer_division = 7 // 2

float_division = 7.1 / 2.6 

add = 1 + 2


subtraction = 2 - 1


expression = 4 < 2
expression = 4 > 3
expression = 4 ==4
expression = 4 >= 7
expression = 4 <= 8
expression = 8 == 4
expression = 4 != 7

x = 10
b = 10

if x > 0 and b > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")

x = 10
b = 24
c = 0

if x or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("Atleast one number has boolean value as False")


a = 10
s = 10

if not s:
    print("Boolean value of a is True")

if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
