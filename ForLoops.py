string_name ="paradigm"

for element in range(0, len(string_name)):
    print(string_name[element])

for i in range(0, 5):
    print(i)



AnimalList = ['Cat','Dog','Tiger','Cow']

for item in AnimalList:
    print(item)

flowers = ['Jasmine', 'Lotus', 'Rose', 'Sunflower']

for item in flowers:
    print(item)

    list1 = [5, 10, 15, 20]
    list2 = ['Tomatoes', 'potatoes', 'Carrots', 'Cucumbers']

for i in list1:
    for j in list2:
        print(i,j)


vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        break
    print(v)

vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        continue
    print(v)


numbers = [12,3,56,67,89,90]
count = 0

for n in numbers:
    count +=1
print(count)

numbers = [12,3,56,67,89,90]
sum = 0

for n in numbers:
    sum += n
print(sum)

numbers = [2,5,6,10,15,20,25]

for n in numbers:
    if n%5 == 0:
        print(n)


list1 = ['Mango','Banana','Orange']
list2 = []
for i in list1:
    list2.append(i)

print(list2)


numbers = [1,4,50,80,12]
max = 0

for n in numbers:
    if(n>max):
        max = n
        
print(max)

numbers = [1,4,50,80,12]
min = 1000

for n in numbers:
    if(n<min):
        min = n
print(min)


numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp
print(numbers)

numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        for j in range(i+1, len(numbers)):
            if(numbers[i] < numbers[j]):
                temp = numbers[i]
                numbers[i] = numbers[j];
                numbers[j] = temp
print(numbers)


for i in range(3, 20, 3):
    print(i)

for i in range(5, 20, 5):
    print(i)

for i in range(10, 0, -1):

    print(i)