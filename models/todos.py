from abs.model import Model
from config import hex

class TodosModel(Model):
  table_name = f'{hex.hex_tables}_todo'
  pk = 'todo_id'
  columes = [
    {
      'n': 'todo_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'todo',
      't': 'TEXT',
      'l': False
    },
    {
      'n': 'user_id',
      't': 'INTEGER',
      'l': False
    },
  ]

  