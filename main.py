from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>This is a paragraph</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')