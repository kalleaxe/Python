import linked_list as LinkedList

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:          # loop until root is none or root key is k
            if k < n.key:                # left or right subtree, set n as said subtree
                n = n.left
            else:
                n = n.right
        return n is not None             # return Bool


    def rec_contains(self, k):

        def _rec_contains(root, k):          # input node is the current node
            if not root:                                # base cases, no node contains k
                return False
            elif root.key == k:                         # the current node is k
                return True
            elif k < root.key:
                return _rec_contains(root.left, k)      # recursive looking at the node of left subtree
            else:
                return _rec_contains(root.right, k)     # recursive looking at the node of right subtree
        return _rec_contains(self.root, k)


    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    def height(self):

        def _height(root):
            if root is None:                                            # base case, end is reached.
                return 0
            return 1 + max(_height(root.right), _height(root.left))     # max() to compare size of subtrees
        return _height(self.root)

    def remove(self, key): 
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):        # r is root of the subtree/tree, k is the key to remove
        
        if r is None:                               #base case, root is None 
            return None
        elif k < r.key:                             # recursive on left subtree
            r.left = self._remove(r.left, k)
        elif k > r.key:                             # recursive on right subtree
            r.right = self._remove(r.right, k)

        else:                                       # else r = k, Found the node to be removed
            if r.left is None:                      # Case 1 and 2: root with only one subtree or none
                return r.right                      # No left subtree, return right subtree
            elif r.right is None:
                return r.left                       # No right subtree, return the left subtree

            current = r.right                       # Case 3: root with two subtrees    
            while current.left:                     # go down left as far as possible in the right subtree.
                current = current.left
            smallest_right = current                
            r.key = smallest_right.key                              # Replace current root's key with the smallest node's key
            r.right = self._remove(r.right, smallest_right.key)     # recursively removes the smallest node from right subtree, it enters L112 or L115
        return r
        
    def __str__(self):                                 
        str = ''
        for data in self:                   # iterate through the LinkedList retrieving data from each node.
            str += f'{data}, '
        return '<' + str[:-2] + '>'         # slice last two chars from string, which well be final unnecessary blank and comma.
    
    def to_list(self):                      # converts a binary tree a python list      
        return ([node for node in self])    # Good looking list comprehension
    "complexity is O(n)"

    def to_LinkedList(self):                 # converts a binary tree to a linked list    
        ll = LinkedList()
        for node in self:
            ll.insert(node)
        return ll
    

def main():
    t = BST()
    for x in [1,2,3,4,5,6,7,8,9]:
        t.insert(x)
    t.print()

if __name__ == "__main__":
    main()