from main import BooksCollector
from random import randint

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_initialize_books_rating_as_dict(self):
        collector = BooksCollector()
        books_rating_dict = collector.get_books_rating()
        assert isinstance(books_rating_dict, dict) and not books_rating_dict

    def test_initialize_favorites_as_list(self):
        collector = BooksCollector()
        favorites_list = collector.get_list_of_favorites_books()
        assert isinstance(favorites_list, list) and not favorites_list

    def test_add_new_book_add_book_book_in_books_rating(self):
        collection = BooksCollector()
        book = 'New Book'
        collection.add_new_book(book)
        collected_books = collection.get_books_rating()
        assert collected_books and book in collected_books

    def test_add_new_book_add_book_book_in_books_rating_equal_1(self):
        collection = BooksCollector()
        book = 'New Book'
        collection.add_new_book(book)
        actual_rating = collection.get_book_rating(book)
        assert actual_rating == 1

    def test_add_new_book_add_duplicate_book_book_not_in_books_rating(self):
        collection = BooksCollector()
        book = 'New Book'
        collection.add_new_book(book)
        new_rating = randint(1,10)
        collection.set_book_rating(book, new_rating)
        collection.add_new_book(book)
        actual_books = collection.get_books_rating()
        actual_rating = collection.get_book_rating(book)  # рейтинг должен установиться 1, если книга перезаписалась
        assert len(actual_books) == 1 and actual_rating == new_rating

    def test_set_book_rating_rating_in_range_1_10_is_equal(self):
        collection = BooksCollector()
        book = 'New Book'
        new_rating = randint(1, 10)
        collection.add_new_book(book)
        collection.set_book_rating(book,new_rating)
        actual_rating = collection.get_book_rating(book)
        assert actual_rating == new_rating

    def test_set_rating_rating_less_1_not_set(self):
        collection = BooksCollector()
        book = 'New Book'
        new_rating = randint(1, 10)
        collection.add_new_book(book)
        collection.set_book_rating(book,new_rating)
        collection.set_book_rating(book, 0)
        actual_rating = collection.get_book_rating(book)
        assert actual_rating != 0 and actual_rating == new_rating

    def test_set_rating_rating_greater_10_not_set(self):
        collection = BooksCollector()
        book = 'New Book'
        new_rating = randint(1,10)
        collection.add_new_book(book)
        collection.set_book_rating(book,new_rating)
        collection.set_book_rating(book, 11)
        actual_rating = collection.get_book_rating(book)
        assert actual_rating != 11 and actual_rating == new_rating

    def test_set_rating_rating_10_set(self):
        collection = BooksCollector()
        book = 'New Book'
        new_rating = 10
        collection.add_new_book(book)
        collection.set_book_rating(book,new_rating)
        actual_rating = collection.get_book_rating(book)
        assert actual_rating == new_rating

    def test_set_rating_book_not_added_in_books_rating_not_in_book_rating(self):
        collection = BooksCollector()
        not_book = 'Not existing book'
        collection.set_book_rating(not_book, randint(1, 10))
        collected_books = collection.get_books_rating()
        assert not_book not in collected_books

    def test_set_rating_book_is_not_in_books_rating_not_set(self):
        collection = BooksCollector()
        not_book = 'Not existing book'
        collection.set_book_rating(not_book, randint(1, 10))
        assert collection.get_book_rating(not_book) is None

    def test_get_book_rating_existing_book_is_equal(self):
        collector = BooksCollector()
        existing_book = 'book'
        new_rating = randint(1, 10)
        collector.add_new_book(existing_book)
        collector.set_book_rating(existing_book, new_rating)
        assert collector.get_book_rating(existing_book) == new_rating

    def test_get_book_rating_not_existing_book_is_none(self):
        collector = BooksCollector()
        existing_book = 'book'
        rating = randint(1, 10)
        collector.add_new_book(existing_book)
        collector.set_book_rating(existing_book, rating)
        actual_book = 'not book'
        assert collector.get_book_rating(actual_book) is None

    def test_get_books_with_specific_rating_rating_in_range_1_10_is_equal_expected(self):
        collection = BooksCollector()
        books = {'book1': 1, 'book2': 2, 'book2_2': 2, 'book3': 3}
        for book in books:
            collection.add_new_book(book)
        for book, rating in books.items():
            collection.set_book_rating(book,rating)
        specific_rating = 2
        expected_books = [book for book in books if books[book] == specific_rating]
        assert collection.get_books_with_specific_rating(specific_rating) == expected_books

    def test_get_books_with_specific_rating_not_existing_rating_is_empty(self):
        collection = BooksCollector()
        books = {'book1': 1, 'book2': 2, 'book3': 3}
        for book in books:
            collection.add_new_book(book)
        for book, rating in books.items():
            collection.set_book_rating(book,rating)
        specific_rating = 10
        assert not collection.get_books_with_specific_rating(specific_rating)

    def test_get_books_with_specific_rating_rating_equal_10_is_equal_expected(self):
        collection = BooksCollector()
        books = {'book1': 1, 'book2': 2, 'book3': 10, 'book3_2': 10}
        for book in books:
            collection.add_new_book(book)
        for book, rating in books.items():
            collection.set_book_rating(book,rating)
        specific_rating = 10
        expected_books = [book for book in books if books[book] == specific_rating]
        assert collection.get_books_with_specific_rating(specific_rating) == expected_books

    def test_get_books_rating_not_add_books_is_empty(self):
        collection = BooksCollector()
        assert not collection.get_books_rating()

    def test_get_books_rating_ratings_are_equal(self):
        collection = BooksCollector()
        books = {'book1': 1, 'book2': 2, 'book3': 10}
        for book in books:
            collection.add_new_book(book)
        for book, rating in books.items():
            collection.set_book_rating(book,rating)
        assert collection.get_books_rating() == books

    def test_add_book_in_favorites_existing_book_in_favorites(self):
        collection = BooksCollector()
        books = ['book1', 'book2', 'book3']
        for book in books:
            collection.add_new_book(book)
        expected_favorites = ['book1', 'book3']
        collection.add_book_in_favorites('book1')
        collection.add_book_in_favorites('book3')
        assert collection.get_list_of_favorites_books() == expected_favorites

    def test_add_book_in_favorites_not_existing_book_not_in_favorites(self):
        collection = BooksCollector()
        books = ['book1', 'book2', 'book3']
        for book in books:
            collection.add_new_book(book)
        not_existing_book = 'book5'
        existing_book = 'book1'
        collection.add_book_in_favorites(not_existing_book)
        collection.add_book_in_favorites(existing_book)
        assert not_existing_book not in collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_books_in_favorites_is_equal(self):
        collection = BooksCollector()
        books = ['book1', 'book2', 'book3']
        for book in books:
            collection.add_new_book(book)
        for book in books:
            collection.add_book_in_favorites(book)
        assert collection.get_list_of_favorites_books() == books

    def test_get_list_of_favorites_books_not_add_book_in_favorites_is_empty(self):
        collection = BooksCollector()
        book = 'book1'
        collection.add_new_book(book)
        assert book not in collection.get_list_of_favorites_books()

    def test_delete_book_from_favorites_deleted_book_is_not_in_favorites(self):
        collection = BooksCollector()
        books = ['book1', 'book2', 'book3', 'book0']
        for book in books:
            collection.add_new_book(book)
        favorites = ['book1', 'book3', 'book0']
        for book in favorites:
            collection.add_book_in_favorites(book)
        expected_favorites = ['book1', 'book3']
        collection.delete_book_from_favorites('book0')
        assert collection.get_list_of_favorites_books() == expected_favorites





