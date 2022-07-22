import sqlalchemy.exc
from users_db import get_users_db
from flask import Flask, jsonify, request


app = Flask(__name__)
db = get_users_db(
    host='localhost',
    user='root',
    password='root',
    database='ss_users'
)
_users_table = db.get_table("users")


@app.route("/user/list", methods=['GET'])
def list_users():
    query = _users_table.select()
    return jsonify([dict(row) for row in db.execute(query)[0]])

# TODO: verify inputs
@app.route("/user/add", methods=['POST'])
def add_user():
    form = request.form.to_dict()       # TODO: keep only relevant keys
    try:
        db.execute(_users_table.insert(), form)
    except sqlalchemy.exc.IntegrityError:
        return f"Error, user already exists!", 400
    return f"Successfully added user {form['username']}"

# TODO: verify inputs
@app.route("/user/delete", methods=['POST'])
def delete_user():
    form = request.form
    result = f"Successfully removed user with id {form['user_id']}", 200
    query = _users_table.delete().where(_users_table.c['user_id'] == form['user_id'])
    _, rowcount = db.execute(query)
    if not rowcount:
        result = "No users removed", 200
    return result


if __name__ == '__main__':
    app.run(debug=True)