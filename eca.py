class ECA:
    def __init__(self, id):
        self.id = bin(id)[2:].zfill(8)
        self.dict = {}

        for i in range(8):
            self.dict[bin(7 - i)[2:].zfill(3)] = self.id[i]

        self.array = [0 for x in range(199)]
        self.array[99] = 1

    def step(self):
        arr = [0 for x in range(len(self.array))]
        for i in range(len(self.array)):
            s = ""
            if i == 0:
                s += "0"
            else:
                s += str(self.array[i - 1])
            s += str(self.array[i])
            if i == len(self.array) - 1:
                s += "0"
            else:
                s += str(self.array[i + 1])
            arr[i] = int(self.dict[s])
        self.array = arr
