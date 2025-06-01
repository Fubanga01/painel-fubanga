
from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'ritual7'

client = MongoClient(os.getenv("MONGO_URI", "mongodb+srv://Fubanga:M27p08_14@clusters.axdjwb8.mongodb.net/?retryWrites=true&w=majority&appName=Clusters"))
db = client.ritual_db

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    if request.form['username'] == 'admin' and request.form['password'] == 'ritual7':
        session['auth'] = True
        return redirect('/painel')
    return redirect('/')

@app.route('/painel')
def painel():
    if not session.get('auth'):
        return redirect('/')
    dados = list(db.executions.find().limit(20))
    return render_template('painel.html', dados=dados)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)


