from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    data = [["Reddit", "Astrophysicist", "Redditor"], ["Google", "Googler", "Programmer"]]
    return render_template("webpage.html", data=data)
