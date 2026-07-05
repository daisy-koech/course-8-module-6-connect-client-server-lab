from flask import Flask, request, jsonify, render_template
from data import get_event_data

events = get_event_data()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")

@app.route("/events", methods=["GET"])
def get_data():
    return jsonify(events), 200

@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    if not data or "title" not in data:
        return ({"error": "title is required"}), 400
    new_event = {
        "id": len(events) + 1,
        "title": data["title"]
    }
    events.append(new_event)
    
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
