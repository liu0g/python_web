#encoding=utf-8

#all the imports
import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
    abort,render_template,flash
from contextlib import closing

#create application
app = Flask(__name__)
# configuration
DATABASE = os.path.join(app.root_path,'flaskr.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME ='admin'
PASSWORD ='default'

# from_object() 会查看给定的对象
# （如果该对象是一个字符串就会 直接导入它），搜索对象中所有变量名均为大字字母的变量。
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title = row[0],text = row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html',entries = entries)

@app.route('/add',methods=['POST'])
def add_entry():
    # 检查用户是否登录
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) VALUES (?,?)',
                 [request.form['title'],request.form['text']])
    g.db.commit()
    flash('New entry was sucessfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','Post'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('you are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('you are logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
