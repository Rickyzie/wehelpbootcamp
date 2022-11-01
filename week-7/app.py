from unicodedata import name
from flask import Flask, Response, request, render_template, redirect, session
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
    pool_size = 5,
    **dbconfig
)

class UserSession:    
    def getSessionName(self):
        return session["name"]
    
    def setSessionByName(self, name):
        session["name"] = name
        
    def popSessionName(self):
        session.pop("name", None)
        
    def getSessionId(self):
        return session["id"]
        
    def setSessionById(self, id):
        session["id"] = id
        
    def popSessionId(self):
        session.pop("id", None)
    
    def isLogin(self):
        if "id" in session:
            return True
        else:
            return False

class MysqlConnecter:
    def __init__(self, sql, na):
        self.cnx = cnxpool.get_connection()
        self.mycursor = self.cnx.cursor(buffered=True)
        self.sql = sql
        self.na = na
    def execute(self):
        self.mycursor.execute(self.sql, self.na)
        
    def commit(self):
        self.cnx.commit()
        
    def close(self):
        self.cnx.close()
        self.mycursor.close()
        
    def fetchall(self):
        self.results = self.mycursor.fetchall()
        
    

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

app.secret_key = 'sexy_secret_key'

user = UserSession()

@app.route('/')
def index():
    try:
        if user.isLogin():
            return redirect('/member')
    except Exception as e:
        print(e)
    else:
        return render_template('index.html')

@app.route('/member')
def member():
    try:
        if user.isLogin():
            return render_template('member.html')
    except Exception as e:
        print(e)
        return redirect('/')
    else:
        return redirect('/')

@app.route('/error')
def error():
    try:
        message = request.args.get('message')
        return render_template('error.html', message = message)
    except Exception as e:
        print(e)
        return redirect('/')

@app.route('/login', methods=['POST'])
def signin():
    try:
        json = request.form
        sql = "SELECT * FROM member WHERE username = %s AND password = %s"
        na = (json["username"], json["password"])
        mc = MysqlConnecter(sql, na)
        mc.execute()
        mc.fetchall()
        user.setSessionById(mc.results[0][0])
        user.setSessionByName(mc.results[0][1])
    except Exception as e:
        print(e)
        mc.close()
        return redirect('/error?message=帳號或密碼輸入錯誤')
    else:
        mc.close()
        return redirect('/member')
        
    
@app.route('/logout', methods=['POST'])
def logout():
    try:
        form = request.form
        if(form["logout"]=="true"):
            user.popSessionId()
            user.popSessionName()
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')
    else:
        return redirect('/member')
    
@app.route('/signup', methods=['POST'])
def signup():    
    try:
        json = request.form
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        na = (json["name"], json["username"], json["password"])
        mc = MysqlConnecter(sql, na)
        mc.execute()
        mc.commit()
        mc.close()
        return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/error?message=資料輸入不完整')
    
    
@app.route('/api/member', methods=['GET'])
def apiMember():
    try:
        if user.isLogin():
            sql = "SELECT * FROM member WHERE username = %s"
            na = (request.args.get('username'),)
            mc = MysqlConnecter(sql, na)
            mc.execute()
            mc.commit()
            mc.fetchall()
            mc.close()
            data = {
                "data":{
                    "id":mc.results[0][0],
                    "name":mc.results[0][1],
                    "username":mc.results[0][2]
                }
            }
            return Response(json.dumps(data), status=201, mimetype='application/json')
        else:
            return Response('{"data":null}', status=201, mimetype='application/json')
    except Exception as e:
        print(e)
        mc.close()
        return Response('{"data":null}', status=201, mimetype='application/json')
    
        
        
    
@app.route('/api/member', methods=['PATCH'])
def patchMember():
    try:
        if user.isLogin():
            json = request.json
            sql = "UPDATE member  SET name = %s WHERE id = %s"
            na = (json["name"], session["id"])
            mc = MysqlConnecter(sql, na)
            mc.execute()
            mc.commit()
            mc.close()
            user.setSessionByName(json["name"])
            return Response('{"ok":true}', status=201, mimetype='application/json')
        else:
            return Response('{"error":true}', status=201, mimetype='application/json')
    except Exception as e:
        print(e)
        mc.close()
        return Response('{"error":true}', status=201, mimetype='application/json')
    
@app.route('/api/memberName', methods=['GET'])
def memberName():
    try:
        if user.isLogin():
            data = {
                "data":{
                    "name":user.getSessionName()
                }
            }
            return Response(json.dumps(data), status=201, mimetype='application/json')
    except Exception as e:
        print(e)
    else:
        return Response('{"error":true}', status=201, mimetype='application/json')

if __name__ == "__main__":
    app.run(port=3000, debug = True) 
