#თუ სახელში ორჯერ მეტჯერ აქვს ასო ი
# და გვარი მთავრდება შვილიზე
#და ქულა მეტია 50-ზე
#დაპრინტოს დაფორმატებული ტექსტით name, surname, grade 
#else (you lose, დაფორმატებული ტექსტი name, surname, grade)


name = input("enter your name: ")
surname = input("Enter your surname: ")
grade = int(input("enter your grade: "))
win_text = "{} {}, you win! your grade is: {}"
lose_text = "{} {}, you lose! your grade is {}"


if name.count("i") > 1 and surname[len(surname)-6:] == "shvili" and grade > 50:
    print(win_text.format(name, surname, grade))
else:
    print(lose_text.format(name, surname, grade))

