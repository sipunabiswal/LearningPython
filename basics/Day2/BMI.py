weight=input("Enter the weight ")
height=input("Enter the height ")
weight_int=int(weight)
height_float=float(height)

#bmi=weight_int/height_float**2
bmi=weight_int/(height_float*height_float)
#round function syntax(value to round, rounding place) ex round(35.33333,2)=35.34
bmi_round=round(bmi,2)
#f-string
print(f"Entered weight is  {weight_int} and height is {height_float} and calculated bmi is {bmi_round}")