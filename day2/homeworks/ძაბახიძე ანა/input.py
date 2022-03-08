name = input("enter your name:")
surname = input("enter your surname:")
grade = int(input("enter your grade:"))


print("i"==2 in surname)
print("shvili" in surname)

text1 = "congratulations, {} {}, you win"
text2 = "sorry, {} {}, you lose"


if grade>50 :
    print(text1.format(name, surname))
if grade<50 :
    print(text2.format(name, surname))


#or 
# else:
#     print(text2.format(name, surname))


