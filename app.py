from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to the home page!"

@app.route("/hello")
def hello():
    return "Hello from openshift!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)