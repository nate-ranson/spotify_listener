import requests
import json
import time
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="PASSWORD",  # your password
                     db="spotify")        # name of the data base

db.set_character_set('utf8')


authorization_token = "TOKEN"
refresh_token = "TOKEN"
refresh_url = "https://accounts.spotify.com/api/token"

request = requests.post(refresh_url, data = {'grant_type':'refresh_token', 'refresh_token':refresh_token, 'redirect_uri':'http://localhost'}, headers = {"Authorization":"Basic " + authorization_token}
	)

key = request.json().get("access_token")

api_url = 'https://api.spotify.com/v1/me/player/currently-playing'

currently_playing = requests.get(api_url, headers={"Authorization":"Bearer " + key})

if currently_playing.json().get("is_playing") is not True:
	sys.exit(0)

album = currently_playing.json().get("item").get("album").get("name")
artist = []

for artists in currently_playing.json().get("item").get("artists"):
	artist.append(artists.get("name"))

artist = ', '.join(artist)
track = currently_playing.json().get("item").get("name")

if artist is not None and track is not None and album is not None:
	cur = db.cursor()
	cur.execute('SET NAMES utf8;')
	cur.execute('SET CHARACTER SET utf8;')
	cur.execute('SET character_set_connection=utf8;')


	sql = "INSERT INTO `spotify` (`artists`, `track`, `album`) VALUES (%s, %s, %s)"
	cur.execute(sql, (artist, track, album))
	db.commit()

