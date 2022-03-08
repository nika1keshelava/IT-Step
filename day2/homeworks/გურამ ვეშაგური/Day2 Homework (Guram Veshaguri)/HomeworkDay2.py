Name = input("Enter your name: ")
Surname = input("Enter your surname: ")
Grade = int(input("Enter your grade: "))
Check = "shvili"
GradeCheck = 50
Final_Text_Win = "Congratulations, {} you have won, becouse your surname is {} and your grade is {}"
Final_Text_Lose = "We are Sorry, {} you have lost, becouse your surname is {} and your grade is {}"



if ((Name.count("i") >= 2) and (Surname[-6:] == Check) and (Grade >= GradeCheck)):
    print(Final_Text_Win.format(Name, Surname, Grade))
else:
    print(Final_Text_Lose.format(Name, Surname, Grade))
    
   