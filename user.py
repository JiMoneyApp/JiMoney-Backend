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
from database import db



user = Blueprint("user", __name__,)

@user.route('/user/get_user_name',methods=['GET', 'POST'])
def get_user_name():
    
    user_Id = request.args.get('user_Id')
    #user_Id = 3
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UName
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

@user.route('/user/get_is_right',methods=['GET', 'POST'])
def get_is_right():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT isRightHander
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_is_dark',methods=['GET', 'POST'])
def get_is_dark():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT isDarkMode
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_ntime',methods=['GET', 'POST'])
def get_ntime():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT NoticeTime
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_acc',methods=['GET', 'POST'])
def get_user_acc():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UAccount
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_password',methods=['GET', 'POST'])
def get_user_password():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UPassword
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_budget',methods=['GET', 'POST'])
def get_budget():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT Budget
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result

@user.route('/user/get_user_nname',methods=['GET', 'POST'])
def get_user_nname():
    
    user_Id = request.args.get('user_Id')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT UNickname
            FROM users 
            WHERE UID = {user_Id};
        """
    )
    result = cursor.fetchone()
    cursor.close()
    return result


@user.route('/user/update_user_name',methods=['PUT', 'POST'])
def update_user_name():
    
    user_Id = request.args.get('user_Id')
    new_name = request.args.get('new_name')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_name}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"

@user.route('/user/update_user_password',methods=['PUT', 'POST'])
def update_user_password():
    
    user_Id = request.args.get('user_Id')
    new_password = request.args.get('new_password')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_password}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"

@user.route('/user/update_user_acc',methods=['PUT', 'POST'])
def update_user_acc():
    
    user_Id = request.args.get('user_Id')
    new_acc = request.args.get('new_acc')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_acc}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"

@user.route('/user/update_user_nname',methods=['PUT', 'POST'])
def update_user_nname():
    
    user_Id = request.args.get('user_Id')
    new_nname = request.args.get('new_nname')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_nname}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"


@user.route('/user/update_user_ntime',methods=['PUT', 'POST'])
def update_user_ntime():
    
    user_Id = request.args.get('user_Id')
    new_ntime = request.args.get('new_ntime')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_ntime}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"


@user.route('/user/update_user_isright',methods=['PUT', 'POST'])
def update_user_isright():
    
    user_Id = request.args.get('user_Id')
    new_isright = request.args.get('new_isright')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_isright}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"

@user.route('/user/update_user_isdark',methods=['PUT', 'POST'])
def update_user_isdark():
    
    user_Id = request.args.get('user_Id')
    new_isdark = request.args.get('new_isdark')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_isdark}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"


@user.route('/user/update_user_budget',methods=['PUT', 'POST'])
def update_user_budget():
    
    user_Id = request.args.get('user_Id')
    new_budget = request.args.get('new_budget')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_budget}
            WHERE UID = {user_Id};
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"

@user.route('/user/update_user_name',methods=['PUT', 'POST'])
def update_user_name():
    
    user_Id = request.args.get('user_Id')
    new_name = request.args.get('new_name')
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            update users
            set UName = {new_name}
            WHERE UID = {user_Id},
        """
    )
    db.connection.commit()
    cursor.close()
    return "Update successfully!"


    



if __name__ == '__main__':
    user.run(debug=True)





