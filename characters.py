from random import randint
from dataclasses import dataclass

from things import create_few_packs_of_items


DEFAULT_ATTACK = 100
DEFAULT_DEFENCE = 0
DEFAULT_HEALTH = 100
MIN_ATTACK = 30
PACKS_OF_ITEMS_QUANTITY = 50

NAMES = [
    'Геральт',
    'Йеннифер',
    'Трисс',
    'Цири',
    'Лютик',
    'Вильгот',
    'Эмиль Регис Роггевизен',
    'Зольтан Хиви',
    'Ярпен Зигрин',
    'Весемир',
    'Фольтест',
    'Эйст Тишина',
    'Эмиля Региссон',
    'Милва',
    'Ангуулема',
    'Венсеремарайме',
    'Райнфарн',
    'Ламберт',
    'Эскал',
    'Фрингильа Виго',
]


@dataclass
class BaseCharacter:
    """Базовый класс персонажа."""
    name: str
    start_attack: float = DEFAULT_ATTACK
    start_defence: float = DEFAULT_DEFENCE
    start_hp: float = DEFAULT_HEALTH
    equipment: [str] = None

    def attack(self):
        return randint(MIN_ATTACK, self.start_attack)

    def defence(self):
        return self.start_defence

    def health(self):
        return self.start_hp

    def taken_damage(self, attack_damage):
        after_armor = self.start_defence - attack_damage
        if after_armor <= 0:
            self.start_defence = 0
            self.start_hp = self.start_hp + after_armor
        else:
            self.start_defence = after_armor
        return after_armor

    def set_things(
            self,
            extra_attack,
            extra_def,
            extra_hp,
            equipment,
    ):
        self.start_attack = (
            extra_attack
            + self.attack() * self.ATTACK_MULTIPLIER
        )
        self.start_defence = (
            extra_def
            + self.defence() * self.DEFENCE_MULTIPLIER
        )
        self.start_hp = (
            extra_hp
            + self.health() * self.HP_MULTIPLIER
        )
        self.equipment = equipment


class Warrior(BaseCharacter):
    ATTACK_MULTIPLIER = 2
    DEFENCE_MULTIPLIER = 1
    HP_MULTIPLIER = 1


class Palladin(BaseCharacter):
    ATTACK_MULTIPLIER = 1
    DEFENCE_MULTIPLIER = 2
    HP_MULTIPLIER = 2


def characters(warriors_quantity):
    warriors = []
    for name in list(set(NAMES))[:warriors_quantity]:
        warriors.append([Warrior(name), Palladin(name)][randint(0, 1)])
    return warriors


def complete_character(characters):
    for character in characters:
        pack = create_few_packs_of_items(
            PACKS_OF_ITEMS_QUANTITY
        )[randint(1, PACKS_OF_ITEMS_QUANTITY - 1)]
        character.set_things(*pack)
    return character


# print(complete_character(characters(1)))
