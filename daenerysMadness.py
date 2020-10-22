class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)
        self.notes = []
        for j in range(len(bells)):
            if isinstance(self.bells[j], BigBell):
                self.notes.append(0)
            else:
                self.notes.append(2)

    def sound(self):
        for i in range(len(self.bells)):
            if isinstance(self.bells[i], BigBell):
                if self.notes[i] == 0:
                    print("ding")
                    self.notes[i] = 1
                else:
                    print("dong")
                    self.notes[i] = 0
            else:
                print("ding")
        print("...")

    def append(self, adding):
        self.bells.append(adding)
        if isinstance(self.bells[-1], BigBell):
            self.notes.append(0)
        else:
            self.notes.append(2)


class BigBell:
    def __init__(self):
        pass


class LittleBell:
    def __init__(self):
        pass
