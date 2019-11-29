"""
Definition d une route avec deux types de methode
"""

import csv
from flask import Flask, request, render_template, redirect, url_for

    # Apres l importation du module Flask
    # On lui un nom d APPlication APP

APP = Flask(__name__)

"""
    # On definit une page (ou route) avec flask
    # APP route permet de préciser a quelle adresse
    # ce qui suit va s APPliquer
"""



@APP.route('/')
def home():
    """
    Definition d une route avec deux types de methode
    """
    return 'Bienvenue !'

@APP.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """
    Definition d une route avec deux types de methode
    """

    if request.method == 'POST':
        if len(request.form.get("user-text")) <= 280:
            for word in request.form.get("user-text").split():
                if word.lower() != 'barre':
                    print(request.form)
                    dump_to_csv(request.form)
        return redirect(url_for('timeline'))


    return render_template('formulaire.html')

@APP.after_request
def add_header(response):
    """
    Definition du header
    """

    response.cache_control.max_age = 300
    response.headers['Access-Control-Allow-Origin'] = 'http://ipssiflo.pythonanywhere.com/'
    return response


@APP.route('/timeline/', methods=['GET'])
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
    with open('./gazouilles.csv', 'r') as __file__:
        reader = csv.reader(__file__)
        for row in reader:
            gaz.append({"user":row[0], "text":row[1]})
    return gaz

def dump_to_csv(__data__):
    """
    Definition de parse pour le csv
    """
    __donnees__ = [__data__["user-name"], __data__["user-text"]]
    if len(__data__["user-text"]) <= 280:
        with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as __file__:
            writer = csv.writer(__file__)
            writer.writerow(__donnees__)


@APP.route('/timeline/<username>/', methods=['GET'])
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
    with open('./gazouilles.csv', 'r') as __file__:
        reader = csv.reader(__file__)
        for row in reader:
            if row[0] == user_id:
                gaz.append({"user":row[0], "text":row[1]})
    return gaz
