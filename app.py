
# flask 클래스를 import 한다.
from flask import Flask, render_template, url_for

# flask 클래스를 인스턴스화한다.
app = Flask(__name__)

# URL과 실행할 함수를 매핑한다.
@app.route("/", endpoint="dendpoint-name")
def index():
    return "Hello, Flask!"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"hello, {name}"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    print(url_for("index"))
    