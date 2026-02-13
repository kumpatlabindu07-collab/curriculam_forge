from flask import Flask, render_template, jsonify

# Create Flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Example API route (Python backend)
@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Python Flask!"
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)