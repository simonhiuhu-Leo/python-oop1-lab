class Book:
    def init(self,title = None,page_count = 0) :
        self.title = title
        self._page_count = page_count

    def get_page_count(self):
        return self._page_count
    def set_page_count(self,value):
        if isinstance(value,int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    def turn_page(self) : 
        print("Flipping the page...wow, you read fast!")
    page_count = property(get_page_count,set_page_count)