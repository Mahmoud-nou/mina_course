from abs.model import Model

class SiteWordsModel(Model):
  table_name = 'site_words'
  pk = 'word_id'
  columes = [
    {
      'n': 'word_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'word_key',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'word',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'lang_id',
      't': 'INTEGER',
      'l': False,
      'pk': False,
      'au': False
    },
  ]

  @classmethod
  def get_by_key(cls, key : str, lang: int):
    try:
        return cls.get_data_one(
            f'"word_key" = "{key}" AND "lang_id" = {str(lang)}'
        )['word']
    except:
        return False

  