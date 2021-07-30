#This part initialises flask
from flask import Flask,render_template
app = Flask(__name__)

#This variable is displayed on the homepage
a = "It Works!"

#This creates the home route because there is nothing after the '/'
@app.route("/")
def home():
    return render_template('home.html', a=a)

#This part runs the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")