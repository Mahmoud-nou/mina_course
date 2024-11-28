import sqlite3

class SQLITE_DB:
    def __init__(self, database : dict) -> None:
        self.__con = sqlite3.connect(
            database["path"],
            check_same_thread = False
        )
        self.__cur = self.__con.cursor()

    def table_exists(self, table_name : str) -> bool:
        sql = 'SELECT name FROM sqlite_master WHERE '
        sql += f'type="table" AND name="{ table_name }"'
        
        table_exists = self.__cur.execute(sql)
        tuple_data = table_exists.fetchone()

        if type(tuple_data) == tuple and table_name in tuple_data:
            return True
        return False

    def create_table(self, table_name : str, columes : list):
        try:
            # primary_key = False
            # auto_inc = False
            
            items = ["n", "t", "l"]
            for colume in columes:
                if type(colume) != dict:
                    for l in items:
                        if not l in colume:
                            return False

            sql = f'CREATE TABLE "{ table_name }" ('
            for colume in columes:
                sql += '"'+ colume["n"] +'" '+ colume["t"]
                sql += ' NULL' if colume["l"] else ' NOT NULL'
                sql += ' PRIMARY KEY' if 'pk' in colume and colume["pk"] else ''
                sql += ' AUTOINCREMENT' if 'au' in colume and colume["au"] else ''
                sql += ', '
                # if colume['pk']:
                #     primary_key = colume["n"]
                #     auto_inc = colume['au']

            # if type(primary_key) == str:
            #     sql += f' PRIMARY KEY("{ primary_key }"'
            #     if auto_inc:
            #         sql += ', AUTOINCREMENT'
            #     sql += '), '

            sql = sql[:-2]
            sql += ')'

            self.__cur.execute(sql)

            return self.table_exists(table_name)
        except:
            return 'This table is exists.'

    def delete_table(self, table_name : str):
        try:
            self.__cur.execute(f'DROP TABLE "{ table_name }"')
            if not self.table_exists(table_name):
                return True
            return False
        except:
            return 'This table isn\'t exists.'
    
    def delete_data(self, table_name : str, where : str = '') -> bool:
        if self.table_exists(table_name):
            sql = f'DELETE FROM "{ table_name }"'
            sql += f' WHERE { where }' if where != '' else ''
            self.__cur.execute(sql)
            self.__con.commit()

            try:
                if where == '':
                    sql_2 = 'DELETE FROM TABLE sqlite_sequence'
                    sql_2 += f' WHERE name = "{ table_name }"'
                    self.__cur.execute(sql_2)
                    self.__con.commit()
            except:
                pass
            return True
        return False

    def add_data(self, table_name : str, data : dict) -> bool:
        try:
            sql = f'INSERT INTO "{ table_name }" ('

            for colume in data:
                if type(data[colume]) == str or type(data[colume]) == int:
                    sql += '`'+ colume +'`, '
            sql = sql[:-2]

            sql += ') VALUES ('

            for colume in data:
                if type(data[colume]) == str:
                    sql += f"'{ data[colume] }', "
                elif type(data[colume]) == int:
                    sql += f'{ str(data[colume]) }, '
            sql = sql[:-2]
            
            sql += ')'

            self.__cur.execute(sql)
            self.__con.commit()
            
            return True
        except:
            return False
    
    def update_data(self, table_name : str, data : dict, pk : str, value_pk : str):
        try:
            sql = f'UPDATE "{table_name}" SET '
            for colume in data:
                if type(data[colume]) == str or type(data[colume]) == int:
                    sql += f'"{colume}" = ' 
                if type(data[colume]) == str :
                    sql+= f'"{data[colume]}", '
                else:
                    sql+= f'{data[colume]} , '
                        
            sql = sql[:-2]  
            sql += f' WHERE "{pk}" = '
            if type(value_pk) == str:
                sql += f'"{ value_pk }"'
            elif type(value_pk) == int:
                sql += f'{ str(value_pk) }'

            self.__cur.execute(sql)
            self.__con.commit()
            
            return True
        except:
            return False

    def get_data(self, table_name : str, where : str = '', limit : int = 0, order : str = ''):
        sql = f'SELECT * FROM "{ table_name }"'
        sql += f' { order }' if order != '' else ''
        sql += f' WHERE { where }' if where != '' else ''
        sql += f' LIMIT { str(limit) }' if limit != 0 else ''

        data = self.__cur.execute(sql)
        # return data.fetchall()
        # return data.description
        
        # [
        #     {
        #         'lang_id': 1,
        #         'lang_name': 'Arabic',
        #     },
        #     {
        #         'lang_id': 2,
        #         'lang_name': 'English',
        #     },
        # ]

        # Convert list of tuple to list of dict
        col_names = data.description
        list_of_data = []
        
        for d in data.fetchall():
            obj = {}
            # list_of_data = ind
            for ind, val in enumerate(d):
                obj[col_names[ind][0]] = val
            list_of_data.append(obj)

        return list_of_data

    def get_data_one(self, table_name : str, where : str):
        sql = f'SELECT * FROM "{ table_name }"'
        sql += f' WHERE { where }'

        data = self.__cur.execute(sql)
        # return data.fetchall()
        # return data.description
    
        # {
        #     'lang_id': 1,
        #     'lang_name': 'Arabic',
        # }

        # Convert tuple to dict
        col_names = data.description
        
        obj = {}
        for ind, val in enumerate(data.fetchone()):
            obj[col_names[ind][0]] = val

        return obj


  
