name = input("your name: ")
surname = input("your surname: ")
grade = int(input("your grade: "))

gvari = "shvili"
char = "i"

my_text = "hallo, {} {} you win, your grade is {} "
my_text1 = "hallo, {} {} you lose, your grade is {}"

if surname[-6:] == gvari and name.count(char) == 2 and int(grade) >= 50:
    print(my_text.format(name, surname, grade))
else:
    print(my_text1.format(name, surname, grade))
    
    
    
