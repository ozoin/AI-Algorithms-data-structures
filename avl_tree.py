from avl_node import AVLNode
import unittest

class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.size = 0
    def get_tree_root(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def get_tree_height(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        if self.root == None:
            return -1
        return self.root.height

    def get_tree_size(self):
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def to_array(self):
        """Yields an array representation of the tree's values (pre-order).
        :return Array representation of the tree values.
        """
        if self.height == -1:
            raise ValueError('ERROR: root is None')
        print_array = list()
        return self._preorder(self.root, print_array)

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError('ERROR: key is None')
        key_found = self._find(key,self.root)
        if not key_found:
            return None
        return key_found.value


    def insert(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if not isinstance(key, int):
            raise ValueError('Key is not integer')
        if key and value is None:
            raise ValueError('Key is none')
        new_node = AVLNode(key, value)
        if not self.root:
            self.root = new_node
            self.size += 1
            return True
        else:
            return self._insert_helper(self.root, new_node)

    def remove_by_key(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if not key and not self.root:
            raise ValueError("ERROR: key is None")
        else: 
            node = self._find(key, self.root)
        if node:
            status = self.remove_node(node)
            self.size -= 1
            return status
        else:
            return False

########################################################################

    def remove_node(self, node):
        if not node:
            return False
        if (node.left and not node.right) or (node.right and not node.left):
            if not node.right:
                child = node.left
            else:
                child = node.right
            if not node.parent:
                self.root = child
            else:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
                child.parent = node.parent
                node.parent.height = self.max_height(node)
            if self.root:
                if self.node_height(self.root.left) > self.node_height(self.root.right):
                    self.root.height = 1+self.root.left.height
                else: 
                    self.root.height = 1+self.root.right.height
            return True

        if node.left and node.right: #CASE 1
            child = self.find_leftmost(node.right)
            node.key, node.value = child.key, child.value
            self.remove_node(child)
            return True
        else: #CASE 2
            if not node.parent:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent.height = self.max_height(node)
            return True

    def find_leftmost(self, node):
        if node:
            while node.left:
                node = node.left
        return node
    def find_largest_h(self, node):
        if self.node_height(node.left) > self.node_height(node.right):
            return node.left
        else:
            return node.right
        
    def balance_factor(self,node):
        if abs(self.node_height(node.left)-self.node_height(node.right)) > 1:
            return True
        else:
            return False
    def _preorder(self, node, print_array):
        """Recursive function to traversal through the tree in preorder.
        :param node: current node
        :param print_array: list where the output is stored
        :return: print_array
        """
        if node:
            print_array.append(node.key)
            print_array = self._preorder(node.left, print_array)
            print_array = self._preorder(node.right, print_array)
        return print_array

    def _find(self, key, current_node):
        """
        Recursive function to find a certain element in a given tree.
        :param key: key which should be searched for
        :param node: current node in the tree
        :return: node with given key ; None otherwise
        """
        # TODO: still needs to be tested
        if current_node:
            if current_node.key == key:
                return current_node
            if key < current_node.key:
                return self._find(key, current_node.left)
            else:
                return self._find(key, current_node.right)        
        else: 
            return None
        
    def _insert_helper(self, current_node, new_node):
        if new_node.key > current_node.key:
            if current_node.right is None:
                current_node.right = new_node
                current_node.right.parent = current_node
                self.node_list(current_node.right)
                self.size += 1
            else:
                self._insert_helper(current_node.right, new_node)
        elif new_node.key < current_node.key:
            if current_node.left is None:
                current_node.left = new_node
                current_node.left.parent = current_node
                self.node_list(current_node.left)
                self.size += 1
            else:
                self._insert_helper(current_node.left, new_node)
        else:
            return False

    def node_list(self, node, node_list=[]):
        if node.parent:
            node_list.append(node)
            balance_factor = self.parent_balance_factor(node) 
            if balance_factor and node.parent:
                node_list.append(node.parent)
                x = node_list[-3]
                y = node_list[-2]
                z =node_list[-1]
                self.get_components(x, y, z)
                return
        else:
            return False
        if node.height+1 > node.parent.height:
            node.parent.height = node.height + 1
        self.node_list(node.parent, node_list)
        
    def get_components(self, x, y, z):
        if z.left == y:  # left version
            if x == y.left:  # single rotation
                self.r_rotate(z)
            else:  # double rotation
                self.l_rotate(y)
                self.r_rotate(z)
        else:
            if y.right == x:
                self.l_rotate(z)  # single rotation
            else:  # double rotation case
                self.r_rotate(y)
                self.l_rotate(z)


    def l_rotate(self, node):
        parent = node.parent
        y = node.right
        t1 = y.left

        y.left = node
        node.parent = y
        node.right = t1
        y.parent = parent
        if t1:
            t1.parent = node
        if y.parent:
            if y.parent.left == node:
                y.parent.left = y
            else:
                y.parent.right == y
        else:
            self.root = y

        node.height = self.max_height(node)
        y.height = self.max_height(y)
        
    def r_rotate(self, node):
        parent = node.parent
        y = node.left
        t1 = y.right

        y.right = node
        node.parent = y
        node.left = t1
        y.parent = parent
        if t1:
            t1.parent = node
        if y.parent:
            if y.parent.right == node:
                y.parent.right = y
            else:
                y.parent.left == y
        else:
            self.root = y
        self.update_node_height(node)
        self.update_node_height(y)
        
    def parent_balance_factor(self,node):
        if abs(self.node_height(node.parent.left) - self.node_height(node.parent.right))>1:
            return True
        else:
            return False
    def max_height(self,node):
        return 1 + max(self.node_height(node.right),self.node_height(node.left))
    
    def update_node_height(self,node):
        node.height =  1 + max(self.node_height(node.right),self.node_height(node.left))
        
    def node_height(self, node):
        if node:
            return node.height
        else:
            return -1        
        
        

# class TestAssignment02(unittest.TestCase):

#     def setUp(self):
#         pass

#     def reset(self):
#         global tree
#         tree = AVLTree()

#     def insert(self, key, elem):
#         # handle a none tree object
#         global tree
#         return tree.insert(key, elem)

#     def insert(self, key):
#         # handle a none tree object
#         global tree
#         return tree.insert(key, float(key))

#     def test_insert(self):
#         global tree
#         self.reset()
#         self.insert(5)
#         self.insert(18)
#         self.insert(2)
#         self.insert(8)
#         self.insert(14)
#         self.insert(16)
#         self.insert(13)
#         self.insert(3)
#         self.insert(12)
#         self.insert(21)
#         self.insert(1)
#         self.insert(0)

#         tree.remove_by_key(4)
#         #tree.remove_by_key(0)
#         root = tree.get_tree_root()
#         elems = []
#         print(root.key)
#         print(tree.to_array())
#         print(tree._preorder(root, elems))


# if __name__ == '__main__':

#     unittest.main()
