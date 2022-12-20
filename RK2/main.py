from operator import itemgetter


class Chapter:  # класс Глава

    def __init__(self, id, name, page, book_id):
        self.id = id  # номер главы
        self.name = name  # название главы
        self.page = page  # страница на которой находится глава
        self.book_id = book_id  # номер книги


class Book:  # класс книга

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ChapterBook:
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id


books = [
    Book(1, 'Сочинения Джека Лондона'),
    Book(2, 'Введение в анализ'),
    Book(3, 'Изучаем С++ через программирование игр'),
    Book(4, 'Спутник работника света'),
    Book(5, 'Механика: основные законы')
]
chapters = [
    Chapter(1, 'Белое Безмолвие', 19, 1),
    Chapter(2, 'Сын Волка', 29, 1),
    Chapter(3, 'Ату их, ату!', 322, 1),
    Chapter(4, 'Элементы теории множеств', 41, 2),
    Chapter(5, 'Отображение множеств', 70, 2),
    Chapter(6, 'Воплощение, или инкарнация', 60, 4)
]
chapters_of_books = [
    ChapterBook(1, 1),
    ChapterBook(1, 2),
    ChapterBook(1, 3),
    ChapterBook(2, 4),
    ChapterBook(2, 5),
    ChapterBook(4, 6),
]


def b1(one_to_many):

    res_11 = {}
    for ch in chapters:
        if ch.name[0] == 'А':
            ch_books = list(filter(lambda i: i[0] == ch.name, one_to_many))
            ch_books_names = ch_books[0][2]
            res_11[ch.name] = ch_books_names
    return res_11


def b2(one_to_many):

    res_12_unsorted = []

    for book in books:
        book_ch = list(filter(lambda i: i[2] == book.name, one_to_many))
        if len(book_ch) > 0:
            book_pages = [page for _, page, _ in book_ch]
            min_pages = sorted(book_pages)
            res_12_unsorted.append((book.name, min_pages[0]))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)

    return res_12


def b3(many_to_many):

    res_13 = sorted(many_to_many, key=itemgetter(0))
    return res_13


one_to_many = [(ch.name, ch.page, book.name)
                   for book in books
                   for ch in chapters
                   if ch.book_id == book.id]

many_to_many_temp = [(book.name, ChOfBooks.book_id, ChOfBooks.chapter_id)
                         for book in books
                         for ChOfBooks in chapters_of_books
                         if book.id == ChOfBooks.book_id]

many_to_many = [(ch.name, ch.page, book_name)
                    for book_name, book_id, ch_id in many_to_many_temp
                    for ch in chapters if ch.id == ch_id]

def main():

    print('B1')
    print(b1(one_to_many))
    print('B2')
    print(b2(one_to_many))
    print('B3')
    print(b3(many_to_many))

if __name__ == '__main__':
    main()
