# In this project we're going to use OOP to make a project related to dogs management
from collections import namedtuple

class Dog:
    def __init__(self, name, race):
        self.name = name
        self.__race = race

    def get_name_race(self):
        return self.name, self.__race
    def bark(self):
        return print('HUL-HUL')

    def change_race(self, new_race):
        self.race = new_race

    def change_number(self, new_number):
        self.number = new_number

    def print_dog(self):
        print(f'Race: {self.race}')
        print(f'Size: {self.number}')


def name_to_object(index, object):
        lst = [f'cachorro{index}']
        lst[0] = object



list_name_dog = ["black", "ted", "bruno", "julie", "mel", "big", "angel", "escobar", "liny"]
list_dog = ["Pitbull", "vira-lata", "caramelo", "pinthcer", "borde", "corgi", "dlabrador", "husky", "pastor"]
list_number = [33, 22, 44, 66, 77, 87, 32, 75, 12]
list_specs_dog = [{'nome': 'rex', 'raca':'pitbull', id:0}]
dct = {}

for count, values in enumerate(list_dog):
    nome = f'Cachorro{count}'
    dct_loop = {nome:Dog(list_name_dog[count], list_dog[count])}
    dct.update(dct_loop)


lst = []1
for count, values in enumerate(list_objects_dog):
    lst.append(f'cachorro{count + 1}')

print(lst)

dct = {}
for count, values in enumerate(lst):
    dct_for = {values: list_objects_dog[count]}
    dct.update(dct_for)
print(dct)





for count, values in dct.items():
    print(values.get_name())







