######## breaking ###############
# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if i >= 5:
#     print("Breaking")
#     break
# print("Finished")
############ my example for break ############
# i = 10
# while True:
#   print (i)
#   i -= 1
#   if i < 0:
#     print("finished")
#     break
########## breaks and continue problem
total = 0
while True:
    p1 = int(input("enter your age: "))
    p2 = int(input("enter your age: "))
    p3 = int(input("enter your age: "))
    p4 = int(input("enter your age: "))
    p5 = int(input("enter your age: "))
    total += 100
    if p1 < 3 or p2 < 3 or p3 < 3 or p4 < 3 or p5 < 3:
        continue
    if total > 500:
        break
    print(total)
