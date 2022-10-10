from flask import Flask
from flask import request
from flask import render_template, url_for
from flask import redirect
from flask import session

from markupsafe import escape

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

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
        elif(json["account"]=="" or json["password"]==""):
            return redirect('/error?message=請輸入帳號密碼')
        else:
            return redirect('/error?message=帳號密碼輸入錯誤')
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
    
@app.route('/square/<int:num>')
def square(num):
    return render_template('number.html')

    
if __name__ == "__main__":
    app.run(port=3000, debug = True) 