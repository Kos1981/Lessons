#1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py). В нем напишите функцию, создающую
# директории от dir_1 до dir_9 в папке, из которой запущен данный код. Затем создайте вторую функцию, удаляющую эти
# папки. Проверьте работу функций в этом же модуле.


import os


def create_folders(name,count):
   for i in range(1,count+1):
        os.mkdir(name+str(i))

def remove_folders(name,count):
    for i in range(1,count+1):
        os.rmdir(name+str(i))

if __name__=='__main__':
    create_folders('dir_',9)

    remove_folders('dir_',9)

