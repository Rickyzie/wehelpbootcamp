from flask import Flask
from flask import request
from flask import render_template, url_for
from flask import redirect
from flask import session
from markupsafe import escape
import mysql.connector

dbconfig = {
    "host":"localhost",      
    "user":"root",    
    "passwd":"aa24572880",   
    "database": "member_db"
}



cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "mypool",
    pool_size = 2,
    **dbconfig
)


app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

app.secret_key = 'sexy_secret_key'

@app.route('/')
def index():
    if 'name' in session:
        return redirect('/member')
    
    return render_template('index.html')

@app.route('/member')
def member():
    try:
        if 'name' in session:
            cnx = cnxpool.get_connection()
            mycursor = cnx.cursor()
            mycursor.execute("SELECT * FROM message")
            myresult = mycursor.fetchall() 
            content = ""
            
            for x in myresult:
                component = '<h1><span id="message">{}:{}</span></h1>'.format(escape(x[1]), escape(x[2])) 
                content+=component
            
            return render_template('member.html', content = content, name = session["name"])
        else:
            return redirect('/')
    except:
        return redirect('/')

@app.route('/error')
def error():
    message = request.args.get('message')
    return render_template('error.html', message = message)

@app.route('/login', methods=['POST'])
def signin():
    try:
        json = request.form
        cnx = cnxpool.get_connection()
        mycursor = cnx.cursor()
        sql = "SELECT * FROM member WHERE account = %s AND password = %s"
        na = (json["account"], json["password"])
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        session['name'] = myresult[0][1]
        cnx.close()
        return redirect('/member')
    except:
        return redirect('/error?message=帳號或密碼輸入錯誤')
    
@app.route('/logout', methods=['POST'])
def logout():
    form = request.form
    print(form)
    if(form["logout"]=="true"):
        session.pop('name', None)
        return redirect('/')
    else:
        return redirect('/member')
    
@app.route('/signup', methods=['POST'])
def signup():    
        json = request.form
        cnx = cnxpool.get_connection()
        mycursor = cnx.cursor()
        sql = "INSERT INTO member (name, account, password) VALUES (%s, %s, %s)"
        val = (json["name"], json["account"], json["password"])
        mycursor.execute(sql, val)
        cnx.commit()
        cnx.close()
        return redirect('/')
    
    
@app.route('/message', methods=['POST'])
def message():
    json = request.form
    sql = "INSERT INTO message (message_member, message) VALUES (%s, %s)"
    val = (session["name"], json["message"])
    cnx = cnxpool.get_connection()
    mycursor = cnx.cursor()
    mycursor.execute(sql, val)
    cnx.commit()
    cnx.close()
    return redirect('/member')
    
if __name__ == "__main__":
    app.run(port=3000, debug = True) 
