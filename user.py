from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for,
    redirect,
    flash,
    jsonify,
    Flask
)
#from database import db
import mysql.connector

user = Flask(__name__)

#user = Blueprint("user", __name__,)

user.config["MYSQL_HOST"] = "localhost"
user.config["MYSQL_PORT"] = 3306
user.config["MYSQL_USER"] = "root"
user.config["MYSQL_PASSWORD"] = "aqaq08243"  # 请替换为您的 MySQL 密码
user.config["MYSQL_DB"] = "Money"
conn = None
try:
    # 连接到 MySQL 数据库
    conn = mysql.connector.connect(
        host=user.config["MYSQL_HOST"],
        port=user.config["MYSQL_PORT"],
        user=user.config["MYSQL_USER"],
        password=user.config["MYSQL_PASSWORD"],
        database=user.config["MYSQL_DB"]
    )
    print("Connection successful!")
except mysql.connector.Error as e:
    # 如果连接建立失败，打印错误消息
    print(f"Error connecting to MySQL: {e}")

cursor = conn.cursor()


@user.route('/user/get_username',methods=['GET', 'POST'])
def get_username():
    
    #userId = request.args.get('userId')
    userId = 3
    #cursor = connection.cursor()
    cursor.execute(
        f"""
            SELECT UName
            FROM users 
            WHERE UID = {userId};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

@user.route('/user/get_is_righthander',methods=['GET', 'POST'])
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


if __name__ == '__main__':
    user.run(debug=True)





