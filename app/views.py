from flask import Flask 

@app.route('/')
def index():
	return 'juma app'