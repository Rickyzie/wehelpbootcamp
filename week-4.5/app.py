from email import message
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
    message = request.args.get('message')
    return render_template('error.html', message = message)

@app.route('/signin', methods=['POST'])
def signin():
    json = request.form
    if(json["account"]=="test" and json["password"]=="test"):
        session['account'] = json['account']
        return redirect('/member')
    elif(json["account"]=="" or json["password"]==""):
        return redirect('/error?message=請輸入帳號密碼')
    else:
        return redirect('/error?message=帳號密碼輸入錯誤')
    
@app.route('/logout', methods=['POST'])
def logout():
    form = request.form
    print(form)
    if(form["logout"]=="true"):
        session.pop('account', None)
        return redirect('/')
    else:
        return redirect('/member')
   
    
@app.route('/square/<int:num>')
def square(num):
    return render_template('number.html', num = num**2)

    
if __name__ == "__main__":
    app.run(port=3000, debug = True) 