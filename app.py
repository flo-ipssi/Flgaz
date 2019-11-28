from flask import Flask, request, render_template, redirect, url_for
import csv
import sys


# Après l'importation du module Flask 
# On lui un nom d'application "app"
app = Flask(__name__)

# On définit une page (ou route) avec flask
#@app.route permet de préciser à quelle adresse 
#ce qui suit va s’appliquer.
@app.route('/')
def home():     
    return 'Bienvenue !'


#Definition d'une route avec deux types de methode 
@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		dump_to_csv(request.form)
		return redirect(url_for('timeline'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')


@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    response.access_control_allow_origin = '*'
    return response


@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	return render_template("timeline.html", gaz = gaz)

def parse_from_csv():
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)