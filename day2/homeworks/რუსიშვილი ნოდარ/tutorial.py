name = input("name? ")
surname = input("surname? ")
grade = int(input("grade? "))

print(name.count("i"))
print(surname.endswith("shvili"))

if int(grade) > 50:
 print("you win ", name , surname, grade)
else:
    print("you lose", name, surname, grade)
 