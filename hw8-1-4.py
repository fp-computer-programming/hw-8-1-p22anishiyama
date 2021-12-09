# Author: ATN 12/9/21

def calc_bmi(height, weight):
    '''Calculates the bmi for a given height in centimeters and weight in kilograms.'''
    bmi = (weight / height / height) * 10000
    if (bmi < 19):
        return("You are underweight.")
    elif (bmi < 25):
        return("You are healthy.")
    elif (bmi < 30):
        return("You are overweight.")
    elif (bmi < 40):
        return("You are obese.")
    elif (bmi > 40):
        return("You are extremely obese.")

print(calc_bmi(23, 2) == "You are obese.")
print(calc_bmi(76, 8) == "You are underweight.")
print(calc_bmi(12, 158) == "You are extremely obese.")
