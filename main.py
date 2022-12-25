from random import randint

from graphic_arts.start_game_banner import run_screensaver


class Character:
    def __init__(self, char_name) -> None:
        self.char_name = char_name

    def start_training(self) -> str:
        """Start training."""
        print('Потренируйся управлять своими навыками.')
        print(
            'Введи одну из команд: attack — чтобы атаковать противника, '
            'defence — чтобы блокировать атаку противника или special '
            '— чтобы использовать свою суперсилу.'
            )
        print('Если не хочешь тренироваться, введи команду skip.')
        cmd: str = ''
        while cmd != 'skip':
            cmd = input('Введи команду: ')
            if cmd == 'attack':
                print(character.attack())
            if cmd == 'defence':
                print(character.defence())
            if cmd == 'special':
                print(character.special())
        return ('Тренировка окончена.')


class Warrior(Character):
    def attack(self) -> str:
        """Attack."""
        return (f'{self.char_name} '
                f'нанёс урон противнику равный {5 + randint(3, 5)}')

    def defence(self) -> str:
        """Defence."""
        return (f'{self.char_name} блокировал {10 + randint(5, 10)} урона')

    def special(self) -> str:
        """Ulta."""
        return (f'{self.char_name} '
                f'применил специальное умение «Выносливость {105}»')

    def start_training(self) -> str:
        """Start training."""
        print(f'{self.char_name}, ты Воитель — отличный боец ближнего боя.')
        print(super().start_training())


class Mage(Character):
    def attack(self) -> str:
        """Attack."""
        return (f'{char_name} '
                f'нанёс урон противнику равный {5 + randint(5, 10)}')

    def defence(self) -> str:
        """Defence."""
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')

    def special(self) -> str:
        """Ulta."""
        return (f'{char_name} применил специальное умение «Атака {45}»')

    def start_training(self) -> str:
        """Start training."""
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
        print(super().start_training())


class Healer(Character):
    def attack(self) -> str:
        """Attack."""
        return (f'{char_name} '
                f'нанёс урон противнику равный {5+ randint(-3, -1)}')

    def defence(self) -> str:
        """Defence."""
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')

    def special(self) -> str:
        """Ulta."""
        return (f'{char_name} применил специальное умение «Защита {40}»')

    def start_training(self) -> str:
        """Start training."""
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
        print(super().start_training())


def choice_char_class() -> str:
    """Select a class."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь '
            'играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или '
            'любую другую кнопку, чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    if char_class == 'warrior':
        character = Warrior(char_name)
    elif char_class == 'mage':
        character = Mage(char_name)
    else:
        character = Healer(char_name)
    character.start_training()
