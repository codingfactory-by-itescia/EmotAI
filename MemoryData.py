class MemoryData:
    values = []

    def __init__(self, initial_values, size):
        self.values = initial_values
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

    def count_value(self, value):
        count = 0
        for index in range(len(self.values)):
            if self.values[index] == value:
                count += 1
        return count
