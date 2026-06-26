from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Healthcare API Version 1"

@app.route("/health")
def health():
    return {"status":"UP"}

app.run(host="0.0.0.0",port=5000)
