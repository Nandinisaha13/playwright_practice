count=19
a= 0
b= 1

print(f"Start: {a}, {b}", end=',')

for i in range(2,count):
    next_sum=a+b

    print(next_sum, end=",")

    a=b
    b=next_sum
print("done")


