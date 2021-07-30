from flask import Flask,render_template

app = Flask(__name__)

a = "It Works!"
@app.route("/")
def home():
    return render_template('home.html', a=a)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")