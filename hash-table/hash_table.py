

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


if __name__ == "__main__":
    hash_table = HashTable()
    print(hash_table.hash_fucntion("Souparna"))
    print(hash_table.hash_fucntion("Bose"))

# 1
# 3
