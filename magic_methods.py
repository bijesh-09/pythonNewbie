class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages in total for '{self.title}' and '{other.title}'"
    
    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return f"{self.num_pages} pages of the book '{self.title}'"
        # raise KeyError("Key not found")
        else:
            return f"Key '{key}' not found"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)
book4 = Book("1984", "George Orwell", 172)

print(book1)
print(book3 == book4)

print(book3 < book4)
print(book3.__lt__(book4)) #equivalent to print(book3 < book4)

print(book3 > book4)

print(book1 + book2)

print(book1.__contains__("Gatsby"))
print("Kill" not in book2) #equivalent to print(book2.__contains__("kill"))

print(book1['num_pages'])