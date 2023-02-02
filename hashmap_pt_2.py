class hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        count = 0
        for char in key:
            count += ord(char)
        
        return count % 100
    
    def __setitem__(self, key,val):
        h = self.get_hash(key)
        found = False
        print(len(self.arr[h]))
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if(len(element) == 2 and element[0] == key):
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                del self.arr[h][idx]



if __name__ == '__main__':
    hm = hashmap()
    hm['mancy'] = 'rabbit'
    hm['lancz'] = 'pear'


    print(hm.arr)
    print(hm['mancy'])
    del hm['mancy']
    print("after deleting")

    print(hm.arr)
