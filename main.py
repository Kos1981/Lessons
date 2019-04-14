#. 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
#Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.



from module5_1 import create_folders, remove_folders
from module5_2 import get_random_from_list

a = [2732, 2334, 5456, 68, 4554, 67567, 677, 0, 1]
create_folders('dir_', 9)
remove_folders('dir_', 9)
print(get_random_from_list(a))