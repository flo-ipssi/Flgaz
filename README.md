# Flgaz

Application codée en python permettant d'envoyer et d'afficher des tweets 

## Contenu de l'application

#### Hader HTTP

L'application dispose de tous les entêtes standard dans le header. Elle comprend les déclarations d'un cache control, d'un access-control allow origin et d'un content-type.

#### Filtrage des messages (+ de 280 caractères)

Une fonctionnalité a été intégrée au projet afin de limiter le nombre de caractères possible à l'envoi d'un tweet.

#### Url message par utilisateur

L'utilisateur a la possibilité de consulter tous ses tweets envoyé sur l'application.

#### Pylint 

L'analyse statistique du code a été valider Pylint :app.py, setting.py
### 10/10

#### Blocage des messages doublons court ou long (en cours) 

L'ajout du filtrage des longs messages a permis à l'équipe de développement de se pencher sur la question des doublons sur les messages et d'envisager une solution pour régler ce problème 

#### Spammers (en cours)

Une autre mise à jour est en cours concernant les attaques de spams. Une limitation de requête est à envisager. 

#### Incident 15h35

Le serveur est tombé le 29/11 à 15h35 suite à l'ajout d'un filtrage. (point bonus 'barre')

#### V2.0 : Une base de données en cours de développement
Une tentative de création d'une base de données a été initiée, mais étant donné les difficultés rencontrées lors de la configuration et la mise de celle-ci ( les requêtes depuis le projet local jusqu'en prod n'étant pas permis, il aurait fallu un abonnement sur pythonanywhere.com pour configurer la base de donnée), le projet sera ajouté dans une prochaine version( models.py ).
