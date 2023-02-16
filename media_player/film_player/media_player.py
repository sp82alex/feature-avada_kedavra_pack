class Player():
    def __init__(self, name, create, content, rank):
        self.name = name
        self.create = create
        self.content = content
        self.rank = rank
        self.country = 'United States'
    def player_info(self):
        info = ("Service name is: " + self.name + ". Current rating is: " + str(self.rank) + ". Created on: " + self.country + " in " + str(self.create) + ". Type content is: " + self.content).title()
        print(info)
    def up_rank(self):
        if self.rank == 1:
            print("У сервиса 1 место, повышение невозможно")
        else:
            self.rank -= 1
            print("Место сервиса в рейтинге повышено на 1 позицию")
    def play(self):
        print("Player " + self.name + " is running")

my_player_1 = Player("youtube", 2005, "Free", 3)
my_player_2 = Player("netflix", 1997, "Not Free", 1)

#1 метод - выводим всю информацию о сервисах
my_player_1.player_info()
my_player_2.player_info()

#2 метод - повышаем позицию сервиса в рейтинге, если уже 1 место, как у нетфликс, но обьявляем об этом
my_player_1.up_rank()
my_player_1.player_info()
my_player_2.up_rank()
my_player_2.player_info()

#3 метод - запускам оба плейера
my_player_1.play()
my_player_2.play()