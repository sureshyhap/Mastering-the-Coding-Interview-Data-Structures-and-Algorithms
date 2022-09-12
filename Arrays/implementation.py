class Array:
    def __init__(self):
        self.size = 0
        self.array = {}

    def push(self, element):
        self.array[self.size] = element
        self.size += 1

    def pop(self):
        data = self.array[self.size - 1]
        del self.array[self.size - 1]
        self.size -= 1
        return data

    def access(self, index : int):
        return self.array[index]

    def insert(self, index : int, element):
        temp = {}
        for i in self.array:
            if i == index:
                break            
            temp[i] = self.array[i]
        temp[index] = element
        for i in range(self.size - index):
            temp[index + 1 + i] = self.array[index + i]
        self.array = temp
        self.size += 1

    def delete(self, index):
        data = self.array[index]
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        del self.array[self.size - 1]
        self.size -= 1
        return data

    def __str__(self):
        string = ""
        for key, value in self.array.items():
            string += f"{key} : {value}\n"
        return string

a = Array()
a.push(5)
a.push(10)
a.push(20)
a.push(40)
print(a)
a.insert(1, -1)
print(a)
a.delete(2)
print(a)
