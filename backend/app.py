from flask import Flask, request, jsonify
from chatbot import handle_query

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    user_input = data.get("question", "")
    response = handle_query(user_input)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
