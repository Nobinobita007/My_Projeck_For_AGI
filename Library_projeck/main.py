from book import Book, Ebook, PrintedBook
from member import Student, Teacher
from library import Library

def main():
    lib = Library()  

    # เพิ่มหนังสือ
    lib.add_book(Ebook("Python 101", "Alice", 2020, 5))
    lib.add_book(PrintedBook("AI Basics", "Bob", 2021, "Full Color"))
    lib.add_book(Book("Learning Python", "Mark Lutz", 2013))

    # เพิ่มสมาชิก
    lib.add_member(Student("Nova", "S001"))
    lib.add_member(Teacher("Bom", "T001"))

    # ยืมหนังสือ
    print(lib.borrow_book("S001", "Python 101"))
    print(lib.borrow_book("T001", "AI Basics"))

    hits = lib.search_books("python")
    if isinstance(hits, list):
        for h in hits:
            print(h)          
    else:
        print(hits)

    # คืนหนังสือ
    print(lib.return_book("S001", "Python 101"))

    # ยืมใหม่หลังคืน
    print(lib.borrow_book("S001", "Python 101"))

if __name__ == "__main__":
    main()
