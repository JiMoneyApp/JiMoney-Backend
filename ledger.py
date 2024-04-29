from flask import Blueprint, render_template, request, abort
from database import db

ledger = Blueprint("ledger", __name__, template_folder="templates")

@ledger.route("/check_ledger", methods=["GET"])
def check_ledger():
    user_id = request.args.get("user_id")
    ledger_name = request.args.get("ledger_name")

    cursor = db.connect.cursor()
    cursor.execute(
        f"""SELECT COUNT(*)
            FROM Ledgers
            WHERE UID = {user_id}
            AND Lname = {ledger_name}
        """
        )
    result = cursor.fetchone()
    cursor.close()
    if len(result) > 0:
        return "already exists"
    else:
        return "none"

#jfiejif

@ledger.route("/amount_ledger", methods=["GET"])
def amount_ledger() -> int:
    user_id = request.args.get("user_id")
    ledger_name = request.args.get("ledger_name")

    cursor = db.connect.cursor()
    cursor.execute(
        f"""SELECT SUM(price)
            FROM Datas
            WHERE UID = {user_id}
        """
        )
    amount = cursor.fetchone()
    cursor.close()
    return amount_sum   