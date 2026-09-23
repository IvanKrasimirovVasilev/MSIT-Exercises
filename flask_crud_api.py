from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = [
    {"id": 1, "username": "alice", "email": "alice@email.com"},
    {"id": 2, "username": "bob", "email": "bob@email.com"},
    {"id": 3, "username": "charlie", "email": "charlie@email.com"}
    ]

@app.route("/")
def index():
    return render_template("flask_crud_api_index.html")

@app.route("/users")
def list_users():
    return jsonify(users)

@app.route("/users/<user_id>")
def profile(user_id):
    user = next((user for user in users if str(user["id"]) == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create():
    data = request.get_json()
    if not data.get("username") or not data.get("email"):
        return jsonify({"error": "Username and email are required"}), 400

    existing_user = next(
        (user for user in users if user["username"] == data.get("username")),
        None
    )
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400

    existing_mail = next(
        (user for user in users if user["email"] == data.get("email")),
        None
    )
    if existing_mail:
        return jsonify({"error": "Email already exists"}), 400

    new_id = max((user["id"] for user in users), default=0) + 1

    new_user = {
        "id": new_id,
        "username": data.get("username"),
        "email": data.get("email")
    }

    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update(user_id):
    data = request.get_json()

    if not data.get("username") or not data.get("email"):
        return jsonify({"error": "Username and email are required"}), 400

    existing_user = next(
        (user for user in users if user["username"] == data.get("username") and str(user["id"]) != user_id),
        None
    )
    if existing_user:
        return jsonify({"error": "Username already exists"}), 409

    existing_mail = next(
        (user for user in users if user["email"] == data.get("email") and str(user["id"]) != user_id),
        None
    )
    if existing_mail:
        return jsonify({"error": "Email already exists"}), 409

    user = next((user for user in users if str(user["id"]) == user_id), None)

    if user:
        user["username"] = data.get("username")
        user["email"] = data.get("email")
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>", methods=["PATCH"])
def update_user_patch(user_id):
    data = request.get_json()
    user = next((user for user in users if str(user["id"]) == user_id), None)

    if "username" in data:
        user["username"] = data["username"]

    if "email" in data:
        user["email"] = data["email"]

    if "username" in data:
        existing_user = next(
            (
                user for user in users
                if user["username"] == data["username"]
                   and str(user["id"]) != user_id
            ),
            None
        )

        if existing_user:
            return jsonify({"error": "Username already exists"}), 409

    if "email" in data:
        existing_mail = next(
            (
                user for user in users
                if user["email"] == data["email"]
                   and str(user["id"]) != user_id
            ),
            None
        )

        if existing_mail:
            return jsonify({"error": "Email already exists"}), 409

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)

@app.route("/users/<user_id>", methods=["DELETE"])
def delete(user_id):
    user = next((user for user in users if str(user["id"]) == user_id), None)

    if user:
        users.remove(user)
        return jsonify({"success": True})
    else:
        return jsonify({"error": "user not found"}), 404

@app.route("/users/count", methods=["GET"])
def count_users():
    len_users = len(users)
    return jsonify({"count": len_users})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)