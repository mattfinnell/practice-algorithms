import math
import sys

def heapsort(arr):
    min_heap = MinHeap(arr)
    return [min_heap.pop() for _ in arr]

class MinHeap(object):
    MAXINT = sys.maxsize

    def __init__(self, arr=None):
        self._arr = []
        self.size = 0

        if arr:
            for item in arr:
                self.push(item)

    def push(self, item):
        self._arr.append(item)
        self.size += 1

        current_index = len(self._arr) - 1
        parent_index = self._parent_index(current_index)

        while parent_index > -1 and self._arr[parent_index] > self._arr[current_index]:
            self._arr[current_index], self._arr[parent_index] = self._arr[parent_index], self._arr[current_index]

            current_index = parent_index
            parent_index = self._parent_index(current_index)
    
    def pop(self):
        if self.size > 0:
            return_value = self._arr[0] 
            self.size -= 1

            self._arr[0] = self._arr[-1]

            self._arr = self._arr[:-1]

            current_index = 0

            min_child_index = self._min_child_index(current_index)

            while min_child_index < self.size and self._arr[min_child_index] < self._arr[current_index]:
                self._arr[min_child_index], self._arr[current_index] = self._arr[current_index], self._arr[min_child_index]

                current_index = min_child_index
                min_child_index = self._min_child_index(current_index)
            
            return return_value

        return None

    def _parent_index(self, current):
        return math.floor((1 + current) / 2) - 1
    
    def _min_child_index(self, current):
        left = self._left_child_index(current)
        right = self._right_child_index(current)

        # both are less than size
        if left < self.size and right < self.size:
            return left if self._arr[left] < self._arr[right] else right

        # left is less than size
        if left < self.size and right >= self.size:
            return left

        # right is less than size
        if right < self.size and left >= self.size:
            return right 
        
        # neither are less than size
        return self.MAXINT 

    def _left_child_index(self, current):
        return ((current + 1) * 2) - 1

    def _right_child_index(self, current):
        return self._left_child_index(current) + 1