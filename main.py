#This part initialises flask
from flask import Flask,render_template
app = Flask(__name__)

#address
address = "27 Punggol Field Walk, Singapore 828649"

#This variable is displayed on the homepage
a = "It Works!"

#This creates the home route because there is nothing after the '/'
@app.route("/")
def home():
    return render_template('home.html', a=a)

@app.route("/login")
def login():
    return render_template('login.html', a=a)

@app.route("/individual")
def login():
    return render_template('individual.html', a=a)

@app.route("/business")
def login():
    return render_template('business.html', a=a)

@app.route("/about")
def about():
    return render_template('home.html', a=a)

#This part runs the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")