# tabletools.py

class LabeledList:

    def __init__(self, data=None, index=None):
        self.data = data
        self.index = index
        if index == None:
            self.index = list(range(len(data)))