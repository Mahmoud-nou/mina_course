from datetime import datetime, timedelta

from flask import Blueprint, render_template, abort, redirect, request, make_response

import pytz

from config import vars

from lib.encrypt import DataEncrypt

# todos
from models.todos import TodosModel

# site
from models.langs import LangsModel
from models.site_words import SiteWordsModel

# users
from models.users import UsersModel
from models.profile import UserProfileModel

# phone number
from models.phone_number import PhoneNumberModel

words = {}
language = LangsModel.get_data()

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

api = Blueprint('api', __name__)

@api.route('/', methods=['POST'])
def api_page(lang):
    if lang in vars.list_langs:
        if request.method == 'POST':
            if 'update_todo' in request.form:
                TodosModel.update_data({
                    'todo': request.form['update_todo']
                }, id)
                return redirect('/')
            # Logout
            if 'logout_url' in request.form:
                resp = make_response(
                    redirect(request.form['logout_url'])
                )

                resp.set_cookie(
                    'LOGIN',
                    '',
                    None
                )

                return resp
            # Singup
            if ('signup_username' in request.form
                and 'signup_password' in request.form
                and 'signup_repassword' in request.form
                and 'first_name' in request.form
                and 'last_name' in request.form
                and 'gender' in request.form
                and 'date_of_birth' in request.form
                and 'profile_img' in request.form):
                if request.form['signup_password'] == request.form['signup_repassword']:
                    UsersModel.add_data({
                        'username': request.form['signup_username'],
                        'password': DataEncrypt.encrypt(request.form['signup_password'])
                    })
                    UserProfileModel.add_data({
                        'first_name': request.form['first_name'],
                        'last_name': request.form['last_name'],
                        'gender': request.form['gender'],
                        'date_of_birth': request.form['date_of_birth'],
                        'profile_img':request.form['signup_username'] +'.jpg' 
                    })
                    # login
                return redirect('/')
            # Singin
            if ('signin_username' in request.form
                and 'signin_password' in request.form):

                users = UsersModel.get_data()
                logedin = False
                err_mess = ''

                for user in users:
                    if request.form['signin_username'] == user['username']:
                        if request.form['signin_password'] == DataEncrypt.decrypt(user['password']):
                            # login
                            logedin = True
                            resp = make_response(
                                redirect(request.form['signin_url'])
                            )

                            now = datetime.now(pytz.timezone('Africa/Cairo'))
                            after = timedelta(days = 3 * 365)

                            resp.set_cookie(
                                'LOGIN',
                                DataEncrypt.encrypt(request.form['signin_username']),
                                # 10 * 60 * 60 * 24, # max_age
                                None, # max_age
                                # datetime(
                                #     2025, 6, 10, 14, 30, 2, 100,
                                #     tzinfo=pytz.timezone('Africa/Cairo') # expires
                                # )
                                now + after, # expires
                                '/', # path
                                request.host, # domain
                                None, # secure
                                False # httponly
                            )

                            return resp
                            # break
                        else:
                            # password wrong
                            err_mess = 'password wrong'
                    else:
                        # username wrong
                        err_mess = 'username wrong'
                    
                if not logedin:
                    return render_template(
                        'home.html',
                        todos = TodosModel.get_data(),
                        lang = lang,
                        words = words,
                        un = request.form['signin_username'],
                        ps = request.form['signin_password'],
                        err = err_mess
                    )
            # Delete Todo
            if 'delete_todo' in request.form:
                TodosModel.delete_data(
                    '"todo_id" = '+ request.form['delete_todo']
                )
                return redirect('/')
        
                    
            # abort(404)
            # add data for phone number
            if ('phone_number' in request.form
                and 'country_code' in request.form
                and 'phone_type' in request.form):

                PhoneNumberModel.add_data({
                    'phone_number' : request.form['phone_number'],
                    'country_code' : request.form['country_code'] ,  #'+2' if request.form['phone_number'] == 'egypt' else '+966',
                    'phone_type' : request.form['phone_type']
                })

                return redirect('/')

                

