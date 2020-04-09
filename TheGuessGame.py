import random
while True:
    no1 = random.randint(0, 10)
    no2 = int(input('Enter a number 1-10: '))

    if no1 == no2:
        print('You won!!!')
    else:
        print('Better luck next time...')
    
    if input('Do you want to continue?y/n: ') == 'y':
        continue
    else:
        break