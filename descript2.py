# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class CheckMeaningNotBigger:

    def __set__(self, instance, value):
        if value > 1000:
            raise ValueError("Значение  дожно быть <= 1000!")
        instance.__dict__[self.weight] = value

    def __set_name__(self, Road, weight):
        self.weight = weight

class Road:

    weight = CheckMeaningNotBigger()

    def __init__(self, width, length_in_km, height, weight):
        self._length_in_km = length_in_km
        self._width = width
        self.weight = weight
        self.height = height

    def asphalt_mass(self):
        asphalt_mass = self._length_in_km * self._width * self.height * self.weight
        # assert asphalt_mass == 12500, "The output is wrong!"
        print(f'We need {asphalt_mass} tons')

r = Road(5,20,25,5)
r.asphalt_mass()
