#შექმენით ფუნქცია რომელსაც გადაეცემა
#არგუმენტად სია
#და დააბრუნებს სიას ოღონდ თითოეული ელემენტი იქნება აკვადრატებული


def my_func(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
        

    return arr

print(my_func([10, 20, 30, 40]))