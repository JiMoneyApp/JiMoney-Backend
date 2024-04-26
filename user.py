from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for,
    redirect,
    flash,
    jsonify
)
from database import db


user = Blueprint("user", __name__, template_folder="templates")


@user.route('/user/get_username',methods=['GET', 'POST'])
def get_username():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT Username
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_is-righthander',methods=['GET', 'POST'])
def get_isRightHander():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT isRightHander
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_is_dark_mode',methods=['GET', 'POST'])
def get_is_dark_mode():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT isDarkMode
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_notice_time',methods=['GET', 'POST'])
def get_notice_time():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT NoticeTime
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_account',methods=['GET', 'POST'])
def get_user_account():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UAccount
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_password',methods=['GET', 'POST'])
def get_user_password():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UPassword
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_budget',methods=['GET', 'POST'])
def get_budget():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT Budget
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_nickname',methods=['GET', 'POST'])
def get_user_nickname():
    
    userId = request.args.get('userId')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UNickname
            FROM users 
            WHERE UID = {userId},
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result





