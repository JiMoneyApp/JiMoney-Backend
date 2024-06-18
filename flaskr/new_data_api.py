from flask import Blueprint, render_template, request, jsonify, abort
from database import db
data = Blueprint("data", __name__, template_folder="flaskr")

@data.route("/insert_data", methods=["GET", "POST"])
def insert_data():
    try:
        # Get user id
        uid = request.args.get("user_id")
        if not uid:
            return jsonify({'error': 'User id not defined'}), 404
        # Avoid insert data to non-exist user
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM Datas WHERE uid = {uid}")
        user_test = cursor.fetchone()
        if not user_test:
            return jsonify({'error': 'User not found'}), 404
        
        # Get necessary data information
        price = request.args.get("price")
        dname = request.args.get("dname")
        dtype = request.args.get("dtype")
        ddate = request.args.get("ddate")
    
        # Get optional data information
        lid = request.args.get("lid")
        gid = request.args.get("gid")
    
        cursor = db.connection.cursor()
        cursor.execute(
            f"""
                INSERT INTO Datas (UID, Price, DName, DType, DDate)
                VALUES ({uid}, {price}, '{dname}', '{dtype}', {ddate});
            """
        )
        cursor.execute('COMMIT')
    
        if lid is not None:
            cursor.execute(
                f"""
                    INSERT INTO DataToLedger (DID, LID)
                    VALUES ((SELECT MAX(DID) FROM Datas), {lid});
                """
            )
            cursor.execute('COMMIT')
        if gid is not None:
            cursor.execute(
                f"""
                    UPDATE Goals
                    SET GCurrentAmount = GCurrentAmount + {price}
                    WHERE GID = {gid}
                """
                )
            cursor.execute('COMMIT')
            cursor.execute(
                f"""
                    INSERT INTO DataToGoal (DID, GID)
                    VALUES ((SELECT MAX(DID) FROM Datas), {gid});
                """
            )
            cursor.execute('COMMIT')
        cursor.close()
        return jsonify({'success':'Insert data successfully'}), 201
    except:
        cursor.execute('ROLLBACK')
        abort(500, 'ERROR 500')

@data.route("update_data", methods=["GET", "POST"])
def update_data():
    try: 
        did = request.args.get("did")
        # Get necessary data information
        new_data = {
            'price':request.args.get("price"),
            'dname':request.args.get("dname"),
            'dtype':request.args.get("dtype"),
            'ddate':request.args.get("ddate")
        }
        # In update, these are necessary, can be either None or not None
        lid = request.args.get("lid")
        gid = request.args.get("gid")
    
        # Avoid update non-exist data
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM Datas WHERE did = {did}")
        original_data = cursor.fetchone()
        if not original_data:
            return jsonify({'error': 'Data not found'}), 404
       
       # Get current price
        cursor.execute(
            f"""
                SELECT Price
                FROM Datas
                WHERE DID = {did}
            """
        )
        original_price = cursor.fetchone()[0]

       # Update Datas
        update_fields = []
        update_values = []
        for key, value in new_data.items():
            if value is not None:
                update_fields.append(f"{key} = %s")
                update_values.append(value) 
            
        if update_fields:
            update_values.append(did)
            update_query = f"UPDATE datas SET {', '.join(update_fields)} WHERE did = %s"
            cursor.execute(update_query, tuple(update_values))
            cursor.execute('COMMIT')
        
        # Update DataToLedger
        if lid is not None:
            cursor.execute(
                f"""
                    DELETE FROM DataToLedger
                    WHERE DID = {did};
                """
            )
            cursor.execute(
                f"""
                    INSERT INTO DataToLedger (DID, LID)
                    VALUES ({did}, {lid});
                """
            )   
            cursor.execute('COMMIT')
        else:
            cursor.execute(
                f"""
                    DELETE FROM DataToLedger
                    WHERE DID = {did};
                """
            )
            cursor.execute('COMMIT')
            
        # Update DataToGoal table, GCurrentAmount of Goal    
        if gid is not None:
            # Minus original price from GCurrentAmount
            cursor.execute(
                f"""
                    UPDATE Goals
                    SET GCurrentAmount = GCurrentAmount - {original_price}
                    WHERE GID = (SELECT GID FROM DataToGoal WHERE DID = {did});
                """
            )
            # Add new price to new Goal's GCurrentAmount
            cursor.execute(
                f"""
                    UPDATE Goals
                    SET GCurrentAmount = GCurrentAmount + (SELECT Price FROM Datas WHERE DID = {did})
                    WHERE GID = {gid};
                """
            )
            # Update DataToGoal
            cursor.execute(
                f"""
                    DELETE FROM DataToGoal
                    WHERE DID = {did};
                """
            )
            cursor.execute(
                f"""
                    INSERT INTO DataToGoal (DID, GID)
                    VALUES ({did}, {gid});
                """
            )   
            cursor.execute('COMMIT')
        # Delete bounding of Data and Goal
        else: 
            cursor.execute(
                f"""
                    UPDATE Goals
                    SET GCurrentAmount = GCurrentAmount - {original_price}
                    WHERE GID = (SELECT GID FROM DataToGoal WHERE DID = {did});
                """
            )
            cursor.execute(
                f"""
                    DELETE FROM DataToGoal
                    WHERE DID = {did};
                """
            )
            cursor.execute('COMMIT')
        
        cursor.close()
        return 'success', 201
    except:
        cursor.execute('ROLLBACK')
        abort(500, 'ERROR 500')
        
@data.route("/get_my_partner_goal", methods=["GET"])
def get_my_partner_goal():
    try:
        did= request.args.get("did")
        cursor = db.connection.cursor()
        cursor.execute(
            f"""
                SELECT GID
                FROM DataToGoal
                WHERE DID = {did}
            """
        )
        gid = cursor.fetchall()
        return jsonify(gid), 200
    except:
        cursor.execute("ROLLBACK")
        abort(500, "ERROR 500")

@data.route("/get_my_partner_ledger", methods=["GET"])
def get_my_partner_ledger():
    try:
        did= request.args.get("did")
        cursor = db.connection.cursor()
        cursor.execute(
            f"""
                SELECT LID
                FROM DataToLedger
                WHERE DID = {did}
            """
        )
        lid = cursor.fetchall()
        return jsonify(lid), 200
    except:
        cursor.execute("ROLLBACK")
        abort(500, "ERROR 500")
        
@data.route("/get_all_datas", methods=["GET"])
def get_all_datas():
    try:
        uid = request.args.get("uid")
        if not uid:
            return jsonify({'error': 'User id not defined'}), 404
        # Avoid show non-exist user's data
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM Datas WHERE uid = {uid}")
        user_test = cursor.fetchone()
        if not user_test:
            return jsonify({'error': 'User not found'}), 404
        
        cursor = db.connection.cursor()
        cursor.execute(
            f"""
                SELECT * FROM Datas
            """
        )
        datas = cursor.fetchall()
        result = []
        for data in datas:
            result.append({
                'uid': data[0],
                'did': data[1],
                'price': data[2],
                'dname': data[3],
                'dtype': data[4],
                'ddate': data[5]
            })
        return jsonify(result), 200
    except:
        cursor.execute("ROLLBACK")
        abort(500, "ERROR 500")
