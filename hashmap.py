class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [[]]*size
    def put(self, key, value):
        #explanation:
        #get index
        index = hash(key) % self.size
        print(index)
        #add data to map
        self.map[index].append((key,value))
    def get(self, key):
        index = hash(key) % self.size
        smallerlist = self.map[index]
        if len(smallerlist)==1:
            return self.map[index][0]
        else:
            d = dict(self.map[index])
            print(d)
            try:
                return d[key]
            except KeyError:
                raise Exception("KEY NOT FOUND.")
                 
h = HashMap(10)
h.put('lol', '51')
h.put('lbl', '51')
print(h.get('lbl'))
        