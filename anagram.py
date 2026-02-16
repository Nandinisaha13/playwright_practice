str1= "Distill"
str2= "Lisdtil"

str1=str1.lower()
str2=str2.lower()

check_letter={}

for letter in str1:
    if letter in check_letter:
        check_letter[letter]= check_letter[letter]+1
    else:
        check_letter[letter]=1

for letter in str2:
    if letter in check_letter:
        check_letter[letter]= check_letter[letter]-1
    else:
        check_letter[letter]=-1

is_anagram= True
for count in check_letter.values():
    if count != 0:
        is_anagram= False
        break

if is_anagram==True:
    print("This is an anagram")

else:
    print("This is not an anagram")

