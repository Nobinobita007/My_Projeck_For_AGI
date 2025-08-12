class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def borrow_book(self, member_id, title):
        for member in self.members:
            if member.member_id == member_id:
                book = self.find_book(title)
                if book:
                    return member.borrow_book(book)
                return f'ไม่พบหนังสือชื่อ {title} '
            return f'ไม่เจอสมาชิกมึงที่มี ID {member_id}'

    def return_book(self, member_id, title):
        for member in self.members:
            if member.member_id == member_id:
                book = self.find_book(title)
                if book:
                    return member.return_book(book)
                return f'มึงไม่ได้ยืมหนังสือ {title} '
        return f'มึงเป็นสมาชิกจริงปะเนี่ย '
       

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = []
        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book.get_info())

        
        if results:  # ถ้าเจออย่างน้อย 1 เล่ม
            return results
        
        else:
            return "ไม่มีหนังสือนี้ไปซื้อเอง"

