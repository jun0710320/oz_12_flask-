from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, ysh"

@app.route("/hello/<name>", methods=["GET"], endpoint="hello-oz")
def hello(name : str) -> str:
    return f"Hello, [name]"


if __name__ == '__main__':
    app.run(debug=True)

with app.test_request_context():
    print(url_for("hello-oz", name="farmer"))