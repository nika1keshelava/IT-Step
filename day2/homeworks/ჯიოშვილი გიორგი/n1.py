# user-s vekitxebit:
# name
# surname
# grade

# vamowmebt tu saxelshi orze metjer aqvs aso "i" 
# da
# gvari mtavrdeba "shvili"-ze
# da 
# qula metia 50-ze
# daprintos(you win,  daformatebuli teqstit name, surname, grade)

# else
# (you lose, daformatebuli teqstit name, surname, grade)


name = 'giorgi'
surname = 'jioshvili'
grade = 20


if name.count('i') > 2:
    if surname[-6 : ] == "shvili":
        if grade > 50:
            print('you win')
else: 
    print('you lose')


