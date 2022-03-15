def divide(arr):

    my_sum = 0

    for element in  arr:

        my_sum += element

   

    return my_sum/len(arr)



arr = []

ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))

for i in range(ammount_of_numbers):

    num = int(input("enter num" + str(i+1) + ":"))

    arr.append(num)

   

print(divide(arr))