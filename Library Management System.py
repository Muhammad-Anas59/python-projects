class Library:
    no_of_books=0
    books=[]
    def __init__(self,no_of_books,books):
        self.no_of_books=no_of_books
        self.books=books
        if self.no_of_books==len(self.books):
            print("NUmber of books is equal to the length of books :")
        else:
            print("Not equal :")
    def show(self):
        print("The books are:")
        for book in books:
            print(book)
    def add(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
    def getnum(self):
        return self.no_of_books
books=["Math","English","Urdu","Ideology"]
lib1=Library(4,books)
lib1.show()
print("The number of books are:",lib1.getnum())
lib1.add("History")
lib1.show()
print("Updated number of books are :",lib1.getnum())
        
        
        
        
    