# Если игрок угадает число, то его рейтинг увеличивается на N очков. Далее спросить каждого игрока, хочет ли он продолжить играть. Если кто-то не хочет, то завершить игру.

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
        while True:  # отгадывание числа
            for p in players:
                print(f"Игрок {p.nickname} в игре. Ваша очередь!")
                user_number = int(input("Введите ваше число: "))
                if bot_number > user_number:
                    print("Ваше число меньше")
                elif user_number > bot_number:
                    print("Ваше число больше")
                else:
                    print("Отгадано правильно! Спасибо за игру!")
                    wanna_play = True if input(
                        "Вы хотите играть дальше? (Да/нет)?").lower() == "да" else False
                    break
