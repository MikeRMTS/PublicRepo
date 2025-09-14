import os
import sys
from flask import Flask, send_from_directory

# Dynamically add the 'common' directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
common_dir = os.path.join(current_dir, 'common')
sys.path.insert(0, common_dir)

# Import greet from utils.py
from utils import greet

# Print a greeting using the greet function
print(greet("Developer"))

# Create a Flask app to serve the HTML file
app = Flask(__name__)

@app.route('/')
def serve_index():
    html_dir = os.path.join(current_dir, 'html')
    return send_from_directory(html_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
