import random


class Buddhist:
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        return self.__karma

    def set_karma(self, path_to_enlightenment):
        self.__karma += path_to_enlightenment


def one_day(count):
    if random.randint(1, 10) == 1:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            deviation = random.choice(
                ['KillError', 'DrunkError', 'CarCrashError',
                 'GluttonyError', 'DepressionError']
            )
            karma_log.write(f'День {count}: сход с пути - {deviation}\n')
            return False
    else:
        return random.randint(1, 7)


my_buddhist = Buddhist()
day = 0
while my_buddhist.get_karma() < 500:
    day += 1
    if one_day(day):
        pass
    else:
        my_buddhist.set_karma(one_day(day))
print(f'Ну наконец-то!!! Просветление пришло через {day} дней.')