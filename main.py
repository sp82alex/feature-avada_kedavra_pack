#Крок 1
import os

#Крок 2
#Створіть гілку feature/avada_kedavra_pack у своєму локальному проекті(на вашому ПК).
#Перключіться на цю гілку.

os.mkdir("feature")
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature")
os.mkdir("avada_kedavra_pack")
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature/avada_kedavra_pack")

#Крок 3

os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/")
#file = open('script_homework_prew.py','w')
#в файл script_homework_prew.py сохранили весь код с предыдущего ДЗ с поправками, что бы отработал в пайчарм
#на следующем шаге при импорте запускаем его и воссоздаем прошлое ДЗ уже в пайчарм - сработало

#Крок 4
#Словник films_awards збережіть у json файл використавши модуль json.

from script_homework_prew import films_awards
import json
from pprint import pprint

films_awards_json = json.dumps(films_awards)
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/")
json_file = open('films_awards_json.json', 'w')
json_file.write(films_awards_json)

#Крок 5-6
#В своєму проекті створіт пайтон пакет з назвою spells
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/spells/")
#В середині spells створіть модуль unforgivable_сurses.
#new_file = open('unforgivable_сurses.py', 'w')

#Крок 7
#Крок 8
#Виконуємо у модулі unforgivable_сurses.py
