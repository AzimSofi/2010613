class HashTable:
    # INIITIAL THE HASHTABLE
    def __init__(self,size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def __setitem__(self,key,value): # used to set H[key_a] = item_a
        self.put(key,value)

    def __getitem__(self,key): # used to grab item H[key_a]
        return self.get(key)

    # HASHING FUNCTIONS
    def hash(self,key):
        return key % self.size

    # Linear rehash
    def rehash(self,key):
        return (key + 1) % self.size

    # GET THE DATA USING THE KEY
    def get(self,key):
        index = self.hash(key)

        # IF THE KEY IS FOUND IMMEDIATELY
        if self.keys[index] == key:
            return self.values[index]
        else:
            # GOING THROUGH THE TABLE TO FIND THE KEY
            oghash = index
            index = self.rehash(index)
            while index is not oghash:
                if self.keys[index] == key:
                    return self.values[index]
                else:
                    return None

    # PUT THE ITEM INTO THE HASH TABLE
    def put(self,key,value):
        index = self.hash(key)

        # IF THE INDEX POSITION HAS NO KEY OR THE SAME KEY REQUESTED
        if self.keys[index] is None or self.keys[index] is key:
            self.keys[index] = key
            self.values[index] = value
            return
        else:
            # GOING THROUGH THE TABLE TO FIND THE EMPTY SPOT OR THE KEY
            oghash = index
            index = self.rehash(index)
            while index is not oghash:
                if self.keys[index] is None or self.keys[index] is key:
                    self.keys[index] = key
                    self.values[index] = value
                    return
                else:
                    index = self.rehash(index) # Keeps rehashing
            # IF THE TABLE IS ALREADY FULL
            print("The hash table is already full")

# Inherits Hashtable but with a different hash function (a=1, b=2, c=3, ..., z=26)
class HT(HashTable):
    def __init__(self, size = 5):
        super().__init__(size)
    
    def hash(self,key):
        if isinstance(key, str):
            # Mapping a=1, b=2, c=3 ...
            alphabet_dict = {chr(i + 97): i + 1 for i in range(26)}
            key = alphabet_dict[key[0].lower()]
            return key % self.size
        
        else:
            print("Key is not a string")
            return

    def delete(self,key):
        # index = 0
        for i in self.keys:
            if i == key:
                self[i] = None # Deletes value
                # self.keys[index] = None # Deletes key
                return
            # index += 1
        print("Key doesn't exist in the Hash table")        
        return

# Test
hash = HT()
hash['name'] = 'Zikri'
hash['age'] = 20
hash['gender'] = 'M'

print(hash['name'])
print(hash['age'])
print(hash['gender'])
print(hash.keys)
print(hash.values)

hash['birthdate'] = '4/12/2003'
print(hash.keys)
print(hash.values)

hash['name'] = 'Hakim'
print(hash['name'])

hash.delete('age')
print(hash.keys)
print(hash.values)
print(hash['age'])
print(hash['birthdate'])

# 
hash.delete('忘れる')
hash['age'] = 21
print(hash.keys)
print(hash.values)
