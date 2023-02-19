print("Welcome to the tip calculator.")
bill_amt=input("What was the total bill? ")
tip_per=input("What percentage tip would you like to give? 10, 12, or 15 ? ")
split_no=input("How many people to split the bill? ")

bill_amt_float=float(bill_amt)
tip_per_int=int(tip_per)
split_no_int=int(split_no)

cal_tip_amt=(bill_amt_float/100)*tip_per_int
total_bill=bill_amt_float+cal_tip_amt
#split_bill=round(total_bill/split_no_int,2)
split_bill="{:.2f}".format(total_bill/split_no_int)
print(f"Each person should pay: {split_bill}")