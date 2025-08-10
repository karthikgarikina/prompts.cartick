from flask import Flask, request, jsonify, render_template
import os
import psycopg2

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# --- Database Connection ---
DATABASE_URL = os.environ.get("DATABASE_URL")
db_conn = psycopg2.connect(DATABASE_URL)

def setup_database():
    with db_conn.cursor() as cur:
        # Create table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usage (
                id INT PRIMARY KEY,
                count INT NOT NULL
            );
        """)
        # Insert the initial row if it doesn't exist
        cur.execute("INSERT INTO usage (id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING;")
        db_conn.commit()

# --- New functions to read/write from the database ---
def load_usage():
    with db_conn.cursor() as cur:
        cur.execute("SELECT count FROM usage WHERE id = 1;")
        # Fetchone() returns a tuple, e.g., (111,)
        result = cur.fetchone()
        return result[0] if result else 0

def save_usage(current_count):
    with db_conn.cursor() as cur:
        cur.execute("UPDATE usage SET count = %s WHERE id = 1;", (current_count,))
        db_conn.commit()

# Run setup once when the app starts
setup_database()
# Load initial count from DB
usage_count = load_usage()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    from prompts import generate_prompt # Keep import here for now
    global usage_count
    data = request.get_json()
    goal = data.get("goal", "").strip()
    tool = data.get("tool", "").strip()

    if not goal:
        return jsonify({"error": "Goal is required"}), 400

    prompt = generate_prompt(goal, tool)
    usage_count += 1
    save_usage(usage_count) # Save the new count to the database

    return jsonify({
        "generated_prompt": prompt,
        "usage_count": usage_count
    })

@app.route("/usage", methods=["GET"])
def usage():
    # To ensure it's always fresh, you could load it again here
    # current_usage = load_usage()
    return jsonify({"count": usage_count})

if __name__ == "__main__":
    app.run(debug=True)