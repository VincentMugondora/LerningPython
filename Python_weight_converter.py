# Python weight convertor

weight = float(input("Enter your weight: "))
units = input("Enter your units {kgs or lbs}: ")

if units == "kgs":
    weight = weight * 2.205
    units = "lbs"
    print(f"Your weight is {round(weight, 1)} {units}")
elif units == "lbs":
    weight = weight / 2.205
    units = "kgs"
    print(f"Your weight is {round(weight, 1)} {units}")
else:
    print(f"{units} is invalid")

