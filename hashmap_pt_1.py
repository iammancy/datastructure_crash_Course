## hashmap

class hashmap1:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self,key):
        key_sum = 0
        for char in key:
            key_sum += ord(char)
        print(key_sum)
        return key_sum % 100
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self, key,val):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None



if __name__ == "__main__":
    t =  hashmap1()
    ##print(t.get_hash(' '))
    t.add("mancy", 30)
    print(t.arr)
    t['pet'] = 'rabbit'

   
    print("before deleting")
    print(t.arr)
    del t['pet']
    print("\nafter deleting\n")
    print(t.arr)