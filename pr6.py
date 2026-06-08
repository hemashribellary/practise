wt = float(input("Enter the weight in kilograms: "))
ht = float(input("Enter the height in meters: "))
bmi = wt / (ht ** 2)
if bmi < 18.5:
    print("Your BMI is",bmi,". You are underweight.")
    print('please type "underweight" to get some diet recommendations')
    if input() == 'underweight':
        print('Here are some diet recommendations for you: \n1. Eat more calories than you burn \n2. Include nutrient-rich foods in your diet \n3. Eat more frequently \n4. Include healthy fats in your diet')
elif 18.5 <= bmi < 25:
    print("Your BMI is",bmi,". You have a normal weight.")
elif 25 <= bmi < 30:
    print("Your BMI is",bmi,". You are overweight.")
    print('please type "overweight" to get some diet recommendations')
    if input() == 'overweight':
        print('Here are some diet recommendations for you: \n1. Eat a balanced diet with plenty of fruits and vegetables \n2. Limit your intake of processed foods and sugary drinks \n3. Control portion sizes \n4. Include regular physical activity in your routine')
else:
    print("Your BMI is",bmi,". You are obese.")
    print('please type "obese" to get some diet recommendations')
    if input() == 'obese':
        print('Here are some diet recommendations for you: \n1. Consult a healthcare professional for personalized advice \n2. Follow a structured weight loss plan \n3. Focus on whole, nutrient-dense foods \n4. Incorporate regular physical activity into your routine')