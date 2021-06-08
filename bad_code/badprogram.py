secret_number = 20

while True:
    number = input('Guess the number: ')

    try:
        number = int(number)
    except:
        print('Sorry that is not a number')
        continue

    if number != secret_number:
        if number > secret_number:
            print(number, 'is greater than the secret number')

        elif number < secret_number:
            print(number, 'is less than the secret number')
    else:
        print('You guessed the number:', secret_number)
        break