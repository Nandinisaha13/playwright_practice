number = 17897

total_sum=0

while number > 0:
    digit= number % 10 #always make it easier with the divisble by 10
    total_sum= total_sum + digit

    number = number // 10

print(total_sum)