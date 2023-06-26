class Hashtable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable, handling collisions.
        """
        index = hash(key) % self.size
        if self.table[index] is None:
            self.table[index] = []
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                self.table[index][i] = (key, value)  
                return
        self.table[index].append((key, value))  

    def get(self, key):
        """
        Returns the value associated with the given key in the table.
        Returns None if the key doesn't exist.
        """
        index = hash(key) % self.size
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry[0] == key:
                    return entry[1]
        return None

    def has(self, key):
        """
        Checks if the given key exists in the table.
        Returns True if the key exists, False otherwise.
        """
        index = hash(key) % self.size
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry[0] == key:
                    return True
        return False

    def keys(self):
        """
        Returns a collection of keys present in the table.
        """
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for entry in bucket:
                    keys.append(entry[0])
        return keys

    def hash(self, key):
        """
        Returns the index in the collection for the given key.
        """
        return hash(key) % self.size



