class Coffee:
    def init(self,size,price):
        self._size = size
        self.price = price
    def get_size(self):
        return self._size
    def set_size(self,value):
        if value != "Small" or value != "Medium" or value != "Large" :
            print("size must be Small, Medium, or Large") 
        else:
            self._size = value
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1 
    size = property(get_size,set_size)