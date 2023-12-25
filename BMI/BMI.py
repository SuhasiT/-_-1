## Oasis Infobyte python programming internship
## project2: BASIC BMI CALCULATOR....

name = input("enter your name :")

weight = int(input("enter your weight(kg) : "))

height = int(input("enter your height(m) : "))

BMI = (703 * weight) / (height * height)

print("your bmi",BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+"catagory : underweight")

    elif (BMI> 18.5 and BMI<=24.9):
        print(name+"catagory: normal weight")

    elif (BMI>25 and BMI<=29.9 ):
        print(name+"catagory: overweight")  

    elif (BMI>30 and BMI<=39.9 ):
        print(name+"catagory: severely obessed")

    elif (BMI>=40 ):
        print(name+"catagory : morbidlyobessed")   

    else:
        print(name+"please enter valid data")

else:
    print("enter valid input")
    