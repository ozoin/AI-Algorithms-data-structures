# import unittest
from chaining_hash_node import ChainingHashNode


class ChainingHashSet():
    def __init__(self, capacity=0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key):
        """Hash function that calculates a hash code for a given key using the modulo division.
        :param key:
                Key for which a hash code shall be calculated according to the length of the hash table.
        :return:
                The calculated hash code for the given key.
        """
        return key % len(self.hash_table)
        pass

    def get_hash_table(self):
        """(Required for testing only)
        :return the hash table.
        """
        return self.hash_table
        pass

    def get_hash_table_values(self):
        """
        Function for testing
        """
        table = list()
        for elem in self.hash_table:
            if elem is not None:
                table.append(elem.key)
            else:
                table.append(None)
        return table

    def set_hash_table(self, table):
        """(Required for testing only) Set a given hash table..
        :param table: Given hash table which shall be used.

        !!!
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!

        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!)."""
        return self.table_size
        pass

    def insert(self, key):
        """
        Inserts a key and returns True if it was successful. If there is already an entry with the
          same key, the new key will not be inserted and False is returned.
         :param key:
                 The key which shall be stored in the hash table.
         :return:
                 True if key could be inserted, or False if the key is already in the hash table.
         :raises:
                 a ValueError if any of the input parameters is None.
         """
        if key is None:
            raise ValueError('key is none')
        if self.contains(key):
            return False
        index = self.get_hash_code(key)
        if self.hash_table[index] == None:
            self.hash_table[index] = ChainingHashNode(key)
            self.table_size += 1
            return True
        else:
            curr_elem = self.hash_table[index]
            while curr_elem:
                if curr_elem.next == None:
                    curr_elem.next = ChainingHashNode(key)
                    self.table_size += 1
                    return True
                curr_elem = curr_elem.next

    def contains(self, key):
        """Searches for a given key in the hash table.
         :param key:
                 The key to be searched in the hash table.
         :return:
                 True if the key is already stored, otherwise False.
         :raises:
                 a ValueError if the key is None.
         """
        if key is None:
            return ValueError('Key is none')
        index = self.get_hash_code(key)
        cur_elem = self.hash_table[index]
        while cur_elem:
            if cur_elem.key == key:
                return True
            else:
                cur_elem = cur_elem.next
        return False

    def remove(self, key):
        """
        Removes the key from the hash table and returns True on success, False otherwise.
        :param key:
                The key to be removed from the hash table.
        :return:
                True if the key was found and removed, False otherwise.
        :raises:
             a ValueError if the key is None.
        """
        if key is None:
            raise ValueError('key is none')
        index = self.get_hash_code(key)
        cur_elem = prev_elem = self.hash_table[index]
        if self.contains(key):
            if cur_elem.key == key:
                self.hash_table[index] = cur_elem.next
                self.table_size -= 1
                return True
            else:
                cur_elem = cur_elem.next
                while cur_elem:
                    if cur_elem.key == key:
                        prev_elem.next = cur_elem.next
                        self.table_size -= 1
                        return True
                    else:
                        cur_elem, prev_elem = cur_elem.next, prev_elem.next
        else:
            return

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        table_len = len(self.get_hash_table())
        self.hash_table = [None] * table_len
        self.table_size = 0
        pass

    def to_string(self):
        """Returns a string representation of the hash table (array indices and stored keys) in the format
            Idx_0 {Node, Node, ... }, Idx_1 {...}
            e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32}, """
        components = str()
        for i, elem in enumerate(self.hash_table):

            if elem:
                components += f'{i} {{{elem.key}}}, '
            else:
                components += f'{i} {{None}}, '


# class TestChainingHashSet(unittest.TestCase):
#     def insert(self, test_set, key):
#         return test_set.insert(int(key))

#     def contains(self, test_set, key):
#         return test_set.contains(int(key))

#     def remove(self, test_set, key):
#         return test_set.remove(int(key))

#     def test_insert_without_chaining(self):
#         # self.assertTrue(self.insert(stud_set, 5), "insert(5) returned false but must be true")
#         # self.assertFalse(self.insert(stud_set, 5), "insert(5) returned true but must be false")
#         # print(stud_set.get_hash_table())
#         # # self.assertTrue(self.insert(stud_set, 16), "insert(16) returned false but must be true")
#         # # self.assertFalse(self.insert(stud_set, 16), "insert(16) returned true but must be false")
#         # #stud_set = ChainingHashSet(capacity=11)
#         stud_set = ChainingHashSet(capacity=11)
#         # arr = [11, 12, 13, 14, 15, 5, 6, 7, 8, 9, 10]
#         # arr2 = [5, 6, 11, 12, 17, 13, 13, 17]
#         # test_set = [ChainingHashNode(11), ChainingHashNode(12), ChainingHashNode(13),
#         #             ChainingHashNode(14), ChainingHashNode(
#         #                 15), ChainingHashNode(5),
#         #             ChainingHashNode(6), ChainingHashNode(
#         #                 7), ChainingHashNode(8),
#         #             ChainingHashNode(9), ChainingHashNode(10)]
#         # for elem in arr:
#         #     stud_set.insert(elem)
#         # print(stud_set.get_hash_table_values())
#         # stud_set._remove(11)
#         # print(stud_set.get_hash_table_values())

#         self.assertEqual(0, stud_set.get_table_size())

#         self.assertTrue(self.insert(stud_set, 5))
#         self.assertEqual(1, stud_set.get_table_size())

#         self.assertTrue(self.insert(stud_set, 6))
#         self.assertEqual(2, stud_set.get_table_size())

#         self.assertTrue(self.insert(stud_set, 11))
#         self.assertEqual(3, stud_set.get_table_size())

#         self.assertTrue(self.insert(stud_set, 12))
#         self.assertEqual(4, stud_set.get_table_size())

#         self.assertTrue(self.insert(stud_set, 13))
#         self.assertEqual(5, stud_set.get_table_size())
#         self.assertFalse(self.insert(stud_set, 13))
#         self.assertTrue(self.insert(stud_set, 17))
#         self.assertEqual(6, stud_set.get_table_size())

#         # print(stud_set.get_hash_table_values())
#         #self.assertFalse(self.insert(stud_set, 16), "insert(16) returned true but must be false")
#         print(stud_set.get_hash_table_values())
#         print(stud_set.to_string())


# if __name__ == '__main__':

#     unittest.main()
