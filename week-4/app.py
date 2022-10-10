from flask import Flask
from flask import request
from flask import render_template, url_for
from flask import redirect
from flask import session

from markupsafe import escape

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")
app.debug = True

app.secret_key = 'sexy_secret_key'


@app.route('/')
def index():
    if 'account' in session:
        return redirect('/member')
    return render_template('index.html')

@app.route('/member')
def member():
    if 'account' in session:
        return render_template('member.html')
    else:
        return redirect('/')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/signin', methods=['POST'])
def signin():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if(json["account"]=="test" and json["password"]=="test"):
            session['account'] = json['account']
            return redirect('/member')
        else:
            return redirect('/error?message=你是個失敗者,沒有仁愛你,但基隆有仁愛區')
    else:
        return 'Content-Type not supported!'
    
@app.route('/logout', methods=['POST'])
def logout():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if(json["logout"]=="true"):
            session.pop('account', None)
            return redirect('/')
        else:
            return redirect('/member')
    else:
        return 'Content-Type not supported!'
    

    
if __name__ == "__main__":
    app.debug = True
    app.run() 