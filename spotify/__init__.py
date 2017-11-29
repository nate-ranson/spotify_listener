from flask import Flask, render_template, json, jsonify
import requests
import json
import time
import MySQLdb
import sys
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def main():
	return render_template("index.html", title = "Anychart Python template")

@app.route("/api/artists")
def artists():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="PASSWORD",  # your password
                     db="spotify")        # name of the data base

	db.set_character_set('utf8')

	cursor = db.cursor()

	cursor.execute("SELECT artists, count(artists) as count from spotify group by artists order by count desc limit 10")
	data = cursor.fetchall()
	db.close()
	
	json = []
        for artist in data:
                json.append({'artist':artist[0], 'count':artist[1]})
        return jsonify(json)

@app.route("/api/tracks")
def tracks():
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="PASSWORD",  # your password
                     db="spotify")        # name of the data base

        db.set_character_set('utf8')

        cursor = db.cursor()

        cursor.execute("SELECT track, count(track) as count, artists from spotify group by track, artists order by count desc limit 10")
        data = cursor.fetchall()
	db.close()

	json = []
	for artist in data:
		json.append({'track':artist[0], 'count':artist[1], 'artist':artist[2]})
        return jsonify(json)

@app.route("/api/albums")
def albums():
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="PASSWORD",  # your password
                     db="spotify")        # name of the data base

        db.set_character_set('utf8')

        cursor = db.cursor()

        cursor.execute("SELECT album, count(album) as count, artists from spotify group by album, artists order by count desc limit 10")
        data = cursor.fetchall()
	db.close()

	json = []
        for artist in data:
                json.append({'album':artist[0], 'count':artist[1], 'artist':artist[2]})
        return jsonify(json)

@app.route("/api/latest")
def latest():
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="PASSWORD",  # your password
                     db="spotify")        # name of the data base

        db.set_character_set('utf8')

        cursor = db.cursor()

        cursor.execute("SELECT * from spotify order by id desc limit 10")
        data = cursor.fetchall()
	db.close()

        json = []
        for artist in data:
                json.append({'time':artist[1], 'artist':artist[2], 'track':artist[3], 'album':artist[4]})
        return jsonify(json)

if __name__ == "__main__": 
	app.run()

