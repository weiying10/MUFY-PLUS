import random
name = input('What is your name?\n')
adjectives=['Happy','Sleepy','Brave','Fluffy','Playful','Hungry']
animals=['Cat','Dog','Panda','Lion','Pig','Tiger']
print(f'{name}, your codename is: {random.choice(adjectives)} {random.choice(animals)}')

print(f'Your lucky number is: {random.randrange(1,99)}')