import csv
from flask import Flask, request, render_template, redirect, url_for
"""
    # Apres l importation du module Flask
    # On lui un nom d application app
"""
app = Flask(__name__)

"""
    # On definit une page (ou route) avec flask
    # app route permet de préciser a quelle adresse
    # ce qui suit va s appliquer
"""

@app.route('/')
def home():
    """
    Definition d une route avec deux types de methode
    """
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """
    Definition d une route avec deux types de methode
    """
    if request.method == 'POST':
        if len(request.form.get("user-text")) <= 280:
            print(request.form)
            dump_to_csv(request.form)
        return redirect(url_for('timeline'))
                
    if request.method == 'GET':
        return render_template('formulaire.html')


@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/timeline', methods=['GET'])
def timeline():
    """
    Definition d une route timeline
    """
    gaz = parse_from_csv()
    return render_template("timeline.html", gaz=gaz)

def parse_from_csv():
    """    
    Definition de parse pour le csv
    """
    gaz = []
    with open('./gazouilles.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            gaz.append({"user":row[0], "text":row[1]})
    return gaz

def dump_to_csv(d):
    donnees = [d["user-name"], d["user-text"]]
    if len(d["user-text"]) <= 280:
        with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(donnees)


@app.route('/timeline/<username>/', methods=['GET'])
def timelineuser(username):
    """
    Definition d une route timeline par user
    """
    gaz = parse_user_from_csv(username)
    return render_template("timeline.html", gaz=gaz)
def parse_user_from_csv(user_id):
    """
    Definition de parse  par user
    """
    gaz = []
    with open('./gazouilles.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == user_id:
                gaz.append({"user":row[0], "text":row[1]})
    return gaz

