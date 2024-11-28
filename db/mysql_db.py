class MYSQL_DB:
  def __init__(self):
    pass

  def create_table(self, table_name : str, columes : list ):
    sql = f'CREATE TABLE "{ table_name }" ('
    for colume in columes:
      sql += f'"{columes["n"]}" {columes["t"]}'
      sql += f' NULL' if columes["l"] == True else ' NOT NULL'
      sql += f' PRIMARY KEY' if columes["pk"] else ''
      sql += f' AUTOINCREMENT' if columes["au"] else ''
      sql += ', '
    sql = sql[:-2]
    sql += ')'

    return self.__cur.execute(sql) 







