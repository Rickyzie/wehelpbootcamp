from flask import Flask, Response
from flask import request
from flask import render_template, url_for
from flask import redirect
from flask import session
import mysql.connector
import json

dbconfig = {
    "host":"localhost",      
    "user":"root",    
    "passwd":"aa24572880",   
    "database": "website"
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "mypool",
    pool_size = 10,
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
            return render_template('member.html', name = session["name"])
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
        sql = "SELECT * FROM member WHERE username = %s AND password = %s"
        na = (json["username"], json["password"])
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        session["id"] = myresult[0][0]
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
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (json["name"], json["username"], json["password"])
        mycursor.execute(sql, val)
        cnx.commit()
        cnx.close()
        return redirect('/')
    
    


@app.route('/api/member', methods=['GET'])
def apiMember():
    try:
        if 'name' in session:
            sql = "SELECT * FROM member WHERE username = %s"
            val = (request.args.get('username'),)
            cnx = cnxpool.get_connection()
            mycursor = cnx.cursor()
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall() 
            cnx.close()
            data = {
                "data":{
                    "id":myresult[0][0],
                    "name":myresult[0][1],
                    "username":myresult[0][2]
                }
            }
        else:
            raise Exception
        return Response(json.dumps(data), status=201, mimetype='application/json')
    except:
        return Response('{"data":null}', status=201, mimetype='application/json')
    
@app.route('/api/member', methods=['PATCH'])
def patchMember():
    try:
        json = request.json
        cnx = cnxpool.get_connection()
        mycursor = cnx.cursor()
        sql = "UPDATE member  SET name = %s WHERE id = %s"
        val = (json["name"], session["id"])
        session["name"] = json["name"]
        mycursor.execute(sql, val)
        cnx.commit()
        cnx.close()
        return Response('{"ok":true}', status=201, mimetype='application/json')
    except:
        return Response('{"error":true}', status=201, mimetype='application/json')

@app.route('/api/memberName', methods=['GET'])
def memberName():
    if 'name' in session:
        data = {
            "data":{
                "name":session["name"]
            }
        }
        return Response(json.dumps(data), status=201, mimetype='application/json')
    else:
        return Response('{"error":true}', status=201, mimetype='application/json')
        
if __name__ == "__main__":
    app.run(port=3000, debug = True) 
