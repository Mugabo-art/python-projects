class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_val = self.hash(key)
        if hash_val not in self.collection:
            self.collection[hash_val] = {}
        self.collection[hash_val][key] = value

    def remove(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection and key in self.collection[hash_val]:
            del self.collection[hash_val][key]
            # Optional: remove the nested dict if it's empty
            if not self.collection[hash_val]:
                del self.collection[hash_val]

    def lookup(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection and key in self.collection[hash_val]:
            return self.collection[hash_val][key]
        return None