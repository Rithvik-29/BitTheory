#This part initialises flask
from flask import Flask,render_template, request
app = Flask(__name__)
isLockdown = {
    'singapore':False,
    'india':False,
    'australia':False,
    'usa':True,
    'uk':False,
    'malaysia':True,
}

#address
address = "27 Punggol Field Walk, Singapore 828649"

#This variable is displayed on the homepage
a = "It Works!"

#This creates the home route because there is nothing after the '/'
@app.route("/")
def home():
    return render_template('home.html', a=a)

#This is the app route for the login page
@app.route("/login")
def login():
    return render_template('login.html', a=a)

#This is the app route for the individual account
@app.route("/individual")
def individual():
    return render_template('individual.html', isLockdown=isLockdown)

#This is the app route for the business account
@app.route("/business")
def business():
    return render_template('business.html',name=request.args.get('name'))

@app.route("/about")
def about():
    return render_template('about.html', a=a)

@app.route("/floaty")
def floaty():
    return render_template('floaty.html')

@app.route("/snake")
def snake():
    return render_template('snake.html')

@app.route("/action")
def action():
    if request.args.get('userType') == 'individual':
        return render_template('/individual.html',userType=request.args.get('userType'),isLockdown=isLockdown,name=request.args.get('name'),country=request.args.get('country'))
    elif request.args.get('userType') == 'business':
        return render_template('/business.html',name=request.args.get('name'),country=request.args.get('country'),userType=request.args.get('userType'))
    else:
        return render_template('/individual.html',userType=request.args.get('userType'),isLockdown=isLockdown,name=request.args.get('name'),country=request.args.get('country'))

#This part runs the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")