def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("BMI = " + str(round(bmi, 2)))

    if bmi < 18.5:
        print("Weight Classification: Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    else:
        print("Weight Classification: Over Weight")

    return bmi

# Test the function
calculate_bmi(weight=60, height=1.80)