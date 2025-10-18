class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)


class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupils)


class House(Building):
    pass


class Shop(Building):
    pass


school = School(100, 2000, 'Moscow')
school.get_info()

house = House(2000, 'Moscow')
shop = Shop(2000, 'Moscow')
