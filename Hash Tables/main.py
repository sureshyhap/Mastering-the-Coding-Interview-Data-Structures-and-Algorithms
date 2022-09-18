import random

class Hash_Table:

    class Hash_Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.isOccupied = False
            self.isDeleted = False

        def __str__(self):
            return f"{self.key} : {self.value}"
    
    prime_list = [53, 97, 193, 389, 769, 1543, 3079]
    @staticmethod
    def get_prime(number):
        for num in Hash_Table.prime_list:
            if number <= num:
                return num

    
    def __init__(self, capacity=13):
        self.capacity = Hash_Table.get_prime(capacity)
        #self.data = [Hash_Table.Hash_Node()] * self.capacity
        self.data = [Hash_Table.Hash_Node() for _ in range(self.capacity)]
        self.size = 0

    def hash(self, element):
        index = 0
        i = 0
        for char in element:
            index += ord(char) * pow(37, i)
            index %= self.capacity
            i += 1
        return index

    def rehash(self):
        self.capacity = Hash_Table.get_prime(self.capacity * 2)
        #data = [Hash_Table.Hash_Node() for _ in range(self.capacity)]
        temp = Hash_Table(self.capacity)
        for hash_element in self.data:
            if hash_element.isOccupied and not hash_element.isDeleted:
                temp.insert(hash_element.key, hash_element.value)
        self.data = temp.data

    def lookup(self, element):
        index = self.get_index(element)
        if index != -1:
            return self.data[index].value
        else:
            return None

    def get_index(self, element):
        index = self.hash(element)
        i = 0
        while self.data[(index + i) % self.capacity].key and \
              self.data[(index + i) % self.capacity].key != element:
            i += 1
            i %= self.capacity
        if not self.data[index + i].key:
            return -1
        return index + i

    
    
    def insert(self, key_element, value_element):
        if self.size + 1 > self.capacity // 2:
            self.rehash()
        index = self.hash(key_element)
        i = 0
        while self.data[(index + i) % self.capacity].isOccupied:
            i += 1
        index = (index + i) % self.capacity
        self.data[index].key = key_element
        self.data[index].value = value_element
        self.data[index].isOccupied = True
        self.size += 1


    def delete(self, key_element):
        index = self.get_index(key_element)
        if index == -1:
            return
        self.data[index].isDeleted = True
        self.size -= 1

ht = Hash_Table()

lyst_keys = []
for _ in range(100):
    length = random.randint(1, 5)
    string = ""
    for __ in range(length):
        offset = random.randrange(26)
        string += chr(ord("a") + offset)
    lyst_keys.append(string)
lyst_values = [len(string) for string in lyst_keys]
zipped = list(zip(lyst_keys, lyst_values))

for key, value in zipped:
    ht.insert(key, value)
    
for _ in range(10):
    word = random.choice(lyst_keys)
    print(f"{word} : {ht.lookup(word)}")

