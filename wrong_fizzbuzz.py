for i in range (1, 101):
    if i % 3 == 0:
        print('Fizz', end = '')
        if i % 5 == 0:
            print('Buzz')
        else:
            print('\n', end = '')
    elif i % 5 == 0:
        if i % 3 == 0:
            print('Fizz', end = '')
        print('Buzz')
    else:
        print(i)
