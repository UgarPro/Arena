from random import randint, sample
from dataclasses import dataclass


@dataclass
class Thing:
    num: int
    name: str
    start_attack: float
    start_defence: float
    start_hp: float

    @property
    def name_num(self):
        return "_".join([self.name, str(self.num)])

    @property
    def attack(self):
        return randint(*self.start_attack)

    @property
    def defence(self):
        return randint(*self.start_defence)

    @property
    def health(self):
        return randint(*self.start_hp)


NUMBER_OF_VARIETY_OF_ITEMS = 10
SAMPLE_CONST = 1

PACKAGES = [
    ('MagicRing', ['магическое кольцо', (3, 5), (5, 10), (0, 0)]),
    ('Sword', ['меч', (5, 10), (0, 0), (0, 0)]),
    ('Shield', ['щит', (0, 0), (2, 8), (0, 0)]),
    ('Bow', ['лук', (2, 5), (0, 0), (0, 0)]),
    ('Herbs', ['магическое зелье', (0, 0), (0, 0), (1, 5)]),
]


def create_subclass_objects(num):
    things = []
    for cls, data in PACKAGES:
        subcls = type(cls, (Thing,), {})
        things.append(subcls(num, *data))
    return things


def one_pack(number_of_items_in_pack):
    pack = {}
    for num in range(randint(0, number_of_items_in_pack)):
        range_things = sample(create_subclass_objects(
            randint(0, NUMBER_OF_VARIETY_OF_ITEMS)),
            SAMPLE_CONST,
        )
        for thing in range_things:
            things = {
                thing.name_num: [thing.attack, thing.defence, thing.health]
            }
            pack.update(things)
    return pack


def equipment_points_summ(pack):
    thing_name = []
    sum_attack = 0
    sum_defence = 0
    sum_hp = 0
    for name, el in pack.items():
        sum_attack += el[0]
        sum_defence += el[1]
        sum_hp += el[2]
        thing_name.append(name)
    return [sum_attack, sum_defence, sum_hp, thing_name]


def create_few_packs_of_items(all_number=20):
    all_packs = []
    for one_num in range(all_number):
        all_packs.append(
            equipment_points_summ(one_pack(len(PACKAGES) - 1))
        )
    return all_packs
