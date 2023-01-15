from flask import Flask, render_template, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = "c7921ab58c09902b64a266614304bbe"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)