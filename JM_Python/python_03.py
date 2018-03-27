# 控制流
# if语句
number = 23
guess = int(input('Enter an integer:'))
if guess == number:
    print('Congratulations ,you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('Done')

# while语句
running = True
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over')
print('Done')

# for循环
for i in range(1,5):
    print(i)
else:print('The for loop is over')

# break语句
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('Length of the string is',len(s))
else:
    print('The while loop is over')
print('Done')

# continue语句
while True:
    s = input('Enter anything:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too samll')
        continue
    print('Input is of sufficient length')