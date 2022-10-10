from flask import Flask
from flask import request
from flask import render_template, url_for
from flask import redirect
from markupsafe import escape

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/signin', methods=['POST'])
def signin():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if(json["account"]=="test" and json["password"]=="test"):
            return redirect('/member')
        else:
            return redirect('/error')
    else:
        return 'Content-Type not supported!'
    

    
if __name__ == "__main__":
    app.debug = True
    app.run() 