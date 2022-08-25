from flask import Blueprint, jsonify
from flask_cors import CORS

user_api = Blueprint("user_api", __name__)

CORS(user_api)


@user_api.route("/", methods=["GET"])
def create_user():
    return jsonify({"hello": "world"})
