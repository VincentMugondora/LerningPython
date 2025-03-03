class JustNotCoolError(Exception):
    pass

x=2
try:
    raise JustNotCoolError('This is just not cool')
    # raise Exception("l am a custom exception")
    # print(x / 1)
    # if not type(x) is str:
        # raise TypeError('Only strings are allowed')
except NameError:
    print('Name error means something is probably undefined')
except ZeroDivisionError:
    print("Please don't devide by zero")
except Exception as e:
    print(f'An error occured: {e}')
else:
    print('All good!')
finally:
    print('This code block will always run with or without an error')