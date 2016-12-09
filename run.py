# from app import app
from flask import Flask, render_template, request, json, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('signup.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('login.html')

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    return render_template('dashboard.html')

    
@app.route("/logout")
def logout():
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)