from flask import Blueprint, request
from flaskr.database import db

data = Blueprint("data", __name__)

@data.route("/data_name", methods=["GET"])
def get_data_name():
    
    ledger_id = request.args.get("ledger_id")
    
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
          SELECT Dname
          FROM Datas
          WHERE LID = {ledger_id};
        """
    )
    
    data_name = cursor.fetchone()
    cursor.close()
    
    if data_name is None:
        return "Have no data record", 404
    
@data.route("/data_amount", methods=["GET"])
def get_amount():
    
    ledger_id = request.args.get("ledger_id")
    
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
          SELECT SUM(Price) 
          FROM Datas
          WHERE LID = {ledger_id};
        """
    )
    
    amount_sum = cursor.fetchone()
    cursor.close()
    
    return amount_sum


    
