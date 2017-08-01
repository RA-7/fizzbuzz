for i in range (1, 101):
    if i % 3 == 0:
        # End '' replaces the newline character
        # that is normally at the end of every print
        # so that Buzz can be added to the end of Fizz
        print('Fizz', end = '')
        if i % 5 == 0:
            print('Buzz')
        # Add a newline at the end of Fizz if there is no Buzz
        else:
            print()
    elif i % 5 == 0:
        if i % 3 == 0:
            print('Fizz', end = '')
        print('Buzz')
    else:
        print(i)
