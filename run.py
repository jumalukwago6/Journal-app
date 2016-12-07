# from app import app
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('signup.html')

if __name__ == "__main__":
	app.run(debug=True, port=4000)