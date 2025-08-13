class Member:
    def __init__(self,name, member_id, ):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
     
    def max_books(self):
        return 0
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books():
            return f'{self.name} หมดสิทธิ์แล้ว'
        
        if not book.available:
            return f'{book.title} หนังสือไม่ว่างแล้ว'
    
        self.borrowed_books.append(book)
        book.available = False
        return f'{self.name} ยังเหลือๆยืมได้ไอน้องง {book.title} สำเร็จแล้วรีบเอามาคืน'
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            return f'{self.name} คืนหนังสือ {book.title} สำเร็จแล้ว'
        return f'{self.name} ไม่มีได้ยืมหนังสือ {book.title} มึงหลอนอะไร'
        

class Student(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
    
    def max_books(self):
        return 3
class Teacher(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
    
    def max_books(self):
        return 5    