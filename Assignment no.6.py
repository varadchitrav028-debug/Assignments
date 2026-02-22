class library:
    def __init__(self,book_name,author,available=True):
        self.book_name=book_name
        self.author=author
        self.available=available

    def check_out(self):
        if self.available:
            self.available=False
            print(f"'{self.book_name}'has been checkout.")
        else:
            print(f"sorry,'{self.book_name}'is not available.")

    def return_book(self):
        if not self.available:
            self.available=True
            print(f"'{self.book_name}'has been return and now available.")
        else:
            print(f"'{self.book_name}'was not checkout.")

    def display_info(self):
        status="Available" if self.available else "checkout"
        print(F"book:{self.book_name},author:{self.author},status:{status}")

#example usage
book1 = library("1984","george orwall") 
book2 = library("the wall","jk",available=False)

book1.display_info()
book2.display_info()

book1.check_out()
book1.display_info()

book1.return_book()
book1.display_info()

        