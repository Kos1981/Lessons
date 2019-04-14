#2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


#def get_max(num1,num2,num3):
 #   return max(num1,num2,num3)

def get_max(num1,num2,num3):
    if num1>=num2:
        if num1>=num3:
            return num1
        else:
            return num3
    else:
        if num2>=num3:
            return num2
        else:
            return num3




print(get_max(1001,1000,888))



