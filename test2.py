height=float(input("enter your height in inches: "))
weight=float(input("enter your weight: "))
output=weight/(height*height)

if output <= 18.4:
    print("You are underweight")
elif output <= 24.9:
    print("You are healthy")
elif output <= 29.9:
    print("You are over weight")
elif output <= 34.9:
    print("You are severely over weight")
elif output <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")