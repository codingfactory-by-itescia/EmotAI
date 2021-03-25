class MemoryData:
    values = []

    def __init__(self, size):
        self.size = size

    def add(self, value):
        if len(self.values) < self.size:
            self.values.append(value)
            return

        new_array = []
        for index in range(1, len(self.values)):
            new_array.append(self.values[index])
        new_array.append(value)
        self.values = new_array
        return
