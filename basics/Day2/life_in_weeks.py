age=input("What is your age? ")
maxage=90
age_as_in=int(age)
remaining_life =maxage-age_as_in
rema_days=remaining_life * 365
rem_weeks=remaining_life * 52
rem_month=remaining_life * 12
message=f"You have {rema_days} days, {rem_weeks} weeks and {rem_month} months left."
print(message)