num =7
if num<=1:
    print("Not a prime number")
else:
    is_prime= True

for i in range(2,num):
    if num %i ==0:
        print(f"failed {num} is divisible by {i}")
        is_prime= False
        break
    
if(is_prime== True):
    print("Prime number")
else:
    print("Not a prime number")