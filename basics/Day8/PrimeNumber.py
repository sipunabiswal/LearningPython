def prime_checker(number):
    isPrime=False
    if number==1:
        print(f"It's not a prime number.")
    else:
        for num in range(2,number):
            if(number % num==0):
                isPrime=True
                break
        
        if isPrime:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")

n= int(input("Check this number: "))
prime_checker(number=n)