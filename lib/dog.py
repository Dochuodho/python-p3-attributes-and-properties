#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Retrieving name")
        return self._name
    
    def set_name(self, name):
        if(type(name) in (str)) and (1 <= len(name) <= 24):
            print(f"Setting name {name}")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
fido = Dog("Fido")
fido.name = "Fido"



    
pass
