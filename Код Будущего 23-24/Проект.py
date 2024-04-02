from random import choice
from datetime import datetime


# Перечень фильмов для просмотра
films = ['Конвой', 'Звёздные войны', 'Человек-паук',
         'Бэтмен', 'Позывной "Пассажир"']
print("Персональный помощник, Василиса")
print("Я понимаю команды:")
print("1. Какой фильм посмотреть?")
print("2. Сколько будет? (математическое выражение)")
print("3. Какое сегодня число?")
print("4. Переведи (слово для перевода на English)")
print("5. Translate (word for translate to Russian)")
print("0. Пока! (завершение работы)")
stop = False
while not stop:  # основной цикл программы
    cmd = input("Жду команду> ").lower()
    if "пока" in cmd or "0" in cmd:
        stop = True
        print('До встречи!')
    elif "фильм" in cmd or "1" in cmd:
        print(f"Давай поглядим {choice(films)}!")
    elif "сколько" in cmd or "2" in cmd:
        comm = input("Введите выражение: ")
        print(f"{comm} = {eval(comm)}")
    elif "сегодня" in cmd or "3" in cmd:
        today = datetime.now()
        print(f"Сегодня: {today.day:02}.{today.month:02}.{today.year}")
