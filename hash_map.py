# Author: Paldin Bet Eivaz
# Description: Program which implements a hash map data structure.


# Import DynamicArray and LinkedList classes
from helper_structs import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the contents of the hash map.
        """

        # replace each bucket wih an empty linked list
        for i in range(self.buckets.length()):
            self.buckets.set_at_index(i, LinkedList())

        self.size = 0

    def get(self, key: str) -> object:
        """
        Returns the value associated with the specified key.
        Returns None if the key is not in the hash map.
        """

        # calculate bucket index and get bucket
        hash = self.hash_function(key)
        idx = hash % self.capacity
        bucket = self.buckets.get_at_index(idx)

        if bucket.contains(key):
            return bucket.contains(key).value

        return None

    def put(self, key: str, value: object) -> None:
        """
        Inserts the specified key/value pair into the hash map.
        If the specified key already exists in the map, its value is replaced by the specified value.
        If the specified key does not exist in the map, the key/value pair is added.
        """

        # calculate bucket index and get bucket
        hash = self.hash_function(key)
        idx = hash % self.capacity
        bucket = self.buckets.get_at_index(idx)

        # if key already exists, replace value
        if bucket.contains(key):
            bucket.contains(key).value = value
        # if key does not exist, insert key/value pair
        else:
            bucket.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes the specified key and its value from the hash map if it exists.
        """

        # calculate bucket index and get bucket
        hash = self.hash_function(key)
        idx = hash % self.capacity
        bucket = self.buckets.get_at_index(idx)

        if bucket.contains(key):
            bucket.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if specified key is in the hash map.
        Returns False otherwise.
        """

        # check if map is empty
        if self.size == 0:
            return False

        # calculate bucket index and get bucket
        hash = self.hash_function(key)
        idx = hash % self.capacity
        bucket = self.buckets.get_at_index(idx)

        if bucket.contains(key):
            return True

        return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table.
        """

        count = 0

        # check if any bucket has an empty linked list
        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:
                count += 1

        return count

    def table_load(self) -> float:
        """
        Returns the hash table's current load factor.
        """

        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table.
        """

        # capacity may not be < 1
        if new_capacity < 1:
            return

        # create a new hash table with the new capacity
        new_buckets = DynamicArray()
        for _ in range(new_capacity):
            new_buckets.append(LinkedList())

        # iterate through each link in each of the buckets
        for i in range(self.buckets.length()):
            for link in self.buckets.get_at_index(i):
                # rehash each link using the new capacity
                hash = self.hash_function(link.key)
                new_idx = hash % new_capacity
                # insert rehashed links into the new hash table
                new_buckets.get_at_index(new_idx).insert(link.key, link.value)

        self.buckets = new_buckets
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stored in the hash map.
        """

        da = DynamicArray()

        # get key at every link in every bucket and append to DynamicArray
        for i in range(self.buckets.length()):
            for link in self.buckets.get_at_index(i):
                da.append(link.key)

        return da


# BASIC TESTING
if __name__ == "__main__":
    pass

    # print("\nempty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)

    # print("\nempty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)

    # print("\ntable_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())

    # print("\ntable_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)

    # print("\nclear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    # print("\nclear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    # print("\nput example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    # print("\nput example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    # print("\ncontains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))

    # print("\ncontains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     all inserted keys must be present
        # result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        # result &= not m.contains_key(str(key + 1))
    # print(result)

    # print("\nget example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))

    # print("\nget example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    # print("\nremove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')

    # print("\nresize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    # print("\nresize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)

    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)
    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')
    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    # print("\nget_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())
    #
    # m.resize_table(1)
    # print(m.get_keys())

    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())
