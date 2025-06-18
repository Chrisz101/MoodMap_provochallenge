from flask import Flask, request, jsonify, render_template
from reddit_client import get_posts
from sentiment import analyze_emotion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    subreddits = data.get("subreddits", [])
    num_posts = int(data.get("num_posts", 5))
    result_map = {}

    for sub in subreddits:
        posts = get_posts(sub)[:num_posts]
        result_map[sub] = [{"text": p, "emotion": analyze_emotion(p)} for p in posts]

    return jsonify(result_map)

if __name__ == "__main__":
    app.run(debug=True)

