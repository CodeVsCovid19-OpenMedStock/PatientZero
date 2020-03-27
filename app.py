from flask import *  #Flask, render_template, request, redirect
import pymysql
from flask_bootstrap import Bootstrap
import json, os.path

app = Flask(__name__)
app.secret_key = 'asldfajslk230asdlfjasdlfkj923kw20929834828394018923klklasdhiguS9D34' # key used to send messages to the user with flash 
Bootstrap(app)



class Database:
    def __init__(self):
        host = "sql7.freemysqlhosting.net"
        user = "sql7329640"
        password = "Q6FRAYZr56"
        db = "sql7329640"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_medical_offices(self):
        self.cur.execute("SELECT id, name, zip_code FROM medical_offices LIMIT 50")
        result = self.cur.fetchall()

        return result


#######################################################################################################################################
@app.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('static/css/', path)


#######################################################################################################################################
@app.route('/')
def home():
    return render_template('/index.html' )



#######################################################################################################################################
@app.route('/search-result')
def search_results():
    def db_query():
        db = Database()
        emps = db.list_medical_offices()
        return emps
    res = db_query()
    return render_template('search_results.html', result=res, content_type='application/json')