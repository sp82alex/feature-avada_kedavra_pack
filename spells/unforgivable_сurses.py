#Крок 7
#В модулі unforgivable_сurses створіть функцію avada_kedavra. Ця функція має видаляти всі дерикторії в кожному з фільмів котрі не містять в собі нагород. Наприклад пуста дерикторія літери Z.

import os
import shutil
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature/avada_kedavra_pack/Harry Potter/")

def func_del_empty():
    for i in os.listdir():
      os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature/avada_kedavra_pack/Harry Potter/"+str(i))
      for q in os.listdir():
        os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature/avada_kedavra_pack/Harry Potter/"+str(i)+"/"+str(q))
        if len(os.listdir()) == 0: # Check if the folder is empty
            shutil.rmtree("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/feature/avada_kedavra_pack/Harry Potter/"+str(i)+"/"+str(q))
func_del_empty()

# Крок 8
#В модулі unforgivable_сurses створіть функцію imperius. Функція відкриває файл json в якому було збережено словник films_awards та зміню type кожної нагороди на "Winner"

import os
import json
from pprint import pprint
os.chdir("/Users/aleksej.nepokulchitskij/PycharmProjects/pythonProject1/")

def imperius():
    with open('films_awards_json.json', 'rt') as f:
        data = json.load(f)
    for i in range(len(data[0]['results'])):
        if data[0]['results'][i]['type'] == "Nominee":
            data[0]['results'][i]['type'] = "Winner"
    pprint(data[0]['results'])
imperius()
