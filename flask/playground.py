from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play1():
    return render_template("play.html", num=3,color="black")


@app.route("/play/<num>")
def play2(num):
    return render_template("play.html", num=int(num),color="black")


@app.route("/play/<num>/<color>")
def play3(num,color):
    return render_template("play.html", num=int(num),color=color)

if __name__ == "__main__":
    app.run(debug=True)
