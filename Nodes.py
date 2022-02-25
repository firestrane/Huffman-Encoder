
class node:
    def __init__(self, l, r):
        self.value = l.value + r.value
        self.leftNode = l
        self.rightNode = r
        self.parentNode = None
        self.path = ''

class endNode:
    def __init__(self, tup):
        self.value = tup[1]
        self.char = tup[0]
        self.parentNode = None
        self.path = ''