# logical operators = evaluate multiple conditions (or, not, and)
#                     or  = at least one condition must be True
#                     and = both conditions must be true
#                     not = inverts the condition (not False, not True)

# or
temp = 20
is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is ok")

# and
if temp >= 28 and is_raining:
   print("It is hot today! 🥵")
   print("It is raining today! 🌧")
elif temp <= 0 and is_raining:
    print("it is cold outside 😱")
    print("It is raining today! 🌧")
elif  28 > temp > 0 and is_raining:
    print("it is warm outside")
    print("It is raining today!")
elif temp >= 28 and not is_raining:
    print("It is hot today! 🥵")
    print("It is not raining today! 🌧")
elif temp <= 0 and not is_raining:
    print("it is cold outside 😱")
    print("It isn't raining today! 🌧")
elif 28 > temp > 0 and not is_raining:
    print("it is warm outside")
    print("It is Sunny!")