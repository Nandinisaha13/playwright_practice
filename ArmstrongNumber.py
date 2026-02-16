number =1634

power= len(str(number))

sum=0

temp=number #otherwise at the end no number to compare

while number>0:
    digit= number % 10
    sum= sum + (digit**power)

    number = number //10

if sum == temp:
    print(f"Armstrong number is {temp}")
else:
    print("Not an armstrong number")
