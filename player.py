class Player:
    def __init__(self, nickname):
        self.__score = 0
        self.__nickname = nickname

    @property
    def nickname(self):
        return self.__nickname

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
