year =int(input("Which year do you want to check? "))

if ((year%4)%2==0 and (year%100)==0 and (year%400)==0):
    print(f"{year} is an leap year.")
else:
    print(f"{year} is not an leap year.")