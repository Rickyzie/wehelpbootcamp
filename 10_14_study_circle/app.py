from flask import Flask
from flask import request
from flask import Response
from markupsafe import escape
from flask_cors import CORS
from flask import Flask, session
from flask_session.__init__ import Session

app = Flask(__name__)
# Check Configuration section for more details

#eyJrZXkiOiJhc2Rkc2EifQ.Y0e7xg.dTIwDDYRjTlkNHE9dZQLKnIYWag
#eyJrZXkiOiJhc2Rkc2FhYWFhYSJ9.Y0e79A.gLzuAuv0vMihbDR3PYl_6DAchb0
#eyJrZXkiOiIifQ.Y0e8BA.X_fUj4GSTUuTUWaBN3PQP1ivaEY
#eyJrZXkiOm51bGx9.Y0e8LA.5fw5HRcKzQDxS5DSTHA3tHfl7Lo
cors = CORS(app, resources={r"/fetch": {"origins": "*"}})

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.secret_key =  "1"

@app.route('/set/')
def set():
    session['key'] = request.args.get('data')
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route('/form', methods=['POST'])
def form():
    print(request.content_type)
    print(request.form)
    return Response("{'status':'201'}", status=201, mimetype='application/json')

@app.route('/application', methods=['POST'])
def application():
    print(request.content_type)
    print(request.form)
    return Response("{'status':'201'}", status=201, mimetype='application/json')

@app.route('/json', methods=['POST'])
def json():
    print(request.content_type)
    print(request.json)
    return Response("{'status':'201'}", status=201, mimetype='application/json')


cors = CORS(app, resources={r"/fetch": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/fetch', methods=['POST'])
def fetch():
    print(request.content_type)
    print(request.json)
    return Response("{'status':'201'}", status=201, mimetype='application/json')


    
if __name__ == "__main__":
    app.run(port=3000, debug = True) 