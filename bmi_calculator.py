# Building BMI Calculator (Meteric system)

def bmi():


    while True:
        user_height = input("""
        What is our height in Meters? 
        :  """)
        user_weight = input("""
        What is our weight in kgs? 
        :  """)
        try:
            height = float(user_height)
            weight = float(user_weight)
            bmi = round((weight/(height ** 2)),2)
            print("""
        --------------------------------------""")
            print(f"""
        Your body mass index is : {bmi} kg/m^2""")
            print("""
        --------------------------------------""")
            break
        except:
            print("You should input numeric data")
            print("Try Again")
            continue
    if bmi > 0:
        if bmi > 40:
            print("""
            Morbidly obese """)
        elif 35 <= bmi < 40:
            print("""
            Severly obese """)
        elif 30 <= bmi < 35:
            print("""
            Obese-weight """)
        elif 25 <= bmi < 30:
            print("""
            Over-weight """) 
        elif 18.5 <= bmi < 25:
            print("""
            Normal-weight""")
        else:
            print("""
            Under-weight""")
        print("\n")
    return 0
    

bmi()

    