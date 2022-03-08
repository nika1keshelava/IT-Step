name = input("enter name: ")
surname = input("enter surname: ")
grade = int(input("enter your grade: "))
surname_lastN = "shvili"
pos_text = "you win, {}, {}, {}."
neg_text = "you lose, {}, {}, {}."

if name.count("i")>2:
    if surname[-6:] == surname_lastN:
        if grade>50:
            print(pos_text.format(name, surname, grade))
else:
    print(neg_text.format(name,surname,grade))
