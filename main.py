import pandas as pd
import numpy as np

df_member_sheet = pd.read_excel('Book Club.xlsx', sheet_name=1)

book1 = df_member_sheet['Book 1']
book2 = df_member_sheet['Book 2']

book_list = np.concatenate((book1, book2))
book_of_the_month = np.random.choice(book_list)
print(book_of_the_month)

# Writing this book name into the excel file
# df_book_sheet = pd.read_excel('Book Club.xlsx', sheet_name=0)
# print(df_book_sheet)
# botm_col = df_book_sheet['Book Of The Month']
# append val to botm_col
# df_book_sheet.to_excel()