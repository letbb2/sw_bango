from dataclasses import dataclass
from abc import ABC

@dataclass
class Character:
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int
    gender: str
    homeworld: str
    date: str
    def to_dict(self):
        return self.__dict__


class Builder(ABC):
    """should be more generic but I don't need anything more than characters"""
    def __init__(self, character_data, planets_list) -> None:
        self.data = character_data
        self.planets = planets_list


class CharacterBuilder(Builder):
    def build(self) -> Character:
        def get_homeworld() -> str:
            homeworld_number = int(self.data['homeworld'].split('/')[5]) - 1 # that is not very efficient...
            return self.planets[homeworld_number]['name']
        def get_date() -> str:
            return self.data['edited'][0:10]
        return Character(
                name = self.data['name'],
                height = self.data['height'],
                mass = self.data['mass'],
                hair_color = self.data['hair_color'],
                skin_color = self.data['skin_color'],
                eye_color = self.data['eye_color'],
                birth_year = self.data['birth_year'],
                gender = self.data['gender'],
                homeworld = get_homeworld(),
                date = get_date(),
            )