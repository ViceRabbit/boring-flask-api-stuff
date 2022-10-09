from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class rabbit(db.Model): # database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) # 80 is the amount of chars
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} ~ {self.description}'

@app.route('/') # basically endpoints ig
def index():
    return 'hi universee'

@app.route('/rabbits') # accessing /rabbits
def getRabbits():
    rabbits = rabbit.query.all() # database, created instances in terminal
    output = []  # rabbits isnt iterable to show so
    for Rabbit in rabbits:
        RabbitInfo = {"Name": Rabbit.name, "Description": Rabbit.description, "Id": Rabbit.id}
        output.append(RabbitInfo)

    return {"rabbits": output} # json

@app.route('/rabbits/<id>') # search rabbits by id 
def getRabbit(id):
    Rabbit = rabbit.query.get_or_404(id)
    return {"Name": Rabbit.name, "Description": Rabbit.description}


@app.route('/rabbits', methods=['POST']) # adding rabbits (web.postman.co)
def add_rabbit():
    try:
        Rabbit = rabbit(name=request.json['name'], description=request.json['description'])
    except KeyError:
        return {"ERROR": "WRONG JSON FORMAT; Ensure it's 'name':<str> and 'description':<str>."}
    db.session.add(Rabbit)
    db.session.commit()
    return {'id': Rabbit.id}

@app.route('/rabbits/<id>', methods=['DELETE'])
def del_rabbit(id):
    Rabbit = rabbit.query.get_or_404(id)
    db.session.delete(Rabbit)
    db.session.commit()
    return {"Deletion": "Successfully deleted.. I guess."}