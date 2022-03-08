name = "tornike"
surname = "tbelishvili"
grade = int("70")
if name.count("i") > 2:
    if surname [-6: ] == "shvili":
        if grade > 50:
            print("you win")
else:
    print("you lose")

text = "hello {} your surname is {}, your surname is {} and you lose."
print(text.format(name, surname, grade))