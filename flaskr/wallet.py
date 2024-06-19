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

wallet = Blueprint("wallet",__name__)

@wallet.route('/get_all_wallets',methods=['GET', 'POST'])
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
        return jsonify(wallets),200
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

