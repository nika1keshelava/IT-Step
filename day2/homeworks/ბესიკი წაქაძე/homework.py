name = input("enter your name: ")
surname = input("enter your surname: ")
grade = int(input("enter your grade: "))
x = int(name.count("i"))
y = str(surname[-6:])
if(grade > 50 and x > 1 and y == "shvili" ):

   print("თქვენ მოიგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} ".format(name, surname, grade))
else:
    print("თქვენ წააგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} ".format(name, surname, grade))

# text1 = "თქვენ მოიგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} "  
# text2 = "თქვენ წააგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} "
# print(text1.format(name, surname, grade))
# else:
#     print(text1.format(name, surname, grade))
# ასე მინდოდა ცამეწერა მარა ვერ ვქენი,ალბატ იერარქიაში ვუშვებ შეცდომას
