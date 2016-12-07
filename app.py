# Importing flask module, render template which is used to render template files,
# request to read posted values
from flask import Flask, render_template, request, json



# Creating app using flask
app = Flask(__name__)

app.config['Debug']=True

# Define the basic route / and its corresponding request handler
@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')

# Define the route for signup and render the signup page once the request
# comes to the route
@app.route("/showSignUp")
def signup():
    return render_template('signup.html')

# Define the route for signup and render the signup page once the request
# comes to the route
@app.route("/showSignIn")
def signin():
    return render_template('signin.html')

# Define the route for signup and render the signup page once the request
# comes to the route
@app.route("/showLanding")
def landing():
    return render_template('landingpage.html')

# Next, check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.run()