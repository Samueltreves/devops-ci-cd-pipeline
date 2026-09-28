



from flask import Flask, jsonify


app = Flask(name)


@app.route('/')
def home():
return jsonify({"status": "success", "message": "DevOps CI/CD Pipeline App is Running!"})


@app.route('/health')
def health():
return jsonify({"status": "healthy"}), 200


if name == 'main':
app.run(host='0.0.0.0', port=5000)


