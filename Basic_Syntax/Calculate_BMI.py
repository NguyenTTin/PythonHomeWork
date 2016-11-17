__auth__ = 'NguyenTTin'

weight = float(input("Please enter your weight (in the kilogram format):  "))
height = float(input("Also enter your height (in the metter format):  "))
BMI=weight/(height**2)
print("%.3f"%BMI)
if BMI < 18.5:
    print("You are Underweight")
elif BMI <25.0:
    print("You are Normal")
elif BMI <30:
    print("You are Overweight ")
elif BMI <=30:
    print("You are Obese")
else:
    print("You are extraodinary")