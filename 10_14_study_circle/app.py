from flask import Flask
from flask import request
from flask import Response
from markupsafe import escape
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)


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

@app.route('/fetch', methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def fetch():
    print(request.content_type)
    print(request.json)
    return Response("{'status':'201'}", status=201, mimetype='application/json')


    
if __name__ == "__main__":
    app.run(port=3000, debug = True) 