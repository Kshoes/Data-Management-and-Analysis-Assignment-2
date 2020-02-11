# tabletools.py

class LabeledList:

    def __init__(self, data=None, index=None):
        self.data = data
        self.index = index
        if index == None:
            self.index = list(range(len(data)))

    def __str__(self):
        string = '""""""\n'
        for x, y in zip(self.index, self.data):
            string += f'{x:>5}   {y}\n'
        return string

    def __repr__(self):
        return self.__str__()