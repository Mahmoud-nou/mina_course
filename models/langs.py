from abs.model import Model

class LangsModel(Model):
  table_name = 'langs'
  pk = 'lang_id'
  columes = [
    {
      'n': 'lang_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'lang_name',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'lang_short',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
  ]

  