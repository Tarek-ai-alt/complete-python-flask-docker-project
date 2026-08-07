from flask import Blueprint, current_app, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def home():
    return jsonify(
        application=current_app.config["APP_NAME"],
        message="Hello from Flask and Docker!",
        status="running"
    )


@main_bp.get("/health")
def health():
    return jsonify(status="healthy"), 200
