from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    # Placeholder for Bedrock integration
    return jsonify({
        "response": f"You said: {prompt}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)