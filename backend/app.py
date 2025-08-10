from flask import Flask, request, jsonify, render_template
import json
from prompts import generate_prompt

app = Flask(__name__, template_folder="../templates", static_folder="../static")

USAGE_FILE = "usage_counter.json"

# Load / save usage count
def load_usage():
    try:
        with open(USAGE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"count": 0}

def save_usage(data):
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f)

usage_data = load_usage()
usage_count = usage_data.get("count", 0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    global usage_count
    data = request.get_json()
    goal = data.get("goal", "").strip()
    tool = data.get("tool", "").strip()

    if not goal:
        return jsonify({"error": "Goal is required"}), 400

    prompt = generate_prompt(goal, tool)
    usage_count += 1
    save_usage({"count": usage_count})

    return jsonify({
        "generated_prompt": prompt,
        "usage_count": usage_count
    })

@app.route("/usage", methods=["GET"])
def usage():
    return jsonify({"count": usage_count})

if __name__ == "__main__":
    app.run(debug=True)
