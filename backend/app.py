# ...existing code...
from flask import Flask, request, jsonify
import uuid

sessions = {}  # {session_id: [messages]}

@app.route("/sessions", methods=["GET"])
def get_sessions():
    return jsonify(list(sessions.keys()))

@app.route("/sessions/<session_id>", methods=["GET"])
def get_session_history(session_id):
    return jsonify(sessions.get(session_id, []))

@app.route("/sessions", methods=["POST"])
def create_session():
    session_id = str(uuid.uuid4())
    sessions[session_id] = []
    return jsonify({"session_id": session_id})

@app.route("/sessions/<session_id>/message", methods=["POST"])
def add_message_to_session(session_id):
    msg = request.get_json().get("message")
    sessions.setdefault(session_id, []).append(msg)
    return jsonify({"success": True})
# ...existing code...
