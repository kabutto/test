from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "index"


@app.route("/detail")
def detail():
    return "detail"


@app.route("/next")
def next():
    return "next"


if __name__ == "__main__":
    app.run(debug=True)

