from abs.model import Model
from config import hex

class UserProfileModel(Model):
    table_name = f'{hex.hex_tables}_user_profile'
    pk = 'user_id'
    columes = [
    {
        'n': 'user_id',
        't': 'INTEGER',
        'l': False,
        'pk': True,
        'au': True
    },
    {
        'n': 'first_name',
        't': 'TEXT',
        'l': False
    },
    {
        'n': 'last_name',
        't': 'TEXT',
        'l': False
    },
    {
        'n': 'gender',
        't': 'TEXT',
        'l': False
    },
    {
        'n': 'date_of_birth',
        't': 'TEXT',
        'l': False
    },
    {
        'n': 'profile_img',
        't': 'TEXT',
        'l': False
    }   
    ]