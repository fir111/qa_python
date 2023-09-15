# qa_python

### Тесты конструктора

`test_initialize_books_rating_as_dict` - проверка инициализации словаря, в который будут добавляться книги

`test_initialize_favorites_as_list` - проверка инициализации списка книг-фаворитов


### Тесты `add_new_book(self, name)`

`test_add_new_book_add_book_book_in_books_rating` - проверка добавления книги в словарь

`test_add_new_book_add_book_book_in_books_rating_equal_1` - проверка рейтинга добавленной книги, должен быть равен 1

`test_add_new_book_add_duplicate_book_book_not_in_books_rating` - проверка невозможности повторного добавления книги в словарь книг


### Тесты `set_book_rating(self, name, rating)`

`test_set_book_rating_rating_in_range_1_10_is_equal` - проверка установки рейтинга в интервале [1,10]

`test_set_rating_rating_less_1_not_set` - проверка невозможности установить рейтинг < 1 

При попытке установить рейтинг < 1 он остается прежним (не сбрасывается до умолчания)

`test_set_rating_rating_greater_10_not_set` - проверка невозможности установить рейтинг > 10
При попытке установить рейтинг > 10 он остается прежним (не сбрасывается до умолчания)

`test_set_rating_rating_10_set` - проверка установки рейтинга равного 10

`test_set_rating_book_not_added_in_books_rating_not_in_book_rating` - проверка того, что установка рейтинга не добавляет книгу в словарь

`test_set_rating_book_is_not_in_books_rating_not_set` -  проверка, что для книги, которую не добавляли в словарь, нельзя получить рейтинг


### Тесты `get_book_rating(self, name)`

`test_get_book_rating_existing_book_is_equal` -  проверка корректности получения рейтинга книги, добавленной в словарь, в случае, когда был проставлен валидный рейтинг

`test_get_book_rating_not_existing_book_is_none` - проверка несуществования результата для книги не из словаря


### Тесты `get_books_with_specific_rating(self, rating)`

`test_get_books_with_specific_rating_rating_in_range_1_10_is_equal_expected` - проверка получения списка книг с валидным рейтингом (из интервала [1-10])

`test_get_books_with_specific_rating_not_existing_rating_is_empty` - проверка получения пустого списка, если книги с указанным рейтингом нет в словаре

`test_get_books_with_specific_rating_rating_equal_10_is_equal_expected` - проверка получения списка книг с рейтингом 10


### Тесты `get_books_rating(self)`

`test_get_books_rating_not_add_books_is_empty` - проверка пустоты результата в случае, когда книги не добавляли

`test_get_books_rating_ratings_are_equal` - проверка совпадения результата с добавленными книгами


### Тесты `add_book_in_favorites(self, name)`

`test_add_book_in_favorites_existing_book_in_favorites` - проверка добавления книги из словаря в фавориты

`test_add_book_in_favorites_not_existing_book_not_in_favorites` - проверка того, что книга не из словаря не попадает в фавориты


### Тесты `get_list_of_favorites_books(self)`

`test_get_list_of_favorites_books_add_books_in_favorites_is_equal` - проверка, что все добавленные в фавориты книги, действительно туда добавляются

`test_get_list_of_favorites_books_not_add_book_in_favorites_is_empty` - проверка, что если книгу не добавлять в фавориты, ее там не будет


### Тесты `delete_book_from_favorites(self, name)`
###
`test_delete_book_from_favorites_deleted_book_is_not_in_favorites` - проверка того, что добавленная в фавориты книга удаляется из списка
