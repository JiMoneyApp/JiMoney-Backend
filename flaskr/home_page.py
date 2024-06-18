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

home_page = Blueprint("home_page",__name__)

@home_page.route('/get_all_wallets',methods=['GET', 'POST'])
def get_all_wallets():

    user_id = request.args.get('user_id')
    cursor = db.connection.cursor()
    try:
        cursor.execute(
            f"""
                SELECT WID, WName
                FROM Wallets
                WHERE UID = {user_id};
            """
        )
        result = cursor.fetchall()
        wallets = []
        for item in result:
            wid, wname = item
            wallets.append({
                "wid": wid,
                "wname": wname
            })
        cursor.close()
        return jsonify(wallets)
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@home_page.route('/get_all_ledgers',methods=['GET', 'POST'])
def get_all_ledgers():

    wallet_id = request.args.get('wallet_id')
    cursor = db.connection.cursor()
    try:
        cursor.execute(
            f"""
                SELECT LID, LName
                FROM Ledgers
                WHERE UID = {wallet_id};
            """
        )
        result = cursor.fetchall()
        ledgers = []
        for item in result:
            lid, lname = item
            ledgers.append({
                "lid": lid,
                "lname": lname
            })
        cursor.close()
        return jsonify(ledgers)
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@home_page.route('/get_all_goals',methods=['GET', 'POST'])
def get_all_goals():

    user_id = request.args.get('user_id')
    cursor = db.connection.cursor()
    try:
        cursor.execute(
            f"""
                SELECT GID, GName
                FROM Goals
                WHERE UID = {user_id};
            """
        )
        result = cursor.fetchall()
        goals = []
        for item in result:
            gid, gname = item
            goals.append({
                "gid": gid,
                "gname": gname
            })
        cursor.close()
        return jsonify(goals)
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

## if exists return goal id
def check_data_to_goal(data_id):

    cursor = db.connection.cursor()
    try:
        cursor.execute(
            f"""
                SELECT GID
                FROM DataToGoal
                WHERE DID = {data_id};
            """
        )
        result = cursor.fetchone()
        cursor.close()
        if len(result) > 0:
            return result[0]
        else:
            return False
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@home_page.route('/delete_data',methods=['DELETE', 'GET'])
def delete_data():

    data_id = request.args.get('data_id')
    cursor = db.connection.cursor()
    try:

        # check if data exists in goal
        # if exists update GCurrentAmount and delete from data
        # else delete from data
        if not check_data_to_goal(data_id):
            cursor.execute(
                f"""
                    DELETE FROM Datas
                    WHERE DID = {data_id};
                """
            )
            cursor.execute("COMMIT")
            cursor.close()
            return "success"
        else:
            gid = check_data_to_goal(data_id)
            cursor.execute(
                f"""
                    SELECT Price
                    FROM Datas
                    WHERE DID = {data_id};
                """
            )
            price = cursor.fetchone() ## price of data
            cursor.execute(
                f"""
                    SELECT GCurrentAmount
                    FROM Goals
                    WHERE GID = {gid};
                """
            )
            current_amount = cursor.fetchone()
            new_amount = int(current_amount[0]) - int(price[0])
            cursor.execute(
                f"""
                    UPDATE Goals
                    SET GCurrentAmount = {new_amount}
                    WHERE GID = {gid};
                """
            )
            cursor.execute(
                f"""
                    DELETE FROM Datas
                    WHERE DID = {data_id};
                """
            )
            cursor.execute("COMMIT")
            cursor.close()
            return "success"

    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

