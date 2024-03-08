from random import randint

from characters import characters, complete_character


WARRIORS_QUANTITY = 10


def battle(fighter_1, fighter_2, warrior_list):
    print('''

            ''')
    print(
        f'На арену выходят воины: '
        f'{fighter_1.__class__.__name__} {fighter_1.name} и '
        f'{fighter_2.__class__.__name__} {fighter_2.name}'
    )
    print(
        f'Очки здоровья: '
        f'{fighter_1.name} {fighter_1.health()}    '
        f'{fighter_2.name} {fighter_2.health()}'
    )
    print(fighter_1.name, 'предметы', fighter_1.equipment)
    print(fighter_2.name, 'предметы', fighter_2.equipment)
    print('+-----------------------------------+')
    while fighter_1.health() > 0 and fighter_2.health() > 0:
        fighter_attack = fighter_2.attack()
        fighter_1.taken_damage(fighter_attack)
        print(
            f'{fighter_2.name} бьет {fighter_1.name} '
            f'и наносит урон {fighter_attack}'
        )
        print(
            f'Очки здоровья: {fighter_1.name} {fighter_1.health()}    '
            f'{fighter_2.name} {fighter_2.health()}'
        )
        print('+-----------------------------------+')
        if fighter_1.health() <= 0:
            warrior_list.remove(fighter_1)
            print('')
            print(
                f'{fighter_2.__class__.__name__} '
                f'{fighter_2.name} THE WINNER!'
            )
            print('')
            break
        fighter_1, fighter_2 = fighter_2, fighter_1
    if len(warrior_list) > 1:
        print(f'Воинов осталось: {len(warrior_list)}')


def battle_start(warriors_quantity):
    warrior_list = characters(warriors_quantity)
    complete_character(warrior_list)
    while len(warrior_list) > 1:
        warrior_num = randint(2, warriors_quantity) - 1
        battle(warrior_list[0], warrior_list[warrior_num], warrior_list)
        warriors_quantity -= 1


if __name__ == '__main__':
    battle_start(WARRIORS_QUANTITY)
