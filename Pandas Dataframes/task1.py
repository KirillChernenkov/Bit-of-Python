import pandas as pd

authors = pd.DataFrame()
authors_id = [1, 2, 3]
authors_name = ['Тургенев', 'Чехов', 'Островский']
authors['Author_id'] = authors_id
authors['Author_name'] = authors_name

book = pd.DataFrame()
author_id = [1, 1, 1, 2, 2, 3, 3]
book_title = ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники']
price = [450, 300, 350, 500, 450, 370, 290]

book['author_id'] = author_id
book['book_title'] = book_title
book['price'] = price

print(authors)
print(book)