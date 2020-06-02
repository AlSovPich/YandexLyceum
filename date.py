class Date:
    def __init__(self, month, day):
        self.days = day
        thirty_one = [1, 3, 5, 7, 8, 10, 12]
        thirty = [4, 6, 9, 11]
        for i in range(1, month):
            if i in thirty_one:
                self.days += 31
            elif i in thirty:
                self.days += 30
            else:
                self.days += 28

    def __sub__(self, other):
        return self.days - other.days

    def days(self):
        return self.days


mar5 = Date(3, 1)
jan1 = Date(1, 1)
print(mar5.days)
print(jan1.days)
print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)