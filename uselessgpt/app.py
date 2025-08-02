

from flask import Flask, request, jsonify, send_from_directory
from .utils import generate_response
import os
import random

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../static'))
app.secret_key = os.getenv('SECRET_KEY', 'dev_secret_key')





# Serve index.html for root and /uselessgpt
@app.route('/')
@app.route('/uselessgpt')
def index():
    return send_from_directory(app.static_folder, 'index.html')



# App URL route
@app.route('/uselessgpt/url')
def show_url():
    return jsonify({"url": "/uselessgpt"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
