from flask import Blueprint, render_template, abort, request
from models.users import UsersModel
from models.profile import UserProfileModel
from lib.encrypt import DataEncrypt


profile = Blueprint('profile', __name__)

@profile.route('/<string:username>/')
def profile_page(lang, username):

    users = UsersModel.get_data()
    for user in users:
        cookie = request.cookies.get('LOGIN')
        cookie = DataEncrypt.decrypt(cookie)

        # if cookie == username:
        #     iam = True
        # else:
        #     iam = False

        if username == user['username']:
            return render_template(
                'profile.html',
                username = username,
                lang = lang,
                user = UserProfileModel.get_data_by_pk(user['user_id']),
                iam = 'am' if cookie == username else 'not am',
                url = request.url
            )
    abort(404)
