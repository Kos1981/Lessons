#3. Создайте программу «Медицинская анкета», где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
#Выведите результат согласно которому:
#1. Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#2. Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг,
#3. Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
#Все остальные варианты можете обработать на ваш вкус и полет фантазии.
#(Формула не соответствует реальной действительности и здесь используется только ради примера)
#    Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной ситуации.
#Пример: Вася Пупкин, 29 год, вес 90 — хорошее состояние.
#Пример: Вася Пупкин, 31 год, вес 121 — следует заняться собой.
#Пример: Вася Пупкин, 31 год, вес 49 — следует заняться собой.
#Пример: Вася Пупкин, 41 год, вес 121 — следует обратиться к врачу!
#Пример: Вася Пупкин, 41 год, вес 49 — следует обратиться к врачу!

name=input("Введит имя: ")
surename=input("Введите фамилию: ")
age=int(input("Введите возраст: "))
weight=int(input("Введите вес: "))

if age<30 and weight>50 and weight<120:
    print(name, surename,",", age, "год",",", "вес", weight, "-- хорошее состояние")
elif (age>30 and age<40) and (weight<50 or weight>120):
    print(name, surename,",", age, "год",",", "вес", weight, "-- следует заняться собой")
elif age>40 and (weight<50 or weight>120):
    print(name, surename,",", age, "год",",", "вес", weight, "-- следует обратится к врачу")
else:
    print("Невозможно дать ответ по введным данным")
