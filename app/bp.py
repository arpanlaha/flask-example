from flask import Blueprint, request, jsonify

bp = Blueprint("bp", __name__, url_prefix="/bp")


@bp.route("", methods=["GET"])
def bp_response():
    return "This is a blueprint."
