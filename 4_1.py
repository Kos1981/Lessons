#1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку
#вида «Василий, 21 год(а), проживает в городе Москва»


def get_info(name,age,city):

    return (name + ', ' + str(age) + ' год, '+ city)

result=get_info('Вася',21,'Москва')
print(result)
