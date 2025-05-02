class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

book1 = Book("Author A", "Book A", 100)
book2 = Book("Author B", "Book B", 200)
book3 = Book("Author C", "Book C", 300)

print(book1.get_title(), book1.get_author(), book1.get_price())
print(book2.get_title(), book2.get_author(), book2.get_price())
print(book3.get_title(), book3.get_author(), book3.get_price())
