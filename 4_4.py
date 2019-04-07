#4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#1. Наносит урон. Это улучшенная версия функции из задачи 3.
#2. Вычисляет урон по отношению к броне.




enemy = {
    'health': 100,
    'damage': 50,
    'armour': 1.2
}

player = {
    'health': 100,
    'damage': 70,
    'armour': 1.4
}

def attack(person1,person2):
    def get_damage(armor,damage):
        return damage/armor

    person1['health'] = person1['health'] - get_damage(person1['armour'],person2['damage'])
    return person1

enemy['name']=input("Введите имя врага: ")
player['name']=input("Введите имя игрока: ")


print(attack(enemy,player))
