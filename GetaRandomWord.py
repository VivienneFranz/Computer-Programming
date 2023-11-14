import random

with open('sowpods.txt', 'r') as f:
  line = f.read()
  text = list(map(str, line.split()))
  print(random.choice(text))

    # do something to the line, for example
    # saving it to disk
