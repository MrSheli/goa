num = int(input("enter number: "))
num1 = int(input("enter number: "))

list = []
for i in range(min(num, num1), max(num, num1)):
    list.append(i)
for u in list:
    if u % 5 == 0:
        print(u)

