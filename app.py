from flask import Flask, render_template, request, redirect, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from pandas_json import grab_data

app = Flask(__name__)

@app.route("/", methods=["GET", 'POST'])
def index():

    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST']) 
def search():

    query = request.args.get('q')
    if query:

        return redirect(url_for('player', player_name=query.lower()))
    
    return redirect(url_for('index'))


@app.route('/player/<player_name>')
def player(player_name):
    n = grab_data()
    player_data = n.get(player_name.lower())
    return render_template('player.html', player_name=player_name, data=player_data)

    
    
def compare():
    return






if __name__ in "__main__":
    app.run(debug=True)