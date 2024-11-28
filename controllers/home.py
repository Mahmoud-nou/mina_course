from flask import Blueprint, render_template, abort, request

from config import vars

from lib.encrypt import DataEncrypt

from models.langs import LangsModel
from models.users import UsersModel
from models.todos import TodosModel
from models.site_words import SiteWordsModel

home = Blueprint('home', __name__)

words = {}
language = LangsModel.get_data()

# {
#     'AR': {
#         'id': 'م',
#         'val': 'بيان',
#         'btns': 'ازرار',
#     },
#     'EN': {
#         'id': 'id',
#         'val': 'value',
#         'btns': 'btns',
#     }
# }

if bool(language):
    for langu in language:
        # words[langu['lang_short']] = langu['lang_short']
        
        words_in_lang = SiteWordsModel.get_data(
            '"lang_id" = '+ str(langu['lang_id'])
        )
        lang_kies = {}
        for word_key in words_in_lang:
            lang_kies[word_key['word_key']] = SiteWordsModel.get_by_key(
                word_key['word_key'],
                langu['lang_id']
            )
        words[langu['lang_short']] = lang_kies

@home.route("/")
def home_page_by_lang(lang):
    if lang in vars.list_langs:
        
        try:
            cookie = DataEncrypt.decrypt(
                request.cookies.get('LOGIN')
            )
        except:
            cookie = False
        
        user = False
        todos = []
        if bool(cookie):
            user = UsersModel.get_by_username(
                cookie
            )
            todos = TodosModel.get_data(
                '"user_id" = '+ str(user['user_id'])
            )

        return render_template(
            'home.html',
            todos = todos,
            lang = lang,
            words = words,
            un = '',
            ps = '',
            err = '',
            cookie = cookie,
            url = request.url,
            user = user
        )
    abort(404)
