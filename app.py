from flask import Flask, render_template, request
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    height, width = 20, 20
    if request.method == "POST":
        height, width = request.form["height"], request.form["width"]
    GameOfLife(width=int(width), height=int(height))
    return render_template("index.html", width=width, height=height)

@app.route("/live")
def live():
    live = GameOfLife()
    if live.counter > 0:
        live.form_new_generation()
    live.counter += 1
    return render_template('live.html', live=live)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)