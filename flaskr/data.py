from flask import Blueprint, render_template, request, jsonify
from database import db

data = Blueprint("data", __name__)

@data.route("/get_ledger_datas", methods=["GET"])
def get_ledger_datas():
    user_id = request.args.get("user_id")
    ledger_id = request.args.get("ledger_id")
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
            SELECT Price, Dtype, DDate
            FROM Datas
            WHERE UID = {user_id} AND LID = {ledger_id}
        """
    )
    result = cursor.fetchall()
    datas = []
    for item in result:
        price, dtype, ddate = item
        datas.append({
            "price": price,
            "dtype": dtype,
            "ddate": ddate
        })
    cursor.close()
    return jsonify(datas)




    

    
