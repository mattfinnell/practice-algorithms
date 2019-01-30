"""
    I totally understand that this is identical to collections.defaultdict(int) 
    I'm simply doing this as an exercise to brush up on magic methods
"""
class FrequencyTable(object):
    def __init__(self, arr):
        self._table = {}

        for item in arr:
            if item not in self._table:
                self._table[item] = 1

            else:
                self._table[item] += 1
    
    def intersection(self, other):
        items = []
        for item in self._table:
            if item in other._table:
                k = min(self._table[item], other._table[item])

                items.extend((item for _ in range(k)))

        return FrequencyTable(items)
        
    def items(self):
        return self._table.items()
    
    def __getitem__(self, key):
        if key in self._table:
            return self._table[key]

    def __setitem__(self, key, value):
        if key not in self._table:
            self._table[key] = 1
        else :
            if value and type(value) == int and value > 0:
                self._table[key] += value
            else:
                self._table[key] += 1

    def __delitem__(self, key):
        if self._table[key] > 1:
            self._table[key] -= 1
        
        else:
            del self._table[key]

    def __iter__(self):
        return iter(self._table.keys())

    def __contains__(self, item):
        return item in self._table

    def __eq__(self, other):
        for key, value in self.items():
            if key not in other:
                return False
            
            if other[key] != value:
                return False
        
        return True