num =190029
if num<=1:
    print("Not a prime number")
else:
    is_prime= True

for i in range(2, int(num ** 0.5) + 1):
    if num %i ==0:
        print(f"failed {num} is divisible by {i}")
        is_prime= False
        break
    
if(is_prime== True):
    print("Prime number")
else:
    print("Not a prime number")