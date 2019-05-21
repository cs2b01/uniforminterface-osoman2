from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()


app = Flask(__name__)


@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Usuario)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')



if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug = True, threaded=True, port=8060, host=('0.0.0.0'))

