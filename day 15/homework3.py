def calulator(num1,num2,calck):
  if calck == "+":
    print(num1 + num2)
  elif calck == "-":
    print(num1 - num2)
  elif calck == "*":
    print(num1 * num2)
  elif calck == "/":
    print(num1 / num2)
  else:
    print("there is no operator like this")

num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))
operator = input("enter operator: ")

calulator(num1,num2,operator)
