# qa_python

### Тесты конструктора

`test_initialize_books_rating_as_dict` - проверка инициализации словаря `self.books_rating`

`test_initialize_favorites_as_list` - проверка инициализации списка `self.favorites`


### Тесты `add_new_book(self, name)`

`test_add_new_book_add_book_book_in_books_rating` - проверка добавления книги в `self.books_rating`

`test_add_new_book_add_book_book_in_books_rating` - проверка рейтинга добавленной в `self.books_rating` книги

`test_add_new_book_add_duplicate_book_book_not_in_books_rating` - проверка невозможности повторного добавления книги в `self.books_rating`

`test_add_new_book_add_book_check_rating_equal_1` - проверка, что рейтинг добавленной книги равен 1


### Тесты `set_book_rating(self, name, rating)`

`test_set_book_rating_rating_in_range_1_10_check_equal}` - проверка установки рейтинга в интервале [1,10]

`test_set_rating_rating_less_1_not_set` - проверка невозможности установить рейтинг < 1

`test_set_rating_rating_greater_10_not_set` - проверка невозможности установить рейтинг > 10

`test_set_rating_rating_10_set` - проверка установки рейтинга равного 10

`test_set_rating_book_is_not_in_books_rating_not_set` - проверка установки валидного рейтинга для книги не из `self.books_rating`

`test_get_book_rating_existing_book_correct_rating` - проверка получения корректного рейтинга для добавленной в `self.books_rating` 

`test_set_rating_book_is_not_in_books_rating_not_set` - проверка несуществования рейтинга для недобавленной в `self.books_rating` книги 


### Тесты `get_book_rating(self, name)`

`test_get_book_rating_existing_book_is_equal` -  проверка корректности рейтинга книги, добавленной в `self.books_rating`

`test_get_book_rating_not_existing_book_is_none` - проверка несуществования результата для книги не из `self.books_rating`


### Тесты `get_books_with_specific_rating(self, rating)`

`test_get_books_with_specific_rating_rating_in_range_1_10_is_equal_expected` - проверка получения списка книг с валидным рейтингом (из интервала [1-10])

`test_get_books_with_specific_rating_not_existing_rating_is_empty` - проверка получения пустого списка, если книги с указанным рейтингом нет в `self.books_rating`

`test_get_books_with_specific_rating_rating_equal_10_is_equal_expected` - проверка получения списка книг с рейтингом 10


### Тесты `get_books_rating(self)`

`test_get_books_rating_not_add_books_is_empty` - проверка пустоты результата в случае, когда книги не добавляли

`test_get_books_rating_ratings_are_equal` - проверка совпадения результата с добавленными книгами


### Тесты `add_book_in_favorites(self, name)`

`test_add_book_in_favorites_existing_book_in_favorites` - проверка добавления книги из `self.books_rating` в `self.favorites`

`test_add_book_in_favorites_not_existing_book_not_in_favorites` - проверка того, что книга не из `self.books_rating` не попадает в `self.favorites`


### Тесты `get_list_of_favorites_books(self)`

`test_get_list_of_favorites_books_not_add_book_in_favorites_is_empty` - проверка, что если книгу не добавлять в `self.favorites`, ее там не будет


### Тесты `delete_book_from_favorites(self, name)`

`test_delete_book_from_favorites_deleted_book_is_not_in_favorites` - проверка того, что добавленная в `self.favorites` книга удаляется из списка