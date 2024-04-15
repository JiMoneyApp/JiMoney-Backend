from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for,
    redirect,
    flash,
    jsonify
)
from database import db


user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/user_root")
def user_root():
    return render_template("user/user_root.html")

# homepage for user
@user_blueprint.route("/")
def user_id():
    # get user_acc from request arguments
    user_acc = request.args.get("user_acc")
    if user_acc is None:
        abort(400, "Parameter not found")

    # query data from db
    cursor = db.connect.cursor()
    cursor.execute(
        f"""
        SELECT UID FROM Users
        WHERE Uaccount = {user_acc};
    """
    )
    user = cursor.fetchone() #what is difference between fetchone/all
    if user is None:
        abort(404, "User not found")
    cursor.close()
    return jsonify(user)



