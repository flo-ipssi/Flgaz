import sqlalchemy 
from sqlalchemy import Column, Boolean, String, Integer, Numeric, Text, Datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaration de la classe de déclaration des modèles de BDD
Base = declarative_base() 

# Création d'une classe selon la syntaxe objet SQLAlchemy
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column('username', String(255))
    role = Column('role', String(255))
    email = Column('email', String(255))
    password = Column('password', String(255))
    is_active = Column('is_active', Boolean)
    is_connected = Column('is_connected', Boolean)
    picture = Column('picture', Text)

    # methode magique pour print()
    def __str__(self):
        return "{} | {}".format(self.username, self.email)

class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    content = Column('content', String(64))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    categorie = Column('categorie', Integer)
    creator = Column('creator', Integer)

    # methode magique pour print()
    def __str__(self):
        return "{} | {}".format(self.content, self.categorie)


class Category(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    name = Column('categorie',  String(255))

    # methode magique pour print()
    def __str__(self):
        return "{}".format( self.name )

if __name__ == "__main__":
    engine = "mysql+mysqlconnector://{login}:{password}@{hostname}/{databasename}".format(
        login=setting.CONST_LOGIN,
        password=setting.CONST_PASSWORD,
        hostname=setting.CONST_HOST,
        databasename=setting.CONST_DATABASE,
    )
    Base.metadata.create_all(engine)