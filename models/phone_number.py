from abs.model import Model
from config.hex import hex_tables

class PhoneNumberModel(Model):
        table_name = f'{hex_tables}_phone_number'
        pk = 'phone_id'
        columes = [
        {
            'n': 'phone_id',
            't': 'INTEGER',
            'l': False,
            'pk': True,
            'au': True
        },
        {
            'n': 'phone_number',
            't': 'INTEGER',
            'l': False
        },
          {
            'n': 'country_code',
            't': 'INTEGER',
            'l': False
        },
          {
            'n': 'phone_type',
            't': 'INTEGER',
            'l': False
        },
        {
            'n': 'user_id',
            't': 'INTEGER',
            'l': False,
            'pk': True,
            'au': True
         }        
    ]