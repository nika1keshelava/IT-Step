name = "Giorgi"
surname = "Tsertsvadze"
grade = 20
my_text1 = "you win {}, {} and {}"
my_text2 = " you lose {}, {} and {}"

name = input("enter your name: ")
surname = input("ener your surname: ")
grade = int(input("enter your grade: "))

print(name.count("i"))
print(surname[7:11])
 
if grade > 50:
    print(my_text1.format(name, surname, grade))
else:
    print(my_text2.format(name, surname, grade))

 