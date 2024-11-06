class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:          # case 1, node will be first if it is the smallest / only node.
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:                   # case 2, iterates until the next data is larger.
                f = f.succ
            f.succ = self.Node(x, f.succ)                       # inserts the node between f and f.succ

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):
        i = 0
        f = self.first          # f is set to first node
        while f:                # loop until f = None
            f = f.succ          # f is set to next node
            i += 1              # could be done with enumerate and generator, complexity is still O(n)
        return i

    def mean(self):               
        pass


    def remove_last(self):      
        f = self.first
        prev = None
        while f:
            if f.succ is None and prev is None:         # case 1, list has 1 or no nodes.
                self.first = None                       
                return f.data
            elif f.succ is None:                        # case 2, reached end of list. remove Node by setting previous pointer to None
                prev.succ = None
            prev = f
            f = f.succ
        return prev.data                                # return data of deleted Node

    def remove(self, x):         
        f = self.first
        prev = None
        while f:
            if f.data == x:                         
                if f.succ:                              # If there is a successor:
                    f.data = f.succ.data                # sets current node data to next node data
                    f.succ = f.succ.succ                # sets current node pointer to two nodes ahead, skipping next node.
                elif f.succ == None and prev is None:   # if there is no successor, last Node.
                    f = None                            # no previous, no successor. remove first!
                elif f.succ == None and prev:
                        prev.succ = None                # removes last node through previous pointer
                return True
            prev = f
            f=f.succ
        return False
        


    def to_list(self):            

        def _to_list(self):
            current = self
            if current is None:                                     # if empty list
                return []
            if current.succ:                                        # if there is a successor 
                return [current.data] + _to_list(current.succ)      # add current data and recursively add the rest to the list
            return [current.data]                                   
        
        return _to_list(self.first)


    def remove_all(self, x):

        def _remove_all(prev, current, x):
            if not current:                         # Base case: reached the end of the list
                return 0
            if current.data == x:                               # If current node has the value x
                if current.succ:                                # and it's not the last node:
                    current.data = current.succ.data            # replace current with successor's data
                    current.succ = current.succ.succ            # replace current pointer to skip the successor
                    return 1 + _remove_all(prev, current, x)    # Continue with current (previously successor!)
                else:                                           # If it's the last node
                    if prev:                                    # If there's a previous node, set its successor to None
                        prev.succ = None
                    else:                                       # If this is the only node in the list, set the list to empty
                        self.first = None
                    return 1                                    # end case, last node removed
            return _remove_all(current, current.succ, x)        # Move to the next node in the list

        return _remove_all(None, self.first, x)

    def __str__(self):            
        str = ''
        for data in self:                   # iterate through the LinkedList retrieving data from each node.
            str += f'{data}, '
        return '(' + str[:-2] + ')'         # slice last two chars from string, the last unnecessary blank and comma.
     
    def copy(self):               
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    
    ''' Complexity for this implementation: 

    line 1: complexity O(1)
    line 2: complexity O(n)
    Line 3: complexity O(n) 
    for a total complexity of O(n^2)
    answer: O(n^2)
    '''
     
    def copy(self):             
        new_list = LinkedList()
        if self.first is None:
            return new_list                       # if input is an empty list, returns empty list
        prev = None
        for data in self:                       # iterate through node data with generator
            new_node = new_list.Node(data, None)       # new node
            if prev is None:                    # if no previous, the new node is first
                new_list.first = new_node
            else:                               # otherwise pointer to new node is assigned
                prev.succ = new_node
            prev = new_node
        return new_list
    
    ''' Complexity for this implementation:
    
    In this improved copy method, the sorting functionality from the insert method is removed,
    which decreases the complexity by O(n) to O(n).
    answer: O(n)
    '''

def main():
    lst = LinkedList()
    for x in [1, 1, 3, 7, 9, 2, 8]:
        lst.insert(x)
    lst.print()

if __name__ == '__main__':
    main()