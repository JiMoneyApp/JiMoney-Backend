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
from tinydb import TinyDB, Query
from userTest import user_table
user = Blueprint("user",__name__)




@user.route('/get_user_id',methods=['GET', 'POST'])
def get_user_id():
    user_acc = request.args.get('user_acc')
    user_password = request.args.get('user_pass')   
 
    user_id = user_table.get(
        (Query().UAccount == user_acc) & (Query().UPassword == user_password)
    )
    if user_id:
        return jsonify(user_id["UID"]), 200
    else:
        return jsonify(user_id), 404

@user.route('/get_name',methods=['GET', 'POST'])
def get_user_name():
    
    user_id = request.args.get('user_id')
    name = user_table.get(
        (Query().UID == userid)
    )
    if user_id:
        return jsonify(user_id["UID"]), 200
    else:
        return jsonify(user_id), 404
         

@user.route('/get_isright',methods=['GET', 'POST'])
def get_is_right():
    
    user_id = request.args.get('user_id')
    isright = user_table.get(
        (Query().UID == user_id)
    )


@user.route('/get_isdark',methods=['GET', 'POST'])
def get_is_dark():
    
    user_id = request.args.get('user_id')
    isdark = user_table.get(
        (Query().UID == user_id)
    )
    

@user.route('/get_ntime',methods=['GET', 'POST'])
def get_ntime():
    
    user_id = request.args.get('user_id')
    ntime = user_table.get(
        (Query().UID == user_id)
    )

@user.route('/get_acc',methods=['GET', 'POST'])
def get_user_acc():
    
    user_id = request.args.get('user_id')
    acc = user_table.get(
        (Query().UID == user_id)
    )

@user.route('/get_password',methods=['GET', 'POST'])
def get_user_password():
    
    user_id = request.args.get('user_id')
    password = user_table.get(
        (Query().UID == user_id)
    )

@user.route('/get_budget',methods=['GET', 'POST'])
def get_budget():
    
    user_id = request.args.get('user_id')
    budget = user_table.get(
        (Query().UID == user_id)
    )

@user.route('/get_nname',methods=['GET', 'POST'])
def get_user_nname():
    
    user_id = request.args.get('user_id')
    nname = user_table.get(
        (Query().UID == userid)
    )


@user.route('/update_name',methods=['PUT', 'GET'])
def update_user_name():
    
    user_id = request.args.get('user_id')
    new_name = request.args.get('new_name')
    
    success = users_table.update(
        {'UName': new_isright}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404


@user.route('/update_password',methods=['PUT', 'GET'])
def update_user_password():
    
    user_id = request.args.get('user_id')
    new_password = request.args.get('new_password')

    success = users_table.update(
        {'UPassword': new_password}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404

@user.route('/update_acc',methods=['PUT', 'GET'])
def update_user_acc():
    
    user_id = request.args.get('user_id')
    new_acc = request.args.get('new_acc')
        
    success = users_table.update(
        {'UAccount': new_acc}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404

@user.route('/update_nname',methods=['PUT', 'GET'])
def update_user_nname():
    
    user_id = request.args.get('user_id')
    new_nname = request.args.get('new_nname')

    
    success = users_table.update(
        {'UNickName': new_nname}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404

@user.route('/update_ntime',methods=['PUT', 'GET'])
def update_user_ntime():
    
    user_id = request.args.get('user_id')
    new_ntime = request.args.get('new_ntime')


@user.route('/update_isright',methods=['PUT', 'GET'])
def update_user_isright():
    
    user_id = request.args.get('user_id')
    new_isright = request.args.get('new_isright')
        
    success = users_table.update(
        {'isrightHander': new_isright}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404

@user.route('/update_isdark',methods=['PUT', 'GET'])
def update_user_isdark():
    
    user_id = request.args.get('user_id')
    new_isdark = request.args.get('new_isdark')

    success = users_table.update(
        {'isDarkMode': new_isdark}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404

@user.route('/update_budget',methods=['PUT', 'GET'])
def update_user_budget():
    
    user_id = request.args.get('user_id')
    new_budget = request.args.get('new_budget')

    success = users_table.update(
        {'BUDGET': new_budget}, 
        Query().UID == int(user_id)
    )
    if success:
        return 'success!', 200
    else:
        return 'fail!', 404


@user.route('/insert_acc_password',methods=['GET','POST'])
def insert_user_acc_password():
    
    user_name = request.args.get('user_name')
    user_acc = request.args.get('user_acc')
    user_password = request.args.get('user_password')
    
    data = [
        {
            "UID": 1,
            "BUDGET": 0,
            "UName": f"{user_name}",
            "UPassword": f"{user_password}",
            "UAccount": f"{user_acc}",
            "UNickname": "Nickname",
            "isrightHander": True,
            "isDarkMode": False,
            "NoticeTime": "21:00:00"
        }
    ]

    success = user_table.insert_multiple(data)

    if success:
        return 'success!', 200
    else:
        return 'fail!', 404
