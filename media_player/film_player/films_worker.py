class Film():
    def __init__(self, name, rating, year, directed, starring):
        self.name = name
        self.rating = rating
        self.year = year
        self.directed = directed
        self.starring = starring
        self.storage_address = 'путь к файлу'
    def film_info(self):
        info = ("Film name is: " + self.name + ". Current rating is: " + self.rating + ". Directed on: " + self.directed + " in " + str(self.year) + ". Starring: " + self.starring).title()
        print(info)
    def upload_file(self):
        import os
        import string

        for c in string.ascii_uppercase:
            os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/media_player/film_player/film_storage")
            if c == self.name[0]:
                os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/media_player/film_player/film_storage/"+str(c))
                file = open(self.name+'.txt','w')

    def get_film_address(self):
        import os
        #сначала получаем во внутреннею переменную метода абсолютный путь к тестовому файлу
        address = os.path.abspath(self.name+'.txt')
        #затем сохраняем путь в атрибут storage_address и распечатываем
        self.storage_address = address
        print(self.storage_address)


my_favorite_film = Film("Fight_Club", "8.8 / 10", 1999, "David Fincher", "Brad Pitt, Edward Norton, and Helena Bonham Carter")

#выводим общую инфо о фильме
my_favorite_film.film_info()

#создаем тейстовый файл с названием фильма по условиям задания
my_favorite_film.upload_file()

#вызываем метод get_film_address который сохраняет путь в атрибут storage_address
my_favorite_film.get_film_address()


