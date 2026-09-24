#CERTIFICATION PROJECT 5: BUILD A HASH TABLE

class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self,key):
        code = 0 
        for char in key:
            code+=ord(char)
        return code
    def add(self,key,value):
        code = self.hash(key)
        if code in self.collection:
            self.collection[code][key] = value
        else:
            self.collection[code] = {key:value}
    def remove(self,key):
        code = self.hash(key)
        if code not in self.collection or key not in self.collection[code]:
            return
        self.collection[code].pop(key)
    def lookup(self,key):
        code = self.hash(key)
        if code not in self.collection:
            return None
        return self.collection[code].get(key,None)