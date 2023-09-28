# Реализовать функцию выбора сложности. Вот шаблон:
# "Выбери уровень сложности.\n\n" +
# "1.Легкий (диапазон от 1 до 50)\n" +
# "2.Средний (диапазон от 1 до 100)\n" +
# "3.Сложный (диапазон от 1 до 1000)\n" +
# "4.Свой диапазон\n"
# "Ответ: "
# Функция должна вернуть кортеж из двух чисел: минимальное число и максимальное число диапазона. Вызвать функцию перед загадыванием числа и загадать число из заданного диапазона.
from player import Player
import random


def registor():  # функция регистрации
    players = []  # список игроков
    amount = int(input("Сколько игроков будут играть: "))  # количество игроков
    for i in range(amount):
        name = input("Введите ваше имя: ")  # имя игрока
        player = Player(name)  # экземпляр класса
        players.append(player)  # экз в списке
        print()  # заполнение списка
    return players  # возвращает  список


if __name__ == "__main__":
    players: list[Player] = registor()  # экземпляр хранящий список игроков
    wanna_play = True
    while wanna_play:  # число бота
        bot_number = random.randrange(1, 100)
        print("Бот задал число")
        while True:  # цикл отгадывание числа
            for p in players:  # перебор игроков
                print(f"Игрок {p.nickname} в игре. Ваша очередь!")
                user_number = int(input("Введите ваше число: "))
                if bot_number > user_number:
                    print("Ваше число меньше")
                elif user_number > bot_number:
                    print("Ваше число больше")
                else:
                    print(
                        f"Отгадано правильно! Это число {bot_number}!")
                    print("Вам начисляется 3 очка")
                    p.score += 3  # добавление очков
                    for p in players:  # цикл о продолжении игры
                        wanna_play = input(
                            f"{p.nickname} вы хотите играть дальше? (Да/Нет)").lower()
                        if wanna_play != "да":
                            wanna_play = False
                            break
            if not wanna_play:  # заканчивает игру если игрок не желает играть дальше
                break
