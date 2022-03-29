
class HashTable:

    def __init__(self):
        # Based on load factor, we can change the size of the underlying data structure(dynamic resizing)
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    # Takes key as parameter and calculates hash value based on the key
    def hash_fucntion(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity

    def insert(self, key, data):
        # Find a valid location for the data
        index = self.hash_fucntion(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            # do linear probing
            index = (index+1) % self.capacity

        self.keys[index] = key
        self.values[index] = data

    def get_item(self, key):
        index = self.hash_fucntion(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        # Item does not exist
        return None


if __name__ == "__main__":
    hash_table = HashTable()
    print(hash_table.hash_fucntion("Souparna"))
    print(hash_table.hash_fucntion("Bose"))
    hash_table.insert("Souparna", 27)
    hash_table.insert("Bose", 26)
    print(hash_table.get_item("Souparna"))
    print(hash_table.get_item("Bose"))

# 1
# 3
# 27
# 26
