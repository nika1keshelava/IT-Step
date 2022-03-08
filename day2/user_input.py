# name = input("enter your name: ") 
# surname = input("enter your surname: ")

# print(name, surname)

#შემოვა ორი რიცხვი input-ით
#ეს ორი რიცხვი უნდა შეიკრიბოს
#და დაიპრინტოს მათი ჯამი

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# print(num1 + num2)


#იუზერს შემოატანინეთ სამი ცვლადის მნიშვნელობა
#1)age
#2)name
#3)surname

#format მეთოდით, დამიგენერირეთ ლამაზი ტექსტი
#hello, სახელი, your surname is გვარი, and your age is ასაკი

age = input("ასაკი: ")
name = input("სახელი: ")
surname = input("გვარი: ")

text = "Hello, {} your surname is {}, and your age is {}"

print(text.format(name, surname, age))