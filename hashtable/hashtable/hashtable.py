class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Replace value if key already exists
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def has(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return False
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for pair in bucket:
                    keys.append(pair[0])
        return keys

    def hash(self, key):
        return self.hash(key)
