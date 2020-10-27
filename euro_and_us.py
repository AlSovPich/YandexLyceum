class AmericanDate:
    
    def __init__(self, year, month, day):
        if self.month < 10:
            self.month = '0' + str(self.month)
        if self.day < 10:
            self.day = '0' + str(self.day)

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def get_year(self):
        print(self.year)

    def get_day(self):
        print(self.day)

    def get_month(self):
        print(self.month)

    def format(self):
        print(str(self.month) + '.' +str(self.day) + '.' + str(self.year))


class EuropeanDate:
    
    def __init__(self, year, month, day):
        if self.month < 10:
            self.month = '0' + str(self.month)
        if self.day < 10:
            self.day = '0' + str(self.day)

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def get_year(self):
        print(self.year)

    def get_day(self):
        print(self.day)

    def get_month(self):
        print(self.month)

    def format(self):
        print(str(self.day) + '.' +str(self.month) + '.' + str(self.year))


        
    
