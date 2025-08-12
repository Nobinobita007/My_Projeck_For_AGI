class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year   = year
        self.available = True

    def get_info(self):
       return f'Book: {self.title}, {self.author}, {self.year}, {self.available}'

class Ebook(Book):
    def __init__(self, title, author, year, size):
        super().__init__(title, author, year )
        self.size = size
    
    def get_info(self):
        return f'{super().get_info()}, size: {self.size}MB'

class PrintedBook(Book):
    def __init__(self, title, author, year, color):
        super().__init__(title, author, year)
        self.color = color
    
    def get_info(self):
        return f'{super().get_info()}, color: {self.color}'
    

    