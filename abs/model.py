from db.sqlite_db import SQLITE_DB
from config import config

class Model:

  con = SQLITE_DB({
    "path": config.database_path
  })

  @property
  def table_name(self) -> str:
    raise NotImplementedError

  @property
  def pk(self) -> str:
    raise NotImplementedError
  
  @property
  def columes(self) -> list:
    raise NotImplementedError

  @classmethod
  def create_table(cls):
    return cls.con.create_table(cls.table_name, cls.columes)

  @classmethod
  def delete_table(cls):
    return cls.con.delete_table(cls.table_name)

  @classmethod
  def delete_data(cls, where : str = ''):
    return cls.con.delete_data(cls.table_name, where)

  @classmethod
  def add_data(cls, data : dict):
    return cls.con.add_data(cls.table_name, data)

  @classmethod
  def update_data(cls, data : dict, pk_val : str):
    return cls.con.update_data(cls.table_name, data, cls.pk, pk_val)

  @classmethod
  def get_data(cls, where : str = '', limit : int = 0):
    return cls.con.get_data(cls.table_name, where, limit)

  @classmethod
  def get_last_pk(cls):
    try:
      return cls.con.get_data(cls.table_name, '', '1', f'ORDER BY "{ cls.pk }" DESC')[0][cls.pk]
    except:
      return False

  @classmethod
  def get_data_by_pk(cls, pk_val : int):
    return cls.con.get_data_one(
      cls.table_name,
      f'"{ cls.pk }" = { str(pk_val) }'
    )
  
  @classmethod
  def get_data_one(cls, where : str):
    return cls.con.get_data_one(cls.table_name, where)
  
