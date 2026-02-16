Name= "Nandini Saha"

# char_list= list(Name)
 
# i=0
# j=len(Name)-1


# while i <j:
#     temp= char_list[i]
#     char_list[i]= char_list[j]
#     char_list[j]= temp

#     i+=1
#     j-=1

# reversed_name= "".join(char_list)
# print(reversed_name)

#second method where putting a reverse_name as a string 

reversed_name=""
for char in Name:
    reversed_name= char+reversed_name

print(reversed_name)
