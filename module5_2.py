#2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.



import random
def get_random_from_list(input_list):
    if len(input_list)!=0:
        return random.choice(input_list)
    #else:
     #   return None



if __name__=='__main__':
    a=[2732,2334,5456,68,4554,67567,677,0,1]
    b=[]
    print(get_random_from_list(a))
    print(get_random_from_list(b))
#print(len(a))
#print(random.choice(a))