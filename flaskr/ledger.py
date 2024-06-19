from flask import Blueprint, render_template, request, abort, jsonify
from database import db

ledger = Blueprint("ledger", __name__)

@ledger.route("/get_ledgers", methods=["GET"])
def get_ledgers():
    wallet_id = request.args.get("wallet_id")
    if not wallet_id:
        return jsonify({"error":"wallet_id not defined"}), 404
    cursor = db.connection.cursor()
    cursor.execute(f"""SELECT * FROM Wallets WHERE WID = {wallet_id};""")
    # Avoid non-exist wallet
    if not cursor.fetchall():
        return jsonify({"error":"wallet not exists"}), 404
    
    cursor.execute(f"""
                   SELECT *
                   FROM Ledgers
                   WHERE WID = {wallet_id};
                   """)
    ledgers = cursor.fetchall()
    result = []
    for ledger in ledgers:
        result.append(
            {
                "WID": ledger[0],
                "LID": ledger[1],
                "LName": ledger[2],
            }
        )
    return jsonify(result), 200

@ledger.route("/insert_ledger", methods=["GET", "POST"])
def insert_ledger():
    wallet_id = request.args.get("wallet_id")
    ledger_name = request.args.get("ledger_name")
    
    if not wallet_id or not ledger_name:
        return jsonify({"error":"wallet_id or ledger_name not defined"}), 404
    cursor = db.connection.cursor()
    cursor.execute(f"""SELECT * FROM Wallets WHERE WID = {wallet_id};""")
    # Avoid non-exist wallet
    if not cursor.fetchall():
        return jsonify({"error":"wallet not exists"}), 404
    
    try:
        cursor.execute(
            f"""
                INSERT INTO Ledgers (WID, LName)
                VALUES ({wallet_id}, '{ledger_name}');
            """
        )
        cursor.execute("COMMIT")
        cursor.close()
        return jsonify({"success":"ledger inserted"}), 201
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@ledger.route("/delete_ledger", methods=["DELETE", "GET"])
def delete_ledger():
    ledger_id = request.args.get("ledger_id")
    cursor = db.connection.cursor()
    if not ledger_id:
        return jsonify({"error":"ledger_id not defined"}), 404
    cursor.execute(f"""SELECT * FROM Ledgers WHERE LID = {ledger_id};""")
    if not cursor.fetchall():
        return jsonify({"error":"ledger not exists, pass"}), 404
    
    try:
        cursor.execute(
            f"""
                DELETE FROM Ledgers
                WHERE LID = {ledger_id};
            """
        )
        cursor.execute("COMMIT")
        cursor.execute(f"""
                        SELECT * 
                        FROM DataToLedger
                        WHERE LID = {ledger_id};""")
        if cursor.fetchall():
            cursor.execute(f"""DELETE FROM DataToLedger WHERE LID = {ledger_id};""")
            cursor.execute("COMMIT")
        
        cursor.close()
        return jsonify({"success":"ledger deleted successfully"}), 200
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@ledger.route("/update_ledger", methods=["PUT", "GET"])
def update_ledger():
    ledger_id = request.args.get("ledger_id")
    cursor = db.connection.cursor()
    if not ledger_id:
        return jsonify({"error":"ledger_id not defined"}), 404
    cursor.execute(f"""
                    SELECT * 
                    FROM Ledgers 
                    WHERE LID = {ledger_id};""")
    if not cursor.fetchall():
        return jsonify({"error":"ledger not exists, pass"}), 404
    
    try:
        new_data = {
            'WID':request.args.get("wallet_id"),
            'LName':request.args.get("ledger_name")
        }
        if not new_data['WID'] or not new_data['LName']:
            return jsonify({"error":"wallet_id or ledger_name not defined"}), 404
        cursor.execute(f"""SELECT * FROM Wallets WHERE WID = {new_data['WID']};""")
        if not cursor.fetchall():
            return jsonify({"error":"wallet not exists"}), 404
        # Update Datas
        update_fields = []
        update_values = []
        for key, value in new_data.items():
            if value is not None:
                update_fields.append(f"{key} = %s")
                update_values.append(value) 
            
        if update_fields:
            update_values.append(ledger_id)
            update_query = f"UPDATE Ledgers SET {', '.join(update_fields)} WHERE LID = %s"
            cursor.execute(update_query, tuple(update_values))
            cursor.execute('COMMIT')
        cursor.close()
        return jsonify({"success":"ledger updated successfully"}), 201
        
    except:
        cursor.execute("ROLLBACK")
        cursor.close()
        abort(500, "ERROR 500")

@ledger.route("/get_ledger_all_datas", methods=["GET"])
def get_ledger_all_datas():
    ledger_id = request.args.get("ledger_id")
    cursor = db.connection.cursor()
    if not ledger_id:
        return jsonify({"error":"ledger_id not defined"}), 404
    cursor.execute(f"""SELECT * FROM Ledgers WHERE LID = {ledger_id};""")
    if not cursor.fetchall():
        return jsonify({"error":"ledger not exists, pass"}), 404
    
    cursor.execute(f"""
                   SELECT DID
                   FROM DataToLedger
                   WHERE LID = {ledger_id};
                   """)
    datas = cursor.fetchall()
    result = []
    for data in datas:
        result.append(
            {
                "DID": data[0]
            }
        )
    return jsonify(result), 200