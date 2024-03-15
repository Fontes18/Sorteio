from flask import Flask, render_template
import random2
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('Sorteio.html')


@app.route("/ganhador", methods=["POST"])
def ganhador():
    lista = [
        "Honda civic",
        "Veloster",
        "Corolla"
    ]
    gan = random2.choice(lista)
    return render_template("Sorteio.html", sorteado=gan)
if __name__ == "__main__":
    app.run(debug=True)