class Singleton(type):
    _my_data = {}

    def __call__(cls, args, kwargs):
        if cls not in cls._my_data:
            cls._my_data[cls] = super(Singleton, cls).__call__(args, kwargs)
        return cls._my_data[cls]


class Logger(metaclass=Singleton):
    pass
