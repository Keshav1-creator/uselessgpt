from flask import Flask, request, jsonify, send_from_directory
from .utils import generate_response  # Make sure utils.py exists and has generate_response()
import os

# Setup Flask app and static folder for frontend files
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../static'))
app.secret_key = os.getenv('SECRET_KEY', 'dev_secret_key')

# -----------------------------
# Serve the Frontend (index.html)
# -----------------------------
@app.route('/')
@app.route('/uselessgpt')
def index():
    return send_from_directory(app.static_folder, 'index.html')


# -----------------------------
# Chat API Endpoint (Frontend talks to this)
# -----------------------------
@app.route('/uselessgpt', methods=['POST'])
def uselessgpt():
    data = request.get_json()
    user_input = data.get("input", "")

    # Generate bot response using your utility
    reply = generate_response(user_input)

    return jsonify({"reply": reply})


# -----------------------------
# Helper Route (Optional)
# -----------------------------
@app.route('/uselessgpt/url')
def show_url():
    return jsonify({"url": "/uselessgpt"})


# -----------------------------
# Run the app
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
