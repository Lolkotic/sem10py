# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: start, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class CheckNonNeg:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не дожно быть отрицательным!")
        instance.__dict__[self.speed] = value

    def __set_name__(self, Car, speed):
        self.speed = speed


class Car:

    speed = CheckNonNeg()

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def start(self):
        return f' {self.name} goes.'

    def stop(self):
        return f'\n {self.name} stops.'

    def turn(self, direction):
        return f'\n {self.name} turnes {direction}'

    def show_speed(self):
        return f'\nThe speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nThe speed is too high!  {self.speed} km per hour'
        else:
            return f'Speed of {self.name} is ok'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nThe speed is too high!  {self.speed} km per hour'
        else:
            return f'Speed of {self.name} is ok'


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


town = TownCar('Ford Focus 2', 70, 'white', False)
print('TownCar:\n' + town.start(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop()+"\n")

sport = SportCar('Ferrari SF90 Stradale', 200, 'red', False)
print('SportCar:\n' + sport.start(), sport.show_speed(), sport.turn('left'), sport.stop()+"\n")

work = WorkCar('Volkswagen Touran', 30, 'blue', False)
print('WorkCar:\n' + work.start(), work.show_speed(), work.turn('right'), work.stop()+"\n")

police = PoliceCar('Kia', 105, 'white-blue', True)
print('PoliceCar:\n' + work.start(), work.show_speed(), work.turn('right'), work.stop()+"\n")