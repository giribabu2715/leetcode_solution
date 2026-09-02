import random

class RandomizedSet:

    def __init__(self):
        self.vals = []          
        self.idx  = {}          

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        last_val = self.vals[-1]
        pos = self.idx[val]
        self.vals[pos] = last_val
        self.idx[last_val] = pos
        self.vals.pop()
        del self.idx[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.vals)