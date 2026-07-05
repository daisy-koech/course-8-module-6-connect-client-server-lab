from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
events = [
    {"id": 1, "title": "Tech Meetup"},
    {"id": 2, "title": "Python Workshop"}
]

# Home route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome"}), 200

# GET /events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# POST /events
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    new_event = {
        "id": len(events) + 1,
        "title": data["title"]
    }

    events.append(new_event)

    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
