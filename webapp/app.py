from flask import Flask, render_template, request, jsonify

from services.bedrock import invoke_model

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy"
        }
    )


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    if not data:
        return jsonify(
            {
                "error": "Invalid JSON body."
            }
        ), 400

    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify(
            {
                "error": "Prompt cannot be empty."
            }
        ), 400

    try:
        response = invoke_model(prompt)

        return jsonify(
            {
                "response": response
            }
        )

    except Exception as e:
        return jsonify(
            {
                "error": str(e)
            }
        ), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )