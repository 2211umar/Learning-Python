import random
with open(r'C:\Users\ismai\OneDrive\Desktop\Learning Python\basic games\hangman.txt') as file:
    data = file.readlines()
words = []
for d in data:
    words.append(d.strip())

myword = random.choice(words)
guess = len(myword) * [" _ "]

chances = 10
while chances >0:
    print(guess)
    char = input(f'please enter your character {chances} left: ')
    # please check if characer is in myword
    for i,c in enumerate(myword):
        if c==char:
            guess[i] = c



    chances = chances -1 
print(myword)