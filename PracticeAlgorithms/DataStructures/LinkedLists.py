import copy 


class SinglyLinkedNode(object):
    def __init__(self, data):
        self.Data = data
        self.Next = None

    def as_string(self):
        if self.Next:
            return self.Data + ", " + self.Next.as_string()

        return self.Data


class SinglyLinkedList(object):
    def __init__(self):
        self._head = None

    def as_list(self):
        if not self._head:
            return []

        return list(self._as_list(self._head))

    def _as_list(self, node):
        while node:
            yield node.Data
            node = node.Next
    
    def as_string(self):
        if not self._head:
            return "<empty>"

        return self._head.as_string()

    def append(self, data):
        if not self._head:
            self._head = SinglyLinkedNode(data)
        
        else:
            self._append(self._head, data)
    
    def _append(self, node, data): 
        if not node.Next:
            node.Next = SinglyLinkedNode(data)
        
        else:
            self._append(node.Next, data)
    
    def length(self):
        return self._length(self._head)
    
    def _length(self, node, count=0):
        if not node:
            return count

        return self._length(node.Next, count + 1)

    def insert_at_index(self, index, data):
        if self._head is None:
            self._head = SinglyLinkedNode(data)
        else :
            self._insert_at_index(self._head, index, data)

    def _insert_at_index(self, node, index, data):
        # Base Case 
        if index == 0:
            node.Next = copy.deepcopy(node) 
            node.Data = data

        # Recursively Iterate
        if index > 0 and node.Next:
            self._insert_at_index(node.Next, index - 1, data)

        if not node.Next:
            node.Next = SinglyLinkedNode(data)
    
    def search(self, key):
        if not self._head:
            return -1
        
        return self._search(self._head, key)

    def _search(self, node, key, index=0):
        if not node:
            return -1

        if node.Data == key:
            return index

        return self._search(node.Next, key, index + 1)

    def delete_by_index(self, index):
        if self._head: 
            if index > 0 :
                self._delete_by_index(None, self._head, index)
            else :
                self._head = self._head.Next
    
    def _delete_by_index(self, previous_node, current_node, index):
        # recursively search
        if index > 0 and current_node.Next:
            self._delete_by_index(current_node, current_node.Next, index - 1)
        
        if index == 0:
            previous_node.Next = current_node.Next
    
    def delete_by_key(self, key):
        if self._head:
            if self._head.Data == key:
                self._head = self._head.Next
            
            else:
                self._delete_by_key(None, self._head, key)
    
    def _delete_by_key(self, previous_node, current_node, key):
        if current_node:
            if current_node.Data == key:
                previous_node.Next = current_node.Next
            
            else : 
                self._delete_by_key(current_node, current_node.Next, key)