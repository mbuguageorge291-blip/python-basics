class Book:
    def __init__(self,title, author, isbn, price):
        self.title =title
        self.author =author
        self.isbn=isbn
        self.price=price
    def print_details(self):
        print("Title",self.title)
        print("Author",self.author)
        print("Price",self.price)

    def apply_discount(self,discount:{}):
        self.price =self.price * (1 - discount/100)
        print("New price is ", self.price)

b1=Book("Two rivers","Chinua Achebe","ISB001",700)
b2=Book("Think and Grow","John More","ISBN002",300)

b1.print_details()
b2.print_details()
b2.apply_discount(10)