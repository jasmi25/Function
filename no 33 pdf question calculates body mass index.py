##Q33. Write function bmi that calculates body mass index (bmi = weight / height2).
##if bmi > 30 return "Obese"
##if bmi <= 18.5 return "Underweight"
##if bmi <= 25.0 return "Normal"
##if bmi <= 30.0 return "Overweight"
def body_mass(w,h):
    bim=w/h
    if bim>30:
         return "Obese"
    if bim<=18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
a=int(input("enter number bmi weight:-"))
b=int(input("enter number bmi height2:-"))
print(body_mass(a,b))

