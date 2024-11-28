# Site
from models.langs import LangsModel
from models.site_words import SiteWordsModel

# Todos
from models.todos import TodosModel

# Users
from models.users import UsersModel
from models.profile import UserProfileModel

print('=' * 30)
print(' ')

table = 'Langs'
print(f'Delete Table { table } is: '+ str(LangsModel.delete_table()))
print(f'Create Table { table } is: '+ str(LangsModel.create_table()))


print(' ')
print(f'Add data to Table { table } is: ', end='')

data = ''

data += str(LangsModel.add_data({
  'lang_name': 'Arabic',
  'lang_short': 'AR'
})) + ', '

data += str(LangsModel.add_data({
  'lang_name': 'English',
  'lang_short': 'EN'
})) + ', '

print(data[:-2])

print(' ')
print('=' * 30)
print(' ')

table = 'Site Word'
print(f'Delete Table { table } is: '+ str(SiteWordsModel.delete_table()))
print(f'Create Table { table } is: '+ str(SiteWordsModel.create_table()))


print(' ')
print(f'Add data to Table { table } is: ', end='')

data = ''

list_data = [
  # Arabic
  {'word_key': 'id', 'word': 'م', 'lang_id': 1},
  {'word_key': 'val', 'word': 'بيان', 'lang_id': 1},
  {'word_key': 'btns', 'word': 'ازرار', 'lang_id': 1},
  # English
  {'word_key': 'id', 'word': 'id', 'lang_id': 2},
  {'word_key': 'val', 'word': 'value', 'lang_id': 2},
  {'word_key': 'btns', 'word': 'btns', 'lang_id': 2},
]

for n in list_data:
  data += str(SiteWordsModel.add_data(n)) + ', '

print(data[:-2])


print(' ')
print('=' * 30)
print(' ')

table = 'Todos'
print(f'Delete Table { table } is: '+ str(TodosModel.delete_table()))
print(f'Create Table { table } is: '+ str(TodosModel.create_table()))

print(' ')
print('=' * 30)
print(' ')

table = 'Users'
print(f'Delete Table { table } is: '+ str(UsersModel.delete_table()))
print(f'Create Table { table } is: '+ str(UsersModel.create_table()))

print(' ')
print('=' * 30)
print(' ')

table = 'User Profile'
print(f'Delete Table { table } is: '+ str(UserProfileModel.delete_table()))
print(f'Create Table { table } is: '+ str(UserProfileModel.create_table()))

print(' ')
print('=' * 30)

