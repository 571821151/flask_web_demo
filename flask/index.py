from flask import Flask,request,render_template,flash,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from Forms.login_form import LoginForm
from Forms.name import BulletinForm
from flask_bootstrap import Bootstrap
import os

app=Flask(__name__)
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '123456'

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


@app.route('/')
@app.route('/search/<keyword>')
def index(keyword=""):
    if  keyword=='':
        return render_template('index.html')
    else:
        return redirect('user')

@app.route('/user')
def user():
   return render_template('user.html',name='cly')

@app.route('/test',methods=['GET','Post'])
def test():
    form = BulletinForm(request.form)
    flash('sb')
    return render_template("test.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def internal_server_error(e):
    return  "500"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        form = LoginForm()
        return render_template("login.html",form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            session['name']=form.name
            print("用户提交的数据用过格式验证，值为：%s"%form.data)
            username=session.get('name')
            print(url_for('index'))
            return  redirect(url_for("index"))
        else:
            print(form.errors,"错误信息")
        return render_template("login.html",form=form)

@app.route('/find',methods=['post'])
def get():
    print(request.form['sb'])
    return 'shabijiusni%s'% request.form['sb']

if  __name__=='__main__':
    app.run(debug=True)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


    def __repr__(self):
        return '<Role %r>' % self.name
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    def __repr__(self):
        return '<User %r>' % self.username