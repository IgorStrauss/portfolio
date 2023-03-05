from flask import Flask, render_template, url_for, abort
from datetime import date

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/sobre")
def sobre():
    return render_template("about.html")


@app.route("/certificacoes")
def certificacoes():
    return render_template("post.html")

if __name__ == '__main__':
    app.run(debug=False)
