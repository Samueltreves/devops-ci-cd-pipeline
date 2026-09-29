

from flask import Flask, jsonify

app = Flask(name)

@app.route('/')
def home():
return jsonify({"status": "success", "message": "DevOps CI/CD Pipeline App is Running!"})

@app.route('/about')
def about():
return jsonify({"version": "1.0.0", "author": "Samuel Treves"})

if name == 'main':
app.run(host='0.0.0.0', port=5000)
