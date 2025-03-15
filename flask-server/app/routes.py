from flask import Blueprint, jsonify


main = Blueprint("main", __name__)

@main.route("/")
def hello():
    return "Hello, World from Flask and Docker!"

@main.route("/ping", methods=["GET"])
def ping():
    """Verifica que el servidor esté funcionando"""
    return jsonify({"message": "pong"}), 200

@main.route("/status", methods=["GET"])
def status():
    """Devuelve el estado de la API"""
    return jsonify({"status": "running", "version": "1.0.0"}), 200
