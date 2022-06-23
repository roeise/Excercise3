from flask import Flask, render_template, redirect, url_for, request, session, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('Home.html')

@app.route('ContactUs')
def main():
    return render_template('/Contact_Us.html')

