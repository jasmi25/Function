#Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"
#if bmi > 30 return "Obese"
def bim(w,h):
    a=w/h
    if a<=18.5:
        return "Underweight"
    elif a<=25.0:
        return "Normal"
    elif a<=30.0:
        return "Overweight"
    elif a>30:
        return "Obese"
x=int(input("enter weight"))
y=int(input("enter height2"))
print(bim(x,y))
    
